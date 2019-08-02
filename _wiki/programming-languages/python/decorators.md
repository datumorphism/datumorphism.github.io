---
title: "The Python Language: Decorators"
excerpt: "Python as a programming language"
date: 2018-03-20
toc: true
category:
- 'Programming Language'
tag:
- 'Python'
- 'Programming Language'
- 'Basics'
weight: 210
---


Functions: first-class objects; can be passed around as arguments.

What that tells us about is that functions can be pass into a function or even returned by a function. For example,

```python
def a_decoration_function( yet_another_function ):

    def wrapper():

        print('Before yet_another_function')

        yet_another_function()

        print('After yet_another_function')

    return wraper


def yet_another_function():

    print('This is yet_another_function')
```


When we excute `a_decoration_function`, we will have

```
Before yet_another_function
This is yet_another_function
After yet_another_function
```

So a decorator is simply a function that takes a function as an argument, adds some salt to it.

To use the decorator, we simply use `@`

```python
@a_decoration_function
def my_function():
    print('This is my function')


my_function()
```

This piece of code will return the decorated function.
