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

{{< message class="warning" >}}

This note is a more detailed version of Algorithm 1 in:

Hasson H, Wang B, Januschowski T, Gasthaus J. Probabilistic forecasting: A level-set approach. Adv Neural Inf Process Syst. 2021;34: 6404–6416. Available: [https://proceedings.neurips.cc/paper/2021/hash/32b127307a606effdcc8e51f60a45922-Abstract.html](https://proceedings.neurips.cc/paper/2021/hash/32b127307a606effdcc8e51f60a45922-Abstract.html).

It maybe hard to comprehend without reading the texts before Algorithm 1.

{{< /message >}}

A level set forecaster converts point forecaster to probabilistic forecasters by constructing the {{< c "cards/math/level-set.md" "level set" >}} of the forecaster[^Hasson2021].


Given a point forecaster $f(x_1, \cdots, x_d)$ trained on dataset $\mathcal D = \{(\mathcal x_i, y_i)\}$, we collect the predictions and true values and build a map, $f(x_i) \to [y_{i_1}, y_{i_2}, \cdots, y_{i_m}]$.


## Example

We go through the algorithm in Hasson2021[^Hasson2021] using a small example. To make it easier to understand, we slightly modify some of the steps.

In this small system, we have

1. a dataset {{< m >}} \mathcal D = \{ (x_1, y_1), (x_2, y_2), (x_3, y_3), (x_4, y_4), (x_5, y_5), (x_6, y_6) \},{{< /m >}}
2. a trained point forecaster $\hat y_i = f(x_i)$.

We collect the unique forecast from the model $f$, and build a list $[v_1, v_2, v_3, v_4]$ so that

1. $v_i \neq v_j$ for $i\neq j$, and
2. $v_1 \lt v_2 \lt v_3 \lt v_4$.

{{< message title="Examples of $v_i$" >}}

We assume a model $f$ that maps $x_2$ to $\hat y_2=f(x_2)$, and also $x_6$ to $\hat y_6=f(x_6)$.

If $\hat y_2 = \hat y_6$, we define $v_1 := \hat y_2 = \hat y_6$.

{{< /message >}}

We build a map for the unique forecast values that maps back to the data points.

| key | value |
|:--:|:---:|
| v_1 |  (x_2, y_2), (x_6, y_6)  |
| v_2 | (x_5, y_5) |
| v_3 | (x_1, y_1) |
| v_4 | (x_3, y_3), (x_4, y_4) |

We loop through $[v_1, v_2, v_3, v_4]$, and build bins of the forecasts, with maximum bin size 3.

1. $v_1$:
   1. create bin_1 as an empty list
   2. append the value we found in the above table to bin_1, we have bin_1 = [(x_2, y_2), (x_6, y_6)]
2. $v_2$:
   1. Update bin_1 = [(x_2, y_2), (x_6, y_6), (x_5, y_5)], since length of bin_1 is smaller than max bin size 3.
3. $v_3$:
   1. bin_1 is full as it reached length 3,
   2. create a new bin: bin_2 = [(x_1, y_1)]
4. $v_4$:
   1. bin_2 = [(x_1, y_1), (x_3, y_3), (x_4, y_4)]

Finishing the above loop and we have built a new map

| key | value |
|:----:|:----:|
| v_1 |  [(x_2, y_2), (x_6, y_6), (x_5, y_5)] |
| v_2 | [(x_2, y_2), (x_6, y_6), (x_5, y_5)] |
| v_3 |  [(x_1, y_1), (x_3, y_3), (x_4, y_4)] |
| v_4 | [(x_1, y_1), (x_3, y_3), (x_4, y_4)] |

With the above new map, we can start predicting quantiles using the point forecaster[^Hasson2021].

## Feature Space Partition

The algorithm is grouping data point that has similar predictions from our model. The input data in these data points forms the level set of our trained model $f$.

The math for the level set formalism can be found in Hasson2021[^Hasson2021].



[^Hasson2021]: {{< cite key="Hasson2021" >}}