---
layout: page
permalink: /summaries/
title: Summaries
description: >
nav: true
nav_order: 5
---

Summaries and critiques of papers (mostly low-level or machine learning) I've read in detail.

This serves to both catalog my own reading and academic progress, and may also
be of interest to others to find interesting papers to check out.

{% include scripts/mathjax_macros.liquid %}

---

<ol>
    {% for summary in site.summaries reversed %}
    <li>
        <a href="{{ summary.url | relative_url }}">
            ({{ summary.date | date: '%b %-d, %Y' }})
            {{ summary.title }}
        </a>
    </li>
    {% endfor %}
</ol>
