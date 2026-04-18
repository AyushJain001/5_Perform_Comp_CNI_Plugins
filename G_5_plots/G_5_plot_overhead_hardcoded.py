import matplotlib.pyplot as plt
import numpy as np

# Hardcoded values derived from measured CSV files for final submission.
cnis = ["Flannel", "Calico", "Cilium"]
cpu_mcores = [124.0, 167.0, 196.0]
mem_mib = [628.0, 1070.0, 1239.0]

x = np.arange(len(cnis))
width = 0.34

fig, ax = plt.subplots(figsize=(10, 6))
cpu_bars = ax.bar(x - width / 2, cpu_mcores, width, label="CPU (mcores)", color="#1f77b4", edgecolor="white", linewidth=1)
mem_bars = ax.bar(x + width / 2, mem_mib, width, label="Memory (MiB)", color="#ff7f0e", edgecolor="white", linewidth=1)

for bar in cpu_bars:
	h = bar.get_height()
	ax.text(bar.get_x() + bar.get_width() / 2, h + 16, f"{h:.0f}", ha="center", va="bottom", fontsize=10, fontweight="bold", color="#1f77b4")
for bar in mem_bars:
	h = bar.get_height()
	ax.text(bar.get_x() + bar.get_width() / 2, h + 16, f"{h:.0f}", ha="center", va="bottom", fontsize=10, fontweight="bold", color="#ff7f0e")

ax.set_title("G5: CNI Resource Overhead", fontsize=15, fontweight="bold")
ax.set_xticks(x)
ax.set_xticklabels(cnis, fontsize=11, fontweight="bold")
ax.set_ylabel("Usage", fontsize=12, fontweight="bold")
ax.tick_params(axis="y", labelsize=11)
ax.grid(axis="y", alpha=0.35, linestyle=":", linewidth=1)
ax.legend(loc="upper left", fontsize=10, frameon=True)
fig.tight_layout()
fig.savefig("/home/iiitd/grs/G_5_plots/G_5_resource_overhead.png", dpi=200)
