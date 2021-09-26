---
title: "Betweenness Centrality of a Graph"
date: "2021-09-25"
categories:
  - 'Graph'
tags:
  - "Graph"
  - "Statistics"
references:
  - name: "Contributors to Wikimedia projects. Betweenness centrality. In: Wikipedia [Internet]. 21 Aug 2021 [cited 26 Sep 2021]. Available: https://en.wikipedia.org/wiki/Betweenness_centrality"
    link: "https://en.wikipedia.org/wiki/Betweenness_centrality"
    key: "BetweennessCentrality"
links:
  - "wiki/graph/basics/what-is-graph.md"
---

Betweenness centrality of a node $v$ is measurement of how likely the shortest path between two nodes $u_s$ and $u_t$ is gonna pass through node $v$,

{{< m >}}
c(v) = \sum_{v\neq u_s\neq u_t} \frac{\sigma_{u_su_t}(v) }{\sigma_{u_su_t}},
{{< /m >}}

where $\sigma_{u_su_t}(v)$ is the number of shortest path between $u_s$ and $u_t$, and passing through $u$, while $\sigma_{u_su_t}$ is the number of shortest path between $u_s$ and $u_t$.

A figure from wikipedia demonstrates this idea well. The nodes on the outreach have smaller betweenness centrality, while the nodes in the core have higher betweenness centrality.

{{< figure src="../assets/graph-betweenness-centrality/1920px-Graph_betweenness.svg.png" caption="Source: [Wikipedia](https://en.wikipedia.org/wiki/Betweenness_centrality#/media/File:Graph_betweenness.svg)" >}}


{{< message title="Outreach and Core" class="warning" >}}

It is almost like cheating using the work "outreach" and "core" here. They are somewhat defined by betweenness centrality.

{{< /message >}}
