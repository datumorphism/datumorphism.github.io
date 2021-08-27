---
title: "Gaussian Integrals"
description: "Gaussian integral is one of the most useful things if one could write it down."
date: 2021-05-11
categories:
  - 'Math'
tags:
  - 'Integral'
references:
  - name: "reference for multidimensional gaussian integral"
    link: "https://math.stackexchange.com/questions/126227/reference-for-multidimensional-gaussian-integral"
---


The diagonalized case

{{<m>}}
\begin{eqnarray}
Z_0 &=& \int d^n z \exp\left(-\frac{1}{2} z^\mathrm{T} D z\right) \\
&=& \prod_i \int d z_i \exp\left(-\frac{1}{2} \lambda_i z_i^2\right) \\
&=& \prod_i \sqrt{\frac{2\pi}{\lambda_i}} \\
&=& \sqrt{\frac{(2\pi)^n}{\det A}}.
\end{eqnarray}
{{</m>}}


For an arbitrary matrix $A$,

{{<m>}}
Z_J = \int d^n x \exp\left(-\frac{1}{2} x^\mathrm{T} A x + J^\mathrm{T} x\right).
{{</m>}}

{{<m>}}
\begin{eqnarray}
Z_J &=& \int d^n y \exp\left(-\frac{1}{2} {y}^\mathrm{T} A y
+ \frac{1}{2} J^\mathrm{T}A^{-1}J\right) \\
&=& \sqrt{\frac{(2\pi)^n}{\det A}}
\exp\left(\frac{1}{2} J^\mathrm{T}A^{-1}J\right).
\end{eqnarray}
{{</m>}}