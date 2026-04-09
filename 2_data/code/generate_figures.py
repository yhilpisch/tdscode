"""Generate matplotlib figures for Module 2.

Each function in this module produces a single PDF file in the book-local
``figures/`` folder. Filenames are wired into ``figures.tex`` via macros such
as ``\\DataTwoTrendPlotFigure`` and are included from the text via ``\\Cref``.

The naming pattern is:

- function name describes the visual (for maintainers),
- output filename begins with ``fig_`` and matches the captioned figure,
- figures are saved as PDF for clean LaTeX integration.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTDIR = Path(__file__).resolve().parent.parent / "figures"
OUTDIR.mkdir(parents=True, exist_ok=True)

# Keep the plotting style consistent with the LaTeX examples.
plt.style.use("seaborn-v0_8")


def monthly_signups_figure() -> None:
    """Generate the line chart used in Chapter 1."""
    months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun"])
    signups = np.array([42, 48, 51, 57, 61, 66])

    fig, ax = plt.subplots(figsize=(6.6, 3.8))
    ax.plot(
        months,
        signups,
        marker="o",
        linewidth=2.0,
        color="#0B3C78",
    )
    ax.set_title("Monthly Signups")
    ax.set_xlabel("Month")
    ax.set_ylabel("New Signups")
    ax.grid(
        axis="y",
        alpha=0.45,
        linestyle="--",
        linewidth=0.6,
    )
    fig.tight_layout()
    fig.savefig(OUTDIR / "fig_monthly_signups.pdf")
    plt.close(fig)


def quiz_scores_histogram() -> None:
    """Generate the histogram used in Chapter 2."""
    scores = np.array([61, 75, 88, 92, 79, 84, 73, 95, 68, 81, 77, 89])

    fig, ax = plt.subplots(figsize=(6.6, 3.8))
    ax.hist(
        scores,
        bins=[60, 70, 80, 90, 100],
        color="#2A7F62",
        edgecolor="white",
    )
    ax.set_title("Quiz Score Distribution")
    ax.set_xlabel("Score")
    ax.set_ylabel("Count")
    ax.grid(
        axis="y",
        alpha=0.45,
        linestyle="--",
        linewidth=0.6,
    )
    fig.tight_layout()
    fig.savefig(OUTDIR / "fig_quiz_scores_hist.pdf")
    plt.close(fig)


def signups_by_channel_bar_chart() -> None:
    """Generate the bar chart of total signups by channel for Chapter 5."""
    # The small example mirrors the grouped table in the text:
    # search and social are the main channels, email is much smaller.
    channels = np.array(["search", "social", "email"])
    totals = np.array([97, 93, 17])  # total signups per channel

    fig, ax = plt.subplots(figsize=(6.0, 3.6))
    ax.bar(channels, totals, color="#0B3C78")
    ax.set_title("Total Signups by Channel")
    ax.set_xlabel("Channel")
    ax.set_ylabel("Total Signups")
    ax.grid(
        axis="y",
        alpha=0.35,
        linestyle="--",
        linewidth=0.6,
    )
    fig.tight_layout()
    fig.savefig(OUTDIR / "fig_signups_by_channel.pdf")
    plt.close(fig)


def visits_vs_signups_scatter() -> None:
    """Generate the scatter plot of site visits versus signups for Chapter 5."""
    # These synthetic values match the teaching example in Chapter 5:
    # more visits generally lead to more signups.
    visits = np.array([100, 120, 150, 180, 210, 240])
    signups = np.array([8, 11, 15, 19, 21, 25])

    fig, ax = plt.subplots(figsize=(6.0, 3.6))
    ax.scatter(visits, signups, color="#0B3C78")
    ax.set_title("Site Visits vs Signups")
    ax.set_xlabel("Visits")
    ax.set_ylabel("Signups")
    ax.grid(
        axis="y",
        alpha=0.35,
        linestyle="--",
        linewidth=0.6,
    )
    fig.tight_layout()
    fig.savefig(OUTDIR / "fig_visits_vs_signups.pdf")
    plt.close(fig)


def country_total_amounts_bar_chart() -> None:
    """Generate the bar chart of total order amounts by country for Chapter 6."""
    # Synthetic example mirroring the country_summary in the text:
    # three countries with different total order amounts.
    countries = np.array(["DE", "US", "UK"])
    totals = np.array([4200.0, 3800.0, 2500.0])  # total order amount per country

    fig, ax = plt.subplots(figsize=(6.0, 3.6))
    ax.bar(countries, totals, color="#0B3C78")
    ax.set_title("Total Order Amount by Country")
    ax.set_xlabel("Country")
    ax.set_ylabel("Total Amount")
    ax.grid(
        axis="y",
        alpha=0.35,
        linestyle="--",
        linewidth=0.6,
    )
    fig.tight_layout()
    fig.savefig(OUTDIR / "fig_country_total_amounts.pdf")
    plt.close(fig)


if __name__ == "__main__":
    # Run this script to regenerate the PDF figures used in the book text.
    monthly_signups_figure()
    quiz_scores_histogram()
    signups_by_channel_bar_chart()
    visits_vs_signups_scatter()
    country_total_amounts_bar_chart()
