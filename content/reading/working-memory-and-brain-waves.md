---
title:  "Working Memory and Brain Waves"
date: 2016-11-20 #2014-08-27T11:57:41-04:00
modified: 2016-11-20
subtitle: ""
speaker: "Lei Ma"
authors:
  - Lei Ma
categories:
  - neuroscience
tags:
  - neuroscience
  - recurrent network
  - population model
summary: "Working memory might be related to the background brain waves from theoretical point of view"
status: Done
references:
  - name: "Flexible frequency control of cortical oscillations enables computations required for working memory"
    link: http://www.pnas.org/content/110/31/12828.short
---

## Working Memory

In a few words, working memory is the cache of our brain, which has limited capacity.

## The Model and Results

A quadratic integrate-and-fire (QIF) model with a reset equation

$$
\begin{align}
\tau \frac{d}{dt}u = & u^2 - I_{\mathrm{inhibit}} + I_{\mathrm{excitatory}}(t)\\
u_{\mathrm{threshold}} \to & u_{\mathrm{reset}}
\end{align},
$$

where they have used a constant inhibit current.

The input current is categorized into three categories

$$
I_{\mathrm{excitatory}}(t) = I_{r}(t) + I_s(t) + I_{\mathrm{background}}(t),
$$

in which $I_r(t)$ is the input from other neurons in the network, $I_s(t)$ is the stimulus added to the system. $I_{\mathrm{background}}(t)$ is the manual simulation of brain waves. The reason they added this background as brain waves is that what we measure as brain waves is more like a local field potential and might not be produced by the small network we are interested in. So this work basically do not talk about the origin of the brain waves but the effect of brain waves, which can be produced by other part of the brain, on the working memory.

**All the inputs are treated as spikes** or delta functions, which is described in the Supporting Information.


## Elevator Speech

{{< figure src="../assets/working-memory-and-brain-waves/fig1-results.png" caption="Different background input has different effects on the working memory. Source: Dipoppa 2013." >}}

Basically this looks like a noise effect on population model. People already know that noise can work as low pass or high pass filters for population activities, so we could interpret this result as the filter property of the background input, or brain waves.
