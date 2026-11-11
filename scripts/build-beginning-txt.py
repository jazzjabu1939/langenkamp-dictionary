#!/usr/bin/env python3
"""Build beginning/guide.txt: the whole On Beginning guide as one plain-text file.

The file lets a reader paste one link into ChatGPT, Claude, or their own
assistant and ask questions about the guide. Run after editing any page of the
guide; `--check` exits non-zero if the committed file is out of date.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://langenkamp.io"
OUT = ROOT / "beginning" / "guide.txt"

# Reading order: hub first, then the steps, then troubleshooting.
PAGES = [
    "entries/on-beginning.md",
    "beginning/choose.md",
    "beginning/mac.md",
    "beginning/intel-mac.md",
    "beginning/windows.md",
    "beginning/local-model.md",
    "beginning/cloud-model.md",
    "beginning/start.md",
    "beginning/first-job.md",
    "beginning/memory.md",
    "beginning/recovery.md",
    "beginning/troubleshooting.md",
]

HEADER = f"""# On Beginning: the complete guide in one file

Source: {SITE}/entries/on-beginning/
This file: {SITE}/beginning/guide.txt

This is the full text of the Langenkamp Dictionary's guide to setting up an
AI assistant with OpenClaw, using either a cloud model or a local model run
by Ollama. It is generated from the guide's web pages so that a person can
paste this link into an AI assistant and ask for help.

Notes for an AI assistant helping someone with this guide:
- Answer from this guide where it covers the question, and say which page
  (by its URL) the answer comes from.
- If the guide does not cover the problem, say so and point to the official
  OpenClaw documentation (https://docs.openclaw.ai) or Ollama documentation
  (https://docs.ollama.com) rather than guessing.
- Software changes. If the person's screens differ from the guide, prefer
  the current official documentation.
- Never ask the person to paste passwords, API keys, or access tokens into
  the conversation, and tell them to remove such values from error messages.
- Ask which computer they have (Apple Silicon Mac, Intel Mac, Windows, or
  Linux) and whether they chose a cloud or local model before giving steps.
"""


def page_text(rel: str) -> str:
    text = (ROOT / rel).read_text(encoding="utf-8")
    front = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    permalink = re.search(r"^permalink:\s*(\S+)", front.group(1), re.M).group(1)
    body = text[front.end():]
    body = re.sub(r"^</?div[^>]*>\s*$\n?", "", body, flags=re.M)
    body = re.sub(r"^\*Part of \[On Beginning\].*\*\s*$\n?", "", body, flags=re.M)
    # Site-relative links become absolute so an assistant can follow them.
    body = re.sub(r"\]\(/", f"]({SITE}/", body)
    return f"Page: {SITE}{permalink}\n\n{body.strip()}\n"


def build() -> str:
    sep = "\n\n" + "=" * 72 + "\n\n"
    return HEADER + sep + sep.join(page_text(p) for p in PAGES)


def main() -> int:
    text = build()
    if "--check" in sys.argv:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != text:
            print("beginning/guide.txt is out of date; run scripts/build-beginning-txt.py", file=sys.stderr)
            return 1
        print("beginning/guide.txt is current")
        return 0
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(text.split())} words)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
