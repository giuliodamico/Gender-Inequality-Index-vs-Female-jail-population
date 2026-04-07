"""
eda.py
------
Exploratory data analysis helpers: summary statistics, correlation, and
quick-look plotting functions.

Inputs:  data/processed/
"""

from __future__ import annotations

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ---------------------------------------------------------------------------
# Summary statistics
# ---------------------------------------------------------------------------

def describe_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Return descriptive statistics for numeric columns."""
    return df.describe().T


def missing_values_report(df: pd.DataFrame) -> pd.DataFrame:
    """Return a DataFrame with count and share of missing values per column."""
    missing = df.isna().sum()
    share = missing / len(df)
    return pd.DataFrame({"missing_count": missing, "missing_share": share}).sort_values(
        "missing_count", ascending=False
    )


# ---------------------------------------------------------------------------
# Correlation
# ---------------------------------------------------------------------------

def correlation_matrix(df: pd.DataFrame, columns: list[str] | None = None) -> pd.DataFrame:
    """
    Compute the Pearson correlation matrix for the selected columns.

    Parameters
    ----------
    df : pd.DataFrame
    columns : list of str, optional
        Subset of columns. If None, all numeric columns are used.
    """
    subset = df[columns] if columns else df.select_dtypes("number")
    return subset.corr()


# ---------------------------------------------------------------------------
# Quick-look plots
# ---------------------------------------------------------------------------

def plot_scatter(
    df: pd.DataFrame,
    x: str,
    y: str,
    hue: str | None = None,
    title: str = "",
    save_path: str | None = None,
) -> plt.Figure:
    """
    Scatter plot of x vs y, optionally coloured by a categorical variable.

    Parameters
    ----------
    df : pd.DataFrame
    x, y : str
        Column names for the axes.
    hue : str, optional
        Column name used for colour encoding (e.g. 'region').
    title : str
        Plot title.
    save_path : str, optional
        If provided, save the figure to this path.
    """
    fig, ax = plt.subplots(figsize=(9, 6))
    sns.scatterplot(data=df, x=x, y=y, hue=hue, ax=ax, s=80)
    ax.set_title(title)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    plt.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150)
    return fig


def plot_trend(
    df: pd.DataFrame,
    x: str,
    y: str,
    group: str,
    title: str = "",
    save_path: str | None = None,
) -> plt.Figure:
    """
    Line plot of y over x, with one line per group (e.g. country or region).

    Parameters
    ----------
    df : pd.DataFrame
    x : str
        Column for the horizontal axis (e.g. 'year').
    y : str
        Column for the vertical axis.
    group : str
        Column used to draw separate lines.
    title : str
        Plot title.
    save_path : str, optional
        If provided, save the figure to this path.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    for name, grp in df.groupby(group):
        ax.plot(grp[x], grp[y], marker="o", label=name)
    ax.set_title(title)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.legend(bbox_to_anchor=(1.01, 1), loc="upper left", fontsize=8)
    plt.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150)
    return fig


if __name__ == "__main__":
    print("eda.py — placeholder. Implement / call functions above.")
