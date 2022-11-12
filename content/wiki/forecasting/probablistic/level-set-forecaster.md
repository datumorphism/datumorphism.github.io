---
title: "Level Set Forecaster"
date: "2022-11-12"
categories:
  - "Time Series"
tags:
  - "Machine Learning"
  - "Time Series"
  - "Probabilistic"
references:
  - name: "Hasson H, Wang B, Januschowski T, Gasthaus J. Probabilistic forecasting: A level-set approach. Adv Neural Inf Process Syst. 2021;34: 6404–6416. Available: https://proceedings.neurips.cc/paper/2021/hash/32b127307a606effdcc8e51f60a45922-Abstract.html"
    link: "https://proceedings.neurips.cc/paper/2021/hash/32b127307a606effdcc8e51f60a45922-Abstract.html"
    key: "Hasson2021"
---


A level set forecaster converts point forecaster to probabilistic forecasters by constructing the {{< c "cards/math/level-set.md" "level set" >}} of the forecaster[^Hasson2021].


Given a point forecaster $f(x_1, \cdots, x_d)$ trained on dataset $\mathcal D = \{(\mathcal x_i, y_i)\}$, we collect the predictions and true values and build a map, $f(x_i) \to [y_{i_1}, y_{i_2}, \cdots, y_{i_m}]$.


## Example


We go through the algorithm in Hasson2021[^Hasson2021] using a small example.

In this small system, we have

1. a dataset {{< m >}} \mathcal D = \{ (x_1, y_1), (x_2, y_2), (x_3, y_3), (x_4, y_4), (x_5, y_5), (x_6, y_6) \},{{< /m >}}
2. a trained point forecaster $\hat y_i = f(x_i)$.


We collect the unique forecast from the model $f$, and build a list $[v_1, v_2, v_3, v_4]$ so that

1. $v_i \neq v_j$ for $i\neq j$, and
2. $v_1 \lt v_2 \lt v_3 \lt v_4$.


pred_to_bin

| key | value |
|:--:|:---:|
| v_1 |  f(x_2), f(x_6)  |
| v_2 | f(x_5) |
| v_3 | f(x_1) |
| v_4 | f(x_3), f(x_4) |


We loop through $[v_1, v_2, v_3, v_4]$, and build bins of the forecasts, with maximum bin size 3.

1. $v_1$:
   1. bin_1 = [f(x_2), f(x_6)]
2. $v_2$:
   1. update bin_1 = [f(x_2), f(x_6), f(x_5)]
3. $v_3$:
   1. bin_1 is full as it reached length 3,
   2. create a new bin: bin_2 = [f(x_1)]
4. $v_4$:
   1. bin_2 = [f(x_1), f(x_3), f(x_4)]

We have built a map

| key | bin |
|:----:|:----:|
| v_1 |  [(x_2, y_2), f(x_6), f(x_5)] |
| v_2 | [f(x_2), f(x_6), f(x_5)] |
| v_3 |  [f(x_1), f(x_3), f(x_4)] |
| v_4 | [f(x_1), f(x_3), f(x_4)] |




## Feature Space Partition







[^Hasson2021]: {{< cite key="Hasson2021" >}}