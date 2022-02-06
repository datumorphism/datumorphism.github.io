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
  - "cards/graph/graph-local-clustering-coefficient.md"
  - "cards/graph/graph-local-overlap-sorensen-index.md"
  - "cards/graph/graph-local-overlap-salton-index.md"
  - "cards/math/jaccard-similarity.md"
  - "cards/graph/graph-local-overlap-resource-allocation-index.md"
  - "cards/graph/graph-local-overlap-adamic-adar-index.md"
  - "cards/graph/graph-global-overlap-katz-index.md"
  - "cards/graph/graph-global-overlap-leicht-holme-newman-similarity.md"
  - "cards/graph/graph-global-overlap-random-walk-similarity.md"
---

## Local Statistics

### Node Degree

{{< e ref="cards/graph/node-degree.md" >}}


### Node Centrality

Importance of a node on a graph:

- {{< e "cards/graph/graph-eigenvector-centrality.md" >}}
- {{< e "cards/graph/graph-betweenness-centrality.md" >}}
- Closeness centrality


### Clustering Coefficients


Proportion of motifs, e.g., closed triangles, in a node's neighborhood.

{{< e "cards/graph/graph-local-clustering-coefficient.md" >}}




## Graph Level Statistics

### Bag of Nodes

Using the statistics of the local statistics, e.g., distribution of node degrees, as graph level statistics.

### Weisfeiler-Lehmen Kernel

{{< e ref="cards/graph/graph-weisfeiler-lehman-kernel.md" >}}



## Neighborhood Overlap

We can define many different similarity measures $\mathbf S$.

- Number of shared neighbor nodes: $\mathbf S[u, v] = \lvert \mathcal N(u) \cap \mathcal N(v) \rvert$. The likelihood of an edge between $u$ and $v$, $P(A[u,v]=1) \propto \mathcal S[u,v]$.

- Local Overlap Measures
  - {{< e "cards/graph/graph-local-overlap-sorensen-index.md" >}}
  - {{< e "cards/graph/graph-local-overlap-salton-index.md" >}}
  - {{< e "cards/math/jaccard-similarity.md" >}}
  - {{< e "cards/graph/graph-local-overlap-resource-allocation-index.md" >}}
  - {{< e "cards/graph/graph-local-overlap-adamic-adar-index.md" >}}
- Global Overlap Measures
  - {{< e "cards/graph/graph-global-overlap-katz-index.md" >}}
  - {{< e "cards/graph/graph-global-overlap-leicht-holme-newman-similarity.md" >}}
  - {{< e "cards/graph/graph-global-overlap-random-walk-similarity.md" >}}




[^Hamilton2020]: {{< cite key="Hamilton2020" >}}
