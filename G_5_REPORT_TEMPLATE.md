# G_5 Final Project Report Template

## (1) Project Title

Performance Comparison of Kubernetes CNI Plugins: Flannel vs Calico vs Cilium

## (2) Team Members

- Name 1 (Entry Number)
- Name 2 (Entry Number)
- Name 3 (Entry Number)

## (3) Problem

Kubernetes CNI plugins implement packet forwarding and policy in different ways, leading to different latency, throughput, and resource costs. We measure these differences under controlled microservice traffic.

## (4) Motivation

Selecting a CNI is critical for production clusters because networking overhead directly affects service latency, compute cost, and SLO reliability.

## (5) Objectives

- Build reproducible benchmark setup for three CNI plugins.
- Measure p50/p90/p99 latency, throughput, and error rate.
- Measure control/data plane overhead using CPU and memory metrics.
- Explain observed differences from architecture and datapath design.

## (5) Background

- CNI basics and Kubernetes pod networking model.
- Flannel VXLAN encapsulation model.
- Calico (iptables/eBPF modes) and policy handling.
- Cilium eBPF datapath and kube-proxy replacement options.

## (6) Methodology/Design

### Components

- Cluster Provisioning Layer: kind cluster with controlled resources.
- CNI Layer: Flannel, Calico, Cilium (one per cluster).
- Workload Layer: HTTP echo service and Fortio load client.
- Measurement Layer: Fortio latency/throughput + kubectl top metrics.
- Analysis Layer: CSV aggregation and plot generation.

### Interaction

1. Setup script installs tools.
2. Cluster script creates and configures CNI.
3. Deploy script applies namespace/workload manifests.
4. Benchmark script executes fixed load profiles.
5. Metrics script captures runtime overhead.
6. Plot scripts generate graphs for report.

## (7) Implementation

- Language: Bash (automation), Python (analysis/plotting)
- Container platform: kind + Docker
- Kubernetes version: UPDATE
- CNI versions: UPDATE

## (8) Evaluation and Observations

### Testbed

- Machine spec: CPU, RAM, OS, kernel version
- Cluster spec: node count, Kubernetes version
- Workload spec: pod replicas, request payload, connection settings

### Experiment E1: Latency vs QPS

- Question: Which CNI maintains lowest tail latency as QPS increases?
- Output: line plot (p50/p90/p99 vs QPS)
- Observation: UPDATE

### Experiment E2: Throughput and Error Rate

- Question: Which CNI sustains higher throughput before errors increase?
- Output: throughput and error plot
- Observation: UPDATE

### Experiment E3: CPU/Memory Overhead

- Question: What is resource overhead of each CNI under same load?
- Output: bar chart for CPU and memory
- Observation: UPDATE

### Statistical Reliability

- Repeat each run >=5 times.
- Report mean and standard deviation.

## (9) Outcomes and Conclusion

- Summarize ranking by latency, throughput, and overhead.
- Mention trade-offs and deployment recommendations.
- Discuss threats to validity and future work.

## (10) References

- Kubernetes docs
- Flannel docs
- Calico docs
- Cilium docs
- Fortio docs
