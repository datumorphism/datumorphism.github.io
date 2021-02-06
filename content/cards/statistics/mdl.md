---
title: "Minimum Description Length"
description: "MDL is a measure of the well a model compresses the data"
date: 2020-11-08
categories:
  - Statistics
tags:
  - MDL
  - Model Selection
references:
  - link: "https://www.oxfordhandbooks.com/view/10.1093/oxfordhb/9780199957996.001.0001/oxfordhb-9780199957996-e-14"
    name: "Vandekerckhove, J., & Matzke, D. (2015). Model comparison and the principle of parsimony. Oxford Library of Psychology."
links:
  - cards/statistics/fia.md
  - cards/statistics/nml.md
---

The minimum description length, aka, MDL, is based on the idea of data compression.

MDL looks for the model that compresses the data well. To compress data, we need to find the regularity in the data.

There are many versions of MDL.
- crude two-part code
- Fisher information approximation ({{< c "/cards/statistics/fia.md" "FIA" >}})
- Normalized Maximum likelihood ({{< c "/cards/statistics/nml.md" "NML" >}})