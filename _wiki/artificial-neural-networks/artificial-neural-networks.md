---
title: "Artificial Neural Networks"
excerpt: "Solving PDEs"
date: 2018-11-19
toc: true
category:
- 'Artificial Neural Networks'
tag:
- 'Machine Learning'
- 'Artificial Neural Networks'
- 'Basics'
references:
- name: ""
  title: ''
notify: 'Machine Learning!'
weight: 1
---




Artificial neural networks works pretty well for some equation solving.



## Universal Approximators


Mawell Stinchcombe and Halber White proved that no theoretical constraints for the feedforward networks to approximate any measureable function. In principle one can use feedforward networks to approximate measurable functions to any accuracy.

However the convergence slows done if we have a lot of hidden units. There is a balance between accuracy and convergence rate. More hidden units means slow convergence but more accuracy.


Here is a quick review of the history of this topic.

<div class="notes--info" markdown="1">
**Kolmogorov's Theorem**

Kolmogorov's theorem shows that one can use finite number of carefully chosen continuous functions to exactly mix up by sums and multiplication with weights to a continuous multivariable fnction on a copact set.

[Here is the exact math.](http://neuron.eng.wayne.edu/tarek/MITbook/chap2/2_3.html)
</div>


1. Cybenko 1989

   Cybenko proved that

   $$
   \sum_k v_k \sigma(w_k x + u_k)
   $$

   is a good approximation of continuous functions because it is dense in continous function space. In this result, $\sigma$ is a continuous sigmoidal function and the parameters are real.


2. Hornik 1989

   "Single hidden layer feedforward networks can approximate any measurable functions arbitrarily well regardless of the activation function, the dimension of the input and the input space environment."
   
   Reference: http://deeplearning.cs.cmu.edu/notes/Sonia_Hornik.pdf



<div class="notes--info" markdown="1">
**Dense**

Set A is dense in set X means that we can use A to arbitarily approximate X. Mathematically for any given element in X, the neighbour of x always has nonzero intersection.
</div>

<div class="notes--info" markdown="1">
**Measurable Function**

Basically it means continuous.
</div>






## Activation Functions


1. Uni-Polar Sigmoid Function

   $$
   \frac{1}{1+e^{-x}}
   $$


   <figure markdown="1">
   ![](../assets/artificial-neural-networks/sigmoidFunction.png)
   <figcaption markdown="1">
   Sigmoid function
   </figcaption>
   </figure>


2. Bipolar Sigmoid Function

   $$
   \frac{1-e^{-x}}{1+e^{-x}}
   $$

   <figure markdown="1">
   ![](../assets/artificial-neural-networks/bipolarSigmoid.png)
   <figcaption markdown="1">
   Bipolar Sigmoid
   </figcaption>
   </figure>


3. Hyperbolic Tangent

   $$
   \tanh(x) = \frac{\sinh(x)}{\cosh(x)} = \frac{e^{x} - e^{-x}}{e^x + e^{-x}}
   $$
   
   <figure markdown="1">
   ![](../assets/artificial-neural-networks/tanh.png)
   <figcaption markdown="1">
   Hyperbolic tangent
   </figcaption>
   </figure>



4. Radial Basis Function

   <figure markdown="1">
   ![](../assets/artificial-neural-networks/unnormalized_radial_basis_functions.svg.png)
   <figcaption markdown="1">
   Two unnormalized Gaussian radial basis functions in one input dimension. The basis function centers are located at x1=0.75 and x2=3.25. Source [Unnormalized Radial Basis Functions](https://en.wikipedia.org/wiki/Radial_basis_function#/media/File:Unnormalized_radial_basis_functions.svg)
   </figcaption>
   </figure>



5. Conic Section Function





## Solving Differential Equations


The problem here to solve is

$$
\frac{d}{dt}y(t)= - y(t),
$$

with initial condition $y(0)=1$.

To construct a single layered neural network, the function is decomposed using

$$
\begin{align}
y(t_i) & = y(t_0) + t_i v_k f(t_i w_k+u_k) \\
 &= 1+t_i v_k f(t_i w_k+u_k) ,
\end{align}
$$

where $y(t_0)$ is the initial condition and $k$ is summed over.

<div class="notes--info" markdown="1">
**Articifial Neural Network**


</div>



Presumably this should be the gate controlling trigering of the neuron or not. Therefore the following expit function serves this purpose well,

$$
f(x) = \frac{1}{1+\exp(-x)}.
$$

One important reason for chosing this is that a lot of expressions can be calculated analytically and easily.


<div class="notes--info" markdown="1">
**Fermi-Dirac Distribution**


   Aha, the Fermi-Dirac distribution.
</div>



With the form of the function to be solved, we can define a cost


$$
I=\sum_i\left( \frac{dy}{dt}(t_i)+y(t_i) \right)^2,
$$

which should be minimized to 0 if our struture of networks is optimized for this problem.

Now the task becomes clear:

1. Write down the cost analytically;
2. Minimized cost to find structure;
3. Substitute back to the function and we are done.







## Overfitting



It is possible that we could over fit a network so that it works only for the training data. To avoid that, people use several strategies.

1. Split data into two parts, one for training and one for testing. [A youtube video](https://www.youtube.com/watch?v=S4ZUwgesjS8)
2. Throw more data in. At least 10 times as many as examples as the DoFs of the model.  [A youtube video](https://www.youtube.com/watch?v=S4ZUwgesjS8)
3. Regularization by plugin a artifical term to the cost function, as an example we could add the . [A youtube video](https://www.youtube.com/watch?v=S4ZUwgesjS8)


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


One of the choice of the function $F$ is a linear combination,

$$
F(x_i, \mathcal N_i) = x_i \mathcal N_i,
$$

and $A(x_i)$ should take care of the boundary condition.

<div class="notes--info" markdown="1">
**Relation to finite element method**

   This function is similar to the finite element function basis approximation. The goal in finite element method is to find the coefficients of each basis functions to achieve a good approximation. In ANN method, each sigmoid is the analogy to the basis functions, where we are looking for both the coefficients of sigmoids and the parameters of them. These sigmoid functions are some kind of adaptive basis functions.
</div>


With such parameterization, the differential equation itself is parameterized such that

$$
\mathcal L \psi - f = 0,
$$

such that the minimization should be

$$
\lvert \mathcal L \psi - f \rvert^2 \to 0
$$

at each point.









## References and Notes

[^Freitag2007]: Freitag, K. J. (2007). Neural networks and differential equations.

1. [Tensorflow and deep learning - without a PhD by Martin Görner](https://www.youtube.com/watch?v=vq2nnJ4g6N0&t=663s).
1. Kolmogorov, A. N. (1957). "On the Representation of Continuous Functions of Several Variables by Superposition of Continuous Functions of one Variable and Addition," Doklady Akademii. Nauk USSR, 114, 679-681.
2. Maxwell Stinchcombe, Halbert White (1989). ["Multilayer feedforward networks are universal approximators"](http://www.sciencedirect.com/science/article/pii/0893608089900208). Neural Networks, Vol 2, 5, 359-366.
1. [Performance Analysis of Various Activation Functions in Generalized MLP Architectures of Neural Networks](http://www.cscjournals.org/manuscript/Journals/IJAE/volume1/Issue4/IJAE-26.pdf)

