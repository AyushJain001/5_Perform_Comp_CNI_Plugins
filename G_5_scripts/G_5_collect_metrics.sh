#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <flannel|calico|cilium>"
  exit 1
fi

CNI="$1"
CTX="kind-g5-${CNI}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RESULT_DIR="${ROOT_DIR}/G_5_results"
mkdir -p "${RESULT_DIR}"

OUT_FILE="${RESULT_DIR}/G_5_resource_${CNI}.csv"
echo "cni,namespace,pod,cpu_mcores,memory_mib" > "${OUT_FILE}"

if ! kubectl --context "${CTX}" top pods -A >/dev/null 2>&1; then
  echo "[WARN] metrics-server not available. Install with:"
  echo "kubectl --context ${CTX} apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml"
  exit 1
fi

kubectl --context "${CTX}" top pods -A --no-headers | while read -r ns pod cpu mem; do
  cpu_num="${cpu%m}"
  mem_num="${mem%Mi}"
  echo "${CNI},${ns},${pod},${cpu_num},${mem_num}" >> "${OUT_FILE}"
done

echo "[DONE] Resource metrics saved: ${OUT_FILE}"

