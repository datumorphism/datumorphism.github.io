---
title: "Information Gain"
excerpt: "The information is a measurement of the entropy of the dataset."
date: 2020-01-16
category:
- 'Machine Learning'
- 'Measurement'
tag:
- 'Data'
references:
  - name: "Shalev-Shwartz, S., & Ben-David, S. (2013). Understanding machine learning: From theory to algorithms. Understanding Machine Learning: From Theory to Algorithms."
    link: "https://doi.org/10.1017/CBO9781107298019"
related:
  - name: Decision Tree
    link: /wiki/machine-learning/tree-based/decision-tree
  - name: Gini Impurity
    link: /cards/machine-learning/measurement/gini-impurity
supplementary:
  - name: Code
    link: https://github.com/datumorphism/mini-code/blob/master/decision_tree/decision_tree_example.ipynb
---

Information gain is a frequently used metric in calculating the gain during a split in tree-based methods.

First o all, the entropy of a dataset if defined as

$$
S = - sum_i p_i \log p_i - sum_i (1-p_i)\log p_i,
$$

where $p_i$ is the probability of a class.

The information gain is the difference between the entropy.

For example, in a decision tree algorithm, we would split a node. Before splitting, we assign a label $m$ to the node,

$$
S_m = - p_m \log p_m - (1-p_m)\log p_m.
$$

After the splitting, we have two groups that contributes to the entropy, group $L$ and group $R$,

$$
S'_m = p_L (- p_m \log p_m - (1-p_m)\log p_m) + p_R (- p_m \log p_m - (1-p_m)\log p_m),
$$

where $p_L$ and $p_R$ are the probabilities of the two groups. Suppose we have 100 samples before splitting and 29 samples in the left group and 71 samples in the right group, we have $p_L = 29/100$ and $p_R = 71/100$.

The information gain is thus

$$
Gain = S_m - S'_m.
$$





