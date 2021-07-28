---
title: "The log-sum-exp Trick"
description: "For numerical stability we can use the log-sum-exp trick to calculate some loss such as cross entropy"
date: 2021-07-28
authors:
  - "LM"
categories:
  - "Machine Learning"
tags:
  - "Numerical"
  - "Neural Network"
  - "Basics"
references:
  - name: "Eisele R. The log-sum-exp trick in Machine Learning • Computer Science and Machine Learning. In: Robert Eisele [Internet]. 22 Jun 2016 [cited 28 Jul 2021]. Available: https://www.xarg.org/2016/06/the-log-sum-exp-trick-in-machine-learning/"
    link: "https://www.xarg.org/2016/06/the-log-sum-exp-trick-in-machine-learning/"
  - name: "Wang X. Numerical stability of binary cross entropy loss and the log-sum-exp trick – Integrative Biology and Predictive Analytics. In: Integrative Biology and Predictive Analytics [Internet]. 26 Sep 2018 [cited 28 Jul 2021]. Available: http://tagkopouloslab.ucdavis.edu/?p=2197"
    link: "http://tagkopouloslab.ucdavis.edu/?p=2197"
weight:
links:
  - "wiki/machine-learning/neural-networks/artificial-neural-networks.md"
---


The cross entropy for a binary class is

{{< m >}}
p \ln \hat p + (1-p) \ln (1-\hat p),
{{< /m >}}

where $p$ is the probability of the label A and $\hat p$ is the predicted probability of label A. Since we have binary classes, $p$ is either 1 or 0. However, the predicted probabilities can be any value between $[0,1]$.


{{< message class="note" title="Probability" >}}

For a very simple case, $\hat p$ might be a sigmoid like expression with exponential in it,

$$
p \sim \frac{1}{1 + \exp(-x)},
$$

where $x$ is some kind of input or intermediate input.
{{< /message >}}



The problem is, exponentials may blow up if $p\to 0$. To deal with it, we can factor a exponential out,

{{< m >}}
p = e^{a} ( e^{-a}p ).
{{< /m >}}

We choose $a$ carefully so that this eliminates the factors that leads to $p\to 0$.


For example, if we have a Gaussian like probability

{{< m >}}
\ln p \sim \ln \left(\sum_i \exp \left( -x_i^2 \right)\right),
{{< /m >}}

we know that $x$ can be as large as $1e^6$. One such value in the training data will destroy our loss function as we will have to calculate the exponential then $\ln$. Though we can calculate this manually and it is fine, our computer will treat $e^{-1e6}$ as 0 and $\ln 0$ leads to negative infinity. We do not get the correct answer. To deal with it, we will factor out the exponentials, and rewrite the expression as

{{< m >}}
\begin{align}
p \sim & a + \ln\left(e^{-a} \sum_i \exp \left( -x_i^2 \right)\right) \\
\sim & a + \ln \left(\sum_i \exp \left( -x_i^2 - a  \right)\right)
\end{align}
{{< /m >}}

where $a$ can be $-1e6$. In this case, we do not hit the overflow problem in the computer.