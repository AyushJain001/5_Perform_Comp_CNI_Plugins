import matplotlib.pyplot as plt

# Hardcoded values derived from measured CSV files (mean throughput across 5 runs).
qps = [100, 300, 500]
flannel_rps = [99.995, 299.983, 499.971]
calico_rps = [99.994, 299.980, 499.963]
cilium_rps = [99.994, 299.981, 499.966]

def ratio_pct(rps_vals, targets):
    return [round((r / t) * 100, 3) for r, t in zip(rps_vals, targets)]

flannel_pct = ratio_pct(flannel_rps, qps)
calico_pct = ratio_pct(calico_rps, qps)
cilium_pct = ratio_pct(cilium_rps, qps)

plt.figure(figsize=(11, 6.5))
plt.plot(qps, qps, color="black", linewidth=2, linestyle=":", label="Target QPS")
plt.plot(qps, flannel_rps, marker="o", markersize=8, linewidth=2.4, color="#1f77b4", label="Flannel")
plt.plot(qps, calico_rps, marker="s", markersize=8, linewidth=2.2, linestyle="--", color="#ff7f0e", label="Calico")
plt.plot(qps, cilium_rps, marker="^", markersize=8, linewidth=2.2, linestyle="-.", color="#2ca02c", label="Cilium")

for x, y in zip(qps, flannel_rps):
    plt.annotate(f"{y:.1f}", (x, y), textcoords="offset points", xytext=(0, 8), ha="center", fontsize=9)
for x, y in zip(qps, calico_rps):
    plt.annotate(f"{y:.1f}", (x, y), textcoords="offset points", xytext=(0, -14), ha="center", fontsize=9)
for x, y in zip(qps, cilium_rps):
    plt.annotate(f"{y:.1f}", (x, y), textcoords="offset points", xytext=(0, 8), ha="center", fontsize=9)

plt.title("G5: Throughput Performance Comparison", fontsize=15, fontweight="bold")
plt.xlabel("Target QPS", fontsize=12, fontweight="bold")
plt.ylabel("Achieved RPS", fontsize=12, fontweight="bold")
plt.xticks(qps, fontsize=11)
plt.yticks(fontsize=11)
plt.grid(alpha=0.35, linestyle=":")
plt.legend(loc="upper left", fontsize=10, frameon=True)
plt.figtext(0.5, 0.01, "Takeaway: all three CNIs maintain nearly identical throughput across tested loads.", ha="center", fontsize=10)
plt.tight_layout(rect=(0, 0.03, 1, 1))
plt.savefig("/home/iiitd/grs/G_5_plots/G_5_throughput_ratio.png", dpi=200)
