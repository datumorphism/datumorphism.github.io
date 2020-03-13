---
layout: page
title: Workflows
description: Workflow for data
exclude: true
---

{% comment %}
<div class="buttons">
{% for wf in site.data.workflows %}
  <a class="button is-info" href="{{wf[0]}}">{{wf[1].name}}</a>
{% endfor %}
</div>
{% endcomment %}

<div class="columns is-desktop">
    <div class="column is-2">
        <aside class="menu">
            <p class="menu-label">
                Table of Contents
            </p>
            <ul class="menu-list">
                {% for cat in site.data.workflows %}
                <li><a href="#{{ cat[0] }}" class="codinfox-category-mark" style="color:#999;text-decoration: none;"> {{ cat[1].name }} </a></li>
                {% endfor %}
            </ul>
        </aside>
    </div>
    <div class="column is-10">
        {% for cat in site.data.workflows %}
        <div class="is-divider" data-content="{{ cat[1].name }}"></div>
        <h2 id="{{ cat[0] }}">{{ cat[1].name }} <a href="{{site.base_url}}/api/workflows/{{cat[0]}}.json">
        <span class="tag is-link">API</span></a>
        {% if cat[1].downloads %}
            {% for download in cat[1].downloads %}
                <a href="{{ download.path }}"><span class="tag is-link">{{ download.type }}</span></a>
            {% endfor %}
        {% endif %}
        </h2>
        <p class="is-size-5 notification">{{ cat[1].description }}</p>
        <ol type="1">
            {% for item in cat[1].workflow %}
                <li style="list-style-type:none; border-top: 2px solid #e95420;">
                    <input type="checkbox"><span>  {{ item.name }} : {{ item.description }}</span>
                    {% if item.steps %}
                    <ol>
                        {% for step in item.steps %}
                        <li style="list-style-type:none;border-top: 1px dashed #e95420;">
                            <input type="checkbox"><span>
                                {% if step.related %} <a href="#{{step.related}}" style="color: red;">{{ step.name }} <i class="fas fa-bookmark"></i></a>
                                {% else %} {{ step.name }}
                                {% endif %}
                            </span>
                            {% if step.description %}
                            <p class="is-size-6 notification" style="margin-left:1em;padding: 0.5em 0.5em 0.5em 0.5em;">
                                {{ step.description }}
                            </p>
                            {% endif %}
                            {% if step.steps %}
                            <ol>
                                {% for sub_step in step.steps %}
                                    <li style="list-style-type:none;">
                                        <input type="checkbox"><span>
                                            {% if sub_step.related %} <a href="#{{sub_step.related}}" style="color: red;">{{ sub_step.name }} <i class="fas fa-bookmark"></i></a>
                                            {% else %} {{ sub_step.name }}
                                            {% endif %}
                                        </span>
                                        {% if sub_step.description %}
                                        <p class="is-size-6 notification" style="margin-left:1em;padding: 0.5em 0.5em 0.5em 0.5em;">{{ sub_step.description }}</p>
                                        {% endif %}
                                        {% if sub_step.steps %}
                                            <ol>
                                                {% for sub_sub_step in sub_step.steps %}
                                                    <li style="list-style-type:none;">
                                                        <input type="checkbox"><span>
                                                            {% if sub_sub_step.related %} <a href="#{{sub_sub_step.related}}" style="color: red;">
                                                                {{ sub_sub_step.name }} <i class="fas fa-bookmark"></i></a>
                                                            {% else %} {{ sub_sub_step.name }}
                                                            {% endif %}
                                                        </span>
                                                        {% if sub_sub_step.description %}
                                                        <p class="is-size-6 notification" style="margin-left:1em;padding: 0.5em 0.5em 0.5em 0.5em;">{{ sub_sub_step.description }}</p>
                                                        {% endif %}
                                                    </li>
                                                {% endfor %}
                                            </ol>
                                        {% endif %}
                                    </li>
                                {% endfor %}
                            </ol>
                            {% endif %}
                        </li>
                        {% endfor %}
                    </ol>
                    {% endif %}
            </li>
            {% endfor %}
        </ol>
        {% endfor %}
    </div>
</div>

{% include highlight-get-params.html %}