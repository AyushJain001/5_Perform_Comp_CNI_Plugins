import matplotlib.pyplot as plt
import numpy as np

# Hardcoded values derived from measured CSV files for final submission.
cnis = ["Flannel", "Calico", "Cilium"]
cpu_mcores = [124.0, 167.0, 196.0]
mem_mib = [628.0, 1070.0, 1239.0]

x = np.arange(len(cnis))
width = 0.36

fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(x - width / 2, cpu_mcores, width, label="CPU (mcores)")
ax.bar(x + width / 2, mem_mib, width, label="Memory (MiB)")

ax.set_title("G5: CNI Resource Overhead")
ax.set_xticks(x)
ax.set_xticklabels(cnis)
ax.set_ylabel("Usage")
ax.grid(axis="y", alpha=0.3)
ax.legend()
fig.tight_layout()
fig.savefig("/home/iiitd/grs/G_5_plots/G_5_resource_overhead.png", dpi=200)
