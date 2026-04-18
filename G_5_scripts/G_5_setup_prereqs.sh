#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BIN_DIR="${ROOT_DIR}/G_5_artifacts/G_5_bin"
mkdir -p "${BIN_DIR}"

export PATH="${BIN_DIR}:$PATH"

echo "[INFO] Installing local tools into ${BIN_DIR}"

install_kubectl() {
  if command -v kubectl >/dev/null 2>&1; then
    echo "[OK] kubectl already present"
    return
  fi

  local version
  version="$(curl -L -s https://dl.k8s.io/release/stable.txt)"
  curl -L -o "${BIN_DIR}/kubectl" "https://dl.k8s.io/release/${version}/bin/linux/amd64/kubectl"
  chmod +x "${BIN_DIR}/kubectl"
  echo "[OK] kubectl installed (${version})"
}

install_kind() {
  if command -v kind >/dev/null 2>&1; then
    echo "[OK] kind already present"
    return
  fi

  curl -Lo "${BIN_DIR}/kind" https://kind.sigs.k8s.io/dl/v0.23.0/kind-linux-amd64
  chmod +x "${BIN_DIR}/kind"
  echo "[OK] kind installed"
}

install_helm() {
  if command -v helm >/dev/null 2>&1; then
    echo "[OK] helm already present"
    return
  fi

  local tmp_dir
  tmp_dir="$(mktemp -d)"
  curl -L -o "${tmp_dir}/helm.tar.gz" https://get.helm.sh/helm-v3.16.2-linux-amd64.tar.gz
  tar -xzf "${tmp_dir}/helm.tar.gz" -C "${tmp_dir}"
  mv "${tmp_dir}/linux-amd64/helm" "${BIN_DIR}/helm"
  chmod +x "${BIN_DIR}/helm"
  rm -rf "${tmp_dir}"
  echo "[OK] helm installed"
}

install_jq() {
  if command -v jq >/dev/null 2>&1; then
    echo "[OK] jq already present"
    return
  fi

  curl -L -o "${BIN_DIR}/jq" https://github.com/jqlang/jq/releases/download/jq-1.7.1/jq-linux-amd64
  chmod +x "${BIN_DIR}/jq"
  echo "[OK] jq installed"
}

install_cilium_cli() {
  if command -v cilium >/dev/null 2>&1; then
    echo "[OK] cilium CLI already present"
    return
  fi

  local version arch
  version="v0.16.23"
  arch="amd64"
  curl -L --fail --output "${BIN_DIR}/cilium.tar.gz" "https://github.com/cilium/cilium-cli/releases/download/${version}/cilium-linux-${arch}.tar.gz"
  tar -xzf "${BIN_DIR}/cilium.tar.gz" -C "${BIN_DIR}"
  rm -f "${BIN_DIR}/cilium.tar.gz"
  chmod +x "${BIN_DIR}/cilium"
  echo "[OK] cilium CLI installed"
}

check_docker() {
  if ! command -v docker >/dev/null 2>&1; then
    echo "[WARN] Docker is required for kind clusters but is not in PATH"
    return
  fi

  echo "[OK] docker found"
}

install_kubectl
install_kind
install_helm
install_jq
install_cilium_cli
check_docker

echo "[DONE] Prerequisites ready. Add this to your shell before running other scripts:"
echo "export PATH=${BIN_DIR}:\$PATH"
