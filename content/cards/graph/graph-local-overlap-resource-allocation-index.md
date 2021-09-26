---
title: "Graph Local Overlap Measure: Resource Allocation Index"
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

The Resource Allocation (RA) index is

{{< m >}}
\mathbf S_{\text{RA}}[v_1,v_2] = \sum_{u\in\mathcal N(u) \cap \mathcal N(v)} \frac{1}{d_u},
{{< /m >}}

where $d_u$ is the node degree of node $u$ and $\mathcal N(u)$ is the neighbor nodes of $u$.

