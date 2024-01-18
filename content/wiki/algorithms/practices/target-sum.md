---
title: "Target Sum"
description: "Target sum problem"
date: 2024-01-18
categories:
- 'Algorithms'
tags:
- 'Algorithms'
- 'Basics'
- 'Code Challenges'
weight: 2
---

## Two Sum


```python
from typing import List, Literal


class TwoSum:
    """Find all the possible combinations of two numbers
    in a list that sum up to a target integer.

    Example:
        Input: nums = [2, 7, 11, 15], target = 9
        Output: [[2, 7]]
    """
    def __init__(self, method: Literal["brute_force"]) -> None:
        self.method = method

    def __call__(self, nums: List, target: int) -> List:
        """
        :param nums: list of integers
        :param target: target integer
        """
        if self.method == "brute_force":
            return self._brute_force_two_sum(nums, target)

    def _brute_force_two_sum(self, nums: List, target: int) -> List:
        """Find all the possible combinations of two numbers
        in a list that sum up to a target integer.

        :param nums: list of integers
        :param target: target integer
        """
        nums_sorted = sorted(nums)
        result = []
        length = len(nums_sorted)
        for i in range(length):
            for j in range(i+1, length):
                combination = [nums_sorted[i], nums_sorted[j]]
                if sum(combination) == target and combination not in result:
                    result.append(combination)

        return result

```