---
title: "Graph Cuts"
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

## Cut

For a subset of nodes $\mathcal A\subset \mathcal V$, the rest of nodes can be denoted as $\bar {\mathcal A} = \mathcal V \setminus \mathcal A$. In other words, $\mathcal A \cup \bar {\mathcal A} = \mathcal V$ and $\mathcal A \cap \bar {\mathcal A} = \emptyset$. That being said, the nodes can be partitioned into two subsets, $\mathcal A$ and $\bar {\mathcal A}$. The cut of this partition is defined as the total number of edges between them,

{{< m >}}
\operatorname{Cut} \left( \mathcal A, \bar{\mathcal A} \right) = \frac{1}{2} \left( \lvert (u, v)\in \mathcal E: u\in \mathcal A, v\in \bar{\mathcal A} \rvert + \lvert (u, v)\in \mathcal E: u\in \bar{\mathcal A}, v\in {\mathcal A} \rvert \right).
{{< /m >}}

To generalize this notion, suppose we partition the nodes into $k$ subsets of nodes, $\mathcal A_1, \cdots, \mathcal A_k$, the **cut** is the total number of edges between $\mathcal A_k$ and $\bar{\mathcal A_k}$ [^Hamilton2020],

{{< m >}}
\operatorname{Cut} \left( \mathcal A_1, \cdots, \mathcal A_k \right) = \frac{1}{2} \sum_{k=1}^K \lvert (u, v)\in \mathcal E: u\in \mathcal A_k, v\in \bar{\mathcal A_k}  \rvert.
{{< /m >}}

For smaller cut value, the proposed patches $\mathcal A_1, \cdots, \mathcal A_k$ are more disconnected from the overall graph.

This definition is biased towards smaller graphlets, i.e., smaller subset of nodes will get smaller cut values.



## Ratio Cut

Ratio Cut normalizes the cut values by the size of the patches,


{{< m >}}
\operatorname{Cut} \left( \mathcal A_1, \cdots, \mathcal A_k \right) = \frac{1}{2} \sum_{k=1}^K \frac{\lvert (u, v)\in \mathcal E: u\in \mathcal A_k, v\in \bar{\mathcal A_k}  \rvert}{ \lvert \mathcal A_k \rvert}.
{{< /m >}}

{{< figure src="../assets/graph-cuts/graph-cuts.jpg" caption="Graph cuts" >}}


This definition punishes smaller patches using $\frac{1}{ \lvert \mathcal A_k \rvert}$.

## Normalized Cut

The normalized cut uses the node degrees as punishment, $\operatorname{vol}(\mathcal A_k) = \sum_{u\in\mathcal A_k} d_u$,


{{< m >}}
\operatorname{Cut} \left( \mathcal A_1, \cdots, $\mathcal A_k \right) = \frac{1}{2} \sum_{k=1}^K \frac{\lvert (u, v)\in \mathcal E: u\in \mathcal A_k, v\in \bar{\mathcal A_k}  \rvert}{ \lvert\operatorname{vol}(A_k) \rvert}.
{{< /m >}}




[^Hamilton2020]: {{< cite key="Hamilton2020" >}}