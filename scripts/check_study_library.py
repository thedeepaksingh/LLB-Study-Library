#!/usr/bin/env python3
"""Validate repository-relative Markdown links in changed Markdown files.

This check validates local link targets only. It does not verify legal accuracy,
external website availability, statutory interpretation or academic correctness.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))(?:\s+[^)]*)?\)")
FENCE_RE = re.compile(r"^\s*(\x60{3,}|~{3,})")


def changed_markdown(base: str) -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=ACMRT", f"{base}...HEAD", "--", "*.md", "*.markdown"],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    if result.returncode != 0:
        print(result.stderr.strip(), file=sys.stderr)
        raise RuntimeError("Could not calculate changed Markdown files.")
    return [line for line in result.stdout.splitlines() if line.strip()]


def strip_code_fences(text: str) -> str:
    output = []
    fence_char = None
    fence_len = 0
    for line in text.splitlines():
        match = FENCE_RE.match(line)
        if match:
            marker = match.group(1)
            if fence_char is None:
                fence_char, fence_len = marker[0], len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_len:
                fence_char, fence_len = None, 0
            continue
        if fence_char is None:
            output.append(line)
    return "\n".join(output)


def target_exists(source: Path, target: str) -> bool:
    parsed = urlparse(target)
    if parsed.scheme or target.startswith("//") or target.startswith("#"):
        return True
    path_part = unquote(parsed.path).strip()
    if not path_part:
        return True
    if path_part.startswith("/"):
        candidate = (ROOT / path_part.lstrip("/")).resolve()
    else:
        candidate = (source.parent / path_part).resolve()
    try:
        candidate.relative_to(ROOT)
    except ValueError:
        return False
    if candidate.is_file():
        return True
    if candidate.is_dir():
        return (candidate / "README.md").is_file() or (candidate / "index.md").is_file()
    return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--changed-from", default="origin/main", help="Git ref used as PR base")
    parser.add_argument("--paths", nargs="*", help="Explicit repository-relative files to validate")
    args = parser.parse_args()

    if args.paths is not None:
        paths = args.paths
    else:
        try:
            paths = changed_markdown(args.changed_from)
        except RuntimeError:
            return 2

    paths = [p for p in paths if p.lower().endswith((".md", ".markdown"))]
    if not paths:
        print("No changed Markdown files to validate.")
        return 0

    errors = []
    checked_links = 0
    for rel in paths:
        source = (ROOT / rel).resolve()
        try:
            source.relative_to(ROOT)
        except ValueError:
            errors.append(f"{rel}: path escapes repository")
            continue
        if not source.is_file():
            errors.append(f"{rel}: changed file does not exist in checkout")
            continue
        text = strip_code_fences(source.read_text(encoding="utf-8"))
        for line_no, line in enumerate(text.splitlines(), start=1):
            for match in LINK_RE.finditer(line):
                target = match.group(1) or match.group(2) or ""
                checked_links += 1
                if not target_exists(source, target):
                    errors.append(f"{rel}:{line_no}: broken local link target: {target}")

    if errors:
        print("Markdown link check failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1

    print(f"Markdown link check passed: {len(paths)} changed Markdown file(s), {checked_links} link(s) inspected.")
    print("External link reachability and legal correctness require separate review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
