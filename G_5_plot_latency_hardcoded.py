import matplotlib.pyplot as plt

# Hardcoded values derived from measured CSV files for final submission.
qps = [100, 300, 500, 800]
flannel_p99 = [1.5, 1.6, 1.7, 1.4]
calico_p99 = [1.5, 1.7, 1.7, 1.4]
cilium_p99 = [1.6, 1.8, 1.6, 1.1]

plt.figure(figsize=(9, 5))
plt.plot(qps, flannel_p99, marker="o", linewidth=2, label="Flannel p99")
plt.plot(qps, calico_p99, marker="s", linewidth=2, label="Calico p99")
plt.plot(qps, cilium_p99, marker="^", linewidth=2, label="Cilium p99")

plt.title("G5: p99 Latency vs QPS ")
plt.xlabel("QPS")
plt.ylabel("Latency (ms)")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("/home/iiitd/grs/G_5_plots/G_5_p99_latency.png", dpi=200)
