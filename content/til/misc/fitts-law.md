---
layout: til
title: Fitt's Law
date: 2018-07-22
author: Lei Ma
comments: true
categories:
- misc
tags:
- 'Visual'
summary: How fast can you move your mouse to target
---

Human coordination between eyes and hand is quite complicated. For example, it takes time for us to move the pointer on the screen from one point to another using mouse. The time spend on this procedure is determined by Fitt's law:

$$
t = 600\mathrm{ms} + 240\mathrm{ms} \log (1+D/S),
$$

where $D$ is the distance to the target and $S$ is size of the target. The $240\mathrm{ms}$ is decomposed into three steps:

1. $70\mathrm{ms}$ for the eyes to determine the target;
2. $100\mathrm{ms}$ for the hand to move to the target;
3. $70\mathrm{ms}$ for the eyes to find out the deficit between the pointer and the target and decide how to correct it.
