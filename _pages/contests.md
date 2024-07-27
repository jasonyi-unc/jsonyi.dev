---
layout: page
permalink: /contests/
title: Contests
description: >
nav: true
nav_order: 5
---

Detailed analysis and walkthroughs of coding contests from Codeforces. I realized that I needed to do two things when it comes to contests: (1) to measure my current ability when competing and (2) to analyze and investigate the things I was lacking during the contest. This page is to make sure that I do the latter and become more familiar with similiar problems in the future. The goal is to improve my thought process instead of jumping from contest to contest with little to no insight carried over.

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
