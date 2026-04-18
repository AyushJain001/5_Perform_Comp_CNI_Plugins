import matplotlib.pyplot as plt

# Hardcoded p99 latency stats (ms) from measured CSV (5 runs per QPS).
qps = [100, 300, 500]

flannel_mean = [1.539, 1.627, 1.713]
flannel_min = [1.282, 1.584, 1.617]
flannel_max = [1.741, 1.654, 1.790]

calico_mean = [1.479, 1.663, 1.711]
calico_min = [1.201, 1.428, 1.407]
calico_max = [1.772, 1.810, 1.818]

cilium_mean = [1.622, 1.787, 1.645]
cilium_min = [1.436, 1.629, 1.485]
cilium_max = [1.863, 1.842, 1.797]

plt.figure(figsize=(10, 6))

plt.fill_between(qps, flannel_min, flannel_max, color="#1f77b4", alpha=0.12)
plt.fill_between(qps, calico_min, calico_max, color="#ff7f0e", alpha=0.12)
plt.fill_between(qps, cilium_min, cilium_max, color="#2ca02c", alpha=0.12)

plt.plot(qps, flannel_mean, marker="o", linewidth=2.6, color="#1f77b4", label="Flannel mean p99")
plt.plot(qps, calico_mean, marker="s", linewidth=2.4, linestyle="--", color="#ff7f0e", label="Calico mean p99")
plt.plot(qps, cilium_mean, marker="^", linewidth=2.4, linestyle="-.", color="#2ca02c", label="Cilium mean p99")

plt.title("G5: p99 Latency with Run-to-Run Variability", fontsize=15, fontweight="bold")
plt.xlabel("QPS", fontsize=12, fontweight="bold")
plt.ylabel("p99 Latency (ms)", fontsize=12, fontweight="bold")
plt.xticks(qps, fontsize=11)
plt.yticks(fontsize=11)
plt.grid(alpha=0.35, linestyle=":")
plt.legend(loc="upper right", fontsize=10, frameon=True)
plt.tight_layout()
plt.savefig("/home/iiitd/grs/G_5_plots/G_5_latency_variability.png", dpi=200)
