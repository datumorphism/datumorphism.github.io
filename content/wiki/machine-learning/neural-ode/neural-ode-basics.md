---
title: "Neural ODE Basics"
description: "The concepts and ideas of neural ODE"
date: 2022-08-13
categories:
  - "Machine Learning"
tags:
  - "Deep Learning"
  - "Neural ODE"
references:
  - name: "He K, Zhang X, Ren S, Sun J. Deep Residual Learning for Image Recognition. arXiv [cs.CV]. 2015. Available: http://arxiv.org/abs/1512.03385"
    link: "http://arxiv.org/abs/1512.03385"
    key: "He2015"
  - name: "Srivastava RK, Greff K, Schmidhuber J. Highway Networks. arXiv [cs.LG]. 2015. Available: http://arxiv.org/abs/1505.00387"
    link: "http://arxiv.org/abs/1505.00387"
    key: "Srivastava2015"
  - name: "Zhang X, Li Z, Loy CC, Lin D. PolyNet: A Pursuit of Structural Diversity in Very Deep Networks. arXiv [cs.CV]. 2016. Available: http://arxiv.org/abs/1611.05725"
    link: "http://arxiv.org/abs/1611.05725"
    key: "Zhang2016"
  - name: "Larsson G, Maire M, Shakhnarovich G. FractalNet: Ultra-Deep Neural Networks without Residuals. arXiv [cs.CV]. 2016. Available: http://arxiv.org/abs/1605.07648"
    link: "http://arxiv.org/abs/1605.07648"
    key: "Larsson2016"
  - name: "Gomez AN, Ren M, Urtasun R, Grosse RB. The Reversible Residual Network: Backpropagation Without Storing Activations. arXiv [cs.CV]. 2017. Available: http://arxiv.org/abs/1707.04585"
    link: "http://arxiv.org/abs/1707.04585"
    key: "Gomez2017"
  - name: "Lu Y, Zhong A, Li Q, Dong B. Beyond Finite Layer Neural Networks: Bridging Deep Architectures and Numerical Differential Equations. arXiv [cs.CV]. 2017. Available: http://arxiv.org/abs/1710.10121"
    link: "http://arxiv.org/abs/1710.10121"
    key: "Lu2017"
weight: 1
---

In {{< c "wiki/machine-learning/neural-networks/artificial-neural-networks.md" "neural networks" >}}, residual connections is a popular architecture to build very deep neural networks.[^He2015] Apart from residual networks, there are many other designs for deep neural networks.[^Srivastava2015][^Zhang2016][^Larsson2016][^Gomez2017][^Lu2017] These methods share similar ideas that the layered structure in deep neural networks can be treated as a dynamical system and these different architectures are different numerical approaches of solving the dynamical system.


{{< figure src="../assets/neural-ode-basics/he2015-residual-block.png" caption="Figure taken from He K, Zhang X, Ren S, Sun J. Deep Residual Learning for Image Recognition. arXiv [cs.CV]. 2015. Available: http://arxiv.org/abs/1512.03385" >}}


{{< card title="The degradation problem" >}}

For deep neural networks, not all deep architectures are able to produce results that are significantly better than shallow architectures. It has been observed that "simply" stacking more layers to a shallow network may reach some saturated performance quite fast and leaving most of the added layers less useful.

In the work by Srivastava et al, they showed a comparison of "plain" deep networks, which has the layers simply stacked, and their highway networks which has gates that control how close to identity each layer is. The following is a figure extracted from their seminal work [*Highway Networks*](http://arxiv.org/abs/1505.00387).

![Highway Networks](../assets/neural-ode-basics/highway-network-plain-vs-highway-loss.png)

{{< /card >}}



## Neural ODE





[^Srivastava2015]: {{< cite key="Srivastava2015" >}}
[^He2015]: {{< cite key="He2015" >}}
[^Zhang2016]: {{< cite key="Zhang2016" >}}
[^Larsson2016]: {{< cite key="Larsson2016" >}}
[^Gomez2017]: {{< cite key="Gomez2017" >}}
[^Lu2017]: {{< cite key="Lu2017" >}}
