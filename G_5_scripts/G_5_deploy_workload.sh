#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <flannel|calico|cilium>"
  exit 1
fi

CNI="$1"
CTX="kind-g5-${CNI}"

kubectl --context "${CTX}" apply -f "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/G_5_manifests/G_5_00_namespace.yaml"
kubectl --context "${CTX}" apply -f "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/G_5_manifests/G_5_10_server.yaml"
kubectl --context "${CTX}" apply -f "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/G_5_manifests/G_5_20_client.yaml"

echo "[INFO] Waiting for benchmark deployments"
kubectl --context "${CTX}" -n g5-bench rollout status deploy/g5-echo --timeout=300s
kubectl --context "${CTX}" -n g5-bench rollout status deploy/g5-client --timeout=300s

echo "[DONE] Workload deployed on ${CTX}"