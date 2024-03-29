---
title: "Graph Convolution Operator"
date: "2021-11-25"
categories:
  - 'Graph'
tags:
  - "Graph"
  - "Convolution"
links:
  - "wiki/graph/basics/what-is-graph.md"
  - "cards/graph/graph-adjacency-matrix.md"
  - "cards/math/convolution-and-fourier-transform.md"
  - "cards/graph/graph-laplacians.md"
---

For a given graph $\mathcal G$, we have an attribute on each node, denoted as $f_v$. All the node attributes put together can be written as a list $\mathbf f\to (f_{v_1}, f_{v_2}, \cdots, f_{v_N})$.

Convolution on graph is combining attributes on nodes with their neighbors'. The {{< c "cards/graph/graph-adjacency-matrix.md" "adjacency matrix" >}} $\mathbf A$ applied on all node attributes $\mathbf f$ is such an operation, i.e,

{{< m >}}
\mathbf A \mathbf f,
{{< /m >}}

as it combines all the neighbors of each node. To include the node attribute itself, we can perform

{{< m >}}
(\mathbf I + \mathbf A) \mathbf f.
{{< /m >}}

{{< e "cards/graph/graph-adjacency-matrix.md" >}}

We could include higher orders too. In general, a graph convolution $\mathbf Q$ can be a polynomial of $\mathbf A$, i.e.,

{{< m >}}
\mathbf Q = \sum_{i=0}^{N} \alpha_i \mathbf A^i.
{{< /m >}}

{{< message title="Commutation Relations" >}}

The above definition of convolution commutes with the adjacency matrix,

$$
\left[ \mathbf Q, \mathbf A \right] = 0.
$$

However, the commutation relation with the Laplacian $\mathbf L$ is not 0 in general, i.e.,

$$
\left[ \mathbf Q, \mathbf L \right] \neq 0.
$$

However, we can make both commutation relations 0 using symmetric normalized adjacency matrix $\mathbf A_{s} = \mathbf D^{-1/2}\mathbf A \mathbf D^{-1/2}$ and symmetric normalized Laplacian $\mathbf L_{s}=\mathbf D^{-1/2}\mathbf L \mathbf D^{-1/2}=\mathbf I - \mathbf A_{s}$.

{{< /message >}}

## Laplacian, Fourier Transform, and Graph Convolution

Using [the relation between convolution and Fourier transform](/cards/math/convolution-and-fourier-transform), as well as [the relation between graph Laplacian and Fourier transform](/cards/graph/graph-laplacians), we can establish the following relation.

{{< m >}}
\mathbf f * \mathbf h = \mathbf U ( \mathbf U^{\mathrm T} \mathbf f \circ \mathbf U^{\mathrm T} \mathbf h ),
{{< /m >}}

where $\mathbf U$ are the eigenvectors,

{{< m >}}
\mathbf L = \mathbf U \mathbf \lambda \mathbf U^{\mathrm T}.
{{< /m >}}

{{< message title="Graph Fourier Transform" >}}

$\mathbf U^{\mathrm T} \mathbf f$ is the graph Fourier transform.

{{< /message >}}
