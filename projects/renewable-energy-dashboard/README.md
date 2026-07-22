# Renewable Energy and Net Production Dashboard

This Tableau project combined three management views: net production, renewable energy as a share of generation, and energy-source mix by region. The workbook used interactive region and period controls so a reviewer could compare locations and timeframes without rebuilding the chart.

## Key findings from the source data

- **Northwest (NW): 52.25% renewable generation** with a positive net-production balance of **21.69 million** in the dataset's annual aggregate.
- **California (CAL): 37.45% renewable generation**, but a negative net-production balance of **-64.94 million**.
- NW's renewable share remained higher than CAL's across the monthly comparison, while CAL showed stronger seasonal swings.

## Recommendation

Using the dashboard's two primary decision factors—renewable share and ability to generate more than regional demand—the Northwest was the strongest candidate among the regions reviewed.

## Quality and usability work

- Created calculated fields for net production and renewable percentage.
- Checked null values before interpreting regional differences.
- Used dropdown parameters for region and period selection.
- Combined multiple charts into a management-oriented dashboard rather than presenting disconnected worksheets.

## Files

- [`regional-energy-summary.csv`](regional-energy-summary.csv): region-level aggregate used for the portfolio
- [`analysis.py`](analysis.py): reproducible selection logic

The portfolio includes a compact aggregate rather than the full 500,000-plus-row course dataset.
