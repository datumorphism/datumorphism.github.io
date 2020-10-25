---
title: "Signal Processing: Audio Basics"
description: "basics about audio"
date: 2018-03-29
category:
- 'Algorithms'
tags:
- 'Audio'
- 'Signal Processing'
- 'Basics'
links:
  - wiki/algorithms/singal-processing.md
references:
- name: "Basic Sound Processing in Python | SciPy 2015 | Allen Downey"
  link: "https://www.youtube.com/watch?v=0ALKGR0I5MA"
- name: "AllenDowney/ThinkDSP"
  link: "https://github.com/AllenDowney/ThinkDSP"
- name: "Think DSP"
  link: "http://greenteapress.com/wp/think-dsp/"
- name: "freesound.org"
  link: "https://freesound.org"
- name: "LTI Systems"
  link: "https://brilliant.org/wiki/linear-time-invariant-systems/"
weight: 21
---

## Keywords

1. Harmonic structure of sound
2. Parson code of music
3. Linear time-invariant theory
4. Autocorrelation
5. Noise
6. Chirps
7. DCT compression
8. Discrete Fourier transform
9. filtering
10. convolution

## Linear Time-Invariant System

We describe the system with $Y(t) = f(X(t))$, where $X(t)$ is the input, and $Y(t)$ is the output.

1. Linear: $f(a X_1(t) + b X_2(t)) = a f(X_1(t)) + b f(X_2(t))$
2. Time-invariant: input $X(t+\Delta t)$ will produce the shifted signal $Y(t+\Delta t)$.


LTI systems are memory systems, casual, real, and stable. Stable means the output won't reach infinite if the input is finite. It's bounded.

## Impulse Response

Suppose we have a impulse $X(t) = I(t)$, and output $h(t)$.

Now we have another input $X(t)$, we can ask that what would the output be if we put the input in the same environment as the previous impulse.

$$
\begin{equation}
Y(t) = \int d\tau h(\tau) X(t-\tau).
\end{equation}
$$


## Transfer Function

For the impulse response, the transfer function is obtained through the Laplace transform of the response,

$$
\begin{equation}
\tilde h(s) = \mathscr L_s [ h(t) ].
\end{equation}
$$

With the response function, we know that the response with some other input that is set in the same environment is

$$
\begin{equation}
   \tilde Y(s) = \tilde h(s) \tilde X(s).
\end{equation}
$$

