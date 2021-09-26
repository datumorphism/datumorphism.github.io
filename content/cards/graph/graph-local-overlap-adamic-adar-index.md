---
title: "Graph Local Overlap Measure: Adamic Adar Index"
date: "2021-09-26"
categories:
  - 'Graph'
tags:
  - "Graph"
  - "Basics"
  - "Clustering"
references:
  - name: "Adamic LA, Adar E. Friends and neighbors on the Web. Soc Networks. 2003;25: 211–230. doi:10.1016/S0378-8733(03)00009-1"
    link: "https://www.sciencedirect.com/science/article/abs/pii/S0378873303000091"
    key: "Adamic2003"
  - name: "Hamilton WL. Graph Representation Learning. Morgan & Claypool Publishers; 2020. pp. 1–159. doi:10.2200/S01045ED1V01Y202009AIM046"
    link: "https://www.morganclaypool.com/doi/10.2200/S01045ED1V01Y202009AIM046"
    key: "Hamilton2020"
---

The Adamic Adar (AA) index is[^Adamic2003]

{{< m >}}
\mathbf S_{\text{AA}}[v_1,v_2] = \sum_{u\in\mathcal N(u) \cap \mathcal N(v)} \frac{1}{\log d_u},
{{< /m >}}

where $d_u$ is the node degree of node $u$ and $\mathcal N(u)$ is the neighbor nodes of $u$.

If two nodes have shared neighbor, the degree of the neighbors will be at least 2. So it is safe to use $1/\log d_u$.


[^Adamic2003]: {{< cite key="Adamic2003" >}}