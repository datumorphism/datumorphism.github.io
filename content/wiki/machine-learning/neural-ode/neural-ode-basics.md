---
title: "Neural ODE"
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
  - name: "msurtsukov. msurtsukov/neural-ode: Jupyter notebook with Pytorch implementation of Neural Ordinary Differential Equations. In: GitHub [Internet]. [cited 21 Aug 2022]. Available: https://github.com/msurtsukov/neural-ode"
    link: "https://github.com/msurtsukov/neural-ode"
    key: "msurtsukov2019"
  - name: "Chen RTQ, Rubanova Y, Bettencourt J, Duvenaud D. Neural Ordinary Differential Equations. arXiv [cs.LG]. 2018. Available: http://arxiv.org/abs/1806.07366"
    link: "http://arxiv.org/abs/1806.07366"
    key: "Chen2018"
weight: 1
garden:
  - "seedling"
---

In {{< c "wiki/machine-learning/neural-networks/artificial-neural-networks.md" "neural networks" >}}, residual connections is a popular architecture to build very deep neural networks[^He2015]. Apart from residual networks, there are many other designs for deep neural networks[^Srivastava2015][^Zhang2016][^Larsson2016][^Gomez2017][^Lu2017]. These methods share similar ideas that the layered structure in deep neural networks can be treated as a dynamical system and these different architectures are different numerical approaches of solving the dynamical system.


{{< figure src="../assets/neural-ode-basics/he2015-residual-block.png" caption="Figure taken from He K, Zhang X, Ren S, Sun J. Deep Residual Learning for Image Recognition. arXiv [cs.CV]. 2015. Available: http://arxiv.org/abs/1512.03385" >}}


{{< card title="The degradation problem" >}}

For deep neural networks, not all deep architectures are able to produce results that are significantly better than shallow architectures. It has been observed that "simply" stacking more layers to a shallow network may reach some saturated performance quite fast and leaving most of the added layers less useful.

In the work by Srivastava et al, they showed a comparison of "plain" deep networks, which has the layers simply stacked, and their highway networks which has gates that control how close to identity each layer is. The following is a figure extracted from their seminal work [*Highway Networks*](http://arxiv.org/abs/1505.00387).

![Highway Networks](../assets/neural-ode-basics/highway-network-plain-vs-highway-loss.png)

{{< /card >}}



## Neural ODE

An alternative view of the above approaches as {{< c "wiki/dynamical-system/ordinary-differential-method.md" >}} of dynamical system. For example, a residual connection structure can be reformulated as a first order different equation[^Chen2018], i.e., a residual connection of the following form

{{< m >}}
h_{t+1} = h_t + f(h_t, \theta_t),
{{< /m >}}

is a discretized case of the differential equation

{{< m >}}
\frac{\mathrm d h(t)}{\mathrm d t} = f(h(t), \theta(t), t).
{{< /m >}}

In the above equation, the variable $t$ is not necessarily physical time. This is an "extrapolated" version of the number of layers. But under some certain problems, $t$ can be the physical time.

{{< message >}}

For simplicity, we can even assume a set of static parameters $\theta$.

{{< /message >}}


Given any Jacobian $f(h(t), \theta(t), t)$, we can, at least numerically, perform integration to find out the value of $h(t)$ at any $t=t_N$,

{{< m >}}
h(t_N) = \int_{t_0}^{t_i} f(h(t), \theta(t), t) \mathrm dt.
{{< /m >}}

In this formalism, we find out the transformed input $h(t_0)$ by solving this differential equation. In traditional neural networks, we achieve this by stacking many layers of neural networks using skip connections.

In the original Neural ODE paper, the authors used the so-called reverse-model derivative method[^Chen2018].


## Time Series and Neural ODE

We can model the data generating process behind time series data using dynamical systems. The simplest continuous formulation is a first order ordinary differential equation. Given time series $\\{y_i\\}$, we can use the following first order differential equation

{{< m >}}
\frac{\mathrm dy(t)}{\mathrm d t} = f(y(t), \theta, t).
{{< /m >}}

Generally speaking, finding $f$ requires a lot of hypothesis and explorations. Neural ODE provides a general framework to approximate such a dynamical system.

For example, we can feed some data points $\\{(t_0, y_0), (t_1, y_1), \cdots, (t_m, y_m)\\}$ into the model, and we solve the differential equation for $t=t_{m+1}$. By calculating the loss and applying backpropagation, we can optimize the parameters $\theta$ in the Jacobian $f$. We then feed the next data points $\\{(t_1, y_1), (t_2, y_2), \cdots, (t_{m+1}, y_{m+1})\\}$ and solving for $t=t_{m+2}$ and do the same. By exhausting the whole dataset, we can find an "optimal" Jacobian $f$ which can be used in inference to rebuild the whole dynamics.




[^Srivastava2015]: {{< cite key="Srivastava2015" >}}
[^He2015]: {{< cite key="He2015" >}}
[^Zhang2016]: {{< cite key="Zhang2016" >}}
[^Larsson2016]: {{< cite key="Larsson2016" >}}
[^Gomez2017]: {{< cite key="Gomez2017" >}}
[^Lu2017]: {{< cite key="Lu2017" >}}
[^Chen2018]: {{< cite key="Chen2018" >}}