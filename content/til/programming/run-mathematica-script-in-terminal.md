---
layout: til
title: "How to Run Mathematica Script in Terminal"
date: 2017-05-08
author: Lei Ma
categories:
- 'programming'
- 'basics'
tags:
- 'Mathematica'
summary: Using math -run or wolfram -run we could execute a Mathematica script through ssh in terminal.
---

A Mathematica script that can be run though ssh should be pure script like a `.m` file of Mathematica.

To run it, the following command is used.

```
math -run "<<my-mathematica-script.m"
```

or

```
math -run < my-mathematica-script.m
```

After `math` executes the script, it falls back to the REPL interface. If this is not useful at all, we apply `-noprompt`.

```
math -run -noprompt "<<my-mathematica-script.m"
```

Combined with `nohup` and screen we can run a Mathematica script in the background.

```
nohup math -run "<<my-mathematica-script.m" &> my-mathematica-script.out&
```
