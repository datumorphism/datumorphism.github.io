---
title:  "Graph Creation"
date: 2020-12-29
speaker: "Lei Ma"
subtitle: "by L. Wilkinson"
speaker: "Lei Ma"
author: LM
types:
  - 'book'
categories:
  - theory
tags:
  - 'data visualization'
summary: ""
status: 10%
references:
  - name: "Wilkinson, L. (2005). The Grammar of Graphics. Springer-Verlag."
    link: https://doi.org/10.1007/0-387-28695-0
---

## Stages


Three stages of making a graph:

1. Specification
2. Assembly
3. Display


### Specification

Statistical graphic specifications are expressed in six statements

- DATA: a set of data operations that create variables from datasets
- TRANS: variable transformations (e.g., rank)
- SCALE: scale transformations (e.g., log)
- COORD: a coordinate system (e.g., polar)
- ELEMENT: graphs (e.g., points) and their aesthetic attributes (e.g., color)
- GUIDE: one or more guides (axes, legends, etc.)


### Assembly

Assembling a scene from a specification requires a variety of structures in order to index and link components with each other. One of the structures we can  use is a network or a tree.

![](../assets/graph-creation-assembly.jpg)

### Display

Rendering the graphics.


## Syntax of the Grammar of Graphics


![](../assets/syntax-of-the-grammar-of-graphics.jpg)

- Create Variables: to extract data into variables
- Apply Algebra: a graphics algebra consisting of three operators — cross, blend and nest —  applied to a set of variables, together with a set of associated rules
- Apply Scales: A categorical scale transformation associates the values of a categorical  variable with the set of integers
- Compute Statistics: do some statistics on the data
- Construct Geometry: the grammar of graphics has a variety of different geometric graphing operations
- Apply Coordinates: to make pie wedges, we apply a polar transformation to the shapes that were  produced from the geometry
- Compute Aesthetics: aesthetic functions translate a graph into a graphic