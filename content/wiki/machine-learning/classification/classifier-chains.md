---
title: "Classifier Chains for Multilabel Classification"
description: "Classifier chains is a method to predict hierarchical class labels"
date: 2021-03-24
authors:
  - "LM"
categories:
  - "machine learning"
tags:
  - "machine learning"
  - "supervised learning"
  - "classification"
  - "multilabel"
references:
  - name: "Read J, Pfahringer B, Holmes G, Frank E. Classifier Chains for Multi-label Classification. 2009. pp. 254–269."
    link: "https://doi.org/10.1007/978-3-642-04174-7_17"
weight:
links:
  - "wiki/machine-learning/performance/roc.md"
  - "wiki/machine-learning/basics/confusion-matrix.md"
---

## Multi-label problem

In some classification problems, we have multilabel labels to be predicted. Many different approaches are proposed to solve such problems.


### Algorithm Level

Develop algorithms for multilabel problems, such as

1. Decision trees,
2. AdaBoost.


### Problem Transformation

On problem or data level, we can transform the multi-label problem to one or more single label problems.

#### Binary Relevance Method

Binary relevance method, aka BM, transforms the problem into a single label problem by training a binary classifier for each label.

By doing so, the correlations between the target labels are lost.

#### Label Combination Method

Label combination method (label power-set method), aka CM, combines the labels into single labels.


#### Classifier Chain

Classifer chains, aka CC, trains $l$ classifiers where $l$ is the number of labels for each record.

{{< figure src="../assets/classifier-chains/classifier-chains-algo.png" title="Algorithm of Classifier Chains" caption="Read J, Pfahringer B, Holmes G, Frank E. Classifier Chains for Multi-label Classification. 2009. pp. 254–269." >}}

