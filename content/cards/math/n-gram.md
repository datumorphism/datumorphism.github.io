---
title: "n-gram"
date: 2019-05-19
category:
- 'Math'
tags:
- 'NLP'
references:
- name: words/n-gram
  link: https://github.com/words/n-gram/blob/master/index.js
---

n-gram is a method to split words into set of substring elements so that those can be used to match words.



## Examples

Use the following examples to get your first idea about it. I created two columns so that we could **compare the n-grams of two different words side-by-side**.

{{< rawhtml >}}
<div id="app">

<div class="columns">
  <div class="column has-text-centered is-2 is-offset-5">
    n in n-gram is <input v-model="nGram.n" class="input" type="number">
  </div>
</div>

<div class="columns">
  <div class="column has-text-centered">
    <div class="field">
        <label class="label">Word One</label>
            <div class="control">
                <input v-model="sentenceOne.sentence" class="input" type="text">
            </div>
        Clean Word: (( sentenceOneWords ))
    </div>
    <div class="has-text-centered">
    n-grams: (( sentenceOneWordsnGram ))
  </div>

  </div>

  <div class="column has-text-centered">
    <div class="field">
        <label class="label">Word Two</label>
            <div class="control">
                <input v-model="sentenceTwo.sentence" class="input" type="text">
            </div>
        Clean Word: (( sentenceTwoWords ))
    </div>
     <div class="has-text-centered">
      n-grams: (( sentenceTwoWordsnGram ))
    </div>

  </div>
</div>


</div>

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

<script>

/*************************/
/** The function nGram is a copy of https://github.com/words/n-gram , under MIT License **/
nGram.bigram = nGram(2)
nGram.trigram = nGram(3)

// Factory returning a function that converts a value string to n-grams.
function nGram(n) {
  if (typeof n !== 'number' || isNaN(n) || n < 1 || n === Infinity) {
    throw new Error('`' + n + '` is not a valid argument for n-gram')
  }

  return grams

  // Create n-grams from a given value.
  function grams(value) {
    var nGrams = []
    var index

    if (value === null || value === undefined) {
      return nGrams
    }

    value = value.slice ? value : String(value)
    index = value.length - n + 1

    if (index < 1) {
      return nGrams
    }

    while (index--) {
      nGrams[index] = value.slice(index, index + n)
    }

    return nGrams
  }
}
/*************************/

var app = new Vue({
    delimiters: ["((", "))"],
    el: '#app',
    data: {
        sentenceOne: { 'sentence': 'Heute'},
        sentenceTwo: { 'sentence': 'Leute'},
        nGram: {'n': 2}
    },
    methods: {
        getUniqueWords: function (sentence) {
            return [...new Set(sentence.replace(/[^a-zA-Z\s]/g, '').toLowerCase().split(' '))].filter(function (el) {
                return el != '';
                })
        },
        getCleanString: function (sentence) {
            return sentence.replace(/[^a-zA-Z\s]/g, '').toLowerCase()
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
            return this.getCleanString( this.sentenceOne.sentence )
        },
        sentenceTwoWords: function () {
            return this.getCleanString( this.sentenceTwo.sentence )
        },
        sentenceOneWordsnGram: function () {
            return nGram( parseInt(this.nGram.n) )( this.sentenceOneWords )
        },
        sentenceTwoWordsnGram: function () {
            return nGram( parseInt(this.nGram.n) )( this.sentenceTwoWords)
        }
    }
})
</script>
{{< /rawhtml >}}