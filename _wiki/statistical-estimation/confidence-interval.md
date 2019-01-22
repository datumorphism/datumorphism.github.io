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
notify: "The name confidence interval is rather misleading."
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


Here $z_{\alpha/2}$ is the [$z$ value](/wiki/statistics/jargons/#z-transformation) which makes the probability to be in between $[-z_{\alpha/2}, z_{\alpha/2}]$ to be $1-\alpha$. As shown in the following figure.

<figure markdown="1">
![](../assets/gaussian-alpha.png)
<figcaption markdown="1">
The definition of $\alpha$ for a [normal distribution](/wiki/distributions/normal-distribution). In a probability distribution, the area under the curve should be 1. Or the integral of the curve from $-\infty$ to $\infty$ should be 1. $\alpha$ is the sum of the two red areas. In this example, we actually have $\alpha=0.05$.
</figcaption>
</figure>

Confidence level is a **weird measurement of our statistical confidence**.

Imagine we are drawing 100 samples from the population and calculate the range $[\bar X - z_{\alpha/2} \sigma_{\bar x}, \bar X + z_{\alpha/2} \sigma_{\bar x} ]$. We would have 100 different ranges. How many of them would actually contain the true mean? The answer is probably around $(1-\alpha)$ fraction of all the 100 calculations. When we have a huge amount of samples, this probability becomes quite faithful.

Why is this a representation of our confidence? Imagine we choose one sample from this 100 calculations. The probability that this specific number $[\bar X - z_{\alpha/2} \sigma_{\bar x}, \bar X + z_{\alpha/2} \sigma_{\bar x} ]$ (with all the numbers substituted using the sample values, for example $[-1,2]$, which is different from every other sample calculations) contains the true mean is also $(1-\alpha)$.

In other words, $[\bar X - z_{\alpha/2} \sigma_{\bar x}, \bar X + z_{\alpha/2} \sigma_{\bar x} ]$ is the interval that we are $1-\alpha$ confident that we have captured the true mean. From this point of view, **the name confidence interval is rather misleading.**