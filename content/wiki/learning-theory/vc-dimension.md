---
title: "VC Dimension"
date: 2021-02-21
categories:
  - Learning Theory
tags:
  - Learning Theory
  - Basics
references:
  - link: "https://doi.org/10.1007/978-1-4757-3264-1"
    name: "Vapnik, V. N. (2000). The Nature of Statistical Learning Theory. Springer New York. "
    key: "Vapnik2000"
  - name: "Deckert D-A. Advanced Topics in Machine Learning. In: Advanced Topics in Machine Learning [Internet]. Apr 2017 [cited 17 Oct 2021]. Available: https://www.mathematik.uni-muenchen.de/~deckert/teaching/SS17/ATML/"
    link: "https://www.mathematik.uni-muenchen.de/~deckert/teaching/SS17/ATML/"
    key: "Deckert2017"
weight: 3
links:
  - cards/machine-learning/learning-theories/set-shatter.md
published: true
---

Two of the key elements in a learning problem are:

- a set of hypothesis $\mathcal H$, and
- a set of data samples $\mathcal S$.

{{< message title="$\mathcal H$" class="info" >}}

Inside $\mathcal H$, we have a lot of hypotheses, for example, $\mathcal h$. Given some input, e.g., $x_1$ and $x_2$, we can produce some outputs, e.g., $h(x_1)$ and $h(x_2)$.

{{< /message >}}


{{< message title="$\mathcal S$" class="info" >}}

A sample $\mathcal S$ is a fair sample drawn from all the possible inputs $\mathcal X$, where $\mathcal X$ is called the **input space**.

{{< /message >}}



A dataset $\mathcal S$ can be used as a probe of the hypothesis set $\mathcal H$. $\mathcal S$ can be used to probe the learning capacity of $\mathcal H$.

Following this idea, the VC dimension of $\mathcal H$ is defined as the largest dataset size $\operatorname{max}(\lvert \mathcal S \rvert)$ that $\mathcal H$ can {{< c "cards/machine-learning/learning-theories/set-shatter.md" "shatter" >}}. There are some simple examples on wikipedia: [Vapnik–Chervonenkis dimension#Examples](https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_dimension#Examples).



## Growth Function of $\mathcal H$

Given a input space, there exists good $\mathcal H_G$ and bad $\mathcal H_B$.

- $\mathcal H_G$ is able to distinguish the input using the outputs.
- $\mathcal H_B$ produces extremely similar outputs for inputs and makes it hard to distinguish the inputs using the outputs.


In a **binary classification** problem, it is easier to understand the goodness of $\mathcal H$. The combinations of outputs when feeding data samples to $\mathcal H$ are called dichotomies, as the elements of $\mathcal H$ are being splitted into two parts based on the **binary classes**. It can be denoted as $\mathcal H(x_1, x_2, \cdots, x_m)$.

In such binary classification problems, dichotomies can be used to understand how good is the hypothesis set $\mathcal H$ on an input space $\mathcal X$.

If we see **more dichotomies**, i.e., larger $\lvert\mathcal H(x_1, x_2, \cdots, x_m)\vert$, over the input space $\mathcal X$, we can think of $\mathcal H$ being more powerful over the input space $\mathcal X$.

For example, if we have $2^m$ dichotomies, that means we can use $\mathcal H$ to distinguish all the $m$ data records since the max possible combinations of labels for these $m$ data records is $2^m$.

The growth function is defined as the maximum $\mathcal H(x_1, x_2, \cdots, x_m)$, if we search through all possible $x_1, x_2, \cdots, x_m$ in the input space $\mathcal X$[^Deckert2017],

{{< m >}}
\Pi_{\mathcal H}(m) = \operatorname{max}_{x_1, x_2, \cdots, x_m \in \mathcal X} \lvert \mathcal H(x_1, x_2, \cdots, x_m)  \rvert
{{< /m >}}

## VC Dimension

For binary classification problems, $\Pi_{\mathcal H}(m) \leq 2^m$. For small $m$, it is easier to have $\Pi_{\mathcal H}(m) = 2^m$. It is probably also easy for $m=2$. As $m$ becomes larger, not every $\mathcal H$ can reach $\Pi_{\mathcal H}(m) = 2^m$. At some point, $m=m_t$, we will start to have $\Pi_{\mathcal H}(m) < 2^m$. The VC dimension $d_{\text{VC}}(\mathcal H)$ is this $m_t$,

{{< m >}}
d_{\text{VC}}(\mathcal H) = m_t.
{{< /m >}}

For some $\mathcal H$, we have $\Pi_{\mathcal H}(m) = 2^m$ for all $m$. These hypothesis sets have $d_{\text{VC}}(\mathcal H) = \infty$.






[^Deckert2017]: {{< cite key="Deckert2017" >}}