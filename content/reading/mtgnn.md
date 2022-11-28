---
title:  "MTGNN"
date: 2022-11-28
modified: 2022-11-28
subtitle: "Temporal Convolution, Graph Representation Learning"
speaker: "L Ma"
authors:
  - L Ma
categories:
  - graph neural network
tags:
  - graph neural network
  - graph
  - forecasting
  - time series
summary: ""
status: Done
references:
  - name: "Wu Z, Pan S, Long G, Jiang J, Chang X, Zhang C. Connecting the Dots: Multivariate Time Series Forecasting with Graph Neural Networks. arXiv [cs.LG]. 2020. Available: http://arxiv.org/abs/2005.11650"
    link: "http://arxiv.org/abs/2005.11650"
    key: "Wu2020"
  - name: "Lässig F. Temporal Convolutional Networks and Forecasting. In: Unit8 [Internet]. 6 Jul 2021 [cited 28 Nov 2022]. Available: https://unit8.com/resources/temporal-convolutional-networks-and-forecasting/"
    link: "https://unit8.com/resources/temporal-convolutional-networks-and-forecasting/"
    key: "Lässig2021"
notify: "This article lists some key ideas of the MTGNN paper."
garden:
  - "seedling"
---


## Key Components

### Time Convolution (TC) Module

{{< e "cards/forecasting/time-convolution.md" >}}


### Graph Convolution Module


{{< e "cards/forecasting/gnn-mix-hop-propagation.md" >}}


### Graph Structure Learning Layer

{{< e "cards/forecasting/gnn-graph-structure-learning.md" >}}


## Architecture

{{< figure src="../assets/mtgnn/mtgnn-architecture.png" caption="Wu et al., 2020" >}}


[^Wu2020]: {{< cite key="Wu2020" >}}
[^Lässig2021]: {{< cite key="Lässig2021" >}}