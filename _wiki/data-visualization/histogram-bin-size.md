---
title: "Bin Size of Histogram"
excerpt: ""
date: 2018-11-22
toc: true
category:
- 'Data Visualization'
tag:
- 'Data Visualization'
weight: 1
references:
- name: "Histogram @ Wikipedia"
  link: https://en.wikipedia.org/wiki/Histogram
- name: "Choose Bin Sizes for Histograms in Easy Steps + Sturge’s Rule"
  link: https://www.statisticshowto.datasciencecentral.com/choose-bin-sizes-statistics/
charts:
- target: histogram-1
  data: "[
      trace = { x: [1.45,2.20,0.75,1.23,1.25,1.25,3.09,1.99,2.00,0.78,1.32,2.25,3.15,3.85,0.52,0.99,1.38,1.75,1.21,1.75], type: 'histogram',
      xbins: {
          size: 0.1
          }
          }
      ]"
  layout: 
- target: histogram-2
  data: "[
      trace = { x: [1.45,2.20,0.75,1.23,1.25,1.25,3.09,1.99,2.00,0.78,1.32,2.25,3.15,3.85,0.52,0.99,1.38,1.75,1.21,1.75], type: 'histogram',
      xbins: {
          size: 2
          }
          }
      ]"
- target: histogram-squareroot
  data: "[
      trace = { x: [1.45,2.20,0.75,1.23,1.25,1.25,3.09,1.99,2.00,0.78,1.32,2.25,3.15,3.85,0.52,0.99,1.38,1.75,1.21,1.75], type: 'histogram',
      xbins: {
          size: 0.67
          }
          }
      ]"
- target: histogram-sturges
  data: "[
      trace = { x: [1.45,2.20,0.75,1.23,1.25,1.25,3.09,1.99,2.00,0.78,1.32,2.25,3.15,3.85,0.52,0.99,1.38,1.75,1.21,1.75], type: 'histogram',
      xbins: {
          size: 0.67
          }
          }
      ]"
- target: histogram-scott
  data: "[
      trace = { x: [1.45,2.20,0.75,1.23,1.25,1.25,3.09,1.99,2.00,0.78,1.32,2.25,3.15,3.85,0.52,0.99,1.38,1.75,1.21,1.75], type: 'histogram',
      xbins: {
          size: 1.1
          }
          }
      ]"
---

Histograms are good for understanding the distribution of your data. 

## The Bin Size Problem

As an example, we will use the following series as an example.
```
[1.45,2.20,0.75,1.23,1.25,1.25,3.09,1.99,2.00,0.78,1.32,2.25,3.15,3.85,0.52,0.99,1.38,1.75,1.21,1.75]
```

If we use bin size 1, we get this spiky chart and it is not so informing.

<div id="histogram-1">
</div>

We could also set bin size to 2.

<div id="histogram-2">
</div>

In principle, we could keep tuning the bin size until we get something pretty and informing. But that would be quite depressing.


## Square-root

One simply way to estimate the number of bins needed is

$$B = \sqrt{N} ,$$

where $N$ is the lenght of the series.

In our example, $N=20$. Then we have $B=4.5\sim 5$ which leads to a bin size of $0.67$.


<div id="histogram-squareroot">
</div>

We immediately see the peak of this distribution.

## Sturge’s formula


Sturges' formula says that the number of bins of the histogram should be

$$
B = 1 + \log_2(N),
$$

where $N$ is the lenght of the series.

In our example, $N=20$. We have $B = 5$. The max and min of our series are $3.85$ and $0.52$, thus we have the bin size $W = 0.67$ which is the same as the square-root method.


<div id="histogram-sturges">
</div>




## Scott's Rule

Scott's rule says we should choose bin width

$$W = 3.49 \sigma N^{-1/3}$$

In our case, we have $N=20$ and $\sigma=0.86$, which leads to $W=1.1$.

<div id="histogram-scott">
</div>

