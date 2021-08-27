---
title: "CBOW: Continuous Bag of Words"
description: "Use the context to predict the center word"
date: 2020-01-16
categories:
  - 'Machine Learning::Embedding'
tags:
  - 'Word2vec'
references:
  - name: "Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Efficient estimation of word representations in vector space. arXiv:1301.3781"
    link: "https://arxiv.org/abs/1301.3781"
    key: mikolov2013
  - name: "The Illustrated Word2vec"
    link: "http://jalammar.github.io/illustrated-word2vec/"
---

{{< message class="info" >}}
Here we encode all words presented in the corpus to demostrate the idea of CBOW. In the real world, we might want to remove some certain words such as `the`.
{{</message>}}

We use the following quote by Ford in Westworld as an example.

> I read a theory once that the human intellect is like peacock feathers. Just an extravagant display intended to attract a mate, just an elaborate mating ritual. But, of course, the peacock can barely fly. It lives in the dirt, pecking insects out of the muck, consoling itself with its great beauty.

The word `intended` is surrunded by `extravagant display` in the front and `to attract` after it. The task is to predict the middle word `intended` using the 'history words' `extravagant display` and `to attract`.

- Input: `extravagant`, `display`, `to`, `attract`
- Output: `intended`

In the bag-of-words model, the order of the words `extravagant`, `display`, `to`, `attract` doesn't matter hence bag-of-words. [[mikolov2013](#mikolov2013)]

This makes it easier to represent the dataset:

| Input (Context) | Output (Center Word) |
|:----:|:-----:|
| `extravagant` | `intended` |
| `display` | `intended` |
| `to` | `intended` |
| `attract` | `intended` |

To create a real dataset, we "slide" over all the words.

| Input (Context) | Output (Center Word) |
|:----:|:-----:|
| `read` | `I` |
| `a` | `I` |
| `I` | `read` |
| `a` | `read` |
| `theory` | `read` |
| `I` | `a` |
| `read` | `a` |
| `theory` | `a` |
| `once` | `a` |
| `read` | `theory` |
| `a` | `theory` |
| `once` | `theory` |
| ... | ... |


It is not required to choose two words as history words and two words as future words. The number of words to choose is the window size.


