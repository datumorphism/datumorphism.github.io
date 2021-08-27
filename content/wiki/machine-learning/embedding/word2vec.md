---
title: "Word2vec"
description: "Single-layer neural network creates embedding space"
date: 2019-06-13
categories:
  - 'Machine Learning'
tags:
  - 'Machine Learning'
  - 'Embedding'
  - 'Word2vec'
references:
  - link: http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/
    name: Word2Vec Tutorial - The Skip-Gram Model
  - name: "The Illustrated Word2vec"
    link: "http://jalammar.github.io/illustrated-word2vec/"
  - name: "On word embeddings - Part 1"
    link: "https://ruder.io/word-embeddings-1/index.html"
links:
  - cards/machine-learning/embedding/continuous-bag-of-words.md
  - cards/machine-learning/embedding/continuous-skip-gram.md
  - cards/machine-learning/embedding/negative-sampling.md
weight: 2
---


Word2vec is a word embedding model that learns the probability of some words being neighbours in a sentence $p_{neighbours}(w_i, w_o)$.

1. Build a dataset of adjacent words. [CBOW](/cards/machine-learning/embedding/continuous-bag-of-words/); [skipgram](/cards/machine-learning/embedding/continuous-skip-gram/); [negative sampling](/cards/machine-learning/embedding/negative-sampling/);
2. Encode the words using vectors.
3. Build a model $f(\\{\theta_i\\})$ to calculate the probability of the words being neighours and improve the parameters $\\{\theta_i\\}$ using the dataset.





