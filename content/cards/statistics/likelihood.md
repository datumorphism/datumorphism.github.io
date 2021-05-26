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

If we are flipping coins, and the head $x=1$ probability is $\theta$, the likelihood for this single event $x=1$ is $L(\theta)=\theta$. For two events with $x_1=1$ and $x_2=0$, the likelihood is

{{<m>}}
\theta (1 - \theta).
{{</m>}}

There is no guarantee that this is a pdf.


