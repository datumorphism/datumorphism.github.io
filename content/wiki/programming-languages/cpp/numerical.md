---
title: "The C++ Language: Numerical Methods"
description: "C++ as a programming language"
date: 2018-03-20
toc: true
category:
- 'Programming Language'
tag:
- 'Numerical Methods'
- 'Programming Language'
- 'Basics'
weight: 202
---

## Modularize

1. The code should be designed to seperate physics or model from numerical methods.


## Speed

1. `vectors` are convinient but slow. [^VectorSlow]
2. Do not copy arrays if not necessary. The example would be for a function return. Most of the times, we can pass pointer of array to the function and update the array itself without copying anything and no return is needed at all.
3. inline function.
4. Use `namespace` instead of class if no data structure is stored in it.

## Refs

[^VectorSlow]: http://en.cppreference.com/w/cpp/container/vector