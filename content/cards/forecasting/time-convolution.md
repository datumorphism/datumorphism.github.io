---
title: "Time Convolution"
description: "The temporal convolution is responsible for capturing temporal patterns in a sequence."
date: 2022-11-28
categories:
  - "Time Series"
tags:
  - "Time Series"
  - "Forecasting"
  - "Convolution Neural Network"
references:
  - name: "Wu Z, Pan S, Long G, Jiang J, Chang X, Zhang C. Connecting the Dots: Multivariate Time Series Forecasting with Graph Neural Networks. arXiv [cs.LG]. 2020. Available: http://arxiv.org/abs/2005.11650"
    link: "http://arxiv.org/abs/2005.11650"
    key: "Wu2020"
  - name: "Lässig F. Temporal Convolutional Networks and Forecasting. In: Unit8 [Internet]. 6 Jul 2021 [cited 28 Nov 2022]. Available: https://unit8.com/resources/temporal-convolutional-networks-and-forecasting/"
    link: "https://unit8.com/resources/temporal-convolutional-networks-and-forecasting/"
    key: "Lässig2021"
weight: 3
---

The temporal convolution is responsible for capturing temporal patterns in a sequence.


### Dilated Temporal Convolution

Unit8 has a [nice blog](https://unit8.com/resources/temporal-convolutional-networks-and-forecasting/) about temporal convolution and dilated temporal convolution[^Lässig2021]. In this

{{< e "cards/math/convolution-and-fourier-transform.md" >}}

{{< e "cards/math/convolution-dilated.md" >}}


### Inception

A good convolutional network should capture both short-term and long-term patterns in the time series data. However,

1. single large kernel is good for long-term pattern but not good at short-term pattern,
2. single small kernel is good for short-term pattern but not good at long-term pattern.

The **inception** strategy employs multiple dilated temporal convolution and the outputs are concatenated. By applying multiple such layers, we can extract patterns longer than any of the single dilated temporal convolutions[^Wu2020].

{{< m >}}
\operatorname{concat}( z\star f_2, z\star f_3, z\star f_6, z\star f_7).
{{< /m >}}


### Dilated Inception Layer

See Fig 5 in the paper[^Wu2020].


[^Wu2020]: {{< cite key="Wu2020" >}}
[^Lässig2021]: {{< cite key="Lässig2021" >}}