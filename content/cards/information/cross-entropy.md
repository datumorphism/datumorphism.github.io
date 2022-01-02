---
title: "Cross Entropy"
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
  - name: "Contributors to Wikimedia projects. Cross entropy. In: Wikipedia [Internet]. 4 Jul 2021 [cited 4 Sep 2021]. Available: https://en.wikipedia.org/wiki/Cross_entropy"
    link: "https://en.wikipedia.org/wiki/Cross_entropy"
    key: "cross_entropy_wiki"
  - name: "Mehta P, Wang C-H, Day AGR, Richardson C, Bukov M, Fisher CK, et al. A high-bias, low-variance introduction to Machine Learning for physicists. Phys Rep. 2019;810: 1–124. doi:10.1016/j.physrep.2019.03.001"
    link: "https://linkinghub.elsevier.com/retrieve/pii/S0370157319300766"
    key: "Mehta2019"
links:
  - "cards/information/shannon-entropy.md"
  - "wiki/machine-learning/basics/kl-divergence.md"
  - "wiki/machine-learning/linear/logistic-regression.md"
---

Cross entropy is[^cross_entropy_wiki]

$$
H(p, q) = \mathbb E_{p} \left[ -\log q \right].
$$

Cross entropy $H(p, q)$ can also be decomposed,

$$
H(p, q) = H(p) + \operatorname{D}_{\mathrm{KL}} \left( p \parallel q \right),
$$

where $H(p)$ is the {{< c "cards/information/shannon-entropy.md" "entropy of $P$" >}} and $\operatorname{D}_{\mathrm{KL}}$ is the {{< c "wiki/machine-learning/basics/kl-divergence.md" "KL Divergence" >}}.

Cross entropy is widely used in classification problems, e.g., {{< c "wiki/machine-learning/linear/logistic-regression.md" "logistic regression" >}}[^Mehta2019].


## Binary Cross Entropy

For dataset with 2 classes ($0$ and $1$) in the target, we denote the true label probability is $p$, and the predicted probability is $q$. For example, $q_{y=1}$ denotes the probability of predicted label being $1$.

{{< m >}}
\begin{align*}
H(p, q) =& - p_{y=0}  \log (q_{\hat y=0}) - p_{y=1}  \log (q_{\hat y=1})  \\
=& - p_{y=0}  \log (q_{\hat y=0}) - (1 - p_{y=0})  \log ( 1 - q_{\hat y=0} )
\end{align*}
{{< /m >}}

For $y\in \\{0,1\\}$, we have

{{< m >}}
H(p, q) = \begin{cases}
- \log (q_{\hat y=0}) ,  & \text{for } y=0 \\
- \log ( 1 - q_{\hat y=0} ) ,  & \text{for } y=1.
\end{cases}
{{< /m >}}

Combining the two expressions, we can simply use the following formula,

{{< m >}}
H(p, q) = - y \log (q_{\hat y=0}) - y \log ( 1 - q_{\hat y=0} ).
{{< /m >}}

The two probabilities of $q_{\hat y=0}$ and $q_{\hat y=1}$ can be predicted by a model.


[^cross_entropy_wiki]: {{< cite key="cross_entropy_wiki" >}}
[^Mehta2019]: {{< cite key="Mehta2019" >}}