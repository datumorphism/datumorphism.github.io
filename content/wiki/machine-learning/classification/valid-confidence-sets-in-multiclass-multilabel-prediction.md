---
title: "Valid Confidence Sets in Multiclass and Multilabel Prediction"
description: ""
date: 2021-04-08
authors:
  - "Lei Ma"
categories:
  - "machine learning"
tags:
  - "statistics"
  - "classification"
  - "multilabel"
  - "multiclass"
  - "conformal inference"
references:
  - name: "Cauchois M, Gupta S, Duchi JC. Knowing what You Know: valid and validated confidence sets in multiclass and multilabel prediction. J Mach Learn Res. 2021;22: 1–42. Available: http://jmlr.org/papers/v22/20-753.html"
    link: "https://jmlr.org/papers/v22/20-753.html"
weight:
links:
  - "wiki/machine-learning/classification/classifier-chains.md"
  - "wiki/machine-learning/classification/hierarchical-classification.md"
  - "wiki/machine-learning/performance/roc.md"
---


Ask for valid confidence:
- "Valid": validate for test data, train data, or the generating process?
- "Confidence": $P(Y \notin C(X)) \le \alpha$



To avoid too much attention on data based validation, a framework called conformal inference was proposed by Vovk et al. in 2005,

- $n$ observations,
- desired confidence level $1-\alpha$,
- construct confidence sets $C(x)$ using conform methods so that the sets capture the underlying the distribution
	- a new pair $(X_{n+1}, Y_{n+1})$ from the same distribution,
	- $P(Y_{n+1}\in C(X_{n+1})) \le 1-\alpha$