---
title: Ordered Member Functions of a Class in Python
description: 'Build an ordered list of methods in a python class by adding attributes to member functions'
date: 2020-12-02T00:00:00.000Z
authors:
  - LM
categories:
  - programming
  - basics
tags:
  - Python
  - OOP
references:
  - name: Can I add attributes to class methods in Python?
    link: 'https://stackoverflow.com/a/48146924/1477359'
license: CC BY-SA 4.0
links:
  - wiki/programming-languages/python/basics.md
  - wiki/programming-languages/python/decorators.md
updated: '2020-12-02T11:56:21+01:00'
---


````Python
# References:
# 1. https://stackoverflow.com/questions/48145317/can-i-add-attributes-to-class-methods-in-python

from functools import wraps

# Define a decorator
def attributes(**attrs):
    """
    Set attributes of member functions in a class.

    ```
    class AGoodClass:
        def __init__(self):
            self.size = 0

        @attributes(order=1)
        def first_good_member(self, new):
            return "first good member"

        @attributes(order=2)
        def second_good_member(self, new):
            return "second good member"
    ```

    References:
    1. https://stackoverflow.com/a/48146924/1477359
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)

        for attr_name, attr_value in attrs.items():
            setattr(wrapper, attr_name, attr_value)

        return wrapper

    return decorator


class AGoodClass:
    def __init__(self):
        self.size = 0

    @attributes(order=1)
    def first_good_member(self, new):
        return "first good member"

    @attributes(order=2)
    def second_good_member(self, new):
        return "second good member"


# Test

agc = AGoodClass()

print(agc.first_good_member.order)
print(agc.second_good_member.order)
````

{{< repl url="https://repl.it/@emptymalei/manipulatememberfunctionattributes?lite=true" >}}


