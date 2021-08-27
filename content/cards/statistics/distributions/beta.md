---
title: "Beta Distribution"
excerpt: ""
date: 2020-03-14
categories:
- 'Statistics'
tags:
- 'Statistics'
- 'Distributions'
scripts:
- src: "https://unpkg.com/@stdlib/stdlib@0.0.32/dist/stdlib-flat.min.js"
- src: "../assets/beta.js"
charts:
references:
- name: Beta Distribution @ Wikipedia
  link: https://en.wikipedia.org/wiki/Beta_distribution
- name: stdlib.js documentation
  link: https://stdlib.io/docs/api/v0.0.90/@stdlib/stats/base/dists/beta
---

## Beta Distribution


![](../assets/beta/beta-1.png)

![](../assets/beta/beta-2.png)


## Interact

{% include extras/vue.html %}

<div id="app">
<div class="columns">
  <div class="column has-text-centered">
    <div class="field">
        <label class="label">Alpha</label>
            <div class="control">
                <input v-model="alpha" class="input" type="number">
            </div>
    </div>
  </div>
  <div class="column has-text-centered">
    <div class="field">
        <label class="label">Beta</label>
            <div class="control">
                <input v-model="beta" class="input" type="number">
            </div>
    </div>
  </div>
</div>


<div class="field is-grouped is-grouped-multiline">
<div class="control">
    <div class="tags has-addons">
      <span class="tag is-dark">mode</span>
      <span class="tag is-primary">((beta_mode))</span>
    </div>
  </div>

  <div class="control">
    <div class="tags has-addons">
      <span class="tag is-dark">median</span>
      <span class="tag is-primary">((beta_median))</span>
    </div>
  </div>
  <div class="control">
    <div class="tags has-addons">
      <span class="tag is-dark">mean</span>
      <span class="tag is-primary">((beta_mean))</span>
    </div>
  </div>


</div>

((makeGraph))

<div id="beta-chart"></div>
</div>



