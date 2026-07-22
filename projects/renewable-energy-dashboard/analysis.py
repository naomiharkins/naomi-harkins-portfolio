"""Create region-level renewable share and net-production metrics."""

from pathlib import Path
import pandas as pd

summary = pd.read_csv(Path(__file__).with_name("regional-energy-summary.csv"))
print(summary[["Region", "Renewable Percentage", "Net Production"]].to_string(index=False))

eligible = summary[summary["Net Production"] > 0]
if eligible.empty:
    raise ValueError("No region has positive net production.")

recommendation = eligible.sort_values("Renewable Percentage", ascending=False).iloc[0]
print("\nRecommended region from this dashboard logic:")
print(recommendation[["Region", "Renewable Percentage", "Net Production"]])
