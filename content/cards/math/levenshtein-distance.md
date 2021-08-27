---
title: "Levenshtein Distance"
date: 2019-05-19
categories:
- 'Math'
tags:
- 'Distance'
- 'NLP'
references:
- name: "levenshtein-distance @ trekhleb/javascript-algorithms"
  link: https://github.com/trekhleb/javascript-algorithms/tree/master/src/algorithms/string/levenshtein-distance
---

Levenshtein distance calculates the number of operations needed to change one word to another by applying single-character edits (insertions, deletions or substitutions).

The reference explains this concept very well. For consistency, I extracted a paragraph from it which explains the operations in Levenshtein algorithm. The source of the following paragraph is the first reference of this article.

{{< message title="Levenshtein Matrix" class="info" >}}

![Levenshtein Matrix](../assets/levenshtein-distance/levenshtein-matrix.png)

- Cell `(0:1)` contains red number 1. It means that we need 1 operation to transform `M` to an empty string. And it is by deleting `M`. This is why this number is red.
- Cell `(0:2)` contains red number 2. It means that we need 2 operations to transform `ME` to an empty string. And it is by deleting `E` and `M`.
- Cell `(1:0)` contains green number 1. It means that we need 1 operation to transform an empty string to `M`. And it is by inserting `M`. This is why this number is green.
- Cell `(2:0)` contains green number 2. It means that we need 2 operations to transform an empty string to `MY`. And it is by inserting `Y` and  `M`.
- Cell `(1:1)` contains number 0. It means that it costs nothing to transform `M` into `M`.
- Cell `(1:2)` contains red number 1. It means that we need 1 operation to transform `ME` to `M`. And it is by deleting `E`.
- And so on...

From: [levenshtein-distance @ trekhleb/javascript-algorithms](https://github.com/trekhleb/javascript-algorithms/tree/master/src/algorithms/string/levenshtein-distance)

{{</message>}}


## Examples

{{< rawhtml >}}
<div id="app">
<div class="columns">
  <div class="column has-text-centered">
    <div class="field">
        <label class="label">Word One</label>
            <div class="control">
                <input v-model="sentenceOne.sentence" class="input" type="text">
            </div>
        Characters: (( sentenceOneWords ))
    </div>
  </div>

  <div class="column has-text-centered">
    <div class="field">
        <label class="label">Word Two</label>
            <div class="control">
                <input v-model="sentenceTwo.sentence" class="input" type="text">
            </div>
        Characters: (( sentenceTwoWords ))
    </div>
  </div>
</div>


<div class="columns">
    <div class="column has-text-centered">
    Levenshtein Distance: (( levenshteinDistance ))
  </div>
</div>


</div>

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

<script>

/**
 * @param {string} a
 * @param {string} b
 * @return {number}
 */
function levenshteinDistance(a, b) {
  // Create empty edit distance matrix for all possible modifications of
  // substrings of a to substrings of b.
  const distanceMatrix = Array(b.length + 1).fill(null).map(() => Array(a.length + 1).fill(null));

  // Fill the first row of the matrix.
  // If this is first row then we're transforming empty string to a.
  // In this case the number of transformations equals to size of a substring.
  for (let i = 0; i <= a.length; i += 1) {
    distanceMatrix[0][i] = i;
  }

  // Fill the first column of the matrix.
  // If this is first column then we're transforming empty string to b.
  // In this case the number of transformations equals to size of b substring.
  for (let j = 0; j <= b.length; j += 1) {
    distanceMatrix[j][0] = j;
  }

  for (let j = 1; j <= b.length; j += 1) {
    for (let i = 1; i <= a.length; i += 1) {
      const indicator = a[i - 1] === b[j - 1] ? 0 : 1;
      distanceMatrix[j][i] = Math.min(
        distanceMatrix[j][i - 1] + 1, // deletion
        distanceMatrix[j - 1][i] + 1, // insertion
        distanceMatrix[j - 1][i - 1] + indicator, // substitution
      );
    }
  }

  return distanceMatrix[b.length][a.length];
}


var app = new Vue({
    delimiters: ["((", "))"],
    el: '#app',
    data: {
        sentenceOne: { 'sentence': 'Heute'},
        sentenceTwo: { 'sentence': 'Leute'}
    },
    methods: {
        getUniqueWords: function (sentence) {
            return [...new Set(sentence.replace(/[^a-zA-Z\s]/g, '').toLowerCase().split(' '))].filter(function (el) {
                return el != '';
                })
        },
        getWords: function (sentence) {
            return sentence.replace(/[^a-zA-Z\s]/g, '').toLowerCase().split(' ').filter(function (el) {
                return el != '';
                })
        },
        getCharacters: function (sentence) {
            return sentence.replace(/[^a-zA-Z]/g, '').toLowerCase().split('').filter(function (el) {
                return el != '';
                })
        },
        getIntersect: function (one, two) {
            return one.filter(value => two.includes(value))
        },
        getUnion: function (one, two) {
            return [...new Set([...one, ...two])]
        },
        getL2Norm: function ( arr ) {
            var l2Norm = 0
            arrLength = arr.length;
            for ( var i = 0; i < arrLength; i ++ ) {
                l2Norm = l2Norm + arr[i] * arr[i]
            }

            return Math.sqrt(l2Norm)
        }
    },
    computed: {
        sentenceOneWords: function () {
            return this.getCharacters( this.sentenceOne.sentence )
        },
        sentenceTwoWords: function () {
            return this.getCharacters( this.sentenceTwo.sentence )
        },
        levenshteinDistance: function () {
            return levenshteinDistance( this.sentenceOneWords,
            this.sentenceTwoWords )
        }
    }
})
</script>
{{< /rawhtml >}}