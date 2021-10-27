---
title: "Shatter"
date: 2021-10-27
categories:
  - 'Machine Learning::Theories'
tags:
  - 'Learning Theory'
  - 'Set'
  - 'Shatter'
references:
  - name: "Murphy, K. P. (2012). Probabilistic Machine Learning: An Introduction."
    link: "https://mitpress.mit.edu/books/machine-learning-1"
    key: "Murphy2012"
links:
  - wiki/learning-theory/vc-dimension.md
references:
  - name: "Shattered Set @ Wikipedia"
    link: https://en.wikipedia.org/wiki/Shattered_set
    key: "shattered_set_wikipedia"
published: true
---

Given a set $\mathcal S$, and a class (collection of sets) $\mathcal H$.

For any subset of $\mathcal S$, denoted as $\mathcal s$, if we have an element of class $\mathcal H$, denoted as $\mathcal h$, that leads to[^shattered_set_wikipedia]

{{< m >}}
\mathcal h \cap \mathcal S = \mathcal s.
{{< /m >}}

Since the power set of $\mathcal S$ ($P(\mathcal S)$) contains all the possible subsets of $\mathcal S$, we can also rephrase the concept using power set. If we can find the power set $P(\mathcal S)$ by looking into intersections of elements $\mathcal h$ of $\mathcal H$ ($\mathcal h\in \mathcal H$), then we say $\mathcal H$ shatters $\mathcal S$ [^shattered_set_wikipedia].


{{< figure src="../assets/set-shatter/set-shatter-illustration.jpg" caption="Set $\mathcal S$ is shattered by class $\mathcal H$ if we can generate all possible subsets of $\mathcal S$ (power set of $\mathcal S$)." >}}



[^shattered_set_wikipedia]: {{< cite key="shattered_set_wikipedia" >}}