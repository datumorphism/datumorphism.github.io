---
title: "Confidence Interval"
excerpt: "Estimates from a sample can be entitled a confidence interval"
date: 2019-01-20
toc: true
category:
- 'Statistical Estimation'
tag:
- 'Statistics'
- 'Basics'
- 'Confidence Interval'
references:
- name: "Schaum's Outline of Theories and Problems of Elements of Statistics II, by Ruth Bernstein and Stephen Bernstein"
  title: ''
weight: 2
published: true
---

* ToC
{:toc}


## Why is Confidence Interval Needed?

Suppose I sample the population multiple times, mean value $\mu_i$ of the sample is calculated for each sample. It is a good question to ask how different these $\mu_i$ are compared to the true mean $\mu_0p$ of the population.


## Confidence Interval

This theorem states that the probability that the true mean $\mu_0$ falls into a specific range can be calculated using

$$
P( \mu \in [\bar X - z_{\alpha/2} \sigma_{\bar x}, \bar X + z_{\alpha/2} \sigma_{\bar x} ] ) = 1-\alpha.
$$


Here $z_{\alpha/2}$ is the [$z$ value](/wiki/statistics/jargons/#z-transformation) which makes the probability to be in between $[-z_{\alpha/2}, z_{\alpha/2}]$ to be $1-\alpha$.

<figure markdown="1">
![](../assets/1-alpha.jpg)
<figcaption markdown="1">
Fig 12-11 in Schaum's Outline of Theories and Problems of Elements of Statistics II, by Ruth Bernstein and Stephen Bernstein
</figcaption>
</figure>

We randomly choose one sample from the bunch of samples. The probability that $[\bar X - z_{\alpha/2} \sigma_{\bar x}, \bar X + z_{\alpha/2} \sigma_{\bar x} ]$ in one sample contains the true mean $\mu_p$ is given by $1-\alpha$. 

$[\bar X - z_{\alpha/2} \sigma_{\bar x}, \bar X + z_{\alpha/2} \sigma_{\bar x} ]$ is our confidence interval for a $1-\alpha$ confidence.