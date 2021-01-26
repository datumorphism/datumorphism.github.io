---
title: "Wavelet Transform"
description: "Transforms that captures the local patterns"
date: 2020-12-07
authors:
  - "LM"
categories:
  - "Math"
tags:
  - Transform
  - Data
  - "Data Science"
  - "Time Series"
references:
  - name: "The Wavelet Transform for Beginners"
    link: "https://www.youtube.com/watch?v=kuuUaqAjeoA"
  - name: "Parameters of Morlet wavelet (time-frequency trade-off)"
    link: "https://www.youtube.com/watch?v=LMqTM7EYlqY"
  - name: "Wavelet Transform from Gwyddion Documentation"
    link: "http://gwyddion.net/documentation/user-guide-en/wavelet-transform.html"
weight: 4
links:
  - "/wiki/time-series/short-time-fourier-transform.md"
---

In general, given a complete set of function $\psi(x; \tilde x)$, we can decompose a function $F(\tilde x)$

$$
F(\tilde x) = \int f(x) \psi(x;\tilde x) dx.
$$

The choice of $\psi(x;\tilde x)$ gives us different properties.

## Fourier Transform

Fourier transform is good for stationary analysis since time is not involved in $F(\omega)$.

$$
F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i \omega t} dt
$$

## Short-time Fourier Transform

STFT is a Fourier transform with a moving time window $\tau$,

$$
F(\tau,\omega) = \int_{-\infty}^{\infty} f(t) w(t - \tau) e^{-i\omega t} dt.
$$

Moving $\tau$ gives us the ability to investigate Fourier components at different time segments (assuming the window function $w(t-\tau)$ is a step function). It is obvious that the STFT can resolve different things with a different window.


## Wavelets

There are many different choices of wavelets.

One of the most used one is the Morlet wavelets or Gabor wavelets,

$$
\psi(t;\omega) = e^{i 2\pi ft - \frac{1}{2}(t/\sigma)^2 },
$$

where
$$
\sigma = \frac{n}{2\pi f}.
$$