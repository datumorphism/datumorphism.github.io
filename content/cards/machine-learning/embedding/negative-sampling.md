---
title: "Negative Sampling"
description: "negative sampling makes the calculations faster"
date: 2020-01-16
category:
- 'Machine Learning::Embedding'
tags:
- 'Word2vec'
references:
  - name: "Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Efficient estimation of word representations in vector space. arXiv:1301.3781"
    link: "https://arxiv.org/abs/1301.3781"
    key: mikolov2013
  - name: "The Illustrated Word2vec"
    link: "http://jalammar.github.io/illustrated-word2vec/"
links:
  - cards/machine-learning/embedding/continuous-bag-of-words.md
  - cards/machine-learning/embedding/continuous-skip-gram.md
---

> Knowledge of [CBOW](/cards/machine-learning/embedding/continuous-bag-of-words/) or [skipgram](/cards/machine-learning/embedding/continuous-skip-gram/) is required.

A naive model to train a model of words is to

1. encode input words and output words using vectors,
2. use the input word vector to predict the output word vector,
3. calculate the errors between predicted output word vector and real output word vector,
4. minimize the errors.

However, it is very expensive to prject out the output words and calcualte the error eveytime. A trick is to use **negative sampling**.

Negative sampling adds a new column to the data as the predictions.

| Input (Center Word) | Output (Context) | Target (is Neighbour) |
|:----:|:-----:|:----:|
| `intended` | `extravagant` | 1 |
| `intended` | `display` | 1 |
| `intended` | `to` | 1 |
| `intended` | `attract` | 1 |

Now we have a problem. The target is always 1. This dataset might lead to network that outputs 1 all the time. We need some nagative samples to make it noisy. We randomly sampled words from the dictionary.

| Input (Center Word) | Output (Context) | Target (is Neighbour) |
|:----:|:-----:|:----:|
| `intended` | `extravagant` | 1 |
| `intended` | `display` | 1 |
| `intended` | `to` | 1 |
| `intended` | `attract` | 1 |
| `intended` | `I` | 0 |
| `intended` | `a` | 0 |
| `intended` | `intellect` | 0 |
| `intended` | `mating` | 0 |
| `intended` | `course` | 0 |


