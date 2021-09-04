---
title: "Shannon Entropy"
description: ""
date: 2021-09-04
authors:
  - "Lei Ma"
categories:
  - "Information"
tags:
  - "Information Theory"
  - "Entropy"
references:
  - name: "Contributors to Wikimedia projects. Entropy (information theory). In: Wikipedia [Internet]. 29 Aug 2021 [cited 4 Sep 2021]. Available: https://en.wikipedia.org/wiki/Entropy_(information_theory)"
    link: "https://en.wikipedia.org/wiki/Entropy_(information_theory)"
    key: "shannon_entropy_wiki"
links:
  - "wiki/machine-learning/linear/logistic-regression.md"
---


Shannon entropy $S$ is the expectation of information content $I(X)=-\log \left(p\right)$[^shannon_entropy_wiki],

\begin{equation}
H(p) = \mathbb E_{p}\left[ -\log \left(p\right) \right].
\end{equation}


Cross entropy is widely used in classification problems, e.g., {{< c "wiki/machine-learning/linear/logistic-regression.md" "logistic regression" >}}.

[^shannon_entropy_wiki]: {{< cite key="shannon_entropy_wiki" >}}
