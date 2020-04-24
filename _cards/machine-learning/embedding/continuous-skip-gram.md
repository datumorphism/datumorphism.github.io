---
title: "CBOW: Continuous Bag of Words"
excerpt: ""
date: 2020-01-16
category:
- 'Machine Learning::Embedding'
tag:
- 'Word2vec'
references:
  - name: "Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Efficient estimation of word representations in vector space. arXiv:1301.3781"
    link: "https://arxiv.org/abs/1301.3781"
    key: mikolov2013
---

We use the following quote by Ford in Westworld as an example.

> I read a theory once that the human intellect is like peacock feathers. Just an extravagant display intended to attract a mate, just an elaborate mating ritual. But, of course, the peacock can barely fly. It lives in the dirt, pecking insects out of the muck, consoling itself with its great beauty.

The word `intended` is surrunded by `extravagant display` in the front and `to attract` after it. The task is to predict the probability of words around the middle word `intended`, which are the 'history words' `extravagant`, `display` and 'future words' `to`, `attract` in our case. [[mikolov2013](#mikolov2013)]
