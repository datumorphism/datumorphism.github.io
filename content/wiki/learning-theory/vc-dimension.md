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
  - name: "Zhang C, Bengio S, Hardt M, Recht B, Vinyals O. Understanding deep learning requires rethinking generalization. arXiv [cs.LG]. 2016. Available: http://arxiv.org/abs/1611.03530"
    link: "http://arxiv.org/abs/1611.03530"
    key: "Zhang2016"
  - name: "Bernstein J. Machine learning is just statistics + quantifier reversal. In: jeremybernste [Internet]. [cited 1 Nov 2021]. Available: https://jeremybernste.in/writing/ml-is-just-statistics"
    link: "https://jeremybernste.in/writing/ml-is-just-statistics"
    key: "Bernstein2021"
  - name: "Guedj B. A Primer on PAC-Bayesian Learning. arXiv [stat.ML]. 2019. Available: http://arxiv.org/abs/1901.05353"
    link: "http://arxiv.org/abs/1901.05353"
    key: "Guedj2019"
  - name: "Abu-Mostafa, Yaser S and Magdon-Ismail, Malik and Lin, Hsuan-Tien. Learning from Data. AMLBook; 2012. Available: https://www.semanticscholar.org/paper/Learning-From-Data-Abu-Mostafa-Magdon-Ismail/1c0ed9ed3201ef381cc392fc3ca91cae6ecfc698"
    link: "https://www.semanticscholar.org/paper/Learning-From-Data-Abu-Mostafa-Magdon-Ismail/1c0ed9ed3201ef381cc392fc3ca91cae6ecfc698"
    key: "Abu-Mostafa2012"
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

## Why Do We Care about the VC Dimension

Why is learning from data feasible? A learning process is the selection of good hypotheses from $\mathcal H$ using a data sample $\mathcal S$.

Given a training data sample $\mathcal S$, we train the model and calculate the in-sample error of the model, $E_{s}$. However, the in-sample error is not necessarily the same as the actual error, or the generalization error/out of sample error, $E_{g}$.

Using the Hoeffding's inequality, one could derive the so called learning bound[^Deckert2017],

{{< m >}}
P\left( E_g(h) - E_s(h) \leq \sqrt{ \frac{\log\lvert H\rvert + \log(2/\delta)}{2m} } \right) \geq 1 - \delta, \forall h\in \mathcal H,
{{< /m >}}

where $\mathcal H$ is a finite hypothesis set.

We immediately realize that if $\lvert\mathcal H\rvert \to \infty$, the bound becomes infinity too. The above theorem becomes useless.

Since the VC dimension describes the number of useful hypotheses, we might want to replace the actual hypothesis set size $\lvert \mathcal H\rvert$. This is not exactly correct but we indeed have a similar form

{{< m >}}
P\left( E_g(h) - E_s(h) \leq \sqrt{ \frac{8d\log(m/d) + 8\log(4/\delta)}{m} } \right) \geq 1 - \delta,
{{< /m >}}

for a binary classification problem.








[^Deckert2017]: {{< cite key="Deckert2017" >}}

[^Zhang2016]: {{< cite key="Zhang2016" >}}