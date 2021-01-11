---
title: "Bernoulli Distribution"
excerpt: ""
date: 2020-03-14
category:
- 'Statistics'
tags:
- 'Statistics'
- 'Distributions'
references:
- name: Bernoulli Distribution @ Wikipedia
  link: https://en.wikipedia.org/wiki/Bernoulli_distribution
---

Two categories with probability $p$ and $1-p$ respectively.

For each experiment, the sample space is $\\{A, B\\}$. The probability for state $A$ is given by $p$ and the probability for state $B$ is given by $1-p$. The Bernoulli distribution describes the probability of $K$ results with state $s$ being $s=A$ and $N-K$ results with state $s$ being $B$ after $N$ experiments,

{{< m >}}
P\left(\sum_i^N s_i = K \right) = C _ N^K p^K (1 - p)^{N-K}.
{{< /m >}}