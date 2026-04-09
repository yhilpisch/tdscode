"""
Figure-generation helpers for Module 3 of The Data Scientist.

This module focuses on small, reproducible scripts that generate PDF figures
for inclusion in the LaTeX book. Each function is designed to be executable as
written and to save its output into the book-local ``figures/`` directory.
"""

from __future__ import annotations

import os
import random
from pathlib import Path

mplconfig = Path(__file__).resolve().parent.parent / "artifacts" / "mplconfig"
mplconfig.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(mplconfig))
os.environ.setdefault("LOKY_MAX_CPU_COUNT", "1")

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


def simulate_ten_flip_counts(num_trials: int = 10_000, seed: int = 42) -> np.ndarray:
    """Simulate ``num_trials`` experiments of 10 fair coin flips each.

    Every experiment records the number of heads in ten flips. The function
    returns a one-dimensional NumPy array of length ``num_trials`` containing
    these counts.
    """
    rng = random.Random(seed)
    counts: list[int] = []

    for _ in range(num_trials):
        heads = 0
        for _ in range(10):
            if rng.random() < 0.5:
                heads += 1
        counts.append(heads)

    return np.array(counts, dtype=int)


def coin_heads_histogram(
    num_trials: int = 10_000,
    seed: int = 42,
    output_name: str = "fig_coin_heads_hist.pdf",
) -> Path:
    """Generate a histogram of heads counts for ten fair coin flips.

    The function simulates ``num_trials`` experiments, each consisting of ten
    fair coin flips, then plots the distribution of the number of heads
    observed in each experiment. The resulting figure is saved as a PDF in the
    book-local ``figures/`` folder and the full path is returned.
    """
    counts = simulate_ten_flip_counts(num_trials=num_trials, seed=seed)

    base_dir = Path(__file__).resolve().parent.parent
    figures_dir = base_dir / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    output_path = figures_dir / output_name

    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots(figsize=(6.0, 4.0))

    ax.hist(
        counts,
        bins=range(0, 12),  # 0 through 11, covering all possible counts
        align="left",
        edgecolor="black",
        alpha=0.85,
    )
    ax.set_xlabel("Number of heads in 10 flips")
    ax.set_ylabel("Number of experiments")
    ax.set_title("Distribution of Heads Counts in Ten Coin Flips")
    ax.grid(axis="y", alpha=0.35, linestyle="--", linewidth=0.6)

    fig.tight_layout()
    fig.savefig(output_path, format="pdf")
    plt.close(fig)

    return output_path


def clustering_pca_demo(
    num_points: int = 200,
    seed: int = 0,
    output_name: str = "fig_clustering_pca.pdf",
) -> Path:
    """Generate a PCA projection colored by clustering labels.

    The function creates a small synthetic dataset with two rough groups in
    three dimensions, fits a KMeans clustering model, projects the data down to
    two dimensions with PCA, and plots the result with cluster labels shown as
    colors. The resulting figure is saved as a PDF in the book-local
    ``figures/`` folder and the full path is returned.
    """
    rng = np.random.default_rng(seed=seed)

    # Two rough groups in 3D space.
    group_1 = rng.normal(loc=[0.0, 0.0, 0.0], scale=0.6, size=(num_points // 2, 3))
    group_2 = rng.normal(loc=[3.0, 3.0, 0.0], scale=0.6, size=(num_points // 2, 3))
    data = np.vstack([group_1, group_2])

    kmeans = KMeans(n_clusters=2, random_state=seed)
    labels = kmeans.fit_predict(data)

    pca = PCA(n_components=2, random_state=seed)
    reduced = pca.fit_transform(data)

    base_dir = Path(__file__).resolve().parent.parent
    figures_dir = base_dir / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    output_path = figures_dir / output_name

    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots(figsize=(6.0, 4.0))

    scatter = ax.scatter(
        reduced[:, 0],
        reduced[:, 1],
        c=labels,
        cmap="tab10",
        alpha=0.85,
        edgecolor="black",
        linewidth=0.4,
    )
    ax.set_xlabel("PC 1")
    ax.set_ylabel("PC 2")
    ax.set_title("PCA Projection Colored by KMeans Clusters")
    ax.grid(alpha=0.35, linestyle="--", linewidth=0.6)

    fig.tight_layout()
    fig.savefig(output_path, format="pdf")
    plt.close(fig)

    return output_path


if __name__ == "__main__":
    # When this module is run as a script, generate the main figures used in
    # Module 3 of the book.
    heads_path = coin_heads_histogram()
    print(f"Saved histogram to {heads_path}")

    clustering_path = clustering_pca_demo()
    print(f"Saved clustering/PCA figure to {clustering_path}")
