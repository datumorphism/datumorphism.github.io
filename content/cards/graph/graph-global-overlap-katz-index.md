---
title: "Graph Global Overlap Measure: Katz Index"
date: "2021-09-26"
categories:
  - 'Graph'
tags:
  - "Graph"
  - "Basics"
  - "Clustering"
references:
  - name: "Katz L. A new status index derived from sociometric analysis. Psychometrika. 1953;18: 39–43. doi:10.1007/BF02289026"
    link: "https://link.springer.com/article/10.1007%2FBF02289026"
    key: "Katz1953"
  - name: "Hamilton WL. Graph Representation Learning. Morgan & Claypool Publishers; 2020. pp. 1–159. doi:10.2200/S01045ED1V01Y202009AIM046"
    link: "https://www.morganclaypool.com/doi/10.2200/S01045ED1V01Y202009AIM046"
    key: "Hamilton2020"
links:
  - "cards/graph/graph-adjacency-matrix.md"
---

The Katz index is

{{< m >}}
\mathbf S_{\text{Katz}}[u,v] = \sum_{i=1}^\infty \beta^i \mathbf A^i[u, v],
{{< /m >}}

where $\mathbf A^i[u, v]$ is the matrix $\mathbf A$ to the $i$th power. Some for $\beta^i$. The Katz index describes the similarity between of node $u$ and node $v$.

{{< message title="Do not confuse power with contravariant indices" class="warning" >}}

For readers familiar with tensor notations, it might be confusing. We some times use contravariant indices on the top right of the tensor notation.

But here ${}^{i}$ means to the $i$th power.

{{< /message >}}

The index is proved to be the following

{{< m >}}
\mathbf S_{\text{Katz}} = (\mathbf I - \beta \mathbf A)^{-1} - \mathbf I.
{{< /m >}}



## Parameter $\beta$

The parameter $\beta$ is the punishment for path length. If $\beta < 1$, each increase in power will make the whole term $\beta^i A^i$ smaller. If a path between $u$ and $v$ is longer, i.e., $i$ is larger, then the weight $\beta^i$ is smaller.

{{< e "cards/graph/graph-adjacency-matrix.md" >}}