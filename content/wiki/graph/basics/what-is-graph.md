---
title: "What is Graph"
date: "2021-09-25"
categories:
  - "Graph"
tags:
  - "Graph"
  - "Basics"
references:
  - name: "Hamilton WL. Graph Representation Learning. Morgan & Claypool Publishers; 2020. pp. 1–159. doi:10.2200/S01045ED1V01Y202009AIM046"
    link: "https://www.morganclaypool.com/doi/10.2200/S01045ED1V01Y202009AIM046"
    key: "Hamilton2020"
  - name: "Sanchez-Lengeling B, Reif E, Pearce A, Wiltschko AB. A Gentle Introduction to Graph Neural Networks. Distill. 2021;6. doi:10.23915/distill.00033"
    link: "https://distill.pub/2021/gnn-intro/"
    key: "Sanchez-Lengeling2021"
weight: 1
links:
  - "cards/graph/graph-laplacians.md"
---


## Graph

A graph $\mathcal G$ has nodes $\mathcal V$ and edges $\mathcal E$,

{{< m >}}
\mathcal G = ( \mathcal V, \mathcal E).
{{< /m >}}

{{< message title="Edges" >}}

Edges are relations between nodes. For $u\in \mathcal V$ and $v\in \mathcal V$, if there is an edge between them, then $(u, v)\in \mathcal E$.

{{< /message >}}

{{< figure src="../assets/what-is-graph/graph-definition.jpg" >}}

## Representations of Graph

There are different representations of a graph.

### Adjacency Matrix

A adjacency matrix of a graph represents the nodes using row and column indices and edges using elements of the matrix.

For simple graph, the adjacency matrix is rank two and dimension $\lvert \mathcal V \rvert \times \lvert \mathcal V \rvert$. For edge $(u, v)\in \mathcal E$, it is represented by the matrix element $\mathbf A[u,v]=1$.


> See [Sanchez-Lengeling, 2021](https://distill.pub/2021/gnn-intro/) for an interactive example[^Sanchez-Lengeling2021].

{{< e "cards/graph/graph-adjacency-matrix.md" >}}


### Laplacians

Laplacians are transformations of the adjacency matrix but provides a lot more convenience for analysis.

{{< e "cards/graph/graph-laplacians.md" >}}


## Multi-Relational Graph

A graph may have different types of edges, $\tau\in \mathcal R$, where $R$ is a set of types of relations. A multi-relational graph is then

{{< m >}}
\begin{align}
u &\in \mathcal V \\
v &\in \mathcal V \\
\tau &\in \mathcal R \\
(u, \tau, v) &\in \mathcal E.
\end{align}
{{< /m >}}

{{< message class="info" title="Adjacency Matrix for Multi-relation Graph">}}

For multi-relational graph, it can have more ranks and the dimension can be $\lvert \mathcal V \rvert \times \lvert \mathcal V \rvert \times \lvert \mathcal R\rvert$, where $\mathcal R$ represents the types of relations.


|  type | adjacency matrix  |
|---|---|
| $\tau=\tau_1$  |  $A_{\tau=\tau_1}$ |
| $\tau=\tau_2$  |  $A_{\tau=\tau_2}$ |
| $\cdots$ | $\cdots$ |


{{< /message >}}



Two popular examples:

- heterogeneous
  - multipartite
- multiplex

### Heterogeneous

Nodes are subsets without intersections, $\mathcal V = \mathcal V_1\cup \mathcal V_2 \cdots \mathcal V_k$ and $\mathcal V_i \cap \mathcal V_j =  \emptyset$ for $\forall i\neq j$.

{{< figure src="../assets/what-is-graph/heterogeneous-graph-example-hamilton.jpg" caption="Heterogeneous graph example. A visualization of the example in Hamilton2020." >}}

The famous multi-partite graph is an example of heterogeneous graph.

{{< message title="Movie and User Bi-partite Graph" >}}

For a website that hosts a movie database and a user database, the relation about which user watched which movie is a bi-partite graph.

{{< /message >}}


### Mutiplex

The edges represent different

{{< figure src="../assets/what-is-graph/multiplex-example.jpg" caption="Multiplex graph example." >}}



[^Hamilton2020]: {{< cite key="Hamilton2020" >}}

[^Sanchez-Lengeling2021]: {{< cite key="Sanchez-Lengeling2021" >}}