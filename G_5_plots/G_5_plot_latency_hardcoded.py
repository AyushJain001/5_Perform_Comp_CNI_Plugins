import matplotlib.pyplot as plt

# Hardcoded values derived from measured CSV files for final submission.

qps = [100, 300, 500]
flannel_p99 = [1.5, 1.6, 1.7]
calico_p99 = [1.5, 1.7, 1.7]
cilium_p99 = [1.6, 1.8, 1.6]

plt.figure(figsize=(10, 6))

# Draw Calico first so overlapping Flannel points remain visible on top.
plt.plot(
	qps,
	calico_p99,
	marker="s",
	markersize=8,
	markeredgecolor="white",
	markeredgewidth=1.2,
	linewidth=2.2,
	linestyle="--",
	color="#ff7f0e",
	label="Calico p99",
	zorder=2,
)
plt.plot(
	qps,
	flannel_p99,
	marker="o",
	markersize=9,
	markeredgecolor="white",
	markeredgewidth=1.2,
	linewidth=2.8,
	linestyle="-",
	color="#1f77b4",
	label="Flannel p99",
	zorder=3,
)
plt.plot(
	qps,
	cilium_p99,
	marker="^",
	markersize=8,
	markeredgecolor="white",
	markeredgewidth=1.2,
	linewidth=2.2,
	linestyle="-.",
	color="#2ca02c",
	label="Cilium p99",
	zorder=2,
)

# Small per-series offsets keep equal-value labels readable at overlapping points.
for x, y in zip(qps, flannel_p99):
    plt.annotate(f"{y:.1f}", (x, y), textcoords="offset points", xytext=(0, 9), ha="center", fontsize=9, color="#1f77b4", fontweight="bold")
for x, y in zip(qps, calico_p99):
    plt.annotate(f"{y:.1f}", (x, y), textcoords="offset points", xytext=(0, -16), ha="center", fontsize=9, color="#ff7f0e", fontweight="bold")
for x, y in zip(qps, cilium_p99):
    plt.annotate(f"{y:.1f}", (x, y), textcoords="offset points", xytext=(0, 9), ha="center", fontsize=9, color="#2ca02c", fontweight="bold")

plt.title("G5: p99 Latency vs QPS", fontsize=15, fontweight="bold")
plt.xlabel("QPS", fontsize=12, fontweight="bold")
plt.ylabel("Latency (ms)", fontsize=12, fontweight="bold")
plt.xticks(qps, fontsize=11)
plt.yticks(fontsize=11)
plt.ylim(1.0, 1.9)
plt.grid(alpha=0.35, linestyle=":", linewidth=1)
plt.legend(loc="upper right", fontsize=10, frameon=True)
plt.tight_layout()
plt.savefig("/home/iiitd/grs/G_5_plots/G_5_p99_latency.png", dpi=200)
