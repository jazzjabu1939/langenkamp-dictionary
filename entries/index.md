---
layout: default
title: Entries — Alphabetical
permalink: /entries/
---

# Entries (alphabetical)

A complete list of dictionary entries, begun May 2026 and growing. New terms are added as the field evolves and as faculty questions surface. For a thematic view, see the [topic index](/topics/). To return to the front page, see the [home page](/).

---

{% assign entries = site.pages | where_exp: "p", "p.permalink contains '/entries/'" | where_exp: "p", "p.permalink != '/entries/'" | where_exp: "p", "p.published != false" | sort: "title" %}
{% for entry in entries %}
- [**{{ entry.title }}**]({{ entry.permalink | relative_url }}) — {{ entry.summary }}
{% endfor %}

---

*The Langenkamp Dictionary of Agentic AI Terminology. Maintained by Matthew D. Langenkamp / 雷邁德. Licensed under [CC BY-NC 4.0](/LICENSE).*
