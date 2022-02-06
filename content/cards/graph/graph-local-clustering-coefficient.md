---
title: "Graph Clustering Coefficient"
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


## Local Clustering Coefficient

{{< m >}}
c_u = \frac{ \lvert (v_1,v_2)\in \mathcal E: v_1, v_2 \in \mathcal N(u) \rvert}{  \color{red}{d_n \choose 2} },
{{< /m >}}

where $\color{red}{d_n \choose 2}$ means all the possible combinations of neighbor nodes, and $\mathcal N(u)$ is the set of nodes that are neighbor to $u$.


## Closed Triangles

{{< message title="Ego Graph" >}}

![](../assets/graph-local-clustering-coefficient/ego-graph.jpg)

{{< /message >}}

Counting the closed triangles of the ego graph of a node and normalize it by the total possible number of triangles is also a measure of clustering coefficients.


- If the ego graph of $u$ is fully connected, we have $c_u=1$;
- If the ego graph of $u$ is a star, we have $c_u=0$.

This concept can be generalized from triangles to any type of motifs.