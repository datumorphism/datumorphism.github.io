---
title: "Graph Local Overlap Measure: Sorensen Index"
date: "2021-09-26"
categories:
  - 'Graph'
tags:
  - "Graph"
  - "Basics"
  - "Clustering"
references:
  - name: "Hamilton WL. Graph Representation Learning. Morgan & Claypool Publishers; 2020. pp. 1–159. doi:10.2200/S01045ED1V01Y202009AIM046"
    link: "https://www.morganclaypool.com/doi/10.2200/S01045ED1V01Y202009AIM046"
    key: "Hamilton2020"
---

The Sorensen index is

{{< m >}}
\mathbf S_{\text{Sorensen}}[u,v] = \frac{ 2\lvert \mathcal N (u) \cap \mathcal N(v) \rvert }{ d_u + d_v},
{{< /m >}}

where $d_u$ is the node degree of node $u$ and $\mathcal N(u)$ is the neighbor nodes of $u$.
