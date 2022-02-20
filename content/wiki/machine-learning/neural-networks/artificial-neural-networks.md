---
title: "Artificial Neural Networks"
description: "Solving PDEs"
date: 2018-11-19
categories:
  - 'Artificial Neural Networks'
tags:
  - 'Machine Learning'
  - 'Artificial Neural Networks'
  - 'Basics'
references:
  - name: "Hassoun MH, Assistant Professor of Computer Engineering Mohamad H Hassoun. Fundamentals of Artificial Neural Networks. MIT Press; 1995. Available: https://mitpress.mit.edu/books/fundamentals-artificial-neural-networks"
    link: "https://mitpress.mit.edu/books/fundamentals-artificial-neural-networks"
  - name: "Shenouda EAMA. A Quantitative Comparison of Different MLP Activation Functions in Classification. Advances in Neural Networks - ISNN 2006. Springer Berlin Heidelberg; 2006. pp. 849–857. doi:10.1007/11759966_125"
    link: "https://link.springer.com/chapter/10.1007%2F11759966_125"
  - link: "https://doi.org/10.1016/0893-6080(89)90020-8"
    name: "Hornik, K., Stinchcombe, M., & White, H. (1989). Multilayer feedforward networks are universal approximators. Neural Networks, 2(5), 359–366."
  - link: "https://doi.org/10.1007/BF02551274"
    name: "Cybenko, G. (1989). Approximation by superpositions of a sigmoidal function. Mathematics of Control, Signals, and Systems, 2(4), 303–314."
  - link:
    name: "Freitag, K. J. (2007). Neural networks and differential equations."
  - name: "Tensorflow and deep learning - without a PhD by Martin Görner"
    link: "https://www.youtube.com/watch?v=vq2nnJ4g6N0&t=663s"
  - name: "Kolmogorov, A. N. (1957). On the Representation of Continuous Functions of Several Variables by Superposition of Continuous Functions of one Variable and Addition, Doklady Akademii. Nauk USSR, 114, 679-681."
  - name: "Maxwell Stinchcombe, Halbert White (1989). Multilayer feedforward networks are universal approximators. Neural Networks, Vol 2, 5, 359-366."
    link: "http://www.sciencedirect.com/science/article/pii/0893608089900208"
  - name: "Performance Analysis of Various Activation Functions in Generalized MLP Architectures of Neural Networks"
    link: "http://www.cscjournals.org/manuscript/Journals/IJAE/volume1/Issue4/IJAE-26.pdf"
  - name: "Lippe P. Tutorial 3: Activation Functions — UvA DL Notebooks v1.1 documentation. In: UvA Deep Learning Tutorials [Internet]. [cited 23 Sep 2021]. Available: https://uvadlc-notebooks.readthedocs.io"
    link: "https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial3/Activation_Functions.html"
    key: "Lippe"
weight: 1
---

Artificial neural networks works pretty well for solving some differential equations.

## Universal Approximators

Maxwell Stinchcombe and Halber White proved that no theoretical constraints for the feedforward networks to approximate any measurable function. In principle, one can use feedforward networks to approximate measurable functions to any accuracy.

However, the convergence slows down if we have a lot of hidden units. There is a balance between accuracy and convergence rate. More hidden units lead to slow convergence but more accuracy.

Here is a quick review of the history of this topic.

{{< message title="Kolmogorov's Theorem" class="info" >}}

Kolmogorov's theorem shows that one can use a finite number of carefully chosen continuous functions to mix up by sums and multiplication with weights to a continuous multivariable function on a compact set.

[Here is the exact math.](http://neuron.eng.wayne.edu/tarek/MITbook/chap2/2_3.html)
{{< /message >}}


1. Cybenko 1989

   Cybenko proved that

   $$
   \sum_k v_k \sigma(w_k x + u_k)
   $$

   is a good approximation of continuous functions because it is dense in continuous function space. In this result, $\sigma$ is a continuous sigmoidal function and the parameters are real.


2. Hornik 1989

   "Single hidden layer feedforward networks can approximate any measurable functions arbitrarily well regardless of the activation function, the dimension of the input and the input space environment."

   Reference: http://deeplearning.cs.cmu.edu/notes/Sonia_Hornik.pdf



{{< message title="Dense" class="info" >}}

Set A is dense in set X means that we can use A to arbitarily approximate X. Mathematically for any given element in X, the neighbour of x always has nonzero intersection.
{{< /message >}}

{{< message title="Measurable Function" class="info" >}}

It means the function is continuous.

{{< /message >}}



## Activation Functions


There are many activation functions.

- {{< c "cards/machine-learning/neural-networks/activation-uni-polar-sigmoid.md" "Uni-Polar Sigmoid Function" >}}
- {{< c "cards/machine-learning/neural-networks/activation-bi-polar-sigmoid.md" "Bipolar Sigmoid Function" >}}
- {{< c "cards/machine-learning/neural-networks/activation-hyperbolic-tangent.md" "Hyperbolic Tangent" >}}
- {{< c "cards/machine-learning/neural-networks/activation-radial-basis-function.md" "Radial Basis Function" >}}
- {{< c "cards/machine-learning/neural-networks/activation-conic-section-function.md" "Conic Section Function" >}}
- {{< c "cards/machine-learning/neural-networks/activation-relu.md" "ReLu" >}}
- {{< c "cards/machine-learning/neural-networks/activation-leaky-relu.md" "Leaky ReLu" >}}
- {{< c "cards/machine-learning/neural-networks/activation-elu.md" "ELU" >}}
- {{< c "cards/machine-learning/neural-networks/activation-swish.md" "Swish" >}}



{{< figure src="../assets/artificial-neural-networks/tutorial_notebooks_tutorial3_Activation_Functions_19_0.svg" caption="[Lippe P. Tutorial 3: Activation Functions — UvA DL Notebooks v1.1 documentation. In: UvA Deep Learning Tutorials [Internet]](https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial3/Activation_Functions.html)." >}}


## Solving Differential Equations


The problem here to solve is

$$
\frac{d}{dt}y(t)= - y(t),
$$

with initial condition $y(0)=1$.

To construct a single layered neural network, the function is decomposed using

{{< m >}}
\begin{align}
y(t_i) & = y(t_0) + t_i v_k f(t_i w_k+u_k) \\
 &= 1+t_i v_k f(t_i w_k+u_k) ,
\end{align}
{{</m>}}

where $y(t_0)$ is the initial condition and $k$ is summed over.



Presumably this should be the gate controlling trigering of the neuron or not. Therefore the following expit function serves this purpose well,

$$
f(x) = \frac{1}{1+\exp(-x)}.
$$

One important reason for choosing this is that a lot of expressions can be calculated analytically and easily.


{{< message title="Fermi-Dirac Distribution" >}}

Aha, the Fermi-Dirac distribution.
{{< /message >}}



With the form of the function to be solved, we can define a cost


$$
I=\sum_i\left( \frac{dy}{dt}(t_i)+y(t_i) \right)^2,
$$

which should be minimized to 0 if our structure of networks is optimized for this problem.

Now the task becomes clear:

1. Write down the cost analytically;
2. Minimized cost to find structure;
3. Substitute back to the function and we are done.



## Overfitting

It is possible that we could over fit a network so that it works only for the training data. To avoid that, people use several strategies.

1. Split data into two parts, one for training and one for testing. [A youtube video](https://www.youtube.com/watch?v=S4ZUwgesjS8)
2. Throw more data in. At least 10 times as many as examples as the DoFs of the model.  [A youtube video](https://www.youtube.com/watch?v=S4ZUwgesjS8)
3. Regularization by plugin a artificial term to the cost function, as an example we could add the . [A youtube video](https://www.youtube.com/watch?v=S4ZUwgesjS8)


## Neural Network and Finite Element Method


We consider the solution to a differential equation

$$
\mathcal L \psi - f = 0.
$$

Neural network is quite similar to finite element method. In terms of finite element method, we can write down a neural network structured form of a function [^Freitag2007]

$$
\psi(x_i) = A(x_i) + F(x_i, \mathcal N_i),
$$

where $\mathcal N$ is the neural network structure. Specifically,

$$
\mathcal N_i = \sigma( w_{ij} x_j + u_i ).
$$


The function is parameterized using the network. Such parameterization is similar to collocation method in finite element method, where multiple basis is used for each location.


One of the choices of the function $F$ is a linear combination,

$$
F(x_i, \mathcal N_i) = x_i \mathcal N_i,
$$

and $A(x_i)$ should take care of the boundary condition.

{{< message title="Relation to finite element method" >}}

This function is similar to the finite element function basis approximation. The goal in finite element method is to find the coefficients of each basis functions to achieve a good approximation. In ANN method, each sigmoid is the analogy to the basis functions, where we are looking for both the coefficients of sigmoids and the parameters of them. These sigmoid functions are some kind of adaptive basis functions.
{{</message>}}


With such parameterization, the differential equation itself is parameterized such that

$$
\mathcal L \psi - f = 0,
$$

such that the minimization should be

$$
\lvert \mathcal L \psi - f \rvert^2 \to 0
$$

at each point.


[^Freitag2007]: Freitag, K. J. (2007). Neural networks and differential equations.

