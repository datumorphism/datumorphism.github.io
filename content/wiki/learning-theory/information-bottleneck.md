---
title: "Information Bottleneck"
date: 2022-04-30
categories:
  - "Learning Theory"
tags:
  - "Learning Theory"
  - "Basics"
  - "Information Bottleneck"
references:
  - name: "Tishby N, Zaslavsky N. Deep Learning and the Information Bottleneck Principle. arXiv [cs.LG]. 2015. Available: http://arxiv.org/abs/1503.02406"
    link: "http://arxiv.org/abs/1503.02406"
    key: "Tishby2015"
weight: 5
---

## Information Bottleneck

In a {{< c "cards/machine-learning/learning-theories/induction-deduction-transduction.md" "induction-deduction framework" >}}, for a given training dataset

{{< m >}}
\{X, Y\},
{{< /m >}}

a prediction Markov chain[^Tishby2015]

{{< m >}}
X \to \hat X \to Y,
{{< /m >}}

where $\hat X$ is supposed to be the minimal sufficient statistics of $X$. $\hat X$ is the minimal data that can still represent the relation between $X$ and $Y$, i.e., $I(X;Y)$, the {{< c "cards/information/mutual-information.md" "mutual information" >}} between $X$ and $Y$. There are competing effects in this framework:

1. On one hand, as an induction process, the less complexity of the representation the better, i.e., smaller $R\equiv I(X;\hat X)$.
2. However, if we are too extreme and come up with a $\hat X$ that is too simple, we reach a very small $R$ but we lose the effectiveness in the deduction process. We can not make good predictions. The deduction process requires the "preserved relevant information", $I_Y\equiv hat X;Y$ to be large.


An optimal representation $\hat X$ should minimize the following Lagrangian[^Tishby2015]

{{< m >}}
\begin{align}
\mathcal L &= R - \beta I_Y \\
&= I(X;\hat X) - \beta I(\hat X;Y),
\end{align}
{{< /m >}}

where $\beta$ is Lagrange multiplier.

To see that this is an Lagrangian, this Lagrangian is equivalent to [^Tishby2015]

{{< m >}}
\tilde{\mathcal L} = I(X;\hat X) + \beta I(X;Y\vert \hat X)
{{< /m >}}

That is we are looking for a $\hat X$ that minimizes the mutual information between $X$ and $\hat X$, $I(X;\hat X)$, but under the constraint $I(X;Y\vert \hat X)=0$, where $I(X;Y\vert\hat X)$ is the mutual information between $X$ and $Y$ but conditioned on $\hat X$. Then $\beta$ is our Lagrange multiplier (see [this chart](https://en.wikipedia.org/wiki/Conditional_mutual_information#/media/File:VennInfo3Var.svg)).




[^Tishby2015]: {{< cite key="Tishby2015" >}}