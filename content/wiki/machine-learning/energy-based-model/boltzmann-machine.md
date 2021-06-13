---
title: "Boltzmann Machine"
description: "Boltzmann machine is much like a spin glass model in physics. In short words, Boltzmann machine is a machine that has nodes that can take values, and the nodes are connected through some weight. It is just like any other neual nets but with complications and theoretical implications."
date: 2017-08-27
category:
  - 'Energy-based Model'
tags:
  - 'Machine Learning'
  - 'Artificial Neural Networks'
  - 'Basics'
references:
  - name: "Mehta P, Bukov M, Wang C-HH, Day AGRR, Richardson C, Fisher CK, et al. A high-bias, low-variance introduction to Machine Learning for physicists. Phys Rep. 2018;810: 122. doi:10.1016/j.physrep.2019.03.001"
    link: "https://arxiv.org/abs/1803.08823"
  - name: "Hinton GE. Boltzmann Machines. 2007."
    link: "https://www.cs.toronto.edu/~hinton/csc321/readings/boltz321.pdf"
links:
  - "cards/statistics/likelihood.md"
  - "wiki/machine-learning/energy-based-model/restricted-boltzmann-machine.md"
  - "wiki/machine-learning/energy-based-model/maxent-energy-based-model.md"
weight: 3
---

Boltzmann machine is much like a spin glass model in physics. In short words, Boltzmann machine is a machine that has nodes that can take values, and the nodes are connected through some weight. It is just like any other neural nets but with complications and theoretical implications.

Boltzmann machine is usually used as a generative model.


## Boltzmann Machine and Physics

To obtain a good understanding of Boltzmann machine for a physicist, we begin with Ising model. We construct a system of neurons $\{ s_i\}$ which can take values of 1 or -1, where each pair of them $s_i$ and $s_j$ is connected by weight $J_{ij}$.

This is described as a Boltzmann machine, or spin glass in physics. Spin glass is a type of material that is a composite of many spins pointing in different directions. In principle, spin glass is hard to calculate.

Nevertheless we can make simplifications to this model. We require each spin to be connected to its nearest neighbours only. Such a model is called Ising model.

Intuitively, those spins can be viewed as tiny magnets that can point up or down only. Each spin interacts with its neighbours. These interactions are calculated in terms of energy,

$$
\begin{equation}
   E = -\sum_{i,j} J_{ij} s_i s_j.
\end{equation}
$$

Why do we care about energy? For a physics system, low energy means stable while high energy means unstable since it might automatically change its configuration into the low energy state. That being said, a system of spins is stable if the energy of all the interactions is low.

To find out a low energy state, one of the numerical methods is the Monte Carlo method.


{{< message title="States" class="info">}}

We have been talking about the word state without being specifying the definition of it. In fact we can think of two different pictures of states. For the purpose of this discussion, we consider a system of $N$ particles and each of the particle has $m$ degrees of freedom.

The first strategy is to set up a $N\times m$ dimension space and describe the state of the whole system with on point in such a space. The distribution of the points can be determined by the corresponding categories of distribution functions. This is dubbed as $\Gamma$ space.

The second strategy is to use a space of $m$ dimensions where each particle of the system is a point in such a space. Such a space is called $\mu$ space. In $\mu$ space, the distribution of each particle state is calculated using BBGKY chain.


Once the macroscopic properties of the system is assigned, all possible states that lead to this macroscopic state show up with equal probability, aka, the principle of **equal a priori probabilities**.

{{< /message >}}


{{< message title="Partition Function" class="info">}}


   Partition function $Z$ is useful as we calculate the statistical properties of the network,

   \begin{equation}
      Z = \sum e^{-E}.
    \end{equation}

   With partition function defined, the distribution of states is

   \begin{equation}
      P = \frac{1}{Z} e^{-E}
    \end{equation}
{{< /message >}}


## Application of Boltzmann in Learning


In many cases, we would like the machine to learn about the pattern of input. Probabilistically speaking, we are working out the probability distribution of the input data using a Boltzmann machine,

\begin{equation}
   \Delta p =  p_{\mathrm{Model}} - p_{\mathrm{Data}}.
\end{equation}

Or for reasons of log-likelihood, we use the ration of them

\begin{equation}
   \Delta \log p =   \log p_{\mathrm{Model}} - \log p_{\mathrm{Data}}.
\end{equation}

In terms of Boltzmann machine weights, which are to be determined, the log probability is proportional to the energy

\begin{equation}
   \Delta \log p \sim \sum_{ij} w_{ij} s_i s_j \vert_{\mathrm{Model}}  -    \sum_{ij} w_{ij} s_i s_j \vert_{\mathrm{Data}}.
\end{equation}

Since we are looking for the weights, the updating rule should be equivalent to the gradient

\begin{equation}
   \frac{ \partial \Delta \log p }{ \partial w_{ij} } \sim  \langle s_i s_j\rangle_{\mathrm{data}} - \langle s_i s_j \rangle_{\mathrm{model}},
\end{equation}

We could update our weights using a rule compatible with the gradient of the probability.

\begin{equation}
   \Delta w_{ij} \sim \langle s_i s_j\rangle_{\mathrm{data}} - \langle s_i s_j \rangle_{\mathrm{model}}.
   \label{eq-weight-update-rule-boltzmann-machine}
\end{equation}

It's easily noticed that the first term is basically Hebbian learning rule, where similar activities enhance the weight. The second term is the some unlearning rule where we have to reduce some weights to relax to the actual working network. Simply put, we kill some connections that have negative effects on our learning network.




### Without Hidden Units

In principle, a learning process can be as simple as a one on one map from the data to all the neurons in Boltzmann machine.

Suppose we have a data set of an image with 10 pixels and each pixel can take values of 0 and 1. We simply construct a network of 10 neurons. To remember the most prominent features of the image with this network, we update the weights and bias of the network to miminize the energy. Once done with minimization, the network we have could be used to generate similar images with similar features.




### With Hidden Units

The complexity of the previous model seems to be low. To introduce more degrees of freedom, we introduce the hidden units.


Hinton and Sejnowski worked out an algorithm for Boltzmann machine in 1983. The energy-based learning rule for Boltzmann machine has two phases, the clamped phase (Phase+) and free phase (Phase-).

1. Clamped phase: we attach the data to the visible units and initialize the hidden units to be some random states.
  a. Then we update the hidden units so that the energy is minimized with clamping.
  b. We calculate the average $s_i s_j$ over all pairs of units, i.e., $\langle s_i s_j\rangle_{\mathrm{data}}$.
  c. Repeat for all data sets of training.
2. Free phase: no clamping and all units are the same and mutatable.
  a. Relax the state of the units to low energy state.
  b. Find out $\langle s_i s_j\rangle_{\mathrm{model}}$.
  c. Repeat N times.


With $\langle s_i s_j\rangle_{\mathrm{data}}$ and $\langle s_i s_j\rangle_{\mathrm{model}}$ found, we use the update rule \ref{eq-weight-update-rule-boltzmann-machine}.


For some reference, Hinton has a set of lectures on [Coursera](https://www.coursera.org/learn/neural-networks/lecture/iitiK/boltzmann-machine-learning-12-min). He also has a lecture for more effective algorithms: [More efficient ways to get the statistics](https://www.coursera.org/learn/neural-networks/lecture/wlELo/optional-video-more-efficient-ways-to-get-the-statistics-15-mins).


## Minimizing Energy of Ising Model is Hebbian Learning


{{< message title="Hebbian Learning Rule" class="info">}}
Simply put, neurons act similarly at the same time would be more likely to be connected.
{{</message>}}

A energy minimization procedure would be the same as Hebbian learning rule. Suppose we pick out two spins, $s_3 = 1$ and $s_8= 1$, the connected weight would be positive in order to have lower energy $-J_{38}s_3 s_8 = - J_{38}$. For spins with different signs, negative weight would be the choice to make sure the energy is lower. This is similar to Hebbian learning rule.



### Programming

To code a Boltzmann machine, we need an algorithm.
