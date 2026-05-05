---
layout: default
title: Entries — Alphabetical
permalink: /entries/
---

# Entries (alphabetical)

A complete list of dictionary entries, begun May 2026 and growing. New terms are added as the field evolves and as faculty questions surface. For a thematic view, see the [topic index](/topics/). To return to the front page, see the [home page](/).

---

{% assign entries = site.pages | where_exp: "p", "p.path contains 'entries/'" | where_exp: "p", "p.name != 'index.md'" | where_exp: "p", "p.name != 'README.md'" | sort: "title" %}
{% for entry in entries %}{% if entry.title and entry.title != "" %}
- [**{{ entry.title }}**]({{ entry.permalink | default: entry.url | relative_url }}){% if entry.summary %} — {{ entry.summary }}{% endif %}
{% endif %}{% endfor %}

---

*The Langenkamp Dictionary of Agentic AI Terminology. Maintained by Matthew D. Langenkamp / 雷邁德. Licensed under [CC BY-NC 4.0](/LICENSE).*
