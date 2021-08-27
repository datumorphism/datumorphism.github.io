---
title: "The C++ Language: Numerical Methods"
description: "C++ as a programming language"
date: 2018-03-20
categories:
- 'Programming Language'
tags:
- 'Numerical Methods'
- 'Programming Language'
- 'C'
- 'C++'
- 'Basics'
references:
  - name: "std::vector"
    link: http://en.cppreference.com/w/cpp/container/vector
weight: 3
---

## Modularize

1. The code should be designed to separate physics or model from numerical methods.


## Speed

1. `vectors` are convenient but slow. [^VectorSlow]
2. Do not copy arrays if not necessary. The example would be for a function return. Most of the time, we can pass the pointer of an array to the function and update the array itself without copying anything and no return is needed at all.
3. inline function.
4. Use `namespace` instead of class if no data structure is stored in it.

## Refs

[^VectorSlow]: http://en.cppreference.com/w/cpp/container/vector