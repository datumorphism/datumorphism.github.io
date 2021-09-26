---
title: "Statistics of Graphs"
date: "2021-09-25"
categories:
  - "Graph"
tags:
  - "Graph"
  - "Basics"
  - "Statistics"
references:
  - name: "Hamilton WL. Graph Representation Learning. Morgan & Claypool Publishers; 2020. pp. 1–159. doi:10.2200/S01045ED1V01Y202009AIM046"
    link: "https://www.morganclaypool.com/doi/10.2200/S01045ED1V01Y202009AIM046"
    key: "Hamilton2020"
weight: 2
links:
  - "wiki/graph/basics/what-is-graph.md"
  - "cards/graph/node-degree.md"
  - "cards/graph/graph-eigenvector-centrality.md"
  - "cards/graph/graph-betweenness-centrality.md"
  - "cards/graph/graph-local-variant-clustering-coefficient.md"
---

## Local Statistics

### Node Degree

{{< c "cards/graph/node-degree.md" >}}


### Node Centrality

Importance of a node on a graph:

- {{< c "cards/graph/graph-eigenvector-centrality.md" >}}
- {{< c "cards/graph/graph-betweenness-centrality.md" >}}
- Closeness centrality


### Clustering Coefficients


Proportion of motifs, e.g., closed triangles, in a node's neighborhood.

- {{< c "cards/graph/graph-local-variant-clustering-coefficient.md" >}}




## Graph Level Statistics

### Bag of Nodes

Using the statistics of the local statistics, e.g., distribution of node degrees, as graph level statistics.

### Weisfeiler-Lehmen Kernel

- {{< c "cards/graph/graph-weisfeiler-lehman-kernel.md" >}}



[^Hamilton2020]: {{< cite key="Hamilton2020" >}}
