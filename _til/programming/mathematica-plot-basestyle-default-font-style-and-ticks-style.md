---
layout: til
title: "Mathematica Plot Default Font Style and Ticks Style: BaseStyle"
date: 2015-12-04
author: OctoMiao
category:
- programming
tag:
- Mathematica
excerpt: Mathematica Plot Default Font Style and Ticks Style BaseStyle
---

Most of time, the plot generated using Mathematica is not a good one for projectors because the font size and ticks size are small. `BaseStyle` is a good solution to this problem. Here is an example from Wolfram Language

```
Plot[Sin[x]^2, {x, 0, 2 Pi}, PlotLabel -> Sin[x]^2, LabelStyle -> Black, FrameTicksStyle -> Larger, BaseStyle -> \
{FontWeight -> "Bold", FontSize -> 18}]
```

As shown in the example, `LabelStyle->Black` and `FrameTicksStyle->Larger` are also very useful when producing slides for projectors.

More on Wolfram Language: [Formats for Text in Graphics](https://reference.wolfram.com/language/tutorial/FormatsForTextInGraphics.html).
