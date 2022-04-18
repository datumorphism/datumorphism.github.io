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
  - name: "Zeni G, Fontana M, Vantini S. Conformal Prediction: a Unified Review of Theory and New Challenges. arXiv [cs.LG]. 2020. Available: http://arxiv.org/abs/2005.07972"
    link: "http://arxiv.org/abs/2005.07972"
    key: "Zeni2020"
links:
  - "wiki/statistical-hypothesis-testing/neyman-pearson-theory.md"
garden:
  - "growing"
weight: 3
---

Conformal prediction is a method to predict a consistent confidence interval in an on-line setting. The algorithms is following the {{< c "wiki/statistical-hypothesis-testing/neyman-pearson-theory.md" "Neyman-Pearson hypothesis testing" >}} framework, thus providing solid theoretical support for the predicted region.

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

In principle, there are a lot of freedom in choosing the nonconformity measure. For example, as long as two nonconformity measures are monotonically related, the predicted regions are the same[^Shafer2007]. One could understand this using the following example.

{{< /message >}}



## A Conformal Algorithm Example


{{< figure src="../assets/conformal-prediction/three-data-points-conformal-algorithm-old-examples-setup.jpg" caption="We have two existing datapoints and try to decide whether the third data point $x_3$ should be included in the predicted region with $\alpha=0.05$ significance level." >}}

Given two existing data points

{{< m >}}
B_3 = \{\{ x_1=1, x_2=4 \}\},
{{< /m >}}

we will decide if $x_3=2$ should be included in our predicted region of significance level $\alpha=0.05$.

To be able to test if $x_3=2$ falls inside the predicted region, we simply take the average of data points for the point prediction, and we use L1 norm as the nonconformity measure, i.e.,

{{< m >}}
\begin{align}
f(B_n) &= \frac{1}{n}\sum_i x_i \\
A(f(B_n), x) &= \lvert x - f(B_n) \rvert.
\end{align}
{{< /m >}}

With the model and nonconformity measure set, we can deicide whether the new data poin $x_3 = 2$ should be included in the predicted region of significance level $\alpha=0.05$.

For $i=1,2,3$,

1. calculate

   {{< m >}}
   f_i = f(B_3\{\{x_i\}\})
   {{< /m >}}

2. calculate the nonconformity measure

   {{< m >}}
   \alpha_i = A(f_i, x_i)
   {{< /m >}}

With all $\alpha_i$, count all the data points that leads to $\alpha_i\geq \alpha_3$, denoted as $N_{\alpha_i\geq\alpha_3}$, calculate the probability

{{< m >}}
p_x = \frac{N_{\alpha_i\geq\alpha_3}}{n}.
{{< /m >}}

{{< figure src="../assets/conformal-prediction/three-data-points-conformal-algorithm-old-examples.jpg" caption="Steps to decide whether to include $x_3=2$ in the predicted region." >}}


{{< message title="Intuition using Extreme Cases" >}}

To get some intuition, let's go to the extreme cases. If the new data point $x_3$ was not $2$ but $1e10$, we can easily see that $\alpha_1\sim\alpha_2\sim 1e10/2$ and $\alpha_3\sim 1e10$. That being said, $\alpha_3$ is always the largest and $p_x$ is minimized. If we have a lot of data points like $x_1$ and $x_2$, and suddenly there is a data point $x_n=1e10$, we have $p_x\to0$. This is an expected result as $1e10$ is so different.

{{< /message >}}

This algorithm is basically a hypothesis test procedure using the {{< c "wiki/statistical-hypothesis-testing/neyman-pearson-theory.md" "Neyman-Pearson theory" >}}[^Shafer2007].

## Requires Exchangeability

The algorithm assumes the data points are exchangeabile as we assume no statistical difference between

{{< m >}}
x_1, x_2, x_3, ..., x_n,
{{< /m >}}

and

{{< m >}}
x_2, x_3, ..., x_n, x_1
{{< /m >}}

and

{{< m >}}
x_1, x_3, ..., x_n, x_2
{{< /m >}}

and all the possible permutations of this pattern. Obviously, i.i.d. data satisfies this condition. Note that i.i.d. is a more stringent condition[^Shafer2007].


## Bonferroni Correction

For predictions involves multiple variable, we should consider the {{< c "cards/statistics/bonferroni-correction.md" >}}.




[^Shafer2007]: {{< cite key="Shafer2007" >}}