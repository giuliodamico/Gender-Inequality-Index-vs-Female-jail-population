"""
integration.py
--------------
Merge and integrate cleaned datasets into a single analysis-ready file.

Inputs:  data/interim/
Outputs: data/processed/
"""

import pandas as pd

# Regional grouping of EU-27 countries (ISO 3166-1 alpha-2 codes)
REGIONAL_GROUPS = {
    "Northern Europe": ["DK", "EE", "FI", "IE", "LT", "LV", "SE"],
    "Eastern Europe": ["BG", "CZ", "HR", "HU", "PL", "RO", "SI", "SK"],
    "Central-Southern Europe": [
        "AT", "BE", "CY", "DE", "EL", "ES", "FR", "IT",
        "LU", "MT", "NL", "PT",
    ],
}

EU27_CODES = [code for codes in REGIONAL_GROUPS.values() for code in codes]


def add_regional_group(df: pd.DataFrame, country_col: str = "country_code") -> pd.DataFrame:
    """Add a 'region' column based on REGIONAL_GROUPS mapping."""
    code_to_region = {
        code: region
        for region, codes in REGIONAL_GROUPS.items()
        for code in codes
    }
    df = df.copy()
    df["region"] = df[country_col].map(code_to_region)
    unmapped = df[df["region"].isna()][country_col].unique()
    if len(unmapped) > 0:
        print(f"[WARNING] Countries not mapped to a region: {unmapped}")
    return df


def merge_datasets(
    eige: pd.DataFrame,
    eurostat: pd.DataFrame,
    on: list[str] | None = None,
    how: str = "inner",
) -> pd.DataFrame:
    """
    Merge the cleaned EIGE and Eurostat datasets.

    Parameters
    ----------
    eige : pd.DataFrame
        Cleaned EIGE Gender Equality Index data.
    eurostat : pd.DataFrame
        Cleaned Eurostat prison statistics data.
    on : list of str, optional
        Columns to merge on. Defaults to ['country_code', 'year'].
    how : str
        Type of merge ('inner', 'left', 'outer'). Default is 'inner'.

    Returns
    -------
    pd.DataFrame
        Merged dataset with a 'region' column added.
    """
    if on is None:
        on = ["country_code", "year"]

    # TODO: implement merge logic after cleaning functions are ready
    raise NotImplementedError("merge_datasets() is not yet implemented.")


def save_processed(df: pd.DataFrame, filepath: str) -> None:
    """Save the processed dataset to CSV."""
    df.to_csv(filepath, index=False)
    print(f"Saved processed dataset to {filepath}  ({len(df)} rows)")


if __name__ == "__main__":
    print("integration.py — placeholder. Implement functions above.")
