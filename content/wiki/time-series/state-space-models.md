---
title: "State Space Models"
description: "The state space model is an important category of models for sequential data such as time series"
date: 2022-02-27
authors:
  - "LM"
categories:
  - "Time Series"
tags:
  - "Machine Learning"
  - "Time Series"
  - "Sequential Data"
  - "HMM"
references:
  - name: "Christpher M. Bishop. Pattern Recognition and Machine Learning. Springer-Verlag New York; 2006."
    link: "https://link.springer.com/gp/book/9780387310732"
    key: "Bishop2006"
weight: 5
links:
  - "wiki/time-series"
  - "wiki/machine-learning/bayesian/latent-variable-models.md"
---

State space model is an important category of model for sequential data. Through simple assumptions, state space models can achieve quite complicated distributions.

To model a sequence, we can use the joint probability of all the nodes,

{{< m >}}
p(x_1, x_2, \cdots, x_N),
{{< /m >}}

where $x_i$ are the nodes in the sequence.


## Orders

We can introduce different order of dependencies on the past.

The simplest model for the sequence is assuming i.i.d..

{{< figure src="../assets/state-space-models/zero-order.jpg" title="Zeroth Order" caption="Each node is independent of each other" >}}

To model the dependencies in the sequence, we can assume a node depends on the previous nodes. The first-order model assume that node $x_{i+1}$ only depends on node $x_i$.

{{< figure src="../assets/state-space-models/first-order.jpg" title="First Order" caption="Each node depends on the previous node">}}

To add more complexities, we introduce the second order model.

{{< figure src="../assets/state-space-models/second-order.jpg" title="Second Order" caption="Each node depends on the previous two nodes" >}}

## Hidden States

For some quantities, such as the GMV of a company, we expect that the dynamics of them are driven by some other factors, which data we may not have.

We introduce a latent space $\\{z_i\\}$ which is described by first order process. The visible states $\\{x_i\\}$ are determined using $p(x_i\vert z_i)$ [^Bishop2006].

{{< figure src="../assets/state-space-models/with-hidden-states.jpg" title="With Hidden States" >}}



[^Bishop2006]: {{< cite key="Bishop2006" >}}