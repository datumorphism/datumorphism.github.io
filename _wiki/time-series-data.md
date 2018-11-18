---
title: "Short-Time-Fourier-Transform"
excerpt: "Some quick start material on regular expression."
date: 2018-06-20T15:58:49-04:00
toc: true
category:
- 'Time Series Data'
tag:
- 'Short-Time-Fourier-Transform'
- STFT
weight: 1
---



# Short-Time-Fourier-Transform


We Fourier transform the time series data using a Fourier transform, with some window function

\begin{equation}
   \tilde Y[n,k] = \sum_m Y[n+m] W[m] e^{-i \lambda_k m},
\end{equation}

where $\lambda_k=2\pi k/N$ and $W[m]$ is the window function at $m$.



# References and Notes


1. [Cousera](https://www.coursera.org/learn/practical-time-series-analysis/lecture/pPtHq/course-introduction)
