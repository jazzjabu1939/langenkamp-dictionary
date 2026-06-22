---
layout: default
title: Entries — Alphabetical
permalink: /entries/
---

# Entries (alphabetical)

A complete list of dictionary entries, begun May 2026 and growing. New terms are added as the field evolves and as faculty questions surface. For a thematic view, see the [topic index](/topics/). To return to the front page, see the [home page](/).

<p><small><span class="reference-badge">Glossary</span> entries are compact reference definitions. <span class="reference-badge">Reference</span> entries explain a term in the standard six-part form. <span class="essay-badge">Essay</span> entries advance an argument, name a pattern, or carry the Dictionary's interpretive position.</small></p>

---

{% assign entries = site.pages | where_exp: "p", "p.permalink contains '/entries/'" | where_exp: "p", "p.permalink != '/entries/'" | where_exp: "p", "p.published != false" | sort: "title" %}
{% for entry in entries %}
- [**{{ entry.title }}**]({{ entry.permalink | relative_url }}){% if entry.kind == "glossary" %} <small class="reference-badge">Glossary</small>{% elsif entry.kind == "essay" or entry.layout == "entry" %} <small class="essay-badge">Essay</small>{% else %} <small class="reference-badge">Reference</small>{% endif %} — {{ entry.summary }}
{% endfor %}

---

*The Langenkamp Dictionary of Agentic AI Terminology. Maintained by Matthew D. Langenkamp / 雷邁德. Licensed under [CC BY-NC 4.0](/LICENSE).*
