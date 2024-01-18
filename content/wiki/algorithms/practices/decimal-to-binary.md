---
title: "Decimal to Binary Representation"
description: "Calculate the digits of a number in a given base."
date: 2024-01-18
categories:
- 'Algorithms'
tags:
- 'Algorithms'
- 'Basics'
- 'Code Challenges'
weight: 1
---

```python
from typing import Tuple, List


class Decimal2Base:
    """Given an integer in decimal representation,
    find the binary representation.

    Example:
        Input: 5
        Output: 101
    """
    def __init__(self, base: int = 2):
        self.base = base

    def _quotient_remainder(self, n: int) -> Tuple[int, int]:
        return (n // self.base, n % self.base)

    def _digits(self, number: int, digits: List) -> List:
        """Recursively find the binary representation of a number.
        """
        if number == 0:
            return digits
        else:
            quotient, remainder = self._quotient_remainder(number)
            digits = [remainder] + digits
            return self._digits(quotient, digits)

    def __call__(self, number: int) -> List:
        digits: List = []
        return self._digits(number, digits)


def test_decimal2binary():
    decimal2binary = Decimal2Base(base=2)

    assert decimal2binary(5) == [1, 0, 1]


def test_decimal2decimal():
    decimal2decimal = Decimal2Base(base=10)

    assert decimal2decimal(5) == [5]
    assert decimal2decimal(14) == [1, 4]
```