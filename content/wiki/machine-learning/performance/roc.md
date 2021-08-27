---
title: "Receiver Operating Characteristics: ROC"
description: "ROC is used to judging the performance of classifiers"
date: 2020-05-13
categories:
  - "Machine Learning"
tags:
  - "Machine Learning"
  - "Performance"
  - "Basics"
links:
  - wiki/machine-learning/basics/confusion-matrix.md
  - wiki/machine-learning/linear/logistic-regression.md
references:
  - name: "Fawcett, T. (2006). An introduction to ROC analysis. Pattern Recognition Letters, 27(8), 861–874."
    link: "https://doi.org/10.1016/j.patrec.2005.10.010"
weight: 1
---

ROC space is the two-dimensional space spanned by True Positive Rate and False Positive Rate.

{{< figure src="../assets/roc/roc-color-blocks.png" caption="ROC Space. The color boxes are indicating the confusion matrices. Green is the fraction of true positive. Orange is the fraction of false positive. Refer to [Confusion Matrix](/wiki/machine-learning/basics/confusion-matrix/) for more details.">}}


## AUC: Area under Curve

1. TPR = TP Rate
2. FPR = FP Rate

The ROC curve is defined by the relation $f(TPR, FPR)$. Area under the ROC curve is

$$
\int TPR(FPR) d(FPR) \sim \sum_i TPR_i *\Delta FPR.
$$

If AUC = 1, we have TP Rate = 1 for all FP Rate. This is the best performance a model could have.

## How to Calculate ROC Curve

> Not every model has an AUC. To get the AUC curve, we need a hyperparameter to be tuned to get different TP Rate and FP Rate.

In logistic regression, a threshold $T$ is predetermined to decide which label to use in classifications.

By tuning the threshold $T$, we get different TP Rate $TPR$ and FP Rate $FPR$, i.e., $TPR(T)$ and $FPR(T)$. The parametric relations between $TPR(T)$ and $FPR(T)$ forms the ROC curve.
