---
title: "Restricted Boltzmann Machine"
description: "Introducing latent variables to Boltzmann machine and restrict the connections within groups."
date: 2021-06-11
category:
  - "Energy-based Model"
tags:
  - "Neural Network"
  - "Energy-based Model"
  - "Entropy"
  - "Restricted Boltzmann Machine"
references:
  - name: "Mehta P, Bukov M, Wang C-HH, Day AGRR, Richardson C, Fisher CK, et al. A high-bias, low-variance introduction to Machine Learning for physicists. Phys Rep. 2018;810: 122. doi:10.1016/j.physrep.2019.03.001"
    link: "https://arxiv.org/abs/1803.08823"
    key: "Mehta2018"
  - name: "Hubbard J. Calculation of Partition Functions. Physical Review Letters. 1959. pp. 77–78. doi:10.1103/physrevlett.3.77"
    link: "http://dx.doi.org/10.1103/physrevlett.3.77"
    key: "Hubbard1959"
links:
  - "cards/information/coding-theory-concepts.md"
  - "cards/statistics/likelihood.md"
  - "wiki/machine-learning/energy-based-model/boltzmann-machine.md"
  - "wiki/machine-learning/energy-based-model/maxent-energy-based-model.md"
  - "cards/math/cholesky-decomposition.md"
  - "cards/math/hubbard-stratonovich-identity.md"
weight: 4
---

Latent variables introduce extra correlations between the nodes in a network. Introducing hidden units can also help us remove the direct connection between some nodes in a Boltzmann machine and create a restricted Boltzmann machine. A restricted Boltzmann machine requires less computation while having some expressing power.


{{< figure src="../assets/restricted-boltzmann-machine/illustration-hidden-unit.jpg" caption="Given Ising like interactions between the nodes, flipping node V1 is likely to also flip node V2 as they are connected through hidden unit H1. They are correlated. Removing the hidden unit leaves us two uncorrelated units." >}}


## The Ising Model

Given a Ising-like energy function (c.f. {{< c "wiki/machine-learning/energy-based-model/maxent-energy-based-model.md" >}})

{{< m >}}
E(x) = - \sum_i h_i x_i - \frac{1}{2} \sum_{ij} J_{ij} x_i x_j,
{{< /m >}}

The term $\sum_{ij} J_{ij} x_i x_j$ can be decomposed using the {{< c "cards/math/cholesky-decomposition.md" >}} Cholesky decomposition,

{{< m >}}
\sum_{ij} J_{ij} x_i x_j = \sum_{ijk} W_{ik} W_{kj}^T x_i x_j = \sum_{ijk} W_{ik} W_{jk} x_i x_j.
{{< /m >}}

The energy function can be rewritten as

{{< m >}}
E(x) = - \sum_i h_i x_i - \frac{1}{2} \sum_{ijk} W_{ik} W_{jk} x_i x_j.
{{< /m >}}

The distribution (derived using {{< c "wiki/machine-learning/energy-based-model/maxent-energy-based-model.md" "the Max Entropy principle" >}}) is

{{< m >}}
\begin{equation}
p(x) \propto \exp{ \left( \sum_i h_i x_i + \frac{1}{2} \sum_{ijk} W_{ik} W_{jk} x_i x_j \right)}
\label{eqn-boltzmann-dist-hopfield}
\end{equation}
{{< /m >}}

Using the {{< c "cards/math/hubbard-stratonovich-identity.md" "the Hubbard-Stratonovich Identity" >}}, we transform equation $\eqref{eqn-boltzmann-dist-hopfield}$ into[^Hubbard1959]

{{< m >}}
\begin{align}
p(x) \propto &  \exp{\left( \sum_i h_i x_i \right)} \exp{ \left(\frac{1}{2} \sum_{ijk} W_{ik} W_{jk} x_i x_j \right)} \\
\propto &  \exp{\left( \sum_i h_i x_i \right)} \frac{1}{\sqrt{2\pi}} \int \mathrm dh_k\, \exp{ \sum_k \left( -\frac{1}{2} h_k^2 + \sum_i x_i W_{ik} h_k \right)} \\
\propto & \frac{1}{\sqrt{2\pi}} \int \mathrm dh_k\, \exp{ \left[ \sum_i h_i x_i + \sum_k \left( -\frac{1}{2} h_k^2 + \sum_i x_i W_{ik} h_k \right) \right]}.
\end{align}
{{< /m >}}

Define a new energy function

{{< m >}}
\tilde E(x,h) = - \sum_i h_i x_i - \sum_k \left( -\frac{1}{2} h_k^2 + \sum_i x_i W_{ik} h_k \right) .
{{< /m >}}

The distribution becomes the marginalization of the hidden variable

{{< m >}}
\begin{equation}
p(x) \propto \int \mathrm dh\, \exp{ \left( -\tilde E(x,h)  \right) }.
\label{eqn-marginalization-new-energy-function}
\end{equation}
{{< /m >}}

Use the result $\eqref{eqn-marginalization-new-energy-function}$, we can define a model with two groups of nodes $x$ and $h$. The group $x$ has no internal connections, i.e., no high order correlations like $x^2$. The group of nodes $x$ is called visible layer while the hidden nodes $h$ are called hidden layer. In general, we require a form of energy

{{< m >}}
E(x, h) = -\sum_i a_i(x_i) - \sum_k b_k(h_k) - \sum_{ik} x_i W_{ik} h_k.
{{< /m >}}

Usually, we use the form

{{< m >}}
E(x, h) = -\sum_i a_i x_i - \sum_k b_k h_k - \sum_{ik} x_i W_{ik} h_k,
{{< /m >}}

with the nodes can only be 0 or 1. The visible layer and hidden layer are called Bernoulli as they have binary states.



[^Hubbard1959]: {{< cite key="Hubbard1959" >}}