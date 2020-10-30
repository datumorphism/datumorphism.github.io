---
title: "Jaccard Similarity"
description: ""
date: 2019-05-06
category:
- 'Math'
tags:
- 'Set'
- 'Distance'
references:
- name: Jaccard index
  link: https://en.wikipedia.org/wiki/Jaccard_index
---

Jaccard index is the ratio of the size of the intersect of the set and the size of the union of the set.

$$
J(A, B) = \frac{ \vert A \cap B \vert }{ \vert A \cup B \vert }
$$

Jaccard distance $d_J(A,B)$ is defined as

$$
d_J(A,B) = 1 - J(A,B).
$$

## Properties

If the two sets are the same, $A=B$, we have $J(A,B)=1$ or $d_J(A,B)=0$. We have maximum similarity.

If the two sets have nothing in common, we have $J(A,B)=0$ or $d_J(A,B)=1$. We have minimum similarity.

## Examples

<div id="app">
<div class="columns">
  <div class="column has-text-centered">
    <div class="field">
        <label class="label">Sentence One</label>
            <div class="control">
                <input v-model="sentenceOne.sentence" class="input" type="text">
            </div>
        Word Set: (( sentenceOneWords ))
    </div>
  </div>

  <div class="column has-text-centered">
    <div class="field">
        <label class="label">Sentence Two</label>
            <div class="control">
                <input v-model="sentenceTwo.sentence" class="input" type="text">
            </div>
        Word Set: (( sentenceTwoWords ))
    </div>
  </div>
</div>

<div class="columns">
    <div class="column has-text-centered">
    Intersect: (( intersectWords ))
  </div>
</div>

<div class="columns">
    <div class="column has-text-centered">
    Union: (( unionWords ))
  </div>
</div>

<div class="columns">
    <div class="column has-text-centered">
    Jaccard Index: (( jaccardIndex ))
  </div>
</div>

<div class="columns">
    <div class="column has-text-centered">
    Jaccard Distance: (( jaccardDistance ))
  </div>
</div>


</div>

{% include extras/vue.html %}

<script>
Vue.component('words-list', {
    props: ['words'],
    template: '<li> (( words.sentence )) </li>'
})
var app = new Vue({
    delimiters: ["((", "))"],
    el: '#app',
    data: {
        sentenceOne: { 'sentence': 'I am a robot'},
        sentenceTwo: { 'sentence': 'You are a robot'}
    },
    methods: {
        getWords: function (sentence) {
            return [...new Set(sentence.replace(/[^a-zA-Z\s]/g, '').toLowerCase().split(' '))].filter(function (el) {
                return el != '';
                })
        },
        getIntersect: function (one, two) {
            return one.filter(value => two.includes(value))
        },
        getUnion: function (one, two) {
            return [...new Set([...one, ...two])]
        }
    },
    computed: {
        sentenceOneWords: function () {
            return this.getWords( this.sentenceOne.sentence )
        },
        sentenceTwoWords: function () {
            return this.getWords( this.sentenceTwo.sentence )
        },
        intersectWords: function () {
            return this.getIntersect( this.sentenceOneWords, this.sentenceTwoWords )
        },
        unionWords: function () {
            return this.getUnion( this.sentenceOneWords, this.sentenceTwoWords )
        },
        jaccardIndex: function () {
            return this.intersectWords.length / this.unionWords.length
        },
        jaccardDistance: function () {
            return 1 - this.jaccardIndex
        }
    }
})
</script>
