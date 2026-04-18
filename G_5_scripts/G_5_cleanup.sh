#!/usr/bin/env bash
set -euo pipefail

for cni in flannel calico cilium; do
  if kind get clusters | grep -q "g5-${cni}"; then
    echo "[INFO] Deleting cluster g5-${cni}"
    kind delete cluster --name "g5-${cni}"
  fi
done

echo "[DONE] Cleanup completed"