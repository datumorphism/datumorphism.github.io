---
title: Python Class Sequential Inheritance
description: 'Sequentially inherit python classes'
date: 2020-12-03
authors:
  - LM
categories:
  - programming
  - basics
tags:
  - Python
  - OOP
links:
  - wiki/programming-languages/python/basics.md
updated: '2020-12-03'
---



```python
# An experiment on python super
class Base:
    def __init__(self):
        print("Start A")

        print("End A")


class IA(Base):
    def __init__(self):
        print("Start IA")
        super(IA, self).__init__()
        print("End IA")


class IB(IA):
    def __init__(self):
        print("Start IB")
        super(IB, self).__init__()
        print("End IB")


print("Experiment 1:")

ib = IB()
```


{{< repl url="https://repl.it/@emptymalei/python-super-nested?lite=true" >}}

