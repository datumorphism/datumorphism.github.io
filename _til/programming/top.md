---
layout: til
title: "TOP Command"
date: 2016-07-21
author: Lei Ma
category:
- 'programming'
- 'basics'
tag:
- 'Linux'
excerpt: Some tips about top command
---



For MacOS, the useful commands are

* sort according to memory: `top -o mreg`
* sort according to execution time: `top -o time`
* sort according to CPU usage (this is default): `top -o cpu`
* sort according to the number of threads running: `top -o threads`
* sort according to the corresponding user name: `top -o user`
* show only N (a number) processes: `top -n N`
* show only one process: `top -pid PIDNUMBER` (where on linux this should be `top -p PIDNUMBER`)

For more options, `top -h` will help.

`htop` is a great replacement for `top`, with build in easy sort, graphical representation etc.
