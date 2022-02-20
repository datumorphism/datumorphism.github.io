---
title: "Cosine Similarity"
date: 2019-05-06
categories:
  - 'Math'
tags:
  - 'Set'
  - 'Distance'
references:
  - name: Cosine Similarity
    link: https://en.wikipedia.org/wiki/Cosine_similarity
links:
  - cards/math/jaccard-similarity.md
---

As simple as the inner product of two vectors

$$
d_{cos} = \frac{\vec A}{\vert \vec A \vert}  \cdot \frac{\vec B }{ \vert \vec B \vert}
$$




## Examples

To use cosine similarity, we have to vectorize the words first. There are many different methods to achieve this. For the purpose of illustrating cosine similarity, we use term frequency.

Term frequency is the occurrence of the words. We do not deal with duplications so duplicate words will have some effect on the similarity.

{{< message class="warning" >}}
In principle, we could also use word set for a sentence to remove the effect of duplicate words. In most cases, if a word is repeating, it would indeed make the sentences different. If duplicating words are becoming a problem, we will consider using [tf-idf](http://www.tfidf.com/).
{{</message>}}

{{< rawhtml >}}
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
    Union as Vector Element Labels: (( unionWords ))
  </div>
</div>

<div class="columns">
  <div class="column has-text-centered">
    <div class="field">
        <label class="label">Sentence One Vector</label>
        Sentence One Vector: (( sentenceOneVector ))
    </div>
  </div>

  <div class="column has-text-centered">
    <div class="field">
        <label class="label">Sentence Two Vector</label>
        Sentence Two Vector: (( sentenceTwoVector ))
    </div>
  </div>
</div>

<div class="columns">
    <div class="column has-text-centered">
    Cosine Similarity: (( cosineSimilarity ))
  </div>
</div>


</div>

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

<script>

var app = new Vue({
    delimiters: ["((", "))"],
    el: '#app',
    data: {
        sentenceOne: { 'sentence': 'I am a robot'},
        sentenceTwo: { 'sentence': 'You are a robot'}
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
        sentenceOneVector: function () {
            var unionLength = this.unionWords.length;
            var theSentenceWords = this.sentenceOneWords
            var theSentenceWordsLength = theSentenceWords.length;

            var vector = new Array(unionLength).fill(0)

            for (var i = 0; i < unionLength; i++) {
                for (var j = 0; j < theSentenceWordsLength; j++ ) {
                            if ( theSentenceWords[j] ==  this.unionWords[i] ) {
                                vector[i] = vector[i] + 1
                            }
                }
            }

            const vectorSum = arr => arr.reduce((a,b) => a * a, 0)
            l2Norm = this.getL2Norm(vector)
            return vector.map( function multiply(x){ return x/l2Norm; } )
        },
        sentenceTwoVector: function () {
            var unionLength = this.unionWords.length;
            var theSentenceWords = this.sentenceTwoWords
            var theSentenceWordsLength = theSentenceWords.length;

            var vector = new Array(unionLength).fill(0)

            for (var i = 0; i < unionLength; i++) {
                for (var j = 0; j < theSentenceWordsLength; j++ ) {
                            if ( theSentenceWords[j] ==  this.unionWords[i] ) {
                                vector[i] = vector[i] + 1
                            }
                }
            }

            l2Norm = this.getL2Norm(vector)

            return vector.map( function multiply(x){ return x/l2Norm; } )
        },
        cosineSimilarity: function () {
            cos_sim = 0
            var unionLength = this.unionWords.length;

            for (var i=0; i<unionLength;i++ ) {
                cos_sim = cos_sim + this.sentenceOneVector[i] * this.sentenceTwoVector[i]
            }

            return cos_sim
        }
    }
})
</script>
{{< /rawhtml >}}