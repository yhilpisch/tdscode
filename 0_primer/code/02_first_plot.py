"""
The Data Scientist
Book 0 · Python Primer for Data Science
Chapter 02 · First Plot

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

from __future__ import annotations

from math import pi, sin
from pathlib import Path


FIGURE_PATH = Path("figures") / "primer_sine.svg"


def build_series(num_points: int = 200) -> list[tuple[float, float]]:
    """Return x/y pairs for a smooth sine curve."""
    step = (2.0 * pi) / (num_points - 1)
    points = []
    for idx in range(num_points):
        x_value = idx * step
        y_value = sin(x_value)
        points.append((x_value, y_value))
    return points


def to_svg_polyline(points: list[tuple[float, float]]) -> str:
    """Convert mathematical points into a small SVG plot."""
    width = 720
    height = 360
    padding = 30
    x_max = 2.0 * pi
    y_min, y_max = -1.0, 1.0

    # Scale the mathematical coordinates into SVG pixel coordinates.
    scaled = []
    for x_value, y_value in points:
        px = padding + (x_value / x_max) * (width - 2 * padding)
        py = padding + (1 - (y_value - y_min) / (y_max - y_min)) * (
            height - 2 * padding
        )
        scaled.append(f"{px:.1f},{py:.1f}")

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <rect width="100%" height="100%" fill="white" />
  <line x1="{padding}" y1="{height / 2:.1f}" x2="{width - padding}" y2="{height / 2:.1f}" stroke="#999" stroke-width="1" />
  <line x1="{padding}" y1="{padding}" x2="{padding}" y2="{height - padding}" stroke="#999" stroke-width="1" />
  <polyline fill="none" stroke="#0B3C78" stroke-width="3" points="{' '.join(scaled)}" />
  <text x="{padding}" y="22" font-size="18" font-family="Arial, sans-serif">A First Saved Plot</text>
  <text x="{width - 140}" y="{height - 12}" font-size="14" font-family="Arial, sans-serif">x from 0 to 2π</text>
  <text x="10" y="{padding + 10}" font-size="14" font-family="Arial, sans-serif">sin(x)</text>
</svg>
"""


def save_sine_plot(path: Path = FIGURE_PATH) -> Path:
    """Save the SVG plot and return the output path."""
    path.parent.mkdir(parents=True, exist_ok=True)
    svg_text = to_svg_polyline(build_series())
    path.write_text(svg_text, encoding="utf-8")
    return path


def inspect_plot_inputs() -> None:
    """Print a tiny preview so the saved figure does not feel magical."""
    preview = build_series(num_points=5)
    rounded = [(round(x_value, 3), round(y_value, 3)) for x_value, y_value in preview]
    print("Preview of plotting inputs")
    for idx, pair in enumerate(rounded, start=1):
        print(f"  point {idx}: x={pair[0]}, y={pair[1]}")


def main() -> None:
    inspect_plot_inputs()
    out_path = save_sine_plot()
    print(f"Figure saved to {out_path.resolve()}")


if __name__ == "__main__":
    main()
