---
title: "Basics of Programming"
description: "Essential knowledge of programming"
date: 2018-09-23
category:
- 'Computation'
tags:
- 'Programming'
- 'Basics'
weight: 2
---

## Recursive and Iterative

Solving problems with iterative and recursive methods are two quite different approaches, somehow, to the same kind of problems.

Here we will calculate the factorial of $n$. We define two functions using the iterative method and the recursive method.

Run the program on [Repl.it](https://repl.it/@emptymalei/recursive-iterative).


```
def recursiveFactorial(n):
  if n == 0:
    return 1
  else:
    return n * recursiveFactorial(n - 1)


def iterativeFactorial(n):
  ans = 1

  i=1

  while i <= n:
    ans = ans * i
    i=i+1

  return ans


print(recursiveFactorial(0))
print(iterativeFactorial(0))
```

{{< repl url="https://repl.it/@emptymalei/recursive-iterative?lite=true" >}}