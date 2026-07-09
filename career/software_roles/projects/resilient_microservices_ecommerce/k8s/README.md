# Kubernetes manifests & resiliency patterns

Apply order (config first, then workloads, then routing/scaling):

```bash
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/product-service.yaml
kubectl apply -f k8s/order-service.yaml
kubectl apply -f k8s/user-service.yaml
kubectl apply -f k8s/gateway.yaml
kubectl apply -f k8s/ingress.yaml
kubectl apply -f k8s/hpa.yaml
```

## Resiliency patterns baked into these manifests

| Pattern | Where | Why it matters |
|---|---|---|
| **Liveness probe** (`/healthz`) | every Deployment | k8s restarts a wedged/deadlocked container automatically. |
| **Readiness probe** (`/readyz`) | every Deployment | a pod receives traffic only once its DB is reachable; unready pods are pulled from the Service endpoints instead of erroring users. |
| **Multiple replicas** (`replicas: 2`) | every Deployment | no single point of failure; a node/pod loss still leaves a serving replica. |
| **Rolling updates** (`maxUnavailable: 0`) | every Deployment | zero-downtime deploys — new pods must pass readiness before old ones are torn down. |
| **Resource requests/limits** | every container | protects the node from a noisy neighbour and lets the scheduler bin-pack correctly; limits enable HPA math. |
| **HorizontalPodAutoscaler** | `hpa.yaml` | scales 2→6 pods at 70% CPU so traffic spikes don't tip the service over. |
| **ConfigMap / Secret split** | `configmap.yaml`, `secret.yaml` | config is externalised (12-factor); secrets never live in the image. |
| **Ingress + gateway** | `ingress.yaml`, `gateway.yaml` | single hardened entry point; internal services stay ClusterIP-only. |

## Application-level resiliency (in the code, complementing k8s)

- **Timeouts** on every cross-service HTTP call (`HTTP_TIMEOUT`) — never hang forever.
- **Bounded retry with backoff** (`HTTP_RETRIES`) for transient upstream failures.
- **Graceful degradation**: order-service returns a clear `503` when product-service
  is down instead of a 500 or a hang; its own `/readyz` stays green so k8s doesn't
  needlessly restart it (a dependency outage is not a reason to kill the pod).
- **Gateway** absorbs a single upstream blip with one retry and reports per-upstream
  health from its aggregate `/readyz`.
