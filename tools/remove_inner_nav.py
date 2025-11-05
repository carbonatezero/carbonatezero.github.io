#!/usr/bin/env python3
"""Remove redundant <nav> elements inside <header class="site-header"> blocks.

Usage:
    python tools/remove_inner_nav.py [--dry-run]

The script recursively scans the repository for HTML files, removing any
<nav> elements that are descendants of a <header class="site-header"> element.
When run with --dry-run, it only reports the files that would be modified.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Iterable, List, Tuple

EXCLUDE_DIRS = {".git", "node_modules"}
HEADER_PATTERN = re.compile(r"(<header\b[^>]*>)(.*?)(</header>)", re.IGNORECASE | re.DOTALL)
CLASS_PATTERN = re.compile(r'class\s*=\s*(".*?"|\'.*?\')', re.IGNORECASE | re.DOTALL)
NAV_PATTERN = re.compile(r"<nav\b[^>]*>.*?</nav>", re.IGNORECASE | re.DOTALL)
BLANK_LINE_PATTERN = re.compile(r"\n[ \t]+\n")
MULTI_BLANK_PATTERN = re.compile(r"\n{3,}")


def iter_html_files(root: Path) -> Iterable[Path]:
    """Yield all .html files under *root*, skipping excluded directories."""
    for html_file in root.rglob("*.html"):
        try:
            rel_parts = html_file.relative_to(root).parts
        except ValueError:
            continue
        if any(part in EXCLUDE_DIRS for part in rel_parts):
            continue
        yield html_file


def has_site_header_class(tag_text: str) -> bool:
    """Return True if tag_text contains a class attribute with 'site-header'."""
    for match in CLASS_PATTERN.finditer(tag_text):
        value = match.group(1)[1:-1]
        classes = {cls for cls in re.split(r"\s+", value.strip()) if cls}
        if "site-header" in classes:
            return True
    return False


def clean_blank_lines(content: str) -> str:
    content = BLANK_LINE_PATTERN.sub("\n", content)
    content = MULTI_BLANK_PATTERN.sub("\n\n", content)
    return content


def remove_navs_from_header(match: re.Match[str]) -> Tuple[str, bool]:
    opening, content, closing = match.groups()
    if not has_site_header_class(opening):
        return match.group(0), False

    new_content, count = NAV_PATTERN.subn("", content)
    if count == 0:
        return match.group(0), False

    new_content = clean_blank_lines(new_content)
    return f"{opening}{new_content}{closing}", True


def remove_inner_navs(html: str) -> Tuple[str, bool]:
    changed = False
    result = []
    last_index = 0

    for header_match in HEADER_PATTERN.finditer(html):
        start, end = header_match.span()
        replacement, header_changed = remove_navs_from_header(header_match)
        if header_changed:
            changed = True
        result.append(html[last_index:start])
        result.append(replacement)
        last_index = end

    result.append(html[last_index:])
    new_html = "".join(result)
    return new_html, changed


def process_file(path: Path, dry_run: bool) -> bool:
    original = path.read_text(encoding="utf-8")
    updated, changed = remove_inner_navs(original)

    if not changed:
        return False

    if not dry_run:
        path.write_text(updated, encoding="utf-8")
    return True


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show which files would be modified without writing changes.",
    )
    args = parser.parse_args(argv)

    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[1]

    changed_files: List[Path] = []
    for html_file in iter_html_files(repo_root):
        if process_file(html_file, args.dry_run):
            changed_files.append(html_file)

    if changed_files:
        heading = "Files that would be modified:" if args.dry_run else "Modified files:"
        print(heading)
        for path in sorted(changed_files):
            print(f" - {path.relative_to(repo_root)}")
    else:
        print("No changes needed.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
