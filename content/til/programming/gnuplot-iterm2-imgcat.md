---
layout: til
title: "GNUPLOT Inline Output in iterm2"
date: 2017-04-07
modified: 2017-04-07
author: Lei Ma
comments: true
categories:
- programming
tags:
- Visualization
- gnuplot
summary: Using gnuplot in iterm2 we can output result inside terminal combined with imgcat
---

iterm2 has a function called imgcat which can show image inside terminal. Combined with it, gnuplot can output result in situ.

```
gnuplot -e "set terminal png; plot 'ho-damped.txt'" | imgcat
```
