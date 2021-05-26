---
title: "Likelihood"
description: "Likelihood is not necessarily a pdf"
date: 2021-05-26
category:
  - "Statistics"
tags:
  - "Statistics"
  - "Likelihood"
  - "Bayes"
references:
  - name: "Jaynes ET. Probability Theory: The Logic of Science. Cambridge University Press; 2003. doi:10.1017/CBO9780511790423"
    link: "https://www.cambridge.org/core/books/probability-theory/9CA08E224FF30123304E6D8935CF1A99"
    key: "jaynes2003"
  - name: "Parameter Estimation | CS109: Probability for Computer Scientists"
    link: "https://web.stanford.edu/class/archive/cs/cs109/cs109.1192/reader/11%20Parameter%20Estimation.pdf"
    key: "cs109"
---

For some data points $\\{x_i\\}$ and a model $\theta$, the likelihood of our data point $x_i$ is $p(x_i\mid \theta)$. To be more specific, the likelihood of all data points is a function of the model $\theta$,

{{< m >}}
L(\theta) = \Pi_i p(x_i\mid\theta).
{{</m>}}


It should be mentioned that this likelihood is not necessarily a pdf. As an example, we can calculate the likelihood of a Bernoulli distribution for a single event $x$,

{{< m >}}
L(\theta) = \theta^x (1-\theta)^{(1-x)}.
{{< /m >}}

If we are flipping coins, and the head $x=1$ probability is $\theta$, the likelihood for this single event $x=1$ is

{{<m>}}
L(\theta)=\theta.
{{</m>}}

For two events with $x_1=1$ and $x_2=0$, the likelihood is

{{<m>}}
L(\theta) = \theta (1 - \theta).
{{</m>}}

There is no guarantee that this is a pdf.

## Maximum likelihood

How do we find out the value of the parameters? One popular method is MLE, aka to maximize the likelihood, i.e., maximizing the probability of the data by choosing a proper model. In the second example, we find the derivatives

{{<m>}}
\partial_\theta L(\theta) = 1 - 2\theta.
{{</m>}}

The maximum value is reached when $\theta=\hat\theta=1/2$.

However, if we have two experiments with $x_1=1$ and $x_2=1$, the likelihood becomes

{{<m>}}
L(\theta) = \theta\theta.
{{</m>}}

MLE shows that $\theta=\hat\theta=0$.

If we have two experiments with $x_1=0$ and $x_2=0$, the likelihood becomes

{{<m>}}
L(\theta) = (1-\theta)(1-\theta).
{{</m>}}

MLE shows that $\theta=\hat\theta=1$.







