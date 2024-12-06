# AUSTIN PERDUE
# PLOTTER FOR COMPARISON RESULTS
# PLOTS THE NUMBER OF COLORS AND BOUNDS FOR EACH TEST CASE
# SAVES THE PLOT AS "color_comparison_dual_axes.png"

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
df = pd.read_csv('test_cases/outputs/comparison_results.tsv', sep='\t')

# Set up positions and width
x = np.arange(len(df["Test Case"]))
width = 0.2

fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot bar graphs for color counts
ax1.bar(x - width, df["Exact Colors"], width, label="Exact")
ax1.bar(x, df["Approx Colors"], width, label="Approx")
ax1.bar(x + width, df["Augment Colors"], width, label="DSATUR (Augment)")

ax1.set_xlabel("Test Case")
ax1.set_ylabel("Number of Colors")
ax1.set_xticks(x)
ax1.set_xticklabels(df["Test Case"], rotation=45)

# Plot bounds on a secondary y-axis
if "Lower Bound" in df.columns and "Upper Bound" in df.columns:
    ax2 = ax1.twinx()
    ax2.plot(x, df["Lower Bound"], 'k--', label='Lower Bound')
    ax2.plot(x, df["Upper Bound"], 'k-', label='Upper Bound')
    ax2.set_ylabel("Bounds")

# Combine legends from both axes
fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
plt.title("Comparison of Coloring Solutions with Bounds")
plt.tight_layout()
plt.savefig("color_comparison_dual_axes.png")
plt.show()