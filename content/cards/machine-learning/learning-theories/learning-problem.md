---
title: "The Learning Problem"
date: 2021-05-06
categories:
- 'Machine Learning::Theories'
tags:
- 'Learning Theory'
references:
  - name: "Vladimir N. Vapnik. The Nature of Statistical Learning Theory. 2000. doi:10.1007/978-1-4757-3264-1"
    link: "https://link.springer.com/book/10.1007%2F978-1-4757-3264-1"
    key: "Vapnik2000"
links:
  - cards/machine-learning/learning-theories/empirical-risk-minimization.md
  - cards/machine-learning/learning-theories/structural-risk-minimization.md
  - wiki/learning-theory/vc-dimension.md
published: true
---


The learning problem posed by Vapnik:[^Vapnik2000]

- Given a sample: $\\{z_i\\}$ in the probability space $Z$;
- Assuming a probability measure on the probability space $Z$;
- Assuming a set of functions $Q(z, \alpha)$ (e.g. loss functions), where $\alpha$ is a set of parameters;
- A risk functional to be minimized by tunning "the handles" $\alpha$, $R(\alpha)$.

The risk functional is

{{< m >}}
R(\alpha) = \int Q(z, \alpha) \,\mathrm d F(z).
{{< /m >}}

A learning problem is the minimization of this risk.

[^Vapnik2000]: {{< cite key="Vapnik2000" >}}