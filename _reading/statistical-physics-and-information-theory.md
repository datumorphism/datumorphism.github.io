---
layout: reading
title:  "Information Theory and Statistical Mechanics"
date: 2019-03-01 #2014-08-27T11:57:41-04:00
subtitle: "Max entropy principle from Jaynes, E. T. (1957)."
author: OctoMiao
comments: true
types: 
- 'paper'
category:
- theory
tag:
- 'intelligence'
summary: Max entropy principle as a method to infer distributions of statistical systems
status: 100%
references:
  - name: "Jaynes, E. T. (1957). Information Theory and Statistical Mechanics. Physical Review, 106(4), 620–630."
    link: https://doi.org/10.1103/PhysRev.106.620
---

## What problem are we solving?

For a large system consisting of small entities, the phase space could be extremely large. In this problem, we assume that only one quantitiy is measure on a macroscopic level. Then we have to find the values for other measurable quantities.


## Line of Reasoning


Jaynes pointed out in this paper that we are solving an insufficient reason problem in statistical physics. What we could measure is some macroscopic quantity, from which we derive other macroscopic quantities. That being said, we know a system with a lot of possible microscopic states, $\{ s_i \}$ while the probabilities of each microscopic state $\{p_i \}$ is not know at all. We also know a macroscopic quantity $\langle f(s_i) \rangle$ which is defined as

$$
\langle f \rangle = \sum_i p_i f(s_i).
$$

The question that Jaynes asked was the following.

**How are we supposed to find another macroscopic quantities that also depends on the microscopic state of the system?** Say $g(s_i)$.

It is a quite interesting question for stat mech. In my opinion, it can be generalized. To visualize this problem, we know think of this landscape of the states. Instead of using the state as the dimensions, we use the probabilities as the dimensions since they are unknown. In the end, we have a coordinate system with each dimension as the value of the probabilities $\{p_i\}$ and the one dimension for the value of $\langle g \rangle (p_i)$ which depends on $\{p_i\}$. Now we constructed a landscape of $\langle g \rangle (p_i)$. The question is, how do our universe arrange the landscape? Where are we in this landscape if we are at equilibrium?


In Jaynes' paper, he mentioned several crucial problems.

1. Do we need to know the landscape formed by $\{p_i\}$ and $\langle f(x_i)\rangle$? No.
2. Do we need to find the exact location of our system? We have to.
3. How? Using max entropy principle.
4. How to calculate another macroscopic quantity based on one observed macroscopic quantity and the conservation of probability density? Using the probabilities found in the previous step.
5. Why max entropy works from the information point of view? Assumping less about the system.
6. Why is the result actually predicting measurements even the theory is purely objective? This shows how simple nature is. Going philosophical.
7. With the generality of the formalism, what else can we do with it to improve our statistical mechanics power? Based on the information we know, we have different formalism of statistical physics. 


Is this related to mutual information?
-----------------------------------------

The idea is great.

However, I think we have to consider another principle. I call this max mutual information principle. Suppose we do not have this max entropy principle. Somehow, we come up with an expression of the average of another quantity. What will happen from a landscape point of view?

If we construct these these two landscapes:

1. $\langle f(x_i)\rangle$ as a function of $\{p_i\}$,
2. and $\langle g(x_i)\rangle$ as a function of $\{p_i\}$.

Max mutual information indicates that the $\{p_i\}$ inferred from the two quantities should be the same. Huh, trivial.

