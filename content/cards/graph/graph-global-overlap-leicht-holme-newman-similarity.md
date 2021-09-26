---
title: "Graph Global Overlap Measure: Leicht-Holme-Newman Index"
date: "2021-09-26"
categories:
  - 'Graph'
tags:
  - "Graph"
  - "Basics"
  - "Clustering"
references:
  - name: "Lu L, Zhou T. Link Prediction in Complex Networks: A Survey. arXiv [physics.soc-ph]. 2010. Available: http://arxiv.org/abs/1010.0725"
    link: "http://arxiv.org/abs/1010.0725"
    key: "Lue2010"
  - name: "Hamilton WL. Graph Representation Learning. Morgan & Claypool Publishers; 2020. pp. 1–159. doi:10.2200/S01045ED1V01Y202009AIM046"
    link: "https://www.morganclaypool.com/doi/10.2200/S01045ED1V01Y202009AIM046"
    key: "Hamilton2020"
links:
  - "cards/graph/graph-adjacency-matrix.md"
  - "cards/graph/graph-global-overlap-katz-index.md"
---

## From Katz Index to LHN Index

{{< c "cards/graph/graph-global-overlap-katz-index.md" "Katz Index" >}} has a knob to tune the punishment towards longer paths. The Leicht-Holme-Newman Similarity, aka, LHN Similarity, has a better normalization factor.

The LHN similarity of a graph $\mathcal G$ normalizes the path calculation by the expected number of path in a random graph $\tilde{\mathcal G}$[^Hamilton2020].

{{< message title="Not Every Random Graph" >}}

We require $\tilde{\mathcal G}$ to have the **same set of node degrees** as $\mathcal G$. Such a graph is a configuration model.

{{< /message >}}

The expected number of path different path length is not analytically feasible in general. We have for lower power

{{< m >}}
\begin{align}
\mathbb E [ A[u,v] ] &= \frac{d_u d_v}{2\lvert \mathcal E\rvert} \\
\mathbb E [ A^2[u,v] ] &= \frac{d_u d_v}{2\lvert \mathcal E\rvert} \sum_{u\in \mathcal V} (d_m-1) d_u.
\end{align}
{{< /m >}}

However, a iterative method shows us an approximation and we can approximate the LHN similarity using[^Hamilton2020],

{{< m >}}
S_{\text{LHN}} = 2\alpha m \lambda_1 \mathbf D^{-1} \left( \mathbf I - \frac{\beta}{\lambda_1} \mathbf A \right)^{-1} \mathbf D^{-1},
{{< /m >}}

where $\mathbf D$ is the matrix $\mathrm{diag} ({d_1, d_2, \cdots})$, and $\lambda_1$ is the largest eigenvalue of the adjacency matrix $\mathbf A$.


## Indications of LHN Index

Lue & Zhou wrote an intuitive review of LHN similarity[^Lue2010]. The idea of LHN implements the idea that two nodes $u$ and $v$ are similar if their neighbors $\mathcal N(u)$ and $\mathcal N(v)$ are similar,

{{< m >}}
\mathbf S_{\text{LHN}} = \beta \mathbf A \mathbf S_{\text{LHN}} + \alpha \mathbf I,
{{< /m >}}

where $\alpha$ and $\beta$ are free parameters that controls the punishment of different lengths.

Moving the matrices around, we get

{{< m >}}
\mathbf S_{\text{LHN}} = \alpha ( \mathbf I - \beta \mathbf A)^{-1}.
{{< /m >}}


[^Hamilton2020]: {{< cite key="Hamilton2020" >}}

[^Lue2010]: {{< cite key="Lue2010" >}}