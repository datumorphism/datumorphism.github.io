---
title: "Conformal Prediction"
description: "Conformal prediction is a method to sequentially predict consistent confidence intervals using nonconformity measures."
date: 2022-04-01
categories:
  - "Statistical Estimation"
tags:
  - "Statistics"
  - "Basics"
  - "Confidence Interval"
  - "Conformal Prediction"
references:
  - name: "Shafer G, Vovk V. A tutorial on conformal prediction. arXiv [cs.LG]. 2007. Available: http://arxiv.org/abs/0706.3188"
    link: "http://arxiv.org/abs/0706.3188"
    key: "Shafer2007"
weight: 3
---

Conformal prediction is a method to predict a consistent confidence interval in an on-line setting.

{{< message title="on-line" >}}

An on-line setting is to predict continuously for sequentially incoming data points. For example, we predict $x_n$ for given data points $\\{\\!\\{x_1, \\cdots, x_{n-1}\\}\\!\\}$. Then we predict $x_{n+1}$ using $\\{\\!\\{x_1, \\cdots, x_{n}\\}\\!\\}$.

{{< /message >}}


## Nonconformity Measure

For a new incoming data point $x$, and an existing {{< c "cards/math/multiset-mset-bag.md" "multiset" >}} of data points

{{< m >}}
B_n = \{\!\{x_1, \cdots, x_{n}\}\!\},
{{< /m >}}

a nonconformity measure, $A(B_n, x)$, measures how different $x_n$ is from the existing multiset[^Shafer2007].

A naive choice would be to reuse our model $x = f(B_n)$. Define a nonconformity measure

{{< m >}}
A(B_n, x) = d(f(B_n), x),
{{< /m >}}

where $d$ is some kind of {{< c "/tags/distance/" >}}.

{{< message title="Choice of Nonconformity Measure" >}}

In principle, there are a lot of freedom in choosing the nonconformity measure. For example, as long as two nonconformity measures are monotonically related, the predicted regions are the same.

{{< /message >}}





[^Shafer2007]: {{< cite key="Shafer2007" >}}