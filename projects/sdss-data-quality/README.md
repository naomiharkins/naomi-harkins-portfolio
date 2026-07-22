# SDSS Data Quality and Survey Completeness

This case study combines SQL, Python, and scientific data validation across Sloan Digital Sky Survey datasets.

## Verified results

- Queried **164,072 galaxy records** and found **140,967 with spectra**, for **85.918% spectroscopic completeness**.
- Explored completeness by magnitude, color, and surface brightness to identify where missing data may be concentrated.
- Built a separate **62,879-record** massive-galaxy sample and converted right ascension, declination, and redshift into 3D Cartesian positions.
- Used a filtered SQL workflow to reduce a broad sky query to **1,306 nearby, bright, extended objects** for detailed output.

## Quality approach

- Applied explicit SQL filters rather than manually selecting records.
- Corrected observed magnitudes for extinction before downstream analysis.
- Used boolean masks to separate records with and without spectra.
- Kept sample counts and calculation steps visible for reproducibility.
- Documented uncertainty, limitations, and unexpected results instead of hiding them.

## Files

- [`spectroscopic-completeness-query.sql`](spectroscopic-completeness-query.sql)
- [`large-scale-structure-query.sql`](large-scale-structure-query.sql)
- [`completeness_analysis.py`](completeness_analysis.py)
- [`sample-summary.csv`](sample-summary.csv)

The portfolio version focuses on verified outputs and cleaned methodology rather than publishing full course notebooks with exploratory or unfinished cells.
