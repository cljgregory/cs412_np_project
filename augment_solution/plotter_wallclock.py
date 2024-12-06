# AUSTIN PERDUE
# PLOTTER FOR COMPARISON RESULTS
# PLOTS THE WALL CLOCK RUNTIME FOR EACH TEST CASE
# SAVES THE PLOT AS "runtime_comparison_log_scale.png"

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
df = pd.read_csv('test_cases/outputs/comparison_results.tsv', sep='\t')

# Check if necessary columns exist
runtime_columns = ["Exact Time", "Approx Time", "Augment Time"]
for col in runtime_columns:
    if col not in df.columns:
        raise ValueError(f"Column '{col}' not found in the data file.")

# Convert runtime strings to seconds
def convert_time_to_seconds(time_str):
    if "seconds" in time_str:
        return float(time_str.split()[0])
    elif "minutes" in time_str:
        parts = time_str.split()
        return float(parts[0]) * 60 + float(parts[2])
    else:
        return float(time_str)

df["Exact Time (s)"] = df["Exact Time"].apply(convert_time_to_seconds)
df["Approx Time (s)"] = df["Approx Time"].apply(convert_time_to_seconds)
df["Augment Time (s)"] = df["Augment Time"].apply(convert_time_to_seconds)

# DEBUG: Print the converted times to verify
print("Converted Runtimes (in seconds):")
print(df[["Test Case", "Exact Time (s)", "Approx Time (s)", "Augment Time (s)"]])

# Set up the bar positions
x = np.arange(len(df["Test Case"]))  # the label locations
width = 0.25  # the width of the bars

# ----------- Plot with Logarithmic Scale ----------- #
plt.figure(figsize=(14, 8))
plt.bar(x - width, df["Exact Time (s)"], width, label="Exact", color='blue')
plt.bar(x, df["Approx Time (s)"], width, label="Approx", color='green')
plt.bar(x + width, df["Augment Time (s)"], width, label="DSATUR (Augment)", color='orange')

# Labels and title
plt.xlabel("Test Case", fontsize=14)
plt.ylabel("Runtime (seconds)", fontsize=14)
plt.title("Comparison of Coloring Solutions Runtimes (Log Scale)", fontsize=16)

# Set y-axis to logarithmic scale
plt.yscale('log')

# X-axis ticks
plt.xticks(x, df["Test Case"], rotation=45)

# Legend positioned at the top right
plt.legend(loc="upper right")

# Add grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Layout adjustments
plt.tight_layout()

# Save and show the plot
plt.savefig("runtime_comparison_log_scale.png")
plt.show()

# ----------- Plot with Linear Scale for Small Runtimes ----------- #
plt.figure(figsize=(14, 8))
plt.bar(x - width, df["Approx Time (s)"], width, label="Approx", color='green')
plt.bar(x, df["Augment Time (s)"], width, label="DSATUR (Augment)", color='orange')

# Labels and title
plt.xlabel("Test Case", fontsize=14)
plt.ylabel("Runtime (seconds)", fontsize=14)
plt.title("Comparison of Approximation and DSATUR Runtimes (Linear Scale)", fontsize=16)

# X-axis ticks
plt.xticks(x, df["Test Case"], rotation=45)

# Legend positioned at the top right
plt.legend(loc="upper right")

# Add grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Layout adjustments
plt.tight_layout()

# Save and show the plot
plt.savefig("runtime_comparison_small_linear_scale.png")
plt.show()
