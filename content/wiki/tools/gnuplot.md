---
title: "GNUPlot"
description: "quickly make a graph in your command line"
date: 2017-09-04
categories:
- 'Tools'
tags:
- 'Tools'
- 'Command Line'
- 'Bash'
references:
- name: 'GNUPLOT'
  link: http://www.gnuplot.info/
weight: 3
---


## Examples


### Plot .csv data.

Suppose we have data of such.

```text
-0.00999983, 0.99995
-0.0199987, 0.9998
-0.0299955, 0.99955
-0.0399893, 0.9992
-0.0499792, 0.99875
-0.059964, 0.998201
```

To plot the second column against the first column, we use the using parameter in gnuplot.

```bash
gnuplot -e "set terminal png; set datafile separator ',' ; plot 'complex.txt' using 1:2" | imgcat

# datafile seperator is not always necessary
# imgcat is a script in iterm2 on mac
```
