---
title: "Centering Matrix"
description: "Useful when centering a vector around its mean"
date: 2021-11-08
categories:
  - 'Math'
tags:
  - 'Matrix'
  - 'Statistics'
  - 'numpy'
references:
- name: "Contributors to Wikimedia projects. Centering matrix. In: Wikipedia [Internet]. 9 Jun 2021 [cited 8 Nov 2021]. Available: https://en.wikipedia.org/wiki/Centering_matrix"
  link: "https://en.wikipedia.org/wiki/Centering_matrix"
---

Given a vector $v$, with mean value of its elements $m$, we can center the vector by subtracting the mean $m$ from each element,

```python
import numpy as np

n = 10

v = np.random.randn(n)
v_c = v - v.mean()
```

This operation is easy and obvious. However, the formalism is not elegant. In some cases, we would like to formulate the process of centering the elements as operators,

$$
v_c = \operatorname{\hat H}v.
$$

In this case, the operator $\operatorname{\hat H}$ is simply a matrix

$$
\operatorname{\hat H} \to I_n - \frac{1}{n} J_n,
$$

where $n$ is the dimension of the vector $v$, $I_n$ is a identity matrix, $J_n$ is a matrix of all $1$s.

```python
cm = np.identity(n) - np.ones((n, n)) / n
np.matmul(cm, v)
```



[^wiki]: Contributors to Wikimedia projects. Centering matrix. In: Wikipedia [Internet]. 9 Jun 2021 [cited 8 Nov 2021]. Available: https://en.wikipedia.org/wiki/Centering_matrix

