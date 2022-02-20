---
title: "Graphs Spectral Methods"
date: "2021-09-25"
categories:
  - "Graph"
tags:
  - "Graph"
  - "Basics"
  - "Statistics"
references:
  - name: "Hamilton WL. Graph Representation Learning. Morgan & Claypool Publishers; 2020. pp. 1–159. doi:10.2200/S01045ED1V01Y202009AIM046"
    link: "https://www.morganclaypool.com/doi/10.2200/S01045ED1V01Y202009AIM046"
    key: "Hamilton2020"
weight: 3
links:
  - "cards/graph/graph-laplacians.md"
  - "cards/graph/graph-cuts.md"
---

The {{< c "cards/graph/graph-cuts.md" "Ratio Cut" >}} is closely related to the {{< c "cards/graph/graph-laplacians.md" >}}.

## Two Clusters

Given a vector $\mathbf a$,

{{< m >}}
\mathbf a[u] = \begin{cases}
\sqrt{ \frac{ \lvert \bar{\mathcal A} \rvert }{ \lvert \mathcal A \rvert } }, & u\in \mathcal A \\
-\sqrt{ \frac{ \lvert \mathcal A \rvert } { \lvert \bar{\mathcal A} \rvert }}, & u\in \bar{\mathcal A}
\end{cases}.
{{< /m >}}


{{< message >}}

We have

- $\sum_{u\in\mathcal V} \mathbf a[u] = 0$, and
- $\lVert{\mathbf a}\rVert = \lvert \mathcal V \rvert$.

{{< /message >}}

Using $\mathbf a$, we have[^Hamilton2020]

{{< m >}}
\mathbf a^T \mathbf L \mathbf a = \lvert \mathcal V \rvert \operatorname{RatioCut}(\mathcal A, \bar{\mathcal A}).
{{< /m >}}


This result is useful as the Rayleigh-Ritz theorem tells us that $\mathbf a$ is the second smallest eigenvector of $\mathbf L$.

We can assign nodes to different groups based on $\mathbf a$.

- If $\mathbf a[u] \geq 0$, we know $u\in\mathcal A$;
- If $\mathbf a[u] \lt 0$, we know $u\in\bar{\mathcal A}$.


## Multiple Clusters

Refer to chapter 2 of Hamilton2020[^Hamilton2020].




[^Hamilton2020]: {{< cite key="Hamilton2020" >}}

