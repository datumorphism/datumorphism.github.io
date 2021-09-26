---
title: "Local Variant of Clustering Coefficient"
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

{{< m >}}
c_u = \frac{ \lvert (v_1,v_2)\in \mathcal E: v_1, v_2 \in \mathcal N(u) \rvert}{  \color{red}{d_n \choose 2} },
{{< /m >}}

where $\color{red}{d_n \choose 2}$ means all the possible combinations of neighbor nodes, and $\mathcal N(u)$ is the set of nodes that are neighbor to $u$.

{{< message title="Ego Graph" >}}

![](../assets/graph-local-variant-clustering-coefficient/ego-graph.jpg)

{{< /message >}}

- If $c_u=1$, the ego graph of $u$ is fully connected;
- If $c_u=0$, the ego graph of $u$ is a star.