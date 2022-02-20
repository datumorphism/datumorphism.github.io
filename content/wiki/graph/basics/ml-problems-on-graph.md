---
title: "Solving Problems on Graph"
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
  - name: "McPherson M, Smith-Lovin L, Cook JM. Birds of a Feather: Homophily in Social Networks. Annu Rev Sociol. 2001;27: 415–444. doi:10.1146/annurev.soc.27.1.415"
    link: "https://www.annualreviews.org/doi/10.1146/annurev.soc.27.1.415"
    key: "McPherson2001"
weight: 4
links:
  - "wiki/graph/basics/what-is-graph.md"
  - "reading/popularity-vs-similarity.md"
  - "cards/graph/homophily.md"
  - "cards/graph/heterophily.md"
  - "cards/graph/structural-equivalence.md"
---

Graphs can be used in many problem and there are many possible problems on graphs. We will mention a few popular problems on graphs[^Hamilton2020][^Sanchez-Lengeling2021].

## Node Classification

{{< figure src="../assets/ml-problems-on-graph/ml-on-graph-node-classification.jpg" title="Is the user in black a bot or a normal user?" caption="Created based on the text in Hamilton2020" >}}

Given graph that has incomplete attribute labeling of the nodes, predict the attributes on the nodes.


The following concepts can be used to classify nodes.

- {{< c "cards/graph/homophily.md" "Homophily" >}}[^McPherson2001],
  {{< e "cards/graph/homophily.md" "Homophily" >}}
- {{< c "cards/graph/structural-equivalence.md" "Structural equivalence" >}},
  {{< e "cards/graph/structural-equivalence.md" "Structural equivalence" >}}
- {{< c "cards/graph/heterophily.md" "Heterophily" >}}
  {{< e "cards/graph/heterophily.md" "Heterophily" >}}
  {{< figure src="../assets/ml-problems-on-graph/structural-equivalence.jpg" >}}



{{< message title="Statement of the node classification problem" class="primary" >}}
Given $\mathcal V_{\mathrm{train}}\subset \mathcal V$ on a graph, infer labels $y_u$ of node $u$, with $u\in \mathcal V\setminus \mathcal V_{\mathrm{train}}$.
{{< /message >}}

## Relation Prediction

Also named as link prediction, graph completion.

{{< figure src="../assets/ml-problems-on-graph/netflix-users-and-movies.jpg" title="Users and Movies as a Bipartite Graph" >}}

{{< figure src="../assets/ml-problems-on-graph/connections-on-social-networks.jpg" title="Connections of Users on Social Network" >}}



{{< message title="Statement of the relation prediction problem" class="primary" >}}

Given the nodes $\mathcal V$ on a graph $\mathcal G$, and $\mathcal E_{\text{train}}\subset \mathcal E$, predict other edges $\mathcal E \setminus \mathcal E_{\text{train}}$.


{{< /message >}}




## Clustering and Community Detection

{{< figure src="../assets/ml-problems-on-graph/communities-on-graph.jpg" title="Communities of collaboration network" caption="Each node is an author, the edges indicate collaborations between the authors." >}}

Assign nodes to groups. See {{< c "reading/popularity-vs-similarity.md" >}} for examples.


## Classification, Regression, and Clustering on Graph Level

Given some graphs, perform classification, regression, and clustering on the set of graphs, e.g., predict the toxicity of molecules.



[^Hamilton2020]: {{< cite key="Hamilton2020" >}}

[^Sanchez-Lengeling2021]: {{< cite key="Sanchez-Lengeling2021" >}}

[^McPherson2001]: {{< cite key="McPherson2001" >}}