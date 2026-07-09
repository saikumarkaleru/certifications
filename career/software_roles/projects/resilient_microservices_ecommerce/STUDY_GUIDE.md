# Interview Study Guide — Resilient Microservices E-Commerce

A defense sheet for this project. Know the *why* behind each decision, not just
the *what*. Everything below is demonstrated by code in this repo.

---

## 1. Microservices vs. Monolith

**Monolith** = one deployable unit, one codebase, one database. Simple to start,
fast local dev, one process to reason about. But it scales as a block, one bad
deploy risks everything, and teams contend on the same code.

**Microservices** = independently deployable services, each owning its data and
exposing an API. Benefits:
- **Independent deployability** — ship order-service without touching
  product-service.
- **Independent scaling** — scale only the hot service (see the HPA on
  product/order, not user).
- **Fault isolation** — product-service dying degrades ordering but the catalog
  reads and user logins keep working.
- **Tech/data autonomy** — each service picks its own store (here: a SQLite DB
  per service; "database-per-service" pattern).

Costs (be honest in interviews): network calls replace function calls (latency +
partial failure), distributed debugging, data consistency across services,
operational overhead (this is exactly why we need Docker/k8s/CI-CD).

**When to choose which**: start monolith for a small team/unknown domain; split
to microservices when scaling, team size, or deploy-cadence pain justifies the
operational cost.

---

## 2. Fault tolerance & resiliency patterns

This project implements the core ones:

- **Timeout** — every cross-service HTTP call has `HTTP_TIMEOUT`. Without it, one
  slow dependency exhausts your threads/connections (cascading failure).
- **Retry with backoff** — retry *transient* failures a bounded number of times
  with increasing delay. Only retry idempotent/safe operations; never retry a
  definitive `404`. Backoff avoids hammering a recovering service.
- **Graceful degradation** — return a clear `503` (order-service when
  product-service is down) instead of hanging or leaking a 500.
- **Circuit breaker** (concept — the natural next step): after N consecutive
  failures, "open" the circuit and fail fast for a cooldown instead of retrying,
  then "half-open" to test recovery. Libraries: `pybreaker`, resilience4j (JVM),
  Istio/Envoy at the mesh layer.
- **Bulkhead** — isolate resource pools so one overloaded dependency can't sink
  the whole service (separate connection pools / thread pools).
- **Health checks** — liveness vs readiness (see below).
- **Redundancy** — 2+ replicas so a single pod/node loss is survivable.
- **Idempotency** — design writes so a retry doesn't double-charge (e.g. an
  idempotency key on order creation — a good "what would you add next" answer).

**Cascading failure** = one slow/down service backs up its callers until the
whole system falls over. Timeouts + circuit breakers + bulkheads exist to stop it.

---

## 3. Health checks: liveness vs readiness

- **Liveness (`/healthz`)** — "is the process alive?" If it fails, k8s
  **restarts** the pod. Keep it cheap and dependency-free; otherwise a dependency
  blip triggers pointless restart loops.
- **Readiness (`/readyz`)** — "can I serve traffic right now?" If it fails, k8s
  **removes the pod from the Service endpoints** but does *not* restart it. Good
  for checking your own DB, warm caches, etc.
- **Design choice in this repo**: order-service's readiness checks only its *own*
  SQLite, not product-service. A dependency being down shouldn't make the pod
  un-ready (that would remove capacity we still need for reads) or get it killed.
  We degrade per-request instead. This distinction is a common interview trap.
- **Startup probe** (mention it): for slow-booting apps, protects a slow start
  from the liveness probe killing it prematurely.

---

## 4. Scaling

- **Vertical** — bigger pods (more CPU/RAM). Simple, but has a ceiling and a
  blast radius.
- **Horizontal** — more replicas. Preferred for stateless services; that's why
  these services keep no in-memory session state.
- **HPA** — `HorizontalPodAutoscaler` scales replicas on a metric (CPU 70% here,
  2→6). Requires resource **requests** (the % is of the request) and
  metrics-server. Can also scale on custom/external metrics (QPS, queue depth).
- **Statelessness** is the enabler — any replica can serve any request. State
  lives in the DB, not the pod. (Our SQLite-per-pod is a demo simplification; in
  real horizontal scaling you'd share Postgres — hence the optional compose
  profile.)
- **Load balancing** — the k8s Service load-balances across ready replicas.

---

## 5. CI/CD

- **CI** — on every push: checkout → install → **lint/compile** → **test** →
  build image. Catches breakage before it merges.
- **CD** — after CI passes on `main`: push image → `kubectl apply` → wait for
  `rollout status`. Our `Jenkinsfile` gates deploy on the `main` branch.
- **Rolling update** — new pods must pass readiness before old pods are removed
  (`maxUnavailable: 0`), giving zero-downtime deploys. Rollback =
  `kubectl rollout undo`.
- **Image tagging** — immutable tags per build (`:${BUILD_NUMBER}`) plus a moving
  `:latest`. Never deploy an untagged/mutable image to prod.
- **Other CD strategies to name-drop**: blue-green (two full environments, flip
  traffic) and canary (send 5% of traffic to the new version, watch metrics,
  ramp up).

---

## 6. Supporting concepts

- **API Gateway** — single entry point: routing, and a natural home for
  cross-cutting concerns (auth, rate limiting, TLS termination, request logging).
  Keeps internal services private (ClusterIP) behind one hardened edge.
- **Service discovery** — in k8s, a Service name resolves via cluster DNS
  (`product-service:8000`). No hardcoded IPs.
- **ConfigMap vs Secret** — non-sensitive vs sensitive config, both injected as
  env vars so config is externalised from the image (12-factor).
- **Container vs VM** — containers share the host kernel (lightweight, fast,
  dense); VMs virtualize hardware (heavier, stronger isolation).
- **Stateless services + external state** — the pattern that makes horizontal
  scaling and rolling updates safe.
- **Observability** — the three pillars: **logs** (structured JSON here),
  **metrics** (what HPA consumes; Prometheus in prod), **traces**
  (distributed tracing / OpenTelemetry — the natural next add).

---

## 7. Q&A (rapid-fire)

1. **Why microservices here?** Independent deploy/scale/fault-isolation for
   catalog, orders, and users — each has different load and change cadence.

2. **How do services find each other?** k8s DNS: the Service name
   (`product-service:8000`). Locally, env-var URLs via compose.

3. **What happens when product-service is down and I create an order?**
   order-service times out, retries with backoff, then returns a clear `503` —
   no hang, no cascading failure.

4. **Why not retry a 404?** It's a definitive answer; retrying wastes time and
   can't change the result. We only retry transient failures.

5. **Liveness vs readiness?** Liveness failing → restart the pod; readiness
   failing → stop routing traffic to it (no restart).

6. **Why is order-service still "ready" when its dependency is down?** A
   dependency outage isn't a reason to kill the pod or drop capacity; we degrade
   per request. Readiness reflects *our own* health (the DB).

7. **How does autoscaling decide?** HPA compares average CPU to the target (70%
   of the pod's CPU *request*) and adjusts replicas within min/max.

8. **Why resource requests AND limits?** Requests drive scheduling and the HPA
   math; limits cap a pod so it can't starve neighbours (noisy-neighbour).

9. **How do you get zero-downtime deploys?** Rolling update with
   `maxUnavailable: 0` + readiness probes: new pods serve only after they're
   ready, old pods drain after.

10. **How would you roll back a bad deploy?** `kubectl rollout undo
    deployment/<name>`; images are immutably tagged per build so it's deterministic.

11. **Where do secrets live?** In a k8s Secret, injected as an env var
    (`SECRET_KEY`) — never baked into the image or committed with real values.

12. **How are passwords stored?** PBKDF2-HMAC-SHA256 with a per-user salt and
    constant-time comparison. Never plaintext, never a fast unsalted hash.

13. **How would you make order creation safe under retries?** An idempotency key
    so a retried POST doesn't create a duplicate order.

14. **What's a circuit breaker and where would it go?** Wrap the
    order→product call: after N failures, open the circuit and fail fast for a
    cooldown to give the dependency room to recover. Next iteration of this repo.

15. **How would you observe this in prod?** Structured logs → a log aggregator;
    Prometheus metrics (incl. the ones HPA uses); OpenTelemetry traces to follow a
    request across the gateway and services.

16. **Why SQLite here, and what changes for real scale?** SQLite keeps the demo
    zero-dependency and offline. For real horizontal scaling you'd move to a
    shared Postgres (the optional compose profile) so replicas share state.

17. **Why a gateway instead of exposing each service?** One public surface, one
    place for auth/rate-limit/TLS, and internal services stay private (ClusterIP).

18. **What is the database-per-service pattern and its trade-off?** Each service
    owns its data (loose coupling), but cross-service consistency needs events/
    sagas rather than a single ACID transaction.

19. **How would you handle distributed transactions across services?** Avoid
    them; use the **Saga** pattern — a sequence of local transactions with
    compensating actions on failure.

20. **What would you add next?** Circuit breaker, idempotency keys, shared
    Postgres, Prometheus/Grafana + tracing, message queue for async order events,
    and a real auth provider (OAuth2/JWT with rotation).
