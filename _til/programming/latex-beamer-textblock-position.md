---
layout: til
title: "Positioning textblock in LaTeX Beamer"
date: 2017-01-17
author: OctoMiao
comments: true
category:
- programming
tag:
- LaTeX
excerpt: Positioning textblock in LaTeX Beamer using textpos package and eso pic package
---

There are times that we wanted to position an equation on the top right of the slide in beamer. The easiest way to do it is to use two packages: `textpos` and `eso-pic`. `textpos` package positions the textblock, while `eso-pic` sets up a grid system on the slides.

We include the two packages with options.

```
\usepackage[absolute,overlay]{textpos}
\usepackage[texcoord,
grid,gridcolor=red!10,subgridcolor=green!10,gridunit=pt]
{eso-pic}
```

To position a textblock, use the options `\begin{textblock}{WIDTH}(XCOORDINATE,YCOORDINATE)`. Here is an example.

```
\begin{textblock*}{10pt}(150pt,1pt)
\small
\begin{equation*}
    \mathbf {H} = \frac{1}{2}\left( - \omega_{\mathrm{m}} + {\color{red}\delta \lambda(x)} \cos 2\theta_{\mathrm{m}} \right) \sigma_3 - \frac{  {\color{red}\delta \lambda(x)}  }{2} \sin \theta_{\mathrm{m}} \sigma_1
\end{equation*}
\end{textblock*}
```
