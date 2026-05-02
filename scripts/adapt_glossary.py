#!/usr/bin/env python3
"""
Adapt entries from the local agentic-systems glossary into dictionary entries.
- Drops the "Filed:" / "Source:" preamble lines (workspace-specific).
- Rewrites cross-reference filename slugs.
- Updates Related entries: lines.
"""
import re
import shutil
from pathlib import Path

SRC = Path.home() / ".openclaw/workspace/teaching/agentic-systems/glossary"
DST = Path.home() / ".openclaw/workspace/langenkamp-dictionary/entries"
DST.mkdir(parents=True, exist_ok=True)

slug_map = {
    "the-importance-of-naming.md": "naming.md",
    "what-is-a-gateway.md": "gateway.md",
    "what-is-a-heartbeat.md": "heartbeat.md",
    "what-is-a-soul-md.md": "soul-md.md",
    "what-is-a-sub-agent.md": "sub-agent.md",
    "what-is-a-tool.md": "tool.md",
    "what-is-a-vector-database.md": "vector-database.md",
    "what-is-an-embedding.md": "embedding.md",
    "what-is-fine-tuning.md": "fine-tuning.md",
    "what-is-mcp.md": "mcp.md",
    "what-is-ollama.md": "ollama.md",
    "what-is-rag.md": "rag.md",
}

# For rewriting cross-refs in related-entries lines.
# Map any reference to old slug → new slug.
ref_map = {old: new for old, new in slug_map.items()}

# Some entries reference files that don't exist yet. Keep them as placeholder names; we'll write them as TBD.

# Title fix per entry — strip "What is" preamble for dict-style headings.
title_map = {
    "naming.md": "Naming",
    "gateway.md": "Gateway",
    "heartbeat.md": "Heartbeat",
    "soul-md.md": "SOUL.md (agent persona file)",
    "sub-agent.md": "Sub-agent",
    "tool.md": "Tool",
    "vector-database.md": "Vector database",
    "embedding.md": "Embedding",
    "fine-tuning.md": "Fine-tuning",
    "mcp.md": "MCP (Model Context Protocol)",
    "ollama.md": "Ollama",
    "rag.md": "RAG (Retrieval-Augmented Generation)",
}

for src_name, dst_name in slug_map.items():
    src = SRC / src_name
    dst = DST / dst_name
    text = src.read_text()

    # 1) Replace H1 heading. Old form: "# What is X?" or "# The importance of naming"
    # New form: "# {title}"
    title = title_map[dst_name]
    text = re.sub(r'^# .*?\n', f"# {title}\n", text, count=1, flags=re.MULTILINE)

    # 2) Drop the "*Filed: ... *" italic preamble (one line, just below H1).
    text = re.sub(r'\n\*Filed:[^\n]*\n', '\n', text, count=1)

    # 3) Rewrite cross-reference slugs in "Related entries" or anywhere in body.
    for old_slug, new_slug in ref_map.items():
        text = text.replace(old_slug, new_slug)

    # 4) Drop references to architecture/* subfolder paths that don't exist in dict yet.
    text = re.sub(r'`architecture/[^`]*\.md`', '*(planned)*', text)
    text = re.sub(r'`commonplace/themes/[^`]+\.md`', '*(maintainer notes, not in this repo)*', text)

    # 5) Replace any remaining glossary/<file>.md path with entries/<file>.md
    text = re.sub(r'glossary/([a-z0-9-]+\.md)', r'\1', text)

    dst.write_text(text)
    print(f"  → {dst.relative_to(Path.home())}")
print("Done.")
