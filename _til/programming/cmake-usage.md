---
layout: til
title: CMake Usage
date: 2017-09-21
author: OctoMiao
comments: true
category:
- programming
tag:
- 'C++'
excerpt: How to use CMake to generate makefiles
---

Write your CMakeLists.txt such as

{% highlight txt %}

cmake_minimum_required(VERSION 3.7)
project(my_parallel_program)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp include/looper.h include/hamiltonian.h include/stepper.h include/recorder.h)
add_executable(my_parallel_out ${SOURCE_FILES})

# for parallel using openmp
SET(CMAKE_CXX_COMPILER /usr/local/Cellar/gcc/7.2.0/bin/g++)
SET(GCC_COVERAGE_COMPILE_FLAGS "-fopenmp")
SET( CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} ${GCC_COVERAGE_COMPILE_FLAGS}" )
{% endhighlight %}

Make a directory to store the compiled files, such as build using `mkdir build`. `cd build`, then execute

{% highlight bash %}
make .. -G"Unix Makefiles"
{% endhighlight %}

CMake will generate all the file need within the current directory, i.e., `build`.

With the generated Makefile, we `make` to compile the program.
