"""
data_cleaning.py
----------------
Functions for cleaning and standardising the raw datasets before integration.

Inputs:  data/raw/
Outputs: data/interim/
"""

import pandas as pd


# ---------------------------------------------------------------------------
# EIGE Gender Equality Index
# ---------------------------------------------------------------------------

def load_eige_raw(filepath: str) -> pd.DataFrame:
    """Load the raw EIGE Gender Equality Index file."""
    # TODO: adjust separator / sheet name as needed after downloading the file
    df = pd.read_csv(filepath)
    return df


def clean_eige(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardise the EIGE dataset.

    Steps (to be implemented):
    - Rename columns to snake_case
    - Filter to EU-27 countries only
    - Handle missing values
    - Ensure 'country_code' uses ISO 3166-1 alpha-2
    - Ensure 'year' is an integer
    """
    # TODO: implement cleaning logic
    raise NotImplementedError("clean_eige() is not yet implemented.")


# ---------------------------------------------------------------------------
# Eurostat Prison Statistics
# ---------------------------------------------------------------------------

def load_eurostat_raw(filepath: str) -> pd.DataFrame:
    """Load the raw Eurostat prison statistics file."""
    # TODO: adjust parameters after downloading the file
    df = pd.read_csv(filepath)
    return df


def clean_eurostat(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardise the Eurostat prison statistics dataset.

    Steps (to be implemented):
    - Rename columns to snake_case
    - Filter to EU-27 countries only
    - Compute female share (%) if not already present
    - Handle missing values and flagged / unreliable observations
    - Ensure 'country_code' uses ISO 3166-1 alpha-2
    - Ensure 'year' is an integer
    """
    # TODO: implement cleaning logic
    raise NotImplementedError("clean_eurostat() is not yet implemented.")


# ---------------------------------------------------------------------------
# Entry point (for quick testing)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("data_cleaning.py — placeholder. Implement functions above.")
