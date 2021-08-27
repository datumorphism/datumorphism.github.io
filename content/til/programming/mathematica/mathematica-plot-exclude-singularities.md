---
layout: til
title: "Mathematica Exclude Singularities in Plot"
date: 2017-03-22
author: Lei Ma
categories:
- programming
tags:
- Mathematica
summary: Mathematica Plot might include some non-existant lines sometimes, Exclusions is the potion for it.
---

Mathematica Plot function brings in weird lines sometimes.

Here is an example of it. I plot

$$
f(x) = \frac{1}{1-0.3 x}.
$$


```
Plot[1/(1 - 0.3 x), {x, 2, 5}, Frame -> True,
 FrameLabel -> {"x", "1/(1-0.3 x)"}, ImageSize -> Large,
 PlotLabel -> "Function: 1/(1-0.3 x)"]
```

What we get is a plot

{{< figure src="../assets/mathematica-plot-exclude-singularities/mathematica-plot-with-singularity-point.png" caption="A plot with singularity point. Mathematica Plot brings in an extra line at the singularity." >}}



This vertical line at $x=3$ is not real. To eliminate this line, we can exclude the singularity point when plotting, using `Exclusions`.

```
Plot[1/(x - 3), {x, 2, 4}, Frame -> True,
 FrameLabel -> {"x", "1/(x-3)"}, ImageSize -> Large,
 PlotLabel -> "Function: 1/(x-3)", Exclusions -> {3}]
```

The plot we get now is much better.

{{< figure src="../assets/mathematica-plot-exclude-singularities/mathematica-plot-with-singularity-point-exclusions.png" caption="With Exclusions->{3}" >}}
