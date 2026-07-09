# Resilient Microservices E-Commerce Backend

A small but production-shaped e-commerce backend built to demonstrate
**microservices + DevOps/SRE** fundamentals: independent FastAPI services, an
API gateway, container orchestration with Docker Compose and Kubernetes, a
Jenkins CI/CD pipeline, and real fault-tolerance patterns (health probes,
timeouts, retries, graceful degradation, autoscaling).

Everything runs **locally and offline** — services default to SQLite, so there
is no external database to stand up.

---

## Architecture

```
                         ┌────────────────────────────┐
        client  ───────► │        Ingress (nginx)      │   host: ecommerce.local
                         └──────────────┬─────────────┘
                                        │
                                ┌───────▼────────┐
                                │   API Gateway  │  :8080  (routes /api/*)
                                │   (FastAPI)    │  timeout + retry + agg /readyz
                                └───┬────────┬───┬┘
                    /api/products   │        │   │   /api/users
                          ┌─────────▼──┐  ┌──▼───▼──────┐  ┌────────────┐
                          │  product-  │  │   order-    │  │   user-    │
                          │  service   │◄─┤  service    │  │  service   │
                          │ (FastAPI)  │  │ (FastAPI)   │  │ (FastAPI)  │
                          │  :8001     │  │   :8002     │  │   :8003    │
                          └─────┬──────┘  └─────┬───────┘  └─────┬──────┘
                                │               │                │
                            SQLite          SQLite            SQLite
                          product.db       order.db          user.db

  order-service calls product-service to validate/price products before
  creating an order. That call is wrapped in timeout + bounded retry +
  clear 503 on failure — the core fault-tolerance demo.
```

### Services

| Service | Port | Responsibility | Key endpoints |
|---|---|---|---|
| `product-service` | 8001 | Catalog CRUD | `POST/GET/PUT/DELETE /products` |
| `order-service`   | 8002 | Create/list orders (calls product-service) | `POST/GET /orders` |
| `user-service`    | 8003 | Register + simple token auth | `POST /register`, `POST /login`, `GET /me` |
| `gateway`         | 8080 | Single entry point, path routing | `/api/products`, `/api/orders`, `/api/users` |

Every service exposes `GET /healthz` (liveness) and `GET /readyz` (readiness).

---

## Run locally with Docker Compose

```bash
docker compose up --build
# then, in another shell:
curl -s localhost:8001/healthz
curl -s -X POST localhost:8001/products -H 'content-type: application/json' \
     -d '{"name":"Keyboard","price":49.9,"stock":10}'
curl -s -X POST localhost:8002/orders   -H 'content-type: application/json' \
     -d '{"product_id":1,"quantity":2}'
# through the gateway:
curl -s localhost:8080/api/products
curl -s localhost:8080/readyz          # aggregate upstream health
```

Optional Postgres (services still default to SQLite, this just stands the DB up):

```bash
docker compose --profile postgres up --build
```

## Run a single service without Docker

```bash
cd services/product-service
python -m venv .venv && . .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --port 8001 --reload
```

## Run the tests

```bash
cd services/product-service && python -m pytest -q
cd ../order-service        && python -m pytest -q   # stubs product-service via httpx MockTransport
cd ../user-service         && python -m pytest -q
```

---

## Deploy to Kubernetes

```bash
# build & (optionally) push images tagged resilient-ecommerce/<svc>:latest, then:
kubectl apply -f k8s/configmap.yaml -f k8s/secret.yaml
kubectl apply -f k8s/product-service.yaml -f k8s/order-service.yaml \
              -f k8s/user-service.yaml    -f k8s/gateway.yaml
kubectl apply -f k8s/ingress.yaml -f k8s/hpa.yaml
kubectl get pods,svc,hpa
```

See [`k8s/README.md`](k8s/README.md) for the full resiliency-pattern breakdown.

---

## Resiliency / fault-tolerance design

**At the application layer**
- **Timeouts** on every inter-service HTTP call — the caller never hangs.
- **Bounded retry with linear backoff** for transient failures (timeout /
  connection reset / upstream 5xx). A definitive `404` is *not* retried.
- **Graceful degradation**: when product-service is unreachable, order-service
  returns a clear `503 product-service unavailable` — fail fast and loud, not a
  hang or opaque 500.
- **Readiness vs liveness separation**: order-service stays *ready* even when its
  dependency is down (a dependency outage shouldn't get the pod killed), while
  `/readyz` on each service verifies its own DB.
- **Structured JSON logs** and **12-factor config** (all tunables via env vars).

**At the orchestration layer** (Kubernetes)
- Liveness + readiness probes, 2+ replicas, rolling updates with
  `maxUnavailable: 0`, CPU-based HPA (2→6), resource requests/limits,
  ConfigMap/Secret separation, and an Ingress fronting the gateway.

---

## CI/CD

`Jenkinsfile` is a declarative pipeline:
`Checkout → Install & Lint (compileall) → Test (pytest per service) →
Docker Build → Deploy to k8s (kubectl apply, main branch only)`.

---

## Repository layout

```
resilient_microservices_ecommerce/
├── services/
│   ├── product-service/{app,tests,Dockerfile,requirements.txt,conftest.py}
│   ├── order-service/  {app,tests,Dockerfile,requirements.txt,conftest.py}
│   └── user-service/   {app,tests,Dockerfile,requirements.txt,conftest.py}
├── gateway/            {app,Dockerfile,requirements.txt}
├── k8s/                *.yaml + README.md (resiliency notes)
├── docker-compose.yml
├── Jenkinsfile
├── README.md
└── STUDY_GUIDE.md
```
