---
title: "Normal Distribution"
description: "Gaussian distribution"
date: 2019-01-22
categories:
- 'Distributions'
tags:
- 'Distributions'
- 'Normal Distribution'
- 'Gaussian Distribution'
charts:
- target: normal-distribution-1
  data: [{ "x": [-3.  , -2.94, -2.88, -2.82, -2.76, -2.7 , -2.64, -2.58, -2.52,
       -2.46, -2.4 , -2.34, -2.28, -2.22, -2.16, -2.1 , -2.04, -1.98,
       -1.92, -1.86, -1.8 , -1.74, -1.68, -1.62, -1.56, -1.5 , -1.44,
       -1.38, -1.32, -1.26, -1.2 , -1.14, -1.08, -1.02, -0.96, -0.9 ,
       -0.84, -0.78, -0.72, -0.66, -0.6 , -0.54, -0.48, -0.42, -0.36,
       -0.3 , -0.24, -0.18, -0.12, -0.06,  0.  ,  0.06,  0.12,  0.18,
        0.24,  0.3 ,  0.36,  0.42,  0.48,  0.54,  0.6 ,  0.66,  0.72,
        0.78,  0.84,  0.9 ,  0.96,  1.02,  1.08,  1.14,  1.2 ,  1.26,
        1.32,  1.38,  1.44,  1.5 ,  1.56,  1.62,  1.68,  1.74,  1.8 ,
        1.86,  1.92,  1.98,  2.04,  2.1 ,  2.16,  2.22,  2.28,  2.34,
        2.4 ,  2.46,  2.52,  2.58,  2.64,  2.7 ,  2.76,  2.82,  2.88,
        2.94,  3.  ],
        "y": [0.011, 0.013, 0.016, 0.019, 0.022, 0.026, 0.031, 0.036, 0.042, 0.049, 0.056, 0.065, 0.074, 0.085, 0.097, 0.11, 0.125, 0.141, 0.158, 0.177, 0.198, 0.22, 0.244, 0.269, 0.296, 0.325, 0.355, 0.386, 0.418, 0.452, 0.487, 0.522, 0.558, 0.594, 0.631, 0.667, 0.703, 0.738, 0.772, 0.804, 0.835, 0.864, 0.891, 0.916, 0.937, 0.956, 0.972, 0.984, 0.993, 0.998, 1.0, 0.998, 0.993, 0.984, 0.972, 0.956, 0.937, 0.916, 0.891, 0.864, 0.835, 0.804, 0.772, 0.738, 0.703, 0.667, 0.631, 0.594, 0.558, 0.522, 0.487, 0.452, 0.418, 0.386, 0.355, 0.325, 0.296, 0.269, 0.244, 0.22, 0.198, 0.177, 0.158, 0.141, 0.125, 0.11, 0.097, 0.085, 0.074, 0.065, 0.056, 0.049, 0.042, 0.036, 0.031, 0.026, 0.022, 0.019, 0.016, 0.013, 0.011],
      type: 'scatter',
      fill: 'tozeroy',
      xbins: {size: 0.1}}
      ]
  layout:
- target: erf-1
  data: [{
         "x": [-3.  , -2.94, -2.88, -2.82, -2.76, -2.7 , -2.64, -2.58, -2.52,
         -2.46, -2.4 , -2.34, -2.28, -2.22, -2.16, -2.1 , -2.04, -1.98,
         -1.92, -1.86, -1.8 , -1.74, -1.68, -1.62, -1.56, -1.5 , -1.44,
         -1.38, -1.32, -1.26, -1.2 , -1.14, -1.08, -1.02, -0.96, -0.9 ,
         -0.84, -0.78, -0.72, -0.66, -0.6 , -0.54, -0.48, -0.42, -0.36,
         -0.3 , -0.24, -0.18, -0.12, -0.06,  0.  ,  0.06,  0.12,  0.18,
         0.24,  0.3 ,  0.36,  0.42,  0.48,  0.54,  0.6 ,  0.66,  0.72,
         0.78,  0.84,  0.9 ,  0.96,  1.02,  1.08,  1.14,  1.2 ,  1.26,
         1.32,  1.38,  1.44,  1.5 ,  1.56,  1.62,  1.68,  1.74,  1.8 ,
         1.86,  1.92,  1.98,  2.04,  2.1 ,  2.16,  2.22,  2.28,  2.34,
         2.4 ,  2.46,  2.52,  2.58,  2.64,  2.7 ,  2.76,  2.82,  2.88,
         2.94,  3.  ],
         "y": [-1.0, -1.0, -1.0, -0.9999, -0.9999, -0.9999, -0.9998, -0.9997, -0.9996, -0.9995, -0.9993, -0.9991, -0.9987, -0.9983, -0.9977, -0.997, -0.9961, -0.9949, -0.9934, -0.9915, -0.9891, -0.9861, -0.9825, -0.978, -0.9726, -0.9661, -0.9583, -0.949, -0.9381, -0.9252, -0.9103, -0.8931, -0.8733, -0.8508, -0.8254, -0.7969, -0.7651, -0.73, -0.6914, -0.6494, -0.6039, -0.5549, -0.5027, -0.4475, -0.3893, -0.3286, -0.2657, -0.2009, -0.1348, -0.0676, 0.0, 0.0676, 0.1348, 0.2009, 0.2657, 0.3286, 0.3893, 0.4475, 0.5027, 0.5549, 0.6039, 0.6494, 0.6914, 0.73, 0.7651, 0.7969, 0.8254, 0.8508, 0.8733, 0.8931, 0.9103, 0.9252, 0.9381, 0.949, 0.9583, 0.9661, 0.9726, 0.978, 0.9825, 0.9861, 0.9891, 0.9915, 0.9934, 0.9949, 0.9961, 0.997, 0.9977, 0.9983, 0.9987, 0.9991, 0.9993, 0.9995, 0.9996, 0.9997, 0.9998, 0.9999, 0.9999, 0.9999, 1.0, 1.0, 1.0],
         type: 'scatter'
      }]
  layout:
weight: 1
---

## Visualization

{{< rawhtml >}}
<div id="normal-distribution-1">
</div>
{{< /rawhtml >}}

## Math

The formula of normal distribution is

$$
\begin{equation}
e^{ ( (x - \mu) / \sqrt{2} \sigma )^2 }
\end{equation}
$$

where $\mu$ controls the "center" or "peak" of the distribution and $\sigma$ tells us how "wide" or "disperse" the distribution is.

To understand the distribution, we take some limits.

### $x = \mu$

First of all, when $x = \mu$ we have

$$
e^0 = 1.
$$

Notice the argument of the exponential is some squared value and can not be negative. This condition gives us the peak value.

### $x=\mu-a$ and $x=\mu + a$

For $x=\mu-a$, we have

$$
e^{ ( (a) / \sqrt{2} \sigma )^2 }.
$$

For $x=\mu + a$, we have

$$
e^{ ( (a) / \sqrt{2} \sigma )^2 }
$$

which is exactly the same as the previous case.

The distribution is symmetric around $x=\mu$.

### $x=\pm \infty$

We have 0 for both cases.

## Tricks

### Integral

We integrate distributions a lot. For Gaussian distribution, it is quite helpful to remember the following identity.

$$
\int_{-\infty}^\infty e^ {- x^2} dx = \sqrt{\pi}.
$$

It tells us that for $\mu=0$ and $\sigma=1/\sqrt{2}$, the area under the distribution is $\sqrt{\pi}$.

Hey, it is time to ask the question. Where the hell is the circle?

### Error Function

The error function is defined as

$$
\mathrm{erf}(x) = \frac{1}{\sqrt{\pi}}\int_{-x}^{x} e^{ - t^2} dt
$$

Obviously, the coefficient $\frac{1}{\sqrt{\pi}}$ normalizes the function to be within $[-1,1]$.

{{< rawhtml >}}
<div id="erf-1">
</div>
{{< /rawhtml >}}
