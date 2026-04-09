"""
The Data Scientist
Notebook Validation Helper

Validate notebooks across all book notebook folders by checking structure,
import availability, and optional execution.

Usage
  python tools/validate_notebooks.py                   # validate all notebooks
  python tools/validate_notebooks.py 2_data/notebooks/*.ipynb
  python tools/validate_notebooks.py --skip-execute
"""
from __future__ import annotations

import argparse
import ast
import importlib
import os
import sys
import time
import warnings
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

ROOT = Path(__file__).resolve().parents[1]
NB_ROOTS = [ROOT / "0_primer" / "notebooks", ROOT / "1_data" / "notebooks", ROOT / "2_data" / "notebooks", ROOT / "3_data" / "notebooks", ROOT / "4_data" / "notebooks"]
BULLET = "  •"

warnings.filterwarnings("ignore", message="Cell is missing an id field")


def format_duration(seconds: float) -> str:
    if seconds < 0.001:
        return f"{seconds * 1_000_000:.1f}µs"
    if seconds < 1.0:
        return f"{seconds * 1_000:.1f}ms"
    return f"{seconds:.2f}s"


def collect_modules(nb_source: Sequence[str]) -> List[str]:
    modules = set()
    for src in nb_source:
        try:
            node = ast.parse(src)
        except SyntaxError:
            continue
        for stmt in ast.walk(node):
            if isinstance(stmt, ast.Import):
                for alias in stmt.names:
                    modules.add(alias.name.split(".")[0])
            elif isinstance(stmt, ast.ImportFrom):
                if stmt.module:
                    modules.add(stmt.module.split(".")[0])
    return sorted(m for m in modules if m and not m.startswith("."))


def check_structure(nb_path: Path):
    import nbformat
    import uuid

    t0 = time.perf_counter()
    nb = nbformat.read(nb_path, as_version=4)

    for cell in nb.get("cells", []):
        if "id" not in cell:
            cell["id"] = uuid.uuid4().hex

    try:
        from nbformat.validator import normalize as _normalize

        normalized = _normalize(nb)
        if isinstance(normalized, tuple):
            if len(normalized) > 1 and isinstance(normalized[1], dict):
                nb = normalized[1]
            else:
                nb = normalized[0]
        else:
            nb = normalized
    except Exception:
        pass

    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            nbformat.validate(nb)
    except Exception as exc:
        return False, nb, exc, time.perf_counter() - t0
    return True, nb, None, time.perf_counter() - t0


def check_imports(
    nb, *, probe: bool = True
) -> Tuple[bool, List[Tuple[str, Exception]], float, float]:
    code_cells = [
        "".join(cell.get("source", []))
        for cell in nb.get("cells", [])
        if cell.get("cell_type") == "code"
    ]
    scan_start = time.perf_counter()
    modules = collect_modules(code_cells)
    scan_duration = time.perf_counter() - scan_start

    missing: List[Tuple[str, Exception]] = []
    probe_duration = 0.0
    if probe:
        for mod in modules:
            start = time.perf_counter()
            try:
                importlib.import_module(mod)
            except Exception as exc:
                missing.append((mod, exc))
            probe_duration += time.perf_counter() - start
    return (len(missing) == 0), missing, scan_duration, probe_duration


def execute_notebook(
    nb, nb_path: Path, *, timeout: int, kernel: str
) -> Tuple[bool, Exception | None, float]:
    import nbformat
    from nbclient import NotebookClient
    from nbclient.exceptions import CellExecutionError

    t0 = time.perf_counter()
    env = os.environ.copy()
    env.setdefault("MPLBACKEND", "Agg")

    client = NotebookClient(
        nbformat.from_dict(nb),
        timeout=timeout,
        kernel_name=kernel,
        resources={"metadata": {"path": str(nb_path.parent)}},
        allow_errors=False,
        env=env,
    )
    try:
        client.execute()
        return True, None, time.perf_counter() - t0
    except CellExecutionError as exc:
        return False, exc, time.perf_counter() - t0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate notebooks with structure/import/execute checks"
    )
    parser.add_argument(
        "notebooks",
        nargs="*",
        help="Notebook paths or glob patterns. Defaults to all notebooks/*.ipynb.",
    )
    parser.add_argument(
        "--skip-execute", action="store_true", help="Skip execution step"
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=180,
        help="Per-notebook execution timeout (seconds)",
    )
    parser.add_argument("--kernel", default="python3", help="Kernel name for execution")
    parser.add_argument(
        "--import-probe/--no-import-probe",
        dest="import_probe",
        default=True,
        action=argparse.BooleanOptionalAction,
    )
    return parser.parse_args()


def expand_notebooks(patterns: Sequence[str]) -> List[Path]:
    paths: List[Path] = []
    if not patterns:
        patterns = ["*.ipynb"]
        for root in NB_ROOTS:
            paths.extend(sorted(root.glob("*.ipynb")))
    else:
        for pat in patterns:
            candidate = Path(pat)
            if candidate.is_file():
                paths.append(candidate.resolve())
            else:
                for root in NB_ROOTS:
                    paths.extend(sorted(root.glob(pat)))
    seen = set()
    ordered: List[Path] = []
    for p in paths:
        if p not in seen:
            ordered.append(p)
            seen.add(p)
    return ordered


def main() -> None:
    args = parse_args()
    notebook_paths = expand_notebooks(args.notebooks)
    if not notebook_paths:
        print("No notebooks matched.", file=sys.stderr)
        sys.exit(1)

    total = len(notebook_paths)
    failures: list[tuple[Path, str, Exception | str]] = []

    for idx, nb_path in enumerate(notebook_paths, start=1):
        nb_path = nb_path.resolve()
        rel = nb_path.relative_to(ROOT)
        header = f"[{idx}/{total}] Validating {rel}"
        print(header)

        total_start = time.perf_counter()

        ok_structure, nb, struct_exc, t_struct = check_structure(nb_path)
        status = "OK" if ok_structure else f"FAIL ({struct_exc})"
        print(f"{BULLET} Structure: {status:<8} ({format_duration(t_struct)})")
        if not ok_structure:
            failures.append((rel, "structure", struct_exc))
            print(f"{BULLET} Imports: SKIP")
            print(f"{BULLET} Execute: SKIP")
            print(f"{BULLET} Total: {format_duration(time.perf_counter() - total_start)}\n")
            continue

        ok_imports, missing, scan_dur, probe_dur = check_imports(
            nb, probe=args.import_probe
        )
        if ok_imports:
            print(
                f"{BULLET} Imports: OK   ({format_duration(scan_dur)} scan, "
                f"{format_duration(probe_dur)} probe)"
            )
        else:
            reason = ", ".join(f"{mod}: {exc!s}" for mod, exc in missing)
            print(
                f"{BULLET} Imports: FAIL ({reason}) "
                f"({format_duration(scan_dur)} scan, {format_duration(probe_dur)} probe)"
            )
            failures.append((rel, "imports", reason))

        if args.skip_execute:
            print(f"{BULLET} Execute: SKIP")
            total_duration = time.perf_counter() - total_start
            print(f"{BULLET} Total: {format_duration(total_duration)}\n")
            continue

        ok_exec, exec_exc, exec_duration = execute_notebook(
            nb, nb_path, timeout=args.timeout, kernel=args.kernel
        )
        exec_status = "OK" if ok_exec else f"FAIL ({exec_exc})"
        print(
            f"{BULLET} Execute: {exec_status:<8} "
            f"({format_duration(exec_duration)})"
        )
        if not ok_exec:
            failures.append((rel, "execute", exec_exc or "unknown error"))

        total_duration = time.perf_counter() - total_start
        print(f"{BULLET} Total: {format_duration(total_duration)}\n")

    if failures:
        print("Summary: FAIL\n")
        for rel, stage, err in failures:
            print(f" - {rel}: {stage} failed ({err})")
        sys.exit(1)
    else:
        print("Summary: OK")


if __name__ == "__main__":
    main()
