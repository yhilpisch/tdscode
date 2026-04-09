"""
The Data Scientist
Code Validation Helper

Validate Python scripts under each book's code/ directory by checking syntax,
import availability, and optional execution. Output is human-readable and
mirrors tools/validate_notebooks.py.

Usage
  python tools/validate_code.py                 # validate all code/**/*.py
  python tools/validate_code.py 1_data/code/*.py
  python tools/validate_code.py --skip-execute
"""
from __future__ import annotations

import argparse
import ast
import importlib
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import List, Sequence, Tuple

ROOT = Path(__file__).resolve().parents[1]
CODE_ROOTS = [ROOT / "0_primer" / "code", ROOT / "1_data" / "code", ROOT / "2_data" / "code", ROOT / "3_data" / "code", ROOT / "4_data" / "code"]
BULLET = "  •"


def format_duration(seconds: float) -> str:
    if seconds < 0.001:
        return f"{seconds * 1_000_000:.1f}µs"
    if seconds < 1.0:
        return f"{seconds * 1_000:.1f}ms"
    return f"{seconds:.2f}s"


def collect_modules_from_source(source: str) -> List[str]:
    modules = set()
    try:
        node = ast.parse(source)
    except SyntaxError:
        return []
    for stmt in ast.walk(node):
        if isinstance(stmt, ast.Import):
            for alias in stmt.names:
                modules.add(alias.name.split(".")[0])
        elif isinstance(stmt, ast.ImportFrom):
            if stmt.module:
                modules.add(stmt.module.split(".")[0])
    return sorted(m for m in modules if m and not m.startswith("."))


def check_syntax(path: Path) -> Tuple[bool, Exception | None, float, str, list[str]]:
    t0 = time.perf_counter()
    try:
        source = path.read_text(encoding="utf8")
    except Exception as exc:
        return False, exc, time.perf_counter() - t0, "", []
    try:
        ast.parse(source, filename=str(path))
    except SyntaxError as exc:
        return False, exc, time.perf_counter() - t0, source, []
    modules = collect_modules_from_source(source)
    return True, None, time.perf_counter() - t0, source, modules


def check_imports(
    modules: Sequence[str], *, probe: bool = True
) -> Tuple[bool, list[Tuple[str, Exception]], float]:
    missing: list[Tuple[str, Exception]] = []
    t0 = time.perf_counter()
    if probe:
        for mod in modules:
            try:
                importlib.import_module(mod)
            except Exception as exc:
                missing.append((mod, exc))
    duration = time.perf_counter() - t0
    return (len(missing) == 0), missing, duration


def execute_script(path: Path, *, timeout: int, cwd: Path) -> Tuple[bool, Exception | None, float]:
    t0 = time.perf_counter()
    env = os.environ.copy()
    env.setdefault("PYTHONWARNINGS", "ignore")
    env.setdefault("MPLBACKEND", "Agg")
    try:
        subprocess.run(
            [sys.executable, str(path)],
            cwd=str(cwd),
            timeout=timeout,
            check=True,
            env=env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )
        return True, None, time.perf_counter() - t0
    except subprocess.CalledProcessError as exc:
        return False, exc, time.perf_counter() - t0
    except subprocess.TimeoutExpired as exc:
        return False, exc, time.perf_counter() - t0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate Python scripts in code/ with syntax/import/execute checks"
    )
    parser.add_argument(
        "files",
        nargs="*",
        help="Code paths or glob patterns. Defaults to all code/**/*.py.",
    )
    parser.add_argument(
        "--skip-execute", action="store_true", help="Skip execution step"
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=120,
        help="Per-script execution timeout (seconds)",
    )
    parser.add_argument(
        "--import-probe/--no-import-probe",
        dest="import_probe",
        default=True,
        action=argparse.BooleanOptionalAction,
    )
    return parser.parse_args()


def expand_files(patterns: Sequence[str]) -> list[Path]:
    paths: list[Path] = []
    if not patterns:
        patterns = ["*.py"]
        for root in CODE_ROOTS:
            paths.extend(sorted(root.glob("*.py")))
    else:
        for pat in patterns:
            candidate = Path(pat)
            if candidate.is_file():
                paths.append(candidate.resolve())
            else:
                for root in CODE_ROOTS:
                    paths.extend(sorted(root.glob(pat)))
    seen: set[Path] = set()
    ordered: list[Path] = []
    for p in paths:
        if p not in seen:
            ordered.append(p)
            seen.add(p)
    return ordered


def main() -> None:
    args = parse_args()
    code_paths = expand_files(args.files)
    if not code_paths:
        print("No code files matched.", file=sys.stderr)
        sys.exit(1)

    total = len(code_paths)
    failures: list[tuple[Path, str, Exception | str]] = []

    for idx, path in enumerate(code_paths, start=1):
        path = path.resolve()
        rel = path.relative_to(ROOT)
        header = f"[{idx}/{total}] Validating {rel}"
        print(header)

        total_start = time.perf_counter()

        ok_syntax, exc, t_syntax, _, modules = check_syntax(path)
        status = "OK" if ok_syntax else f"FAIL ({exc})"
        print(f"{BULLET} Syntax: {status:<8} ({format_duration(t_syntax)})")
        if not ok_syntax:
            failures.append((rel, "syntax", exc or "syntax error"))
            print(f"{BULLET} Imports: SKIP")
            print(f"{BULLET} Execute: SKIP")
            print(f"{BULLET} Total: {format_duration(time.perf_counter() - total_start)}\n")
            continue

        ok_imports, missing, t_imports = check_imports(
            modules, probe=args.import_probe
        )
        if ok_imports:
            print(
                f"{BULLET} Imports: OK   ({format_duration(t_imports)} probe)"
            )
        else:
            reason = ", ".join(f"{mod}: {exc!s}" for mod, exc in missing)
            print(
                f"{BULLET} Imports: FAIL ({reason}) "
                f"({format_duration(t_imports)} probe)"
            )
            failures.append((rel, "imports", reason))

        if args.skip_execute:
            print(f"{BULLET} Execute: SKIP")
            total_duration = time.perf_counter() - total_start
            print(f"{BULLET} Total: {format_duration(total_duration)}\n")
            continue

        cwd = path.parent.parent  # book root
        ok_exec, exec_exc, t_exec = execute_script(path, timeout=args.timeout, cwd=cwd)
        exec_status = "OK" if ok_exec else f"FAIL ({exec_exc})"
        print(f"{BULLET} Execute: {exec_status:<8} ({format_duration(t_exec)})")
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
