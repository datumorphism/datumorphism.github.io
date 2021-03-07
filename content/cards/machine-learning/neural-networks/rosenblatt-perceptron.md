---
title: "Rosenblatt's Perceptron"
description: "Connected perceptrons"
date: "2021-02-25"
authors:
  - "LM"
categories:
  - "Machine Learning"
tags:
  - "Artificial Neuron"
  - "Neural Network"
  - "Perceptron"
  - "Basics"
references:
  - name: "Vladimir N. Vapnik. 2000. The Nature of Statistical Learning Theory."
    link: "https://doi.org/10.1007/978-1-4757-3264-1"
  - name: "Novikoff, Albert B. 1963. On Convergence Proofs for Perceptrons. STANFORD RESEARCH INST MENLO PARK CA."
    link: "http://classes.engr.oregonstate.edu/eecs/fall2017/cs534/extra/novikoff-1963.pdf."
weight:
links:
  - "wiki/machine-learning/neural-networks/artificial-neural-networks.md"
  - "cards/machine-learning/neural-networks/mcculloch-pitts-model.md"
---

Rosenblatt's perceptron connects McCulloch-Pitts neurons in levels.

{{< figure src="../assets/rosenblatt-perceptron/rosenblatt-perceptrons.png" >}}

Rosenblatt proposed that we fix all the weights and leave the weights of the last neuron free.

The first few layers but the last layer is used as a transformation of the input data $\{x_1, \cdots, x_i, \cdots, x_N\}$ into a new space $\{z_1, \cdots, z_i, \cdots, z_{N'}\}$. The classification is done on the $\{z_1, \cdots, z_i, \cdots, z_{N'}\}$ space by tuning the last neuron.

Initially, we set $w=0$. At step $k$,
1. if the sign prediction by the perceptron $( w_k \cdot z_{k+1} )$ is the same as the data $y_{k+1}$, i.e., $y_{k+1} \cdot ( w_k \cdot z_{k+1} ) >0$, we keep the last neuron unchanged,
2. if the sign is different $y_{k+1} \cdot ( w_k \cdot z_{k+1} ) <0$, we change the slope to $w_{k+1} = w_k + y_{k+1}z_{k+1}$ because $y_{k+1} \cdot ( w_{k+1} \cdot z_{k+1} ) = y_{k+1} \cdot ( w_k \cdot z_{k+1} ) + y_{k+1}^2 z_{k+1}^2$. In this way we are making sure that $y_{k+1} \cdot ( w_{k+1} \cdot z_{k+1} )>y_{k+1} \cdot ( w_k \cdot z_{k+1} )$ so that we can match the predictions and the actual classification.
