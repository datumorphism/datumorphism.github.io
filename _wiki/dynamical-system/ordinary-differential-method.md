---
title: "Ordinary Differential Equations"
excerpt: "Solving ODEs Using Finite Difference Methods"
date: 2018-11-19
toc: true
category:
- 'Dynamical System'
tag:
- 'Dynamical System'
- 'ODE'
- 'Finite Difference Method'
references:
- name: ""
  link: ''
notify: 'Difference equations are fun!'
weight: 1
---




For a first order differentiation $\frac{\partial f}{\partial t}$, we might have many finite differencing methods.

1. Forward Euler Method: $(f_{i+1} - f_i)/\Delta t$



## Euler Method




For linear first ODE,

$$
\frac{dy}{dx} = f(x, y),
$$

we can discretize the equation using a step size $\delta x \cdot$ so that the differential equation becomes

$$
\frac{y_{n+1} - y_n }{ \delta x } = f(x_n, y_n),
$$

which is also written as

$$
y_{n+1} = y_n + \delta x \cdot  f(x_n, y_n).
\label{euler-method-discretized-form-y-n-plus-1}
$$
   

This is also called **forward Euler** differencing. It is first order accurate in $\Delta t$.

Generally speaking, a simple iteraction will do the work.



## Adams' Method



<div class="notes--info" markdown="1">
**Taylor Expansion of Functions**

Suppose we have a function $f(x)$, Taylor expansion arround a point $x_0$ is

$$
f(x) = f(x_0) + f'(x_0) (x - x_0) + \cdots
$$

This is also named Maclaurin series.
</div>

For linear first ODE,

$$
\frac{dy}{dx} = f(x, y),
$$


This equation can always be written as a integral form

$$
y(x_{n+1}) - y(x_n) = \int_{x_n}^{x_{n+1}} f(x,y) dx,
$$

which is basically a very general idea of how to numerically solve such an equation, as long as we can solve the integral efficiently and accurately. In other words, we are dealing with

$$
y(x_{n+1}) =  y(x_n) + \int_{x_n}^{x_{n+1}} f(x,y) dx.
$$


The problem is how exactly do we calculate the integral or the iteraction. Two methods are proposed as explicit method **Adams-Bashforth Method** and implicit method **Adams-Moulton Method**.


What can be done is to Taylor expand the integrand. At first order of $f(x,y)$, we would have

$$
y(x_{n+1}) = y(x_n) + \int_{x_n}^{x_{n+1}} f(x_{n},y(x_n)) dx =  y(x_n) +(x_{n+1}- x_n) f(x_{n},y(x_n)) ,
$$

which is the Euler method. For simplicity step size is defined as

$$
\begin{equation}
\delta x = x_{n+1}- x_n.
\label{adams-method-step-size-def}
\end{equation}
$$

Also to simplify the notation, we introduce the notation

$$
y_n = y(x_n).
$$


For second order, we have at least two different methods to approximate the integral.


- Adams-Bashforth method is to approximate the integral using

  $$
  \int_{x_n}^{x_{n+1}} f(x,y) dx \sim \frac{1}{2} ( 3 f( x_n - f( x_{n-1}, y_{n-1} ) , y_n) ) \delta x
  $$

  where we used the definition of step size equation ($\ref{adams-method-step-size-def}$).


- Adams-Moulton method uses trapezoidal rule, which approximates the integral as

  $$
  \int_{x_n}^{x_{n+1}} f(x,y) dx \sim \frac{1}{2} f( x_{n+1} + f(x_n, y_n) , y_{n+1} ),
  $$

  which is similar to backward Euler method but of second order.


In fact the AB and AM methods to the first order are

- Adams-Bashforth Method First Order = Forward Euler Method;
- Adams-Moulton Method First Order = Backward Euler Method.


<div class="notes--info" markdown="1">
**scipy.odeint**

`scipy.odeint` uses `adams` for nonstiff equations, where even higher order are used. The return infodictionary entry `nqu` shows the orders for each successful step.
</div>

## Refs & Notes

1. [Adams Methods @ MIT Web Course](http://web.mit.edu/10.001/Web/Course_Notes/Differential_Equations_Notes/node6.html)
2. [Adams' Method @ Wolfram MathWorld](http://mathworld.wolfram.com/AdamsMethod.html)