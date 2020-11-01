---
layout: til
title: "Turn a Series Expansion into Function in Mathematica"
date: 2017-05-15
author: Lei Ma
category:
- programming
tags:
- Mathematica
excerpt: Turn a series expansion in Mathematica into a function
---

`Series` in Mathematica returns a series with higher orders denoted as $\mathscr O[x^3]$. To define a function out of this returned expression, we have to truncate this tail using `Normal`.

What `Normal` does here is to truncate the higher orders.

Reference: [Converting Power Series to Normal Expressions](https://reference.wolfram.com/language/tutorial/ConvertingPowerSeriesToNormalExpressions.html)
