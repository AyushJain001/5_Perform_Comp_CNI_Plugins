# G_5 Execution Plan (Full Project)

## Phase 1: Environment Setup

- Run prerequisites script.
- Ensure Docker daemon is running.
- Ensure local PATH includes `G_5_artifacts/G_5_bin`.

## Phase 2: Controlled Cluster Creation

- Create three separate kind clusters:
  - `g5-flannel`
  - `g5-calico`
  - `g5-cilium`
- Keep node count and machine constant for fairness.

## Phase 3: Workload Deployment

- Deploy namespace, echo service, and benchmark client in each cluster.
- Validate readiness and service DNS reachability.

## Phase 4: Benchmark Execution

- For each CNI:
  - QPS sweep: 100, 300, 500, 800
  - Run each point 5 times
  - Duration per run: 30s
- Store raw JSON and summarized CSV.

## Phase 5: Resource Collection

- Install metrics-server if needed.
- Collect pod-level CPU and memory overhead during load windows.

## Phase 6: Plot and Report

- Use final hardcoded plotting scripts for submission-compliant charts.
- Fill report sections in template and convert to PDF.
- Prepare presentation with architecture, plots, and takeaways.

## Full-Marks Checklist

- Include architectural explanation (why performance differs).
- Show repeatability (multiple runs + mean/std dev).
- Include all scripts, raw data, processed CSV, and final plots.
- Maintain strict naming convention on every submitted file.
- Zip with exact required name format.
