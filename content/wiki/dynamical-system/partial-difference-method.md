---
title: "Partial Differential Equations"
description: "Solving PDEs"
date: 2018-11-19
categories:
- 'Dynamical System'
tags:
- 'Dynamical System'
- 'PDE'
- 'Finite Difference Method'
notify: 'Differential equations are fun!'
weight: 2
---

## Forward Time Centered Space


For $\frac{d f}{d t} = - v \frac{ d f }{ dx }$, we write down the finite difference form [^NumericalRecipes]

$$
\frac{f(t_{n+1}, x_i ) - f(t_n, x_i)}{ \Delta t } = - v \frac{ f(t_n, x_{i+1}) - f(t_n, x_{i-1}) }{ 2\Delta x }.
$$

FTCS is an explicit method and is not stable.


## Lax Method


Change the term $f(t_n, x_i)$ in FTCS to $( f(t_n, x_{i+1}) + f(t_n, x_{i-1}) )/2$  [^NumericalRecipes].

Stability condition is

$$
\frac{ \lvert v \rvert \Delta t }{ \Delta x } \leq 1,
$$

which is the Courant-Fridriches-Lewy stability criterion.



## Staggered Leapfrog


$$
\frac{f(t_{n+1}, x_i) - f(t_{n-1}, x_i)}{2 \Delta t} = -v \frac{ f(t_n, x_{i+1} ) - f(t_n, x_{i-1} ) }{ 2\Delta x}
$$

It's kind of a Centered Space Centered Time method.


## Two-Step Lax-Wendroff Scheme



## Fully Implicit


$$
\frac{ f( t_{n+1} , x_i ) - f( t_{n} , x_i ) }{ \Delta t } = - v \frac{ f(t_{n+1}, x_{i+1}) - f(t_{n+1}, x_{i-1}) }{ 2\Delta x }.
$$

It is called implicity because we can not simply iterate over the formula to get the solutions as like for the explicit method.


## Crank-Nicholson


Crank-Nicholson is a average of the explicit and fully implicit method.

$$
\frac{ f( t_{n+1} , x_i ) - f( t_{n} , x_i ) }{ \Delta t } = - \frac{v}{2} \frac{ \left(f(t_{n+1}, x_{i+1}) - f(t_{n+1}, x_{i-1}) \right) + \left( f(t_{n}, x_{i+1}) - f(t_{n}, x_{i-1}) \right)}{ 2\Delta x }.
$$




## References and Notes


[^NumericalRecipes]: Numerical Recipes in C