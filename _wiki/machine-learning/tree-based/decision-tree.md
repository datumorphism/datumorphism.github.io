---
title: "Decision Tree"
excerpt: "decision tree"
date: 2019-12-25
toc: true
category:
- 'Machine Learning::Tree'
tag:
- 'Decision Tree'
- 'Supervised Learning'
- 'Statistical Learning'
- 'Basics'
mermaid: true
weight: 2
---

In this article, we will explain how decision trees work and build a tree by hand.

## Definition of the problem

We will predict whether I should go to work today. In this demo project, we consider the following features.

| feature | possible values |
|:----:|:---:|
| health | 0: feeling bad, 1: feeling good |
| weather | 0: bad weather, 1: good weather |
| holiday | 0: holiday, 1: not holiday |

For more compact notations, we use the abstract notation $\{0,1\}^3$ to describe a set of three features each with 0 and 1 as possible values.
{: .notes--info}

## How to Describe a Decision Tree

In theory, we would expect a decision tree of the following.

<div class="mermaid">
graph TD
	A[health] --> |feeling good| E[stay home]
  A[health] --> |feeling bad| B[weather]
  B --> |bad weather| E
  B --> |good weather| C[holiday]
  C --> |holiday| E
  C --> |not holiday| G[go to the office]

</div>

**However, we do not forge trees using experience. We build the tree using data.**

## Data

