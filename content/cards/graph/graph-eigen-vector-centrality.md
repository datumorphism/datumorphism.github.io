---
title: "Eigenvector Centrality of a Graph"
date: "2021-09-25"
categories:
  - 'Graph'
tags:
  - "Graph"
  - "Statistics"
references:
  - name: "Hamilton WL. Graph Representation Learning. Morgan & Claypool Publishers; 2020. pp. 1–159. doi:10.2200/S01045ED1V01Y202009AIM046"
    link: "https://www.morganclaypool.com/doi/10.2200/S01045ED1V01Y202009AIM046"
    key: "Hamilton2020"
links:
  - "wiki/graph/basics/what-is-graph.md"
---

Given a graph with adjacency matrix $\mathbf A$, the eigenvector centrality is

{{< m >}}
\mathbf e_u = \frac{1}{\lambda} \sum_{v\in\mathcal V} \mathbf A[u,v] \mathbf e_v, \qquad \forall u \in \mathcal V.
{{< /m >}}

{{< message title="Why is it called Eigenvector Centrality" >}}

The definition is equivalent to

$$
\lambda \mathbf e = \mathbf A\mathbf e.
$$

{{< /message >}}