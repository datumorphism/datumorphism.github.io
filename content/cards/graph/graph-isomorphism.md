---
title: "Graph Isomorphism"
date: "2021-09-26"
categories:
  - 'Graph'
tags:
  - "Graph"
  - "Basics"
references:
  - name: "Hamilton WL. Graph Representation Learning. Morgan & Claypool Publishers; 2020. pp. 1–159. doi:10.2200/S01045ED1V01Y202009AIM046"
    link: "https://www.morganclaypool.com/doi/10.2200/S01045ED1V01Y202009AIM046"
    key: "Hamilton2020"
links:
  - "cards/graph/graph-weisfeiler-lehman-kernel.md"
---


For two graphs, $\mathcal G$ and $\mathcal H$, the two graphs are isomorphism on the following condition

{{< m >}}
u, v \text{ adjacent in } G \iff u, v \text{ adjacent in } H.
{{< /m >}}

An algorithm to find approximate isomorphism is the {{< c "cards/graph/graph-weisfeiler-lehman-kernel.md" "Weisfeiler Lehman Method" >}}.