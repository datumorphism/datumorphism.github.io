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
