---
title: "Centered Kernel Alignment (CKA)"
description: "Centered Kernel Alignment (CKA) is a similarity metric designed to measure the similarity of between representations of features in neural networks."
date: 2021-11-08
categories:
  - "Machine Learning"
tags:
  - "Data"
  - "Representation"
  - "Similarity"
links:
  - cards/math/statistics-centering-matrix.md
  - cards/machine-learning/measurement/hilbert-schmidt-independence-criterion.md
---

Centered Kernel Alignment (CKA) is a similarity metric designed to measure the similarity of between representations of features in neural networks[^Kornblith2019].


## Definition of CKA


CKA is based on the {{< c "cards/machine-learning/measurement/hilbert-schmidt-independence-criterion.md" "Hilbert-Schmidt Independence Criterion (HSIC)" >}}.

{{< e "cards/machine-learning/measurement/hilbert-schmidt-independence-criterion.md" "Hilbert-Schmidt Independence Criterion (HSIC)" >}}

But HSIC is not invariant to isotropic scaling which is required for a similarity metric of representations[^Kornblith2019]. CKA is a normalization of HSIC,

$$
\operatorname{CKA}(K,L) = \frac{\operatorname{HSIC}(K, L)}{\sqrt{\operatorname{HSIC}(K,K) \operatorname{HSIC}(L,L)}}.
$$


## Applications

{{< figure src="../assets/centered-kernel-alignment/cka-cnn-different-number-of-layers.png" caption="Kornblith2019" >}}


## CKA has Problems too

Seita et al argues that CKA is a metric based on intuitive tests, i.e., calculate cases that we believe that should be similar and check if the CKA values is consistent with this intuition[^Seita]. Seita et al built a quantitive benchmark[^Seita].


[^Kornblith2019]: Kornblith S, Norouzi M, Lee H, Hinton G. Similarity of Neural Network Representations Revisited. arXiv [cs.LG]. 2019. Available: http://arxiv.org/abs/1905.00414

[^Gretton2005]: Gretton A, Bousquet O, Smola A, Schölkopf B. Measuring Statistical Dependence with Hilbert-Schmidt Norms. Algorithmic Learning Theory. Springer Berlin Heidelberg; 2005. pp. 63–77. doi:10.1007/11564089_7

[^Seita]: Seita D. How should we compare neural network representations? In: The Berkeley Artificial Intelligence Research Blog [Internet]. [cited 8 Nov 2021]. Available: [https://bair.berkeley.edu/blog/2021/11/05/similarity/](https://bair.berkeley.edu/blog/2021/11/05/similarity/)
