"""
utils.py
--------
Shared utility functions used across the project.
"""

from __future__ import annotations

import os
from pathlib import Path

import pandas as pd


# ---------------------------------------------------------------------------
# Path helpers
# ---------------------------------------------------------------------------

def project_root() -> Path:
    """Return the absolute path to the repository root."""
    return Path(__file__).resolve().parents[1]


def data_path(*parts: str) -> Path:
    """Return an absolute path inside the data/ directory."""
    return project_root() / "data" / Path(*parts)


def visuals_path(*parts: str) -> Path:
    """Return an absolute path inside the visuals/ directory."""
    return project_root() / "visuals" / Path(*parts)


# ---------------------------------------------------------------------------
# Country / region helpers
# ---------------------------------------------------------------------------

# Mapping from ISO 3166-1 alpha-2 to full country name (EU-27)
EU27_NAMES: dict[str, str] = {
    "AT": "Austria",
    "BE": "Belgium",
    "BG": "Bulgaria",
    "CY": "Cyprus",
    "CZ": "Czechia",
    "DE": "Germany",
    "DK": "Denmark",
    "EE": "Estonia",
    "EL": "Greece",
    "ES": "Spain",
    "FI": "Finland",
    "FR": "France",
    "HR": "Croatia",
    "HU": "Hungary",
    "IE": "Ireland",
    "IT": "Italy",
    "LT": "Lithuania",
    "LU": "Luxembourg",
    "LV": "Latvia",
    "MT": "Malta",
    "NL": "Netherlands",
    "PL": "Poland",
    "PT": "Portugal",
    "RO": "Romania",
    "SE": "Sweden",
    "SI": "Slovenia",
    "SK": "Slovakia",
}


def iso2_to_name(code: str) -> str:
    """Convert an ISO 3166-1 alpha-2 code to the full country name."""
    return EU27_NAMES.get(code.upper(), code)


def name_to_iso2(name: str) -> str | None:
    """Convert a full country name to its ISO 3166-1 alpha-2 code, or None."""
    reverse = {v.lower(): k for k, v in EU27_NAMES.items()}
    return reverse.get(name.lower())


# ---------------------------------------------------------------------------
# I/O helpers
# ---------------------------------------------------------------------------

def read_csv_safe(filepath: str | Path, **kwargs) -> pd.DataFrame:
    """
    Read a CSV file with a helpful error message if the file is not found.

    Parameters
    ----------
    filepath : str or Path
    **kwargs : passed to pd.read_csv

    Returns
    -------
    pd.DataFrame
    """
    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(
            f"File not found: {filepath}\n"
            "Make sure you have downloaded the raw data and placed it in data/raw/."
        )
    return pd.read_csv(filepath, **kwargs)


def ensure_dir(path: str | Path) -> Path:
    """Create directory (and parents) if it does not exist."""
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


if __name__ == "__main__":
    print(f"Project root: {project_root()}")
    print(f"EU-27 countries: {list(EU27_NAMES.keys())}")
