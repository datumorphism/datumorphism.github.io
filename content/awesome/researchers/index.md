---
layout: page
title: Researchers
description: Curated list of researchers
exclude: true
---

{{< awesomeresearchers >}}

<div class="columns is-desktop">
    <div class="column is-2">
        <aside class="menu">
            <p class="menu-label">
                Table of Contents
            </p>
            <ul class="menu-list">
                {% for cat in site.data.researchers %}
                <li><a href="#{{ cat[0] }}" class="codinfox-category-mark" style="color:#999;text-decoration: none;"> {{ cat[0] }} </a></li>
                {% endfor %}
            </ul>
        </aside>
    </div>
    <div class="column is-10">
        {% for cat in site.data.researchers %}
        <h2 id="{{ cat[0] }}">{{ cat[0] }}</h2>
        <ol type="1">
            {% for item in cat[1] %}
            <li> <a href="{{ item.link }}" style="text-decoration: none;" target="_blank">  {{ item.name }} </a> {% if item.keywords %} [<div class="tags" style="display: inline;"> {% for kw in item.keywords %} <span class="tag">{{ kw }}</span> {% endfor %} </div>] {% endif %}: {{ item.description }}
            </li>
            {% endfor %}
        </ol>
        {% endfor %}
    </div>
</div>
