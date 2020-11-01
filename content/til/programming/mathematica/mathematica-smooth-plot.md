---
layout: til
title: "Mathematica Smooth Plot"
date: 2015-12-04
author: Lei Ma
category:
- programming
tags:
- Mathematica
summary: Mathematica Smooth Plot
---


Mathematica doesn't plot oscillating functions correctly. Weird wiggles and breaks in the plots are so common at least in the new versions of Mathematica. The solution to this problem is, of course, increase the sampling points. One way of doing this is through

```
PlotPoints->....
```

For example, suppose the plot range is from 0 to `endpoint=1000`, I could use

```
PlotPoints->Length@endpoint
```
