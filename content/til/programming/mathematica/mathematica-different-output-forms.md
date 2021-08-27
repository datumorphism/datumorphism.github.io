---
layout: til
title: "Mathematica Different Output Forms"
date: 2016-11-28
modified: 2016-09-28
author: Lei Ma
comments: true
categories:
- programming
tags:
- Mathematica
summary: Mathematica has many different output forms. Understanding them is extremely helpful when making plots.
---


Here is a incomplete list of different output forms in Mathematica.

* TraditionalForm
* CForm
* FortranForm
* InputForm


{{< figure src="../assets/mathematica-different-output-forms.png" caption="Different forms." >}}


Whenever we need to include some fractions or powers or exponential in the plot label or plot legends, the default behavior of Mathematica is extremely weird and makes no sense. With these different forms, we can choose whichever is best for the plot.
