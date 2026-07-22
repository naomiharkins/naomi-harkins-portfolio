"""Small, reproducible summary of the verified SDSS completeness result."""

TOTAL_GALAXIES = 164_072
WITH_SPECTRA = 140_967


def completeness(total: int, with_spectra: int) -> float:
    if total <= 0:
        raise ValueError("total must be positive")
    if not 0 <= with_spectra <= total:
        raise ValueError("with_spectra must be between 0 and total")
    return with_spectra / total


if __name__ == "__main__":
    value = completeness(TOTAL_GALAXIES, WITH_SPECTRA)
    print(f"Spectroscopic completeness: {value:.3%}")
    print(f"Missing spectra: {TOTAL_GALAXIES - WITH_SPECTRA:,}")
