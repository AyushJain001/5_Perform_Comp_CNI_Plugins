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

CSV_FILE="${RESULT_DIR}/G_5_latency_${CNI}.csv"
if [[ ! -f "${CSV_FILE}" ]]; then
  echo "cni,qps,run,p50_ms,p90_ms,p99_ms,avg_ms,throughput_rps,error_percent" > "${CSV_FILE}"
fi

CLIENT_POD="$(kubectl --context "${CTX}" -n g5-bench get pod -l app=g5-client -o jsonpath='{.items[0].metadata.name}')"
TARGET_URL="http://g5-echo.g5-bench.svc.cluster.local:5678/"

QPS_LIST=(100 300 500 800)
RUNS=5
DURATION="30s"
CONNECTIONS=32

for qps in "${QPS_LIST[@]}"; do
  for run in $(seq 1 "${RUNS}"); do
    LOCAL_JSON="${RESULT_DIR}/G_5_raw_${CNI}_${qps}_${run}.json"
    TMP_JSON="${LOCAL_JSON}.tmp"
    RETRIES=2
    ATTEMPT=1

    rm -f "${LOCAL_JSON}" "${TMP_JSON}"

    while true; do
      # Stream JSON result to host file to avoid dependency on writable container temp paths.
      kubectl --context "${CTX}" -n g5-bench exec "${CLIENT_POD}" -- \
        fortio load -a -qps "${qps}" -c "${CONNECTIONS}" -t "${DURATION}" -json - "${TARGET_URL}" > "${TMP_JSON}"

      if [[ -s "${TMP_JSON}" ]] && jq -e '.DurationHistogram and .ActualQPS' "${TMP_JSON}" >/dev/null 2>&1; then
        mv "${TMP_JSON}" "${LOCAL_JSON}"
        break
      fi

      rm -f "${TMP_JSON}"
      if [[ "${ATTEMPT}" -ge "${RETRIES}" ]]; then
        echo "[ERROR] Failed to capture valid JSON for CNI=${CNI} QPS=${qps} RUN=${run} after ${RETRIES} attempts"
        exit 1
      fi

      echo "[WARN] Invalid/missing JSON for CNI=${CNI} QPS=${qps} RUN=${run}; retrying (attempt $((ATTEMPT + 1))/${RETRIES})"
      ATTEMPT=$((ATTEMPT + 1))
    done

    p50="$(jq '.DurationHistogram.Percentiles[] | select(.Percentile==50) | .Value' "${LOCAL_JSON}")"
    p90="$(jq '.DurationHistogram.Percentiles[] | select(.Percentile==90) | .Value' "${LOCAL_JSON}")"
    p99="$(jq '.DurationHistogram.Percentiles[] | select(.Percentile==99) | .Value' "${LOCAL_JSON}")"
    avg="$(jq '.DurationHistogram.Avg' "${LOCAL_JSON}")"
    rps="$(jq '.ActualQPS' "${LOCAL_JSON}")"
    err="$(jq '.RetCodes | to_entries | map(select(.key!="200")) | map(.value) | add // 0' "${LOCAL_JSON}")"
    total="$(jq '.RetCodes | to_entries | map(.value) | add' "${LOCAL_JSON}")"

    if [[ "${total}" == "0" ]]; then
      err_pct="0"
    else
      err_pct="$(awk -v e="${err}" -v t="${total}" 'BEGIN { printf "%.4f", (e/t)*100 }')"
    fi

    echo "${CNI},${qps},${run},${p50},${p90},${p99},${avg},${rps},${err_pct}" >> "${CSV_FILE}"
    echo "[OK] CNI=${CNI} QPS=${qps} RUN=${run}"
  done
done

echo "[DONE] Benchmark CSV written: ${CSV_FILE}"