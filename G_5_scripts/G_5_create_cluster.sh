#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <flannel|calico|cilium>"
  exit 1
fi

CNI="$1"
CLUSTER_NAME="g5-${CNI}"
KIND_CONFIG_FILE="$(mktemp)"
POD_SUBNET="10.244.0.0/16"

cat > "${KIND_CONFIG_FILE}" <<EOF
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
networking:
  disableDefaultCNI: true
  podSubnet: ${POD_SUBNET}
nodes:
  - role: control-plane
  - role: worker
  - role: worker
EOF

echo "[INFO] Creating kind cluster ${CLUSTER_NAME}"
kind create cluster --name "${CLUSTER_NAME}" --config "${KIND_CONFIG_FILE}" --wait 120s
rm -f "${KIND_CONFIG_FILE}"

kubectl cluster-info --context "kind-${CLUSTER_NAME}" >/dev/null

install_flannel() {
  kubectl --context "kind-${CLUSTER_NAME}" apply -f https://raw.githubusercontent.com/flannel-io/flannel/master/Documentation/kube-flannel.yml
}

install_calico() {
  kubectl --context "kind-${CLUSTER_NAME}" apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.29.2/manifests/calico.yaml
}

install_cilium() {
  cilium install --context "kind-${CLUSTER_NAME}" --version 1.16.3
}

case "${CNI}" in
  flannel)
    install_flannel
    ;;
  calico)
    install_calico
    ;;
  cilium)
    install_cilium
    ;;
  *)
    echo "Unsupported CNI: ${CNI}"
    exit 1
    ;;
esac

echo "[INFO] Waiting for system pods to become ready"
kubectl --context "kind-${CLUSTER_NAME}" wait --for=condition=Ready node --all --timeout=300s

if [[ "${CNI}" == "flannel" ]]; then
  if kubectl --context "kind-${CLUSTER_NAME}" -n kube-flannel get pods 2>/dev/null | grep -qv "Running"; then
    echo "[WARN] Flannel pod(s) not running yet. Recent logs:"
    kubectl --context "kind-${CLUSTER_NAME}" -n kube-flannel logs ds/kube-flannel-ds --tail=80 || true
  fi
fi

kubectl --context "kind-${CLUSTER_NAME}" get pods -A

echo "[DONE] Cluster ready for CNI=${CNI}"