#!/usr/bin/env python3
"""Guarded creation and publication workflow for the AI in Higher Education brief."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date as date_type
from pathlib import Path
from typing import Optional, Tuple


REPO = Path(__file__).resolve().parents[1]
WORKSPACE = REPO.parent
LEDGER = REPO / "newsletter" / "ledger.json"
ARCHIVE = REPO / "newsletter" / "index.md"
OTHER_WRITING = REPO / "other-writing" / "index.md"
ARCHIVE_START = "<!-- NEWSLETTER_ARCHIVE_START -->"
ARCHIVE_END = "<!-- NEWSLETTER_ARCHIVE_END -->"
CURRENT_START = "<!-- NEWSLETTER_CURRENT_START -->"
CURRENT_END = "<!-- NEWSLETTER_CURRENT_END -->"


def load_ledger() -> dict:
    return json.loads(LEDGER.read_text(encoding="utf-8"))


def save_ledger(data: dict) -> None:
    data["issues"] = sorted(data["issues"], key=lambda item: item["volume"])
    LEDGER.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def published(data: dict) -> list[dict]:
    return sorted(
        (item for item in data["issues"] if item["status"] == "published"),
        key=lambda item: item["volume"],
    )


def validate(data: dict, require_files: bool = True) -> None:
    issues = data.get("issues", [])
    volumes = [item["volume"] for item in issues]
    dates = [item["date"] for item in issues if item["status"] == "published"]
    if len(volumes) != len(set(volumes)):
        raise ValueError("Duplicate volume number in newsletter ledger")
    if len(dates) != len(set(dates)):
        raise ValueError("Two published issues share the same date")
    pubs = published(data)
    if pubs:
        expected = list(range(pubs[0]["volume"], pubs[-1]["volume"] + 1))
        actual = [item["volume"] for item in pubs]
        if actual != expected:
            raise ValueError(f"Published volume gap: expected {expected}, found {actual}")
    if require_files:
        missing = [item["site_file"] for item in pubs if not (REPO / item["site_file"]).is_file()]
        if missing:
            raise ValueError("Missing published site files: " + ", ".join(missing))


def next_volume(data: dict) -> int:
    pubs = published(data)
    return pubs[-1]["volume"] + 1 if pubs else 1


def human_date(value: str) -> str:
    parsed = date_type.fromisoformat(value)
    return f"{parsed.strftime('%B')} {parsed.day}, {parsed.year}"


def replace_between(path: Path, start: str, end: str, replacement: str) -> None:
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    block = f"{start}\n{replacement.rstrip()}\n{end}"
    if not pattern.search(text):
        raise ValueError(f"Managed markers missing from {path}")
    path.write_text(pattern.sub(block, text), encoding="utf-8")


def sync_indexes(data: dict) -> None:
    issues = list(reversed(published(data)))
    archive_lines = [
        f'- **[{human_date(item["date"])}]({item["date"]}/)** · Vol. {item["volume"]} - {item["title"]}'
        for item in issues
    ]
    current_lines = [
        f'- **[{human_date(item["date"])}](/newsletter/{item["date"]}/)** · Vol. {item["volume"]} - {item["title"]}'
        for item in issues[:8]
    ]
    replace_between(ARCHIVE, ARCHIVE_START, ARCHIVE_END, "\n".join(archive_lines))
    replace_between(OTHER_WRITING, CURRENT_START, CURRENT_END, "\n".join(current_lines))


def source_body(source: Path) -> Tuple[str, Optional[int], Optional[str]]:
    text = source.read_text(encoding="utf-8").strip()
    header = re.search(r"^# AI in Higher Education.*?Vol\.\s*(\d+)", text, re.MULTILINE)
    source_volume = int(header.group(1)) if header else None
    source_date_match = re.search(r"^\*\*Date:\*\*\s*(.+?)\s*$", text, re.MULTILINE)
    source_date = source_date_match.group(1).strip() if source_date_match else None
    lines = text.splitlines()
    if lines and lines[0].startswith("# AI in Higher Education"):
        lines = lines[1:]
    while lines and (not lines[0].strip() or re.match(r"^\*\*(Date|To|From|Re):\*\*", lines[0])):
        lines.pop(0)
    return "\n".join(lines).strip(), source_volume, source_date


def infer_title(body: str) -> str:
    match = re.search(r"^##\s+(.+)$", body, re.MULTILINE)
    return match.group(1).strip() if match else "Weekly developments in AI and higher education"


def render_site_page(issue_date: str, volume: int, title: str, body: str) -> str:
    safe_title = title.replace('"', '\\"')
    return f'''---
layout: default
title: "AI in Higher Education - {human_date(issue_date)}"
date: {issue_date}
volume: "{volume}"
description: "{safe_title}"
permalink: /newsletter/{issue_date}/
---

# AI in Higher Education Newsletter

**{human_date(issue_date)}** · Vol. {volume}

*A weekly brief for the Management Department, Isenberg School of Management, UMass Amherst. By Matthew D. Langenkamp / 雷邁德, prepared in collaboration with Thea 🪻✨.*

[← Back to archive](/newsletter/) · [← Back to Dictionary](/)

---

{body}

---

[← Back to archive](/newsletter/) · [← Back to Dictionary](/)
'''


def command_status(args: argparse.Namespace) -> None:
    data = load_ledger()
    validate(data)
    last = published(data)[-1]
    print(f'Latest published: Vol. {last["volume"]} - {human_date(last["date"])}')
    print(f'Next volume: Vol. {next_volume(data)}')


def command_sync(args: argparse.Namespace) -> None:
    data = load_ledger()
    validate(data)
    sync_indexes(data)
    print("Newsletter archive listings synchronized from ledger.")


def command_new(args: argparse.Namespace) -> None:
    data = load_ledger()
    validate(data)
    volume = next_volume(data)
    target = WORKSPACE / "dept-memos" / f"{args.date}-education-ai-brief.md"
    if target.exists():
        raise ValueError(f"Refusing to overwrite existing draft: {target}")
    target.write_text(
        f"# AI in Higher Education - Weekly Brief, Vol. {volume}\n\n"
        f"**Date:** {human_date(args.date)}  \n"
        "**To:** Management Department Faculty, Isenberg School of Management  \n"
        "**From:** Matthew D. Langenkamp / 雷邁德  \n"
        f"**Re:** Weekly Brief - AI in Higher Education (Vol. {volume})  \n\n"
        "## Working title\n\nDraft text.\n",
        encoding="utf-8",
    )
    print(f"Created Vol. {volume} draft: {target}")


def command_publish(args: argparse.Namespace) -> None:
    data = load_ledger()
    validate(data)
    expected = next_volume(data)
    volume = args.volume if args.volume is not None else expected
    if volume != expected:
        raise ValueError(f"Next published volume must be {expected}; received {volume}")
    if any(item["date"] == args.date for item in data["issues"]):
        raise ValueError(f"Ledger already contains issue date {args.date}")
    source = Path(args.source).resolve()
    if not source.is_file():
        raise ValueError(f"Source file not found: {source}")
    body, source_volume, source_date = source_body(source)
    if source_volume is not None and source_volume != volume:
        raise ValueError(f"Source says Vol. {source_volume}; ledger expects Vol. {volume}")
    if source_date is not None and source_date != human_date(args.date):
        raise ValueError(f"Source date is {source_date}; requested {human_date(args.date)}")
    title = args.title or infer_title(body)
    site_file = REPO / "newsletter" / f"{args.date}.md"
    if site_file.exists():
        raise ValueError(f"Refusing to overwrite existing site issue: {site_file}")
    site_file.write_text(render_site_page(args.date, volume, title, body), encoding="utf-8")
    issue = {
        "volume": volume,
        "date": args.date,
        "status": "published",
        "title": title,
        "source": str(source.relative_to(WORKSPACE)),
        "site_file": str(site_file.relative_to(REPO)),
    }
    data["issues"].append(issue)
    save_ledger(data)
    sync_indexes(data)
    validate(data)
    if not args.no_build:
        subprocess.run([str(REPO / "bin" / "jekyll-local"), "build"], cwd=REPO, check=True)
    print(f'Published Vol. {volume}: /newsletter/{args.date}/')
    print(f'Next volume is Vol. {volume + 1}.')


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    sub = result.add_subparsers(dest="command", required=True)
    status = sub.add_parser("status", help="Validate ledger and report the next volume")
    status.set_defaults(func=command_status)
    sync = sub.add_parser("sync", help="Regenerate archive listings from the ledger")
    sync.set_defaults(func=command_sync)
    new = sub.add_parser("new", help="Create a correctly numbered canonical memo draft")
    new.add_argument("--date", required=True, help="Issue date in YYYY-MM-DD format")
    new.set_defaults(func=command_new)
    publish = sub.add_parser("publish", help="Publish an approved canonical memo to the site")
    publish.add_argument("--source", required=True)
    publish.add_argument("--date", required=True)
    publish.add_argument("--volume", type=int)
    publish.add_argument("--title")
    publish.add_argument("--no-build", action="store_true")
    publish.set_defaults(func=command_publish)
    return result


def main() -> int:
    args = parser().parse_args()
    try:
        args.func(args)
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
