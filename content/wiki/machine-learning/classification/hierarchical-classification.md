---
title: "Hierarchical Classification"
description: ""
date: 2021-03-30
authors:
  - "LM"
categories:
  - "machine learning"
tags:
  - "machine learning"
  - "supervised learning"
  - "classification"
  - "multilabel"
  - "multiclass"
references:
  - name: "Silla CN, Freitas AA. A survey of hierarchical classification across different application domains. Data Min Knowl Discov. 2011;22: 31–72. doi:10.1007/s10618-010-0175-9"
    link: "https://link.springer.com/article/10.1007%2Fs10618-010-0175-9"
    key: "Silla2011"
  - name: "Read J, Pfahringer B, Holmes G, Frank E. Classifier Chains for Multi-label Classification. 2009. pp. 254–269. doi:10.1007/978-3-642-04174-7_17"
    link: "https://doi.org/10.1007/978-3-642-04174-7_17"
    key: "Read2009"
  - name: "The Hitchhiker’s Guide to Hierarchical Classification"
    link: "https://towardsdatascience.com/https-medium-com-noa-weiss-the-hitchhikers-guide-to-hierarchical-classification-f8428ea1e076"
weight:
links:
  - "wiki/machine-learning/classification/classifier-chains.md"
---

## Hierarchical Classification Problem

Hierarchical classification labels involves hierarchical class labels. The hierarchical class labels maybe predefined or inferred. [^Silla2011]

### Class Taxonomy

A hierarchical classification problem comes with a class taxonomy.

- "IS-A" operator: $\prec$,
- "IS-NOT-A" operator: $\nprec$

A IS-A relationship of the labels $c_a$ class set $C$ is

- one root $R$ in the tree,
- asymmetric, i.e., $c_i \prec c_j$ and $c_j\prec c_i$ can not be both true,
- anti-reflexive, i.e., $c_i \nprec c_i$,
- transitive, i.e., $c_i \prec c_j$ and $c_j\prec c_k$ $\Rightarrow$ $c_i \prec c_k$.

There are different representations of the hierarchical taxonomies.

{{< figure src="../assets/hierarchical-classification/hierarchical-classification-taxonomy-tree-vs-dag.png" caption="Figure 2 in Silla2011, showing the difference between tree taxonomy and DAG taxonomy." >}}



- A classifier doesn't necessarily classify the labels to the leaves on the tree all the time.
- A classifier can utilize the tree of DAG differently:
	- top-down: local classifiers that only utilizes partial hierarchical information, e.g., the prediction of the children will use the prediction of the parent as input; {{< c "wiki/machine-learning/classification/classifier-chains.md" "Classifier Chains" >}};
	- big-bang: global classifiers with each classifier utilizes the whole paths;
	- flat: classifiers ignores the hierarchical relations and predicting the leaves.



## Flat Classification

Classify the leaves and forget about the hierarchies.


1. The hierarchical information is not being used.


## Global Classifiers

Also called Big-Bang approach, golbal classifiers can utilize

1. Clusters in the taxnomony,
2. Multi-label classification with full paths,
3. Revise models, e.g., loss function calculation to include hierarchical information.



[^Silla2011]: {{< cite key="Silla2011" >}}