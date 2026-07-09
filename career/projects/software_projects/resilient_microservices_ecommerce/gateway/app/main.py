"""API Gateway — single entry point that routes to the backend microservices.

Responsibilities demonstrated here:
  * Path-based routing to product/order/user services.
  * A single public surface so clients don't need to know internal topology.
  * Per-request timeout + one retry so a blip in a backend doesn't 500 the edge.
  * An aggregate /readyz that reports which upstreams are healthy.

Kept intentionally thin: a real deployment might use Kong/NGINX/Traefik, but
this shows the *concept* in idiomatic FastAPI and is fully runnable offline.
"""
from __future__ import annotations

import json
import logging
import os
import sys
import time

import httpx
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

SERVICE_NAME = os.getenv("SERVICE_NAME", "gateway")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
HTTP_TIMEOUT = float(os.getenv("HTTP_TIMEOUT", "3.0"))

# Route table: URL prefix -> upstream base URL (all env-configurable).
ROUTES = {
    "/api/products": os.getenv("PRODUCT_SERVICE_URL", "http://localhost:8001"),
    "/api/orders": os.getenv("ORDER_SERVICE_URL", "http://localhost:8002"),
    "/api/users": os.getenv("USER_SERVICE_URL", "http://localhost:8003"),
}
# Strip the /api/<name> prefix down to the upstream's own path root.
PREFIX_STRIP = {
    "/api/products": "/products",
    "/api/orders": "/orders",
    "/api/users": "",
}


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        return json.dumps(
            {
                "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(record.created)),
                "level": record.levelname,
                "service": SERVICE_NAME,
                "msg": record.getMessage(),
            }
        )


def _build_logger() -> logging.Logger:
    logger = logging.getLogger(SERVICE_NAME)
    logger.setLevel(LOG_LEVEL)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonFormatter())
    logger.handlers = [handler]
    logger.propagate = False
    return logger


log = _build_logger()
app = FastAPI(title="API Gateway", version="1.0.0")


def _resolve(path: str) -> tuple[str, str] | None:
    """Map an incoming path to (upstream_base, rewritten_path)."""
    for prefix, base in ROUTES.items():
        if path == prefix or path.startswith(prefix + "/"):
            remainder = path[len(prefix):]  # keep sub-path, e.g. /42
            rewritten = PREFIX_STRIP[prefix] + remainder
            return base, rewritten or "/"
    return None


@app.get("/healthz")
def healthz() -> dict:
    return {"status": "ok", "service": SERVICE_NAME}


@app.get("/readyz")
def readyz() -> JSONResponse:
    """Aggregate readiness — report each upstream's health, degrade gracefully."""
    results: dict[str, str] = {}
    all_ok = True
    for prefix, base in ROUTES.items():
        try:
            with httpx.Client(timeout=1.5) as client:
                r = client.get(f"{base}/healthz")
            results[prefix] = "up" if r.status_code == 200 else f"http {r.status_code}"
            all_ok = all_ok and r.status_code == 200
        except Exception as exc:  # noqa: BLE001
            results[prefix] = f"down: {exc.__class__.__name__}"
            all_ok = False
    return JSONResponse(
        status_code=200 if all_ok else 503,
        content={"status": "ready" if all_ok else "degraded", "upstreams": results},
    )


@app.api_route(
    "/api/{full_path:path}",
    methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
)
async def proxy(full_path: str, request: Request) -> Response:
    target = _resolve(request.url.path)
    if target is None:
        return JSONResponse(status_code=404, content={"detail": "no route"})

    base, rewritten = target
    url = base + rewritten
    body = await request.body()
    headers = {
        k: v for k, v in request.headers.items()
        if k.lower() not in {"host", "content-length"}
    }

    # One retry: gateways should absorb transient upstream blips.
    last_exc: Exception | None = None
    for attempt in range(2):
        try:
            async with httpx.AsyncClient(timeout=HTTP_TIMEOUT) as client:
                upstream = await client.request(
                    request.method, url, content=body, headers=headers,
                    params=request.query_params,
                )
            return Response(
                content=upstream.content,
                status_code=upstream.status_code,
                headers={"content-type": upstream.headers.get("content-type", "application/json")},
            )
        except (httpx.TimeoutException, httpx.TransportError) as exc:
            last_exc = exc
            log.warning("upstream %s failed (attempt %s): %s", url, attempt + 1, exc)
            time.sleep(0.1)

    log.error("upstream %s unavailable: %s", url, last_exc)
    return JSONResponse(
        status_code=502,
        content={"detail": f"upstream unavailable: {last_exc}"},
    )
