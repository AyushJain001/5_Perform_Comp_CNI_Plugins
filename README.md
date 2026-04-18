# G_5 Performance Comparison of Kubernetes CNI Plugins

## Project Statement

This project compares Flannel, Calico, and Cilium for Kubernetes networking performance under realistic microservice communication.

## Group

- Group ID: 5
- Team Members: UPDATE_THIS

## What This Repository Contains

- End-to-end setup scripts for local tool installation and cluster creation.
- Kubernetes manifests for benchmark workload deployment.
- Benchmark automation scripts for latency, throughput, and resource overhead collection.
- Plot scripts and report template aligned with submission format.

## Evaluation Questions

1. Which CNI gives the lowest latency (p50, p90, p99) at increasing QPS?
2. Which CNI gives the best sustained throughput under fixed error budget?
3. Which CNI incurs the lowest CPU and memory overhead during load?
4. How do architecture differences explain observed behavior?

## High-Level Workflow

1. Install tools locally.
2. Create one cluster per CNI (same node resources).
3. Deploy same workload and benchmark client.
4. Run identical load profiles.
5. Collect latency and resource metrics.
6. Convert measured CSV metrics into hardcoded values.
7. Generate plots.
8. Fill report and presentation.

## Quick Start

```bash
cd /home/iiitd/grs
chmod +x G_5_scripts/*.sh
./G_5_scripts/G_5_setup_prereqs.sh
./G_5_scripts/G_5_create_cluster.sh flannel
./G_5_scripts/G_5_create_cluster.sh calico
./G_5_scripts/G_5_create_cluster.sh cilium
./G_5_scripts/G_5_deploy_workload.sh flannel
./G_5_scripts/G_5_run_benchmark.sh flannel
./G_5_scripts/G_5_collect_metrics.sh flannel
./G_5_artifacts/G_5_venv/bin/python G_5_scripts/G_5_generate_hardcoded_plot_data.py
./G_5_artifacts/G_5_venv/bin/python G_5_plots/G_5_plot_latency_hardcoded.py
./G_5_artifacts/G_5_venv/bin/python G_5_plots/G_5_plot_overhead_hardcoded.py
```

Repeat deployment and benchmark for `calico` and `cilium`.

For final submission, keep the plot scripts hardcoded using your measured values from `G_5_results/*.csv`.

## Submission Naming Conventions (Critical)

- Zip file: `G_5_Part_B_nameOfProject.zip`
- Every file should follow naming convention with `G_5_` prefix.
- Use only `.zip` extension, no binaries.
- Plot scripts should be `.py` and use hardcoded values for final submission.

## Recommended Final Folder (inside zip)

- `G_5_README.md`
- `G_5_report.pdf`
- `G_5_presentation.pdf`
- `G_5_scripts/`
- `G_5_manifests/`
- `G_5_results/` (CSV, logs)
- `G_5_plots/` (PNG + py plotting scripts)

## Reproducibility Controls

- Use the same Kubernetes version for all three CNIs.
- Use same node count and machine size.
- Use same benchmark duration, connections, and QPS schedule.
- Run each experiment at least 5 times and average.

## Notes

- If `kubectl top` fails, install metrics-server using script comments in `G_5_collect_metrics.sh`.
- If CNI install fails due version mismatch, pin tested versions in `G_5_scripts/G_5_create_cluster.sh`.

## Optional Live Demo Dashboard (Streamlit)

This dashboard is optional and intended for demo/viva presentation. It does not replace the submission norms.

```bash
cd /home/iiitd/grs
/home/iiitd/grs/G_5_artifacts/G_5_venv/bin/python -m pip install -r G_5_demo/G_5_demo_requirements.txt
./G_5_demo/G_5_run_dashboard.sh
```

Then open:

- <http://localhost:8501>

Dashboard file:

- `G_5_demo/G_5_dashboard_streamlit.py`
