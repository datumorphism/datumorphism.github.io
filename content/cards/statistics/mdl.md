---
title: "Minimum Description Length"
description: "MDL is a measure of how well a model compresses data"
date: 2020-11-08
categories:
  - Statistics
tags:
  - MDL
  - Model Selection
references:
  - link: "https://www.oxfordhandbooks.com/view/10.1093/oxfordhb/9780199957996.001.0001/oxfordhb-9780199957996-e-14"
    name: "Vandekerckhove, J., & Matzke, D. (2015). Model comparison and the principle of parsimony. Oxford Library of Psychology."
  - name: "Grünwald, P. D. (2007). The Minimum Description Length Principle. MIT Press."
    link: "https://ieeexplore.ieee.org/book/6267274"
    key: "Grünwald2007"
links:
  - cards/statistics/kolmogorov-complexity.md
  - cards/statistics/fia.md
  - cards/statistics/nml.md
  - wiki/model-selection/model-selection.md
---

The minimum description length, aka, MDL, is based on the relations between regularity and data compression. (See {{< c "cards/statistics/kolmogorov-complexity.md" "Kolmogorov complexity" >}} for more about data descriptions.).

In statistical inferences, given a dataset $\mathcal D$, the compressions of the data is our model $\mathcal M$, or hypothesis $\mathcal H$ in the language of hypothesis testing.

MDL looks for the model that compresses the data well but with a reasonable cost of complexity. The complexity of the model is described by a length $L(\mathcal M)$, the goodness of the model is $G$. MDL looks into the balance of $L(\mathcal M)$ and $G$. For example, one could calculate the length of the model using the number of parameters $k$ in the model, and the goodness of the model using likelihood $p(\mathcal D \mid \mathcal M)$.


There are many versions of MDL: [^Grünwald2007]
- crude two-part code,
- Fisher information approximation ({{< c "/cards/statistics/fia.md" "FIA" >}}),
- Normalized Maximum likelihood ({{< c "/cards/statistics/nml.md" "NML" >}}).


[^Grünwald2007]: {{< cite key="Grünwald2007" >}}