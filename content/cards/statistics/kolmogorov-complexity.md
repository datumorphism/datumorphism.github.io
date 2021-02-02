---
title: Kolmogorov Complexity
date: 2020-11-08
tags:
  - Model Selection
references:
  - link: https://people.cs.uchicago.edu/~fortnow/papers/kaikoura.pdf
    name: Fortnow, L. (2000). Kolmogorov complexity. (January), 1–14.
---

Description:

$\Sigma=\\{0,1\\}$, a map $f:\Sigma^* \to\Sigma^*$. To describe a string of 0 and 1 $\sigma$, the description is a map so that $f(\tau)=\sigma$.

Kolmogorov complexity $C_f$

{{< m >}}
C_f(x) = \begin{cases} min\{ \vert p \vert : f(p) = x & \text{if x} \\
\infty & \text{otherwise} \} \end{cases}
{{< /m >}}

$f$ can be a universal turing machine.