---
title: "Receiver Operating Characteristics: ROC"
excerpt: "ROC is used to judging the performance of classifiers"
date: 2020-05-13
toc: true
category:
- 'Machine Learning::Performance'
tag:
- 'Machine Learning'
- 'Basics'
related:
  - name: Confusion Matrix
    link: /wiki/machine-learning/basics/confusion-matrix
references:
  - name: "Fawcett, T. (2006). An introduction to ROC analysis. Pattern Recognition Letters, 27(8), 861–874."
    link: "https://doi.org/10.1016/j.patrec.2005.10.010"
weight: 1
---

ROC space is the two dimensional space spanned by True Positive Rate and False Positive Rate.

<figure markdown="1">
![](../assets/roc/roc-color-blocks.png)
<figcaption markdown="1">
ROC Space. The color boxes are indicating the confusion matrices. Refer to [Confusion Matrix](/wiki/machine-learning/basics/confusion-matrix/) for more details.
</figcaption>
</figure>


## AUC: Area under Curve

1. TPR = TP Rate
2. FPR = FP Rate

The ROC curve is defined by the relation $f(TPR, FPR)$. Area under the ROC curve is

$$
\int TPR(FPR) d(FPR) \sim \sum_i TPR_i *\Delta FPR.
$$

If AUC = 1, we have TP Rate = 1 for all FP Rate. This is the best performance a model could have.
