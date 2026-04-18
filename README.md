## G_5 Performance Comparison of Kubernetes CNI Plugins

## Project Overview

This repository contains the complete implementation of Group 5's Kubernetes networking performance study.

We compare three widely used CNI plugins:

1. Flannel
2. Calico
3. Cilium

The comparison is performed under a controlled microservice workload and focuses on:

1. Latency behavior (including p99 tail latency)
2. Throughput consistency
3. CPU and memory overhead

## Team Information

                                            ##Group Number: 5
                                            ##Ayush Jain - MT25066
                                            ##Singh Tharun - MT25087
                                            ##Ruchir Jain - MT25080 

## Repository Structure

Key folders used in final submission:

1. `G_5_manifests/`: Kubernetes YAML manifests for namespace, server, and client
2. `G_5_scripts/`: Automation scripts for setup, cluster creation, benchmark runs, and metrics collection
3. `G_5_results/`: Final CSV outputs (latency and resource metrics for all CNIs)
4. `G_5_plots/`:  matplotlib scripts and generated plot images
5. `G_5_report/`: Final report files

## Prerequisites

Run on Linux with the following available:

1. Docker
2. Bash
3. Python 3

The setup script handles most tool bootstrapping used by this project.

## Setup Commands

From repository root:

```bash
chmod +x G_5_scripts/*.sh
./G_5_scripts/G_5_setup_prereqs.sh
```

What this does:

1. Prepares required tooling environment
2. Sets up local artifacts used by project scripts

## End-to-End Benchmark Workflow

Run these steps for each CNI: `flannel`, `calico`, `cilium`.

### Create Cluster

```bash
./G_5_scripts/G_5_create_cluster.sh flannel
./G_5_scripts/G_5_create_cluster.sh calico
./G_5_scripts/G_5_create_cluster.sh cilium
```

### Deploy Workload

```bash
./G_5_scripts/G_5_deploy_workload.sh flannel
./G_5_scripts/G_5_deploy_workload.sh calico
./G_5_scripts/G_5_deploy_workload.sh cilium
```

### Run Benchmark

```bash
./G_5_scripts/G_5_run_benchmark.sh flannel
./G_5_scripts/G_5_run_benchmark.sh calico
./G_5_scripts/G_5_run_benchmark.sh cilium
```

### Collect Resource Metrics

```bash
./G_5_scripts/G_5_collect_metrics.sh flannel
./G_5_scripts/G_5_collect_metrics.sh calico
./G_5_scripts/G_5_collect_metrics.sh cilium
```

### Cleanup (Optional)

```bash
./G_5_scripts/G_5_cleanup.sh
```

##  Plot Generation Commands

Use project Python environment if required by your machine setup.

```bash
./G_5_artifacts/G_5_venv/bin/python G_5_plots/G_5_plot_latency_hardcoded.py
./G_5_artifacts/G_5_venv/bin/python G_5_plots/G_5_plot_latency_variability_hardcoded.py
./G_5_artifacts/G_5_venv/bin/python G_5_plots/G_5_plot_overhead_hardcoded.py
./G_5_artifacts/G_5_venv/bin/python G_5_plots/G_5_plot_throughput_ratio_hardcoded.py
```

Generated figures are written to `G_5_plots/`.

## Expected Output Files

### Final Results (CSV)

1. `G_5_results/G_5_latency_flannel.csv`
2. `G_5_results/G_5_latency_calico.csv`
3. `G_5_results/G_5_latency_cilium.csv`
4. `G_5_results/G_5_resource_flannel.csv`
5. `G_5_results/G_5_resource_calico.csv`
6. `G_5_results/G_5_resource_cilium.csv`

### Final Report

1. `G_5_report/G_5_report.pdf`

## Reproducibility Notes

For fair CNI comparison:

1. Keep machine and Docker environment constant across runs
2. Use same cluster topology and same workload settings
3. Run repeated measurements per load point
4. Compare results only after all three CNIs complete full run cycle

## Troubleshooting

1. If `kubectl top` fails, ensure metrics-server is available before running resource collection.
2. If any script is not executable, run:

```bash
chmod +x G_5_scripts/*.sh
```

3. If Python plot command fails due missing package, install from:

```bash
./G_5_artifacts/G_5_venv/bin/pip install -r G_5_requirements.txt
```



## Quick Run Checklist

Use this short sequence if starting fresh:

```bash
chmod +x G_5_scripts/*.sh
./G_5_scripts/G_5_setup_prereqs.sh

./G_5_scripts/G_5_create_cluster.sh flannel
./G_5_scripts/G_5_deploy_workload.sh flannel
./G_5_scripts/G_5_run_benchmark.sh flannel
./G_5_scripts/G_5_collect_metrics.sh flannel

./G_5_scripts/G_5_create_cluster.sh calico
./G_5_scripts/G_5_deploy_workload.sh calico
./G_5_scripts/G_5_run_benchmark.sh calico
./G_5_scripts/G_5_collect_metrics.sh calico

./G_5_scripts/G_5_create_cluster.sh cilium
./G_5_scripts/G_5_deploy_workload.sh cilium
./G_5_scripts/G_5_run_benchmark.sh cilium
./G_5_scripts/G_5_collect_metrics.sh cilium
```




##Thank You 
