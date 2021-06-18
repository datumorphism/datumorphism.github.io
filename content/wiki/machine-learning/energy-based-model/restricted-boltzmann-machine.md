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
  - name: "Contributors to Wikimedia projects. Cumulant. In: Wikipedia [Internet]. 7 May 2021 [cited 18 Jun 2021]. Available: https://en.wikipedia.org/wiki/Cumulant"
    link: "https://en.wikipedia.org/wiki/Cumulant"
    key: "Cumulant"
links:
  - "cards/information/coding-theory-concepts.md"
  - "cards/statistics/likelihood.md"
  - "wiki/machine-learning/energy-based-model/boltzmann-machine.md"
  - "wiki/machine-learning/energy-based-model/maxent-energy-based-model.md"
  - "cards/math/cholesky-decomposition.md"
  - "cards/math/hubbard-stratonovich-identity.md"
notify: "This article uses Mehta2018 extensively."
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

## Latent Variables: From Energy Function to Distribution

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
\tilde E(x, h) = -\sum_i a_i(x_i) - \sum_k b_k(h_k) - \sum_{ik} x_i W_{ik} h_k.
{{< /m >}}

Usually, we use the form

{{< m >}}
\begin{equation}
\tilde E(x, h) = -\sum_i a_i x_i - \sum_k b_k h_k - \sum_{ik} x_i W_{ik} h_k,
\label{eqn-energy-function-with-latent-variables}
\end{equation}
{{< /m >}}

with the nodes can only be 0 or 1. The visible layer and hidden layer are called Bernoulli as they have binary states.


## Latent Variables: From Distribution to Energy Function

We can also derive the energy function for distributions of the form $\eqref{eqn-energy-function-with-latent-variables}$. For easier understanding, we define a new joint distribution $p(x, h)$ from

{{< m >}}
p(x, h) =  \frac{\exp{\left( -\tilde E(x, h) \right)}}{Z},
{{< /m >}}

so that

{{< m >}}
p(x) = \int \mathrm d h\, p(x, h) = \frac{ \exp{\left( -E(x) \right)} }{Z}.
{{< /m >}}

Using the above two definitions, we have

{{< m >}}
\exp{\left(-E(x)\right)} = \int \mathrm d h \, \exp{\left( -\tilde E(x, h) \right)},
{{< /m >}}

from which we derive a formalism for the marginalized energy function

{{< m >}}
\begin{align}
E(x) =& - \ln \int \mathrm d h \, \exp{\left( -\tilde E(x, h) \right)} \\
=& \sum_i a_i(x_i) - \sum_k \ln \int \mathrm d h_k \, \exp{\left( b_k(h_k) \right)} \exp{\left( \sum_j x_j W_{jk}h_k \right)}.
\label{eqn-e-x}
\end{align}
{{< /m >}}

This energy function can be expanded using the cumulant[^Cumulant], we can decompose the energy function $E(x)$, equation $\eqref{eqn-e-x}$,

{{< m >}}
E(x) = -\sum_i a_i(x_i) - \sum_i \sum_k \kappa^{(1)}_k W_{ik} x_i - \frac{1}{2}\sum_{ij} \left( \sum_{k} \kappa^{(2)}_k W_{ik} W_{jk} \right) x_i x_j + \cdots
{{< /m >}}

where $\kappa^{(\cdot)}$ are coefficients related to the cummulant[^Mehta2018]. We can find any order of correlations even without in-group connections between the visible nodes.


{{< message title="Expansion of the Energy Function" class="info" >}}

The integral in our energy function,

$$
\sum_k \ln \int \mathrm d h_k \, \exp{\left( b_k(h_k) \right)} \exp{\left( \sum_j x_j W_{jk}h_k \right)}
$$

is similar to the cumulant generating function

$$
\ln \int \mathrm d h q(h) e^{ht}  = K(t) = \sum_{n=1}^\infty \kappa^{(n)} \frac{t^n}{n!},
$$

with $\kappa^{(n)}=\partial^n_t K(t=0)$. This is a Taylor expansion around $t=0$.

To perform the expansion, we define a new quantity $q_k(h_k) = e^{b_k(h_k)}/Z$ so that

$$
\sum_k \ln \int \mathrm d h_k \exp{\left( b_k(h_k) \right)} \exp{\left( \sum_j x_j W_{jk}h_k \right)} = \sum_k \ln \int \mathrm d h_k  Z q_k(h_k) e^{t h_k },
$$

with $t=\sum_j x_j W_{jk}$.


{{< /message >}}


## Gradient of Log-likelihood

In this section, we will focus on Bernoulli layers, i.e., $a_i(x_i) = a^0_i x_i$ and $b_k(h_k) = b^0_k h_k$

Using the results from {{< c "wiki/machine-learning/energy-based-model/maxent-energy-based-model.md" "MaxEnt model" >}}, we can find the gradient of the log-likelihood $\mathcal L(W_{ik}, a_i, b_k)$,

{{< m >}}
\begin{align}
\partial_{W_{ik}} \mathcal L =& \langle x_i h_k \rangle_{\text{model}} - \langle x_i h_k \rangle_{\text{data}} \\
\partial_{a^0_i} \mathcal L =& \langle x_i \rangle_{\text{model}} - \langle x_i \rangle_{\text{data}} \\
\partial_{b^0_k} \mathcal L =& \langle  h_k \rangle_{\text{model}} - \langle h_k \rangle_{\text{data}}.
\end{align}
{{< /m >}}

The calculation of $\langle \cdot \rangle_{\text{model}}$ is easier in RBM.

For first order Markov chains, the visible units do not depend on themselves as there are not direct connections between the visible units. So are the hidden units. That being said, we have $p(x\mid h)$ and $p(h\mid x)$.

In this simple situation, the distributions can be sampled using Gibbs sampling. To calculate $p(h\mid x)$, we will clamp our visible units to the data values then infer $h$ which will be used to infer $x$ based on $p(x\mid h)$. Iterate this process we will be able to sample the model, i.e.,

{{< m >}}
\begin{align}
& p(h\mid x_0) \to h_0 \\
\Rightarrow & p(x\mid h_0) \to x_1 \\
\Rightarrow & p(h\mid x_1) \to h_1 \\
\Rightarrow & \cdots
\end{align}
{{< /m >}}





[^Mehta2018]: {{< cite key="Mehta2018" >}}
[^Hubbard1959]: {{< cite key="Hubbard1959" >}}
[^Cumulant]: {{< cite key="Cumulant" >}}