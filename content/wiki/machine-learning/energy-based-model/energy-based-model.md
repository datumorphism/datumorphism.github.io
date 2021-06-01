---
title: "MaxEnt Model"
description: "Maximum Entropy models makes least assumption about the data"
date: 2021-05-31
category:
  - 'Energy-based Model'
tags:
  - 'Neural Network'
references:
  - name: "Mehta P, Bukov M, Wang C-HH, Day AGRR, Richardson C, Fisher CK, et al. A high-bias, low-variance introduction to Machine Learning for physicists. Phys Rep. 2018;810: 122. doi:10.1016/j.physrep.2019.03.001"
    link: "https://arxiv.org/abs/1803.08823"
    key: "Mehta2018"
links:
  - "cards/information/coding-theory-concepts.md"
  - "cards/statistics/likelihood.md"
weight: 1
---

The Maximum Entropy model, aka MaxEnt model, is a fascinating generative model as it is based on a very intuitive idea from statistical physics - the Principle of Maximum Entropy.

## The Idea

The essence of the MaxEnt model is that the underlying probability distribution $p(x)$ of the random variables $x$ should

1. gives the whole system the **largest uncertainty**, while
2. producing **reasonable observables**.

### Uncertainty

The **uncertainty of the whole system** is described by the Shannon entropy based on the probability distributions $p(x)$,

{{<m>}}
S[p] = -\operatorname{Tr} p(x) \log p(x).
{{</m>}}

The {{< c "cards/information/coding-theory-concepts.md" "Shannon entropy" >}} is a functional of the distribution $p(x)$ and the trace $\operatorname{Tr}$ sums over all values of $x$.

### Observables

The **reasonable observables** are the measured by the average of a set of observable functions $\\{f_i\\}$.

The statistical measures of the observable functions from the model have to be the same as those from the data. For example, we make sure the average from the model to be the same as the average from the data,

{{<m>}}
\begin{equation}
\langle f_i \rangle_{\text{model}} = \langle f_i \rangle_{\text{data}}.
\label{eqn-constraint-model-avg-data-avg}
\end{equation}
{{</m>}}

The average of from the data $\langle f_i \rangle_{\text{data}}$ is straight forward. The average from the model $\langle f_i \rangle_{\text{model}}$ has the following form

{{<m>}}
\langle f_i \rangle_{\text{model}} = \int \mathrm \,dx' f(x') p(x').
{{</m>}}

### The Principle of Maximum Entropy

In this example, the Principle of Maximum Entropy is to maximize the Shannon entropy while maintaining equation $\ref{eqn-constraint-model-avg-data-avg}$, i.e.,

{{< m >}}
\begin{align}
\hat{p}=&\operatorname{argmax}_p{S[p]}, \\
&\text{subject to } \langle f_i \rangle_{\text{model}} - \langle f_i \rangle_{\text{data}} \lt \Lambda_i \\
&\text{and } \int \mathrm\,dx p(x) - 1 \lt \Gamma.
\end{align}
{{</m>}}


Using Lagrange multiplers, we can reformulate it into

{{< m >}}
\begin{align}
\hat{p}=\operatorname{argmin}_p{\mathscr L[p]}
\end{align}
{{</m>}}

where

{{<m>}}
\mathscr L[p] = S[p] + \sum_i\lambda_i\left( \langle f_i \rangle_{\text{model}} - \langle f_i \rangle_{\text{data}} \right) + \gamma \left( \int \mathrm\,dx p(x) - 1 \right).
{{</m>}}

Perform variations on $\mathscr L[p]$, we find that the underlying probability density have to carry the form

{{<m>}}
p(x) \propto \exp\left( \sum_i \lambda_i f_i(x)\right).
{{</m>}}

Introduce the partition function

{{<m>}}
Z=\int \mathrm d x \exp\left( \sum_i \lambda_i f_i(x)\right),
{{</m>}}

the general form of the underlying distribution is

{{<m>}}
p(x) = \frac{\exp\left( \sum_i \lambda_i f_i(x)\right)}{Z}.
{{</m>}}

This is the Boltzmann distribution with energy function

{{<m>}}
E(x) = - \sum_i \lambda_i f_i(x).
{{</m>}}


## Observables of Data

In physics, the observables are easy to come up with as there are "physical properties", e.g., pressure, that we can measure. These "physical properties" are nothing but "statistical properties" from a theoretical point of view.

In data, the convenient "statistical properties" are the moments of the data distribution. For example, the first two moments are $x_i$ and $x_i x_j$. If we require that the model gives the same first two moments are the observation from the data,

{{<m>}}
\begin{align}
\langle x_i \rangle_{\text{model}} &= \langle x_i \rangle_{\text{data}}\\
\langle x_i x_j \rangle_{\text{model}} &= \langle x_i x_j \rangle_{\text{data}}.
\end{align}
{{</m>}}

This constraint leads to the famous Ising model where the energy function is

{{<m>}}
E(x) = - \sum_i h_i x_i - \frac{1}{2} \sum_{ij} J_{ij} x_i x_j.
{{</m>}}


## Training

Training the MaxEnt model is very different from the backprop neural networks.

### Log-Likelihood as the Cost Function

As usual, we will maximize the log-likelihood of the given dataset. For our MaxEnt model, the log-likelihood is [^Mehta2018]

{{<m>}}
\begin{align}
\mathcal L(\{\theta_i\}) =& \langle \log p_{\{\theta_i\}} (x) \rangle_{\text{data}} \\
=& \langle  \log \frac{\exp{\left(-E_{\{\theta_i\}}(x)\right)}}{Z_{\{\theta_i\}}}  \rangle_{\text{data}} \nonumber \\
=& - \langle  E_{\{\theta_i\}}(x) \rangle_{\text{data}} - \langle  \log Z_{\{\theta_i\}} \rangle_{\text{data}}.
\end{align}
{{</m>}}

{{< message class="info" title="What are the model parameters?" >}}

The model parameters mentioned in the log-likelihood, $\\{\theta_i\\}$, refers to the parameters in the energy function, if we have one.

If we do not have an explicit formula of the energy function, but using some kind of universal approximator to represent a generic energy function, the model parameters will be the parameters of the universal approximator.

{{< /message >}}


### Gradient of Log-likelihood

The gradient of the log-likelihood has a beautiful form [^Mehta2018]

{{<m>}}
\partial_{\theta_i} \mathcal L(\{\theta_i\}) = \langle \partial_{\theta_i} E_{\{\theta_i\}}(x) \rangle_{\text{model}} - \langle \partial_{\theta_i} E_{\{\theta_i\}}(x) \rangle_{\text{data}},
{{</m>}}

where the gradient of the energy function is denoted as $O_i$,

{{<m>}}
O_i(x) = \partial_{\theta_i} E_{\{\theta_i\}}(x).
{{</m>}}


The gradient of the log-likelihood is the difference between the gradient of the energy function averaged on the model $\langle O_i(x) \rangle_{\text{model}}$ and that averaged on the data $\langle O_i(x) \rangle_{\text{data}}$.

{{< message title="Gradient of Energy Function Averaged on the Model" >}}

It has a simple form

$$
\begin{equation}
\langle O_i(x) \rangle_{\text{model}} = -\partial_{\theta_i} \log Z_{\\{\theta_i\\}}
\end{equation}
$$

{{< /message >}}

In this MLE approach, we will adjust the model parameters $\\{\theta_i\\}$ so that the average of the gradient of the energy function will vanish when calculated on data and model.

{{< message title="How to Tune the Model" >}}

If the gradient of the energy function average on the model is larger, i.e.,  $\langle O_i(x) \rangle_{\text{model}} - \langle O_i(x) \rangle_{\text{data}}>0$, we need to tune the model parameters so that the the energy function becomes smoother on the model than that on the data.

{{< /message >}}


[^Mehta2018]: {{< cite key="Mehta2018" >}}