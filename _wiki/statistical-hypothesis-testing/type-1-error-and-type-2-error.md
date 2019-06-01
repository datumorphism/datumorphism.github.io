---
title: "Types of Errors in Statistical Hypothesis Testing"
excerpt: "We all make mistakes. The question is, what kind of mistakes."
date: 2019-05-31
toc: true
category:
- 'Statistical Hypothesis Testing'
tag:
- 'Statistics'
- 'Basics'
- 'Hypothesis Testing'
references:
- name: "Elements of Statistics II by Stephen Bernstein and Ruth Bernstein"
  link: 'https://books.google.de/books/about/Schaum_s_Outline_of_Elements_of_Statisti.html?id=3LhPwUhrVIcC'
weight: 3
---

* ToC
{:toc}

## Type I and Type II Errors

In statistical hypothesis testing, we always have a null hypothesis $H_0$ which refers to the statement to be tested. We have two possible conclusions from a hypothesis testing,
1. to accept the hypothesis, that is concluding that $H_0$ is true,
2. to reject the hypothesis, that is concluding that $H_0$ is false.

However, it is possible that our conflusion is not correct. There are four possible results.


|      | $H_0$ is True (Ground Truth) |  $H_0$ is False (Ground Truth) |
|:-------:|:-------:|:-------:|
| **Accept** $H_0$ **(after hypothesis testing)**  | Correct  |  Type II Error  |
| **Reject** $H_0$ **(after hypothesis testing)** | Type I Error | Correct |

We could tell that there are two types of errors:
1. Type I: The hypothesis $H_0$ is correct but we rejected it:
2. Type II: the hypothesis $H_0$ is wrong but we accepted it.

## What Kind of Mistakes

We all make mistakes. The question is, what kind of mistakes.

If we forget about the name "Null Hypothesis" and only consider just any hypothesis, the name I and II won't matter. So there is a reason that we design our null hypothesis correctly.

<div class="card">
	<header class="card-header">
		<p class="card-header-title card-toggle">Why is that</p>
	</header>
	<div class="card-content is-hidden">
		<div class="content">
			For cancer screening, we definitely don't want to miss out some real cancer samples. If we are using "the sample is a cancer sample" as a hypothesis, we would like to reduce type I errors. However, if we are using "the sample is not a cancer sample" as a hypothesis, we would like to reduce type II errors. In fact, null hypothesis should be the statement "the sample is not a cancer sample".
		</div>
	</div>
</div>


If we look at the threshold of p-value in a hypothesis testing, we are basically managing the risks of different types of errors.

Here I quote this very wise paragraph from *Elements of Statistics II* as shown in the reference.

> A P value can be thought of as a descriptive statistic that measures how much support the data give to the null hypothesis: the smaller the P value, the less the support. But what level of support is considered so small that the null hypothesis should be rejected?
> 
> -- 16.8 in the book Elements of Statistics II by Stephen Bernstein and Ruth Bernstein


We will denote the threshold of the hypothesis testing as $p_t$. If the $p < p_t$, then we reject our hypothesis. Here $p_t$ is linked to our risk of type I errors. The larger the threshold we choose, the higher the risk of making type I errors.

In hypothesis testing, it is crucial that we place the actual null hypothesis $H_0$ we would like to test so that type I error is the type of error we care about.

However, I believe that the theory doesn't prevent us from using a non-null hypothesis if we insist. But null hypothesis is the most important one when we are dealing with new findings. If you have different opinions, I would appreciate it if you leave a comment.
{: .notes--warning}