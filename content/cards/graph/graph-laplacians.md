---
title: "Graph Laplacians"
date: "2021-09-25"
categories:
  - 'Graph'
tags:
  - "Graph"
  - "Heterophily"
references:
  - name: "Hamilton WL. Graph Representation Learning. Morgan & Claypool Publishers; 2020. pp. 1–159. doi:10.2200/S01045ED1V01Y202009AIM046"
    link: "https://www.morganclaypool.com/doi/10.2200/S01045ED1V01Y202009AIM046"
    key: "Hamilton2020"
---


Laplacian is a useful representation of graphs. The unnormalized Laplacian is

{{< m >}}
\mathbf L = \mathbf D - \mathbf A,
{{< /m >}}

where $\mathbf A$ is the {{< c "cards/graph/graph-adjacency-matrix.md" "adjacency matrix" >}} and $\mathbf D$ is the degree matrix, i.e., a diagonalized matrix with the diagonal elements being the degrees.

## Normalized Laplacian

The symmetric normalized Laplacian is

{{< m >}}
\mathbf L_{\text{sym}} = \mathbf D^{-1/2} \mathbf A \mathbf D^{-1/2}.
{{< /m >}}

The random walk Laplacian is

{{< m >}}
\mathbf L_{\text{RW}} = \mathbf D^{-1} \mathbf A.
{{< /m >}}
