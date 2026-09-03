---
layout: default
title: Entries — Alphabetical
permalink: /entries/
---

# Entries (alphabetical)

A complete list of dictionary entries, begun May 2026 and growing. New terms are added as the field evolves and as faculty questions surface. For a thematic view, see the [topic index](/topics/). To return to the front page, see the [home page](/).

<p><small><span class="reference-badge">Glossary</span> entries are compact definitions. <span class="reference-badge">Reference</span> entries answer six working questions, sometimes under headings suited to the subject. <span class="essay-badge">Essay</span> entries advance an argument, name a pattern, or carry the Dictionary's interpretive position.</small></p>

---

{% assign entries = site.pages | where_exp: "p", "p.permalink contains '/entries/'" | where_exp: "p", "p.permalink != '/entries/'" | where_exp: "p", "p.published != false" | sort_natural: "title" %}

<div class="entry-finder">
  <label class="entry-search-label" for="entry-search">Search entries</label>
  <div class="entry-search-row">
    <input id="entry-search" class="entry-search" type="search" placeholder="Search the Dictionary" autocomplete="off">
    <button class="entry-search-clear" type="button" aria-label="Clear search">Clear</button>
  </div>
  <p class="entry-search-status" aria-live="polite"></p>
</div>

<nav class="entry-letter-grid" aria-label="Browse entries by first character">
  {% assign letters = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,0-9" | split: "," %}
  {% for letter in letters %}
  <a href="#{{ letter | slugify }}" class="entry-letter-tile">{{ letter }}</a>
  {% endfor %}
</nav>

<div class="entry-index">
{% assign current_letter = "" %}
{% for entry in entries %}
  {% assign first_char = entry.title | slice: 0 | upcase %}
  {% assign alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" %}
  {% if alpha contains first_char %}
    {% assign entry_letter = first_char %}
  {% else %}
    {% assign entry_letter = "0-9" %}
  {% endif %}
  {% if entry_letter != current_letter %}
    {% unless forloop.first %}
    </ul>
    {% endunless %}
    {% assign current_letter = entry_letter %}
    <h2 id="{{ current_letter | slugify }}" class="entry-letter-heading">{{ current_letter }}</h2>
    <ul class="entry-list">
  {% endif %}
      <li class="entry-list-item" data-entry-search="{{ entry.title | downcase | escape }} {{ entry.summary | downcase | escape }}" data-entry-letter="{{ entry_letter }}">
        <a href="{{ entry.permalink | relative_url }}"><strong>{{ entry.title }}</strong></a>{% if entry.kind == "glossary" %} <small class="reference-badge">Glossary</small>{% elsif entry.kind == "essay" %} <small class="essay-badge">Essay</small>{% elsif entry.kind == "reference" %} <small class="reference-badge">Reference</small>{% else %} <small class="reference-badge">Unclassified</small>{% endif %} — {{ entry.summary }}
      </li>
{% endfor %}
{% if entries.size > 0 %}
    </ul>
{% endif %}
</div>

<script>
  (function () {
    var input = document.getElementById('entry-search');
    var clear = document.querySelector('.entry-search-clear');
    var status = document.querySelector('.entry-search-status');
    var items = Array.prototype.slice.call(document.querySelectorAll('.entry-list-item'));
    var headings = Array.prototype.slice.call(document.querySelectorAll('.entry-letter-heading'));

    if (!input || !items.length) return;

    function update() {
      var query = input.value.trim().toLowerCase();
      var visibleCount = 0;

      items.forEach(function (item) {
        var matches = !query || item.getAttribute('data-entry-search').indexOf(query) !== -1;
        item.hidden = !matches;
        if (matches) visibleCount += 1;
      });

      headings.forEach(function (heading) {
        var list = heading.nextElementSibling;
        var visibleInGroup = list && Array.prototype.some.call(list.querySelectorAll('.entry-list-item'), function (item) {
          return !item.hidden;
        });
        heading.hidden = !visibleInGroup;
        if (list) list.hidden = !visibleInGroup;
      });

      status.textContent = query ? visibleCount + ' matching entr' + (visibleCount === 1 ? 'y' : 'ies') : '';
    }

    input.addEventListener('input', update);
    clear.addEventListener('click', function () {
      input.value = '';
      input.focus();
      update();
    });
  }());
</script>

---

*The Langenkamp Dictionary of Agentic AI Terminology. Maintained by Matthew D. Langenkamp / 雷邁德. Licensed under [CC BY-NC 4.0](/LICENSE).*
