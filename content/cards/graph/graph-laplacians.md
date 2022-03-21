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
  - name: "Li J, Guo J-M, Shiu WC. Bounds on normalized Laplacian eigenvalues of graphs. J Inequal Appl. 2014;2014: 1–8. doi:10.1186/1029-242X-2014-316"
    link: "http://dx.doi.org/10.1186/1029-242X-2014-316"
    key: "Li2014"
links:
  - "cards/graph/graph-adjacency-matrix.md"
  - "cards/graph/graph-cuts.md"
  - "cards/math/convolution-and-fourier-transform.md"
  - "cards/graph/graph-convolution-operator.md"
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

The eigenvalues of normalized Laplacian is bounded ($[0,2]$)[^Li2014].

The random walk Laplacian is

{{< m >}}
\mathbf L_{\text{RW}} = \mathbf D^{-1} \mathbf A.
{{< /m >}}



## Diagonalizing Graph Laplacian

The eigenvectors of Graph Laplacian can be used to diagonalize the graph Laplacian $\mathbf L$,

{{< m >}}
\begin{equation}
\mathbf U \mathbf L_D \mathbf U^{\mathrm T} = \mathbf L.\label{eq-laplacian-diag}
\end{equation}
{{< /m >}}


## Laplacians and Fourier Transform

{{< message title="Laplacian and Fourier Transform" >}}

The eigen-equation of Laplacian $\nabla^2$ shows that the eigenvectors of the Laplacian (in Hilbert space) have the form $e^{2\pi i \xi x}$. On the other hand, $e^{2\pi i \xi x}$ is also the Fourier basis.

{{< /message >}}

The eigenvectors of the graph Laplacian (Eq. $\eqref{eq-laplacian-diag}$) can be used to perform Fourier transforms on graph[^Hamilton2020]. We apply the matrix $\mathbf U^{\mathrm T}$ in $\eqref{eq-laplacian-diag}$ onto a vector of node attributes,

{{< m >}}
\mathbf U^{\mathrm T} \mathbf f.
{{< /m >}}

The above is the Fourier transform of the node attributes on the graph.

{{< e "cards/graph/graph-convolution-operator.md" >}}

{{< e "cards/math/convolution-and-fourier-transform.md" >}}


[^Hamilton2020]: {{< cite key="Hamilton2020" >}}

[^Li2014]: {{< cite key="Li2014" >}}