---
title: "Solving Problems on Graph"
date: "2021-09-25"
categories:
  - "Graph"
tags:
  - "Graph"
  - "Basics"
references:
  - name: "Hamilton WL. Graph Representation Learning. Morgan & Claypool Publishers; 2020. pp. 1–159. doi:10.2200/S01045ED1V01Y202009AIM046"
    link: "https://www.morganclaypool.com/doi/10.2200/S01045ED1V01Y202009AIM046"
    key: "Hamilton2020"
  - name: "Sanchez-Lengeling B, Reif E, Pearce A, Wiltschko AB. A Gentle Introduction to Graph Neural Networks. Distill. 2021;6. doi:10.23915/distill.00033"
    link: "https://distill.pub/2021/gnn-intro/"
    key: "Sanchez-Lengeling2021"
  - name: "McPherson M, Smith-Lovin L, Cook JM. Birds of a Feather: Homophily in Social Networks. Annu Rev Sociol. 2001;27: 415–444. doi:10.1146/annurev.soc.27.1.415"
    link: "https://www.annualreviews.org/doi/10.1146/annurev.soc.27.1.415"
    key: "McPherson2001"
weight: 4
links:
  - "wiki/graph/basics/what-is-graph.md"
  - "reading/popularity-vs-similarity.md"
  - "cards/graph/homophily.md"
  - "cards/graph/heterophily.md"
  - "cards/graph/structural-equivalence.md"
---


## Node Classification

Given graph that has incomplete attribute labeling of the nodes, predict the attributes on the nodes.


The following concepts can be used to classify nodes.

- {{< c "cards/graph/homophily.md" "Homophily">}},
- {{< c "cards/graph/structural-equivalence.md" "Structural equivalence">}},
- {{< c "cards/graph/heterophily.md" "Heterophily" >}}.



## Relation Prediction

Given $\mathcal V$, $\mathcal E_{\text{train}}\subset \mathcal E$, predict other edges $\mathcal E \setminus \mathcal E_{\text{train}}$.



## Clustering and Community Detection

Assign nodes to groups. See {{< c "reading/popularity-vs-similarity.md" >}} for examples.

## Graph Classification, Regression, and Clustering

Given some graphs, perform classification, regression, and clustering on the set of graphs.



[^Hamilton2020]: {{< cite key="Hamilton2020" >}}

[^Sanchez-Lengeling2021]: {{< cite key="Sanchez-Lengeling2021" >}}