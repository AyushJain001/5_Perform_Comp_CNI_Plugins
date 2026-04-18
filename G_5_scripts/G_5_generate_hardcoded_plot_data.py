#!/usr/bin/env python3
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "G_5_results"
PLOTS = ROOT / "G_5_plots"
OUT_JSON = RESULTS / "G_5_hardcoded_values.json"


def build_latency_values() -> dict:
    out = {"qps": []}
    found = []
    missing = []

    for cni in ("flannel", "calico", "cilium"):
        path = RESULTS / f"G_5_latency_{cni}.csv"
        if not path.exists():
            missing.append(path.name)
            continue
        df = pd.read_csv(path)
        grouped = df.groupby("qps", as_index=False)["p99_ms"].mean().sort_values("qps")

        if not out["qps"]:
            out["qps"] = grouped["qps"].astype(int).tolist()

        out[f"{cni}_p99"] = grouped["p99_ms"].round(4).tolist()
        found.append(cni)

    if missing:
        print(f"[WARN] Missing latency files: {', '.join(missing)}")
    if not found:
        raise RuntimeError("No latency CSV files found under G_5_results.")

    return out


def build_resource_values() -> dict:
    cni_labels = []
    cpu_vals = []
    mem_vals = []
    missing = []

    for cni in ("flannel", "calico", "cilium"):
        path = RESULTS / f"G_5_resource_{cni}.csv"
        if not path.exists():
            missing.append(path.name)
            continue
        df = pd.read_csv(path)
        cpu_vals.append(round(float(df["cpu_mcores"].sum()), 4))
        mem_vals.append(round(float(df["memory_mib"].sum()), 4))
        cni_labels.append(cni.capitalize())

    if missing:
        print(f"[WARN] Missing resource files: {', '.join(missing)}")
    if not cni_labels:
        raise RuntimeError("No resource CSV files found under G_5_results.")

    return {
        "cnis": cni_labels,
        "cpu_mcores": cpu_vals,
        "mem_mib": mem_vals,
    }


def write_output(latency: dict, resource: dict) -> None:
    payload = {
        "note": "Generated from measured CSV files. Use these values in final hardcoded plot scripts.",
        "latency": latency,
        "resource": resource,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def main() -> None:
    latency = build_latency_values()
    resource = build_resource_values()
    write_output(latency, resource)
    print(f"[DONE] Wrote hardcoded plot values to {OUT_JSON}")
    print("[NEXT] Copy values from JSON into hardcoded plotting scripts in G_5_plots.")


if __name__ == "__main__":
    main()
