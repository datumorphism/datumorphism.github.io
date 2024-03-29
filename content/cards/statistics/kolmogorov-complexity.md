---
title: Kolmogorov Complexity
date: 2020-11-08
tags:
  - Model Selection
references:
  - link: https://people.cs.uchicago.edu/~fortnow/papers/kaikoura.pdf
    name: Fortnow, L. (2000). Kolmogorov complexity. (January), 1–14.
    key: Fortnow2000
  - name: "Grünwald, P. D. (2007). The Minimum Description Length Principle. MIT Press."
    link: "https://ieeexplore.ieee.org/book/6267274"
    key: "Grünwald2007"
links:
  - cards/statistics/mdl.md
---

{{< message class="info" title="Description of Data" >}}

The measurement of complexity is based on the observation that the compressibility of data doesn't depend on the "language" used to describe the compression process that much. This makes it possible for us to find a universal language, such as a universal computer language, to quantify the compressibility of the data.

One intuitive idea is to use a programming language to describe the data. If we have a sequence of data,

> 0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,...,9999

It takes a lot of space if we show the complete sequence. However, our math intuition tells us that this is nothing but a list of consecutive numbers from 0 to 9999. Using programming languages, we can express this using `range(9999)` (python) or `[0..9999]` (haskell). (Of course, these programs are not the exact implementations, and it is hard to measure the length using these snippets. We have to look behind the scene. But we get the intuitions that programs can compress data.)

If the sequence is random, an accurate description using programming languages is not exactly easier than writing down the sequence itself.

{{< /message >}}


A naive definition of **description** of a sequence $\mathcal D=\\{x_1, \cdots, x_i, \cdots, x_N\\}$ is a program $p$, which can be mapped to $\mathcal D$ through a map $f$, i.e., $f(p)=\mathcal D$. For example, a universal Turing machine can serve as a map $f$ and is mostly independent of the tasks.

For a given data sequence of length $N$, denoted as $\mathcal D = \\{x_1, \cdots, x_i, \cdots, x_N\\}$, the length of the shortest description of $\mathcal D$ using a specific universal language $l$ is denoted as $L_l(\mathcal D)$ (length of $p$).

The **invariance theorem** indicates that the difference between two shortest descriptions using two different universal languages $l_1$ and $l_2$ is negligible when the length of the sequence $N$ becomes large, [^Grünwald2007]

{{< m >}}
\begin{align}
\lim_{N\to\infty} \frac{L_{l_1}(\mathcal D) - L_{l_2}(\mathcal D) }{N} = 0.
\end{align}
{{< /m >}}



Kolmogorov complexity $C_f$ is [^Fortnow2000]

{{< m >}}
C_f(x) = \begin{cases} \operatorname{min}\{ \vert p \vert : f(p) = x \} & \text{if x is generated by f} \\
\infty & \text{otherwise}
\end{cases}
{{< /m >}}


[^Fortnow2000]: {{< cite key="Fortnow2000" >}}
[^Grünwald2007]: {{< cite key="Grünwald2007" >}}