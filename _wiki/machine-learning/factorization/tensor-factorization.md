---
title: "Tensor Factorization"
excerpt: "A generalization of matrix factorization"
date: 2019-06-17
toc: true
category:
- 'Machine Learning'
tag:
- 'Machine Learning'
- 'Factorization'
- 'Tensor'
references:
- link: https://doi.org/10.1007/978-3-319-24486-0_2
  name: 'Anandkumar, A., Ge, R., Hsu, D., Kakade, S. M., & Telgarsky, M. (2012). Tensor decompositions for learning latent variable models. Journal of Machine Learning Research, 15(1), 2773–2832.'
- link: https://www.offconvex.org/2015/12/17/tensor-decompositions/
  name: Tensor Methods in Machine Learning
- link: https://en.wikipedia.org/wiki/Penrose_graphical_notation
  name: Penrose graphical notation
- link: https://math.stackexchange.com/questions/455478/what-is-the-practical-difference-between-abstract-index-notation-and-ordinary
  name: What is the practical difference between abstract index notation and “ordinary” index notation
weight: 3
---

* ToC
{:toc}

## Tensors

We will be talking about tensors. We will skip the introduction to tensor.

In this article, we follow a commonly used convention for tensors in physics, the abstract index notation. We will denote tensors as $T^{ab\cdots}_ {\phantom{ab\cdots}cd\cdots}$, where the latin indices such as $^{a}$ are simply a placebo for the slot for this "tensor machine". For a given basis (coordinate system), we can write down the components of this tensor $T^{\alpha\beta\cdots} _ {\phantom{\alpha\beta\cdots}\gamma\delta\cdots}$.

<div class="card">
<header class="card-header">
<p class="card-header-title card-toggle">Okay, But Why</p>
</header>
<div class="card-content is-hidden">
<div class="content">
What is usually seen in blog posts is the use of component forms of tensors, $T^{\alpha\beta\cdots}_{\phantom{\alpha\beta\cdots}\gamma\delta\cdots}$. Those are the numbers for a given basis. We would like to keep it general.
</div>
</div>
</div>

