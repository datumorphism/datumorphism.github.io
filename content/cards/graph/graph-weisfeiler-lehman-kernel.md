---
title: "Weisfeiler-Lehman Kernel"
date: "2021-09-25"
categories:
  - 'Graph'
tags:
  - "Graph"
  - "Statistics"
references:
  - name: "Shervashidze N, Schweitzer P, van Leeuwen EJ, Mehlhorn K, Borgwardt KM. Weisfeiler-Lehman Graph Kernels. J Mach Learn Res. 2011;12: 2539–2561. Available: https://dl.acm.org/doi/10.5555/1953048.2078187"
    link: "https://dl.acm.org/doi/10.5555/1953048.2078187"
    key: "Shervashidze2011"
  - name: "Hamilton WL. Graph Representation Learning. Morgan & Claypool Publishers; 2020. pp. 1–159. doi:10.2200/S01045ED1V01Y202009AIM046"
    link: "https://www.morganclaypool.com/doi/10.2200/S01045ED1V01Y202009AIM046"
    key: "Hamilton2020"
links:
  - "wiki/graph/basics/what-is-graph.md"
---


The Weisfeiler-Lehman kernel is an iterative integration of neighborhood information.

We initialize the labels for each node using its own node degree. At each step, we take the neighboring node degrees to form a multiset. At step $K$, we have the multisets for each node. Those multisets at each node can be processed to form an representation of the graph which is in turn used to calculate statistics of the graph.

{{< figure src="../assets/graph-weisfeiler-lehman-kernel/weisfeiler-lehman-kernel.png" caption="Iterate $k$ steps" >}}

This iteration can be used to test if two graphs are isomorphism[^Shervashidze2011].

[^Shervashidze2011]: {{< cite key="Shervashidze2011" >}}