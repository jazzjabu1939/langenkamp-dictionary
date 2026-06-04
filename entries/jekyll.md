---
layout: default
kind: glossary
title: "Jekyll"
permalink: /entries/jekyll/
date: 2026-06-04
summary: "The static-site generator that turns the Dictionary's Markdown files into the HTML served at langenkamp.io."
draft: false
published: true
---

**Jekyll** is the static-site generator that turns the Dictionary's Markdown files, layouts, and configuration into ordinary HTML pages.

That matters because langenkamp.io is not a database-backed web application. It is a set of source files in a GitHub repository. Jekyll reads those files, applies the shared layout, builds the entry pages, and publishes the result as a static site. This is why adding a Dictionary entry is mostly a matter of adding a Markdown file with the right front matter.

The trade-off is that local preview depends on a working Ruby/Jekyll environment. When the local machine accidentally uses Apple's old system Ruby instead of the newer Homebrew Ruby, the content may be perfectly fine while the local build still fails. That is an environment problem, not an editorial problem.

## See also

- *[JSON](json.md)*
- *[Tool](tool.md)*
- *[MCP](mcp.md)*
