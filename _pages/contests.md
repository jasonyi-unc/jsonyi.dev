---
layout: page
permalink: /contests/
title: Contests
description: >
nav: true
nav_order: 5
---

Detailed analysis and walkthroughs of coding contests from Codeforces. This page is for me to become more familiar with similiar problems in the future. The goal is to improve my thought process instead of jumping from contest to contest with little to no insight carried over. You'll notice that some contests does not contain all problems from A-G. This is because that the later problems in any given contest would require some knowledge about a obscure data structure or an algorithm not widely used. It's better to focus on solving the earlier problems faster compared to memorizing algorithms that is far beyond your current skill level. Inspiration [here](https://codeforces.com/blog/entry/92248).

## Codeforces

{% include codeforces_rating.liquid %}

### Division 1

<ul>
    {% for contest in site.contests reversed %}
    {% if contest.division == 1 %}
    <li>
        <a href="{{ contest.url | relative_url }}">
            {{ contest.title }}
        </a>
    </li>
    {% endif %}
    {% endfor %}
</ul>

---

### Division 2

<ul>
    {% for contest in site.contests reversed %}
    {% if contest.division == 2 %}
    <li>
        <a href="{{ contest.url | relative_url }}">
            {{ contest.title }}
        </a>
    </li>
    {% endif %}
    {% endfor %}
</ul>

---

### Division 3

<ul>
    {% for contest in site.contests reversed %}
    {% if contest.division == 3 %}
    <li>
        <a href="{{ contest.url | relative_url }}">
            {{ contest.title }}
        </a>
    </li>
    {% endif %}
    {% endfor %}
</ul>

---

### Division 4

<ul>
    {% for contest in site.contests reversed %}
    {% if contest.division == 4 %}
    <li>
        <a href="{{ contest.url | relative_url }}">
            {{ contest.title }}
        </a>
    </li>
    {% endif %}
    {% endfor %}
</ul>
