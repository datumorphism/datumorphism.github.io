---
title: "Statistical Hypothesis Testing"
excerpt: "hypothesis testing is about the probability of alternative hypothesis if the null hypothesis is true, or even more general"
date: 2019-01-20
toc: true
category:
- 'Statistical Hypothesis Testing'
tag:
- 'Statistics'
- 'Basics'
- 'Hypothesis Testing'
references:
- name: "Schaum's Outline of Theories and Problems of Elements of Statistics II, by Ruth Bernstein and Stephen Bernstein, Chapter 16"
  title: ''
weight: 1
---

When we have a sample of the population, we immediately calculate the mean using the sample, say the result is $\mu_0$. Of course, the population mean $\mu_p$ is unknown and probably can never be known.

This specific sample mean $\mu_0$ is nothing but like an **advanced** educated guess. Then again, how do we know if our this specific sample mean $\mu_0$ is a faithful representation of the population mean? In fact, this question is not limited to mean. It applies to any statistical measurement.

<div class="card">
	<header class="card-header">
		<p class="card-header-title card-toggle">The Statistical Estimation Theory Solution to This Problem</p>
	</header>
	<div class="card-content is-hidden">
		<div class="content">
			In statistical estimation theory, we would tell the sample value with some indication of the degrees of faithfulness. For example, we would tell the sample mean together with a <a href="/wiki/statistical-estimation/confidence-interval/">confidence interval</a>.
		</div>
	</div>
</div>

The hypothesis testing theory solution to this problem is to tell whether our hypothesis is correct.

To explain this method, we have to establish two hypotheses for our statistical result. We will still use the mean as the measurement. For example, we could have the two hypothesis:

1. Null hypothesis $H_0$: the population mean $\mu_p$ equals to this specific educated guess $\mu_0$.
2. Alternative hypothesis $H_a$: the population mean $\mu_p$ doesn't equal to our educated guess $\mu_0$.

The hypotheses themselves could be much more general but we always have a null hypothesis and alternative hypothesis.

Hypothesis testing is in fact a conditional probability. To see this, we reformulate our statistical procedures.

1. We get an educated guess of our population mean, $\mu_p = \mu_0$.
2. We set up the null hypothesis and alternative hypothesis.
   1. $H_0$: the population mean $\mu_p$ equals to this specific educated guess $\mu_0$.
   2. $H_a$: the population mean $\mu_p$ doesn't equal to our educated guess $\mu_0$.
3. We draw samples from our population and calculate the sample mean $\mu_i$, where $i$ is used to label the samples.
4. Then we ask the question: Are the sample means tolerable assumping the null hypothesis is true? In other words, we are calculating
   $$
   P( \text{sample mean is located at } \mu_i  | \text{null hypothesis is true} )
   $$

However, the conclusion from hypothesis testing is only about whether the null hypothesis is accepted or rejected, nothing more. In our example:

1. We can NOT determine what mean value to take if the hyposis is rejected.
2. We can NOT understand how likely our educated guess $\mu_p = \mu0$ is true. The probability we calculated is about the sample not the hypothesis.

As mentioned, it doesn't have to be related to the mean value. We can do hypothesis test on other statistical measurements.


## Choosing a test method

A map on this topic: [Map](https://www.plectica.com/maps/8ORZBLFDO)

![](../assets/hypothesis-testing/statistical-tests.png)

