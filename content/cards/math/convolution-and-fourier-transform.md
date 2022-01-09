---
title: "Convolutions Using Fourier Transform"
description: "Convolution and Fourier transform"
date: "2021-12-04"
categories:
  - "Math"
tags:
  - "Fourier Transform"
  - "Convolution"
references:
  - name: "Hamilton WL. Graph Representation Learning. Morgan & Claypool Publishers; 2020. pp. 1–159. doi:10.2200/S01045ED1V01Y202009AIM046"
    link: "https://www.morganclaypool.com/doi/10.2200/S01045ED1V01Y202009AIM046"
---


Convolution

{{< m >}}
(f*h)(x) = \int \mathrm d f(y) h(x-y),
{{< /m >}}

is equivalent to

{{< m >}}
\mathcal F^{-1}\left[ \mathcal F[ f(x) ] \circ \mathcal F[h(x)] \right],
{{< /m >}}

with $\mathcal F$ being the Fourier transform, i.e.,

{{< m >}}
\mathcal F[f(x)] = \int \mathrm d x f(x) e^{-2\pi i x s}.
{{< /m >}}


{{< message title="Proof" >}}

One could prove it using the Fourier integral theorem,

$$
f(x) = \iint dy d\xi f(y)e^{2\pi i (x-y)\xi}.
$$

{{< /message >}}


## Derivation

Given

{{< m >}}
\begin{align}
\mathcal F_s \left(f(y)\right) &= \int dy f(y) e^{-2\pi i y s}, \\
\mathcal F_s \left(h(y)\right) &= \int dz h(z) e^{-2\pi i z s},
\end{align}
{{< /m >}}


we have

{{< m >}}
\mathcal F_s(f(y)) \mathcal F_s(h(z)) = \int dz dy f(y)h(z) e^{-2\pi i (y+z) s}.
{{< /m >}}

Inverse transform of the above shows

{{< m >}}
\mathcal F_x^{-1}\left( \mathcal F_s(f(y)) \mathcal F_s(h(z)) \right) = \int ds \int dz dy f(y)h(z) e^{-2\pi i (y+z) s + 2\pi i x s}.
{{< /m >}}

Using Fourier integral theorem, we can simplify the formula by defining a new variable ${\color{red}\bar x} = {\color{red}y + z}$

{{< m >}}
\begin{align}
\mathcal F_x^{-1}\left( \mathcal F_s(f(y)) \mathcal F_s(h(z)) \right) &= \int dy \int dz ds f(y) h(z) e^{2\pi i ( x - ({\color{red}y+z}) ) s} \\
&= \int dy \int d \bar x ds f(y) h(\bar x - y) e^{2\pi i ( x - {\color{red}\bar x} ) s} \\
&= \int dy f(y) h(\bar x - y) \\
&= (f * h) (\bar x)
\end{align}
{{< /m >}}




