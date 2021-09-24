---
title: "Initialize Artificial Neural Networks"
description: "Initialize a neural network is important for the training and performance. Some initializations simply don't work, some will degrade the performance of the model. We should choose wisely."
date: "2021-09-23"
authors:
  - "L Ma"
categories:
  - "Neural Networks"
tags:
  - "Artificial Neuron"
  - "Neural Network"
  - "Basics"
references:
  - name: "Lippe P. Tutorial 3: Activation Functions — UvA DL Notebooks v1.1 documentation. In: UvA Deep Learning Tutorials [Internet]. [cited 23 Sep 2021]. Available: https://uvadlc-notebooks.readthedocs.io"
    link: "https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial3/Activation_Functions.html"
    key: "Lippe2020"
  - name: "Ouannes P. How to initialize deep neural networks? Xavier and Kaiming initialization. In: Title [Internet]. 22 Mar 2019 [cited 24 Sep 2021]. Available: https://pouannes.github.io/blog/initialization"
    link: "https://pouannes.github.io/blog/initialization/#mjx-eqn-eqfwd_K"
  - name: "Glorot X, Bengio Y. Understanding the difficulty of training deep feedforward neural networks. Teh YW, Titterington M, editors. 2010;9: 249–256. Available: http://proceedings.mlr.press/v9/glorot10a.html"
    link: "http://proceedings.mlr.press/v9/glorot10a.html"
    key: "Glorot2010"
  - name: 'Katanforoosh & Kunin, "Initializing neural networks", deeplearning.ai, 2019.'
    link: "https://www.deeplearning.ai/ai-notes/initialization/"
    key: "Katanforoosh2019"
links:
  - "wiki/machine-learning/neural-networks/artificial-neural-networks.md"
---

The weights are better if they[^Lippe2020]

- are zero centered, and
- have similar variance across layers.

{{< message class="info" title="Why" >}}

If we have very different variances across layers, we will need a different learning rate for each layer for our optimization. Setting the variances to be on the same scale, we can use a global learning rate for the whole network.

{{< /message >}}


## Variance is related to the input size of the layer

Suppose we are using a simple linear activation, $\sigma(x) = \alpha x$. For a series of inputs $x_j$, the outputs $y_i$ are

{{< m >}}
y_i = \sum_{j} w_{ij} x_j.
{{< /m >}}

The variance of $y_i$ is

{{< m >}}
\begin{align}
\operatorname{Var}\left[ y \right] &= \alpha^2 \operatorname{Var}\left[\sum_{j} w_{ij} x_j \right] \\
& = \alpha^2 \sum_{j}\operatorname{Var}\left[ w_{ij} x_j \right] \\
&= \alpha^2 \sum_j \left( \mathbb E\left[ (w_{ij}x_j)^2 \right] - \mathbb E^2 \left[ w_{ij} x_j \right] \right) \label{eq-var-expand-var}\\
&= \alpha^2 \sum_j \left( \mathbb E\left[ (w_{ij}x_j)^2 \right] - {\color{red}\mathbb E^2 \left[ w_{ij} \right]} \mathbb E^2 \left[ x_j \right] \right) \label{eq-var-expand-expectation-sq} \\
&= \alpha^2 \sum_j \left( \mathbb E\left[ (w_{ij}x_j)^2 \right]\right) \label{eq-var-drop-zero-exp} \\
&= \alpha^2 \sum_j \left( \mathbb E\left[ w_{ij}^2x_j^2 \right]\right) \label{eq-var-expand-sq-expectation}\\
&= \alpha^2 \sum_j \left( \mathbb E\left[ w_{ij}^2\right]\mathbb E\left[x_j^2 \right]\right) \label{eq-var-propagate-exp}\\
&= \alpha^2 \sum_j \left( \left(\mathbb E\left[ w_{ij}^2\right] - {\color{red}\mathbb E^2\left[ w_{ij} \right]}\right)\left(\mathbb E\left[x_j^2 \right] - {\color{red}\mathbb E^2\left[ x_j \right]} \right) \right) \label{eq-var-add-zero-exp-w-x}\\
&= \alpha^2 \sum_j \left( \operatorname{Var}\left[ w_{ij} \right]\operatorname{Var}\left[x_j \right]\right) \label{eq-var-form-var-w-x}\\
&= D \alpha^2 \left( \sigma_w^2\sigma_x^2\right) \label{eq-var-calculate-sum}.
\end{align}
{{< /m >}}

In the derivation,

- the red term in $\eqref{eq-var-expand-expectation-sq}$, ${\color{red}\mathbb E^2 \left[ w_{ij} \right]}$ is zero,
- we assume the input has zero expectation in $\eqref{eq-var-add-zero-exp-w-x}$, i.e., ${\color{red}\mathbb E^2\left[ x_j \right]}=0$,
- in the last step {eq-var-calculate-sum}, we assumed all the variances are the same, $\operatorname{Var}\left[ w_{ij} \right]=\sigma_w^2$ and $\operatorname{Var}\left[x_j \right]=\sigma_x^2$,
- $D$ is the dimension of the input data $x$.

If we require $\operatorname{Var}\left[ y \right] = \sigma_x^2$, the variance of the weights should be

{{< m >}}
\sigma_w^2  = \frac{1}{D \alpha^2}.
{{< /m >}}

For linear activation function, $\alpha=1$, thus

{{< m >}}
\sigma_w^2  = \frac{1}{D}.
{{< /m >}}

For more features we have in the input, we should choose smaller initial variance for the weights.


## Weight Variance is also related to the output size of the layer

Assuming $\hat D$ is the output dimension of the layer, it is also proved that we need


{{< m >}}
\sigma_w^2  = \frac{1}{\hat D},
{{< /m >}}

to make sure the back-prop is also stable, i.e., have similar gradient variance across layers.

## Xavier Initialization

The Xavier initialization is something in between the above two idea,

{{< m >}}
\sigma_w^2 = \frac{2}{D + \hat D}.
{{< /m >}}

In Glorot2010, the authors also proposed a uniform distribution alternative to normal distribution, which they call the **normalized initialization**[^Glorot2010]. In this proposal, we uniformly sample from the range

{{< m >}}
\left[ -\frac{\sqrt{6}}{D + \hat D}, \frac{\sqrt{6}}{D + \hat D} \right].
{{< /m >}}

This proposal is essentially the same idea as the Xavier initialization.

## What are the differences

[deeplearning.ai has an interactive session](https://www.deeplearning.ai/ai-notes/initialization/) on the effects of initializations for classification tasks on MNIST.


[^Lippe2020]: {{< cite key="Lippe2020" >}}
[^Glorot2010]: {{< cite key="Glorot2010" >}}