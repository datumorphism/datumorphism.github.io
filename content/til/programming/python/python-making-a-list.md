---
layout: til
title: "Python Making a List"
date: 2015-12-04
author: Lei Ma
category:
- programming
- basics
tags:
- Python
summary: Python Making a List
---

Integrated with loops


```python
list_with_for_loop = [x for x in range(10)]
print list_with_for_loop
```


    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


Even with conditions in the for loop


```python
list_with_for_loop_conditional = [x for x in range(10) if x%2 == 1]
print list_with_for_loop_conditional
```

    [1, 3, 5, 7, 9]


Nested loops in a list


```python
list_with_nested_loops = [ [x, y] for x in range(3) for y in range(3) ]
print list_with_nested_loops
```

    [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]


Another example of nested loops


```python
list_with_nested_loops_2 = [ x for x in range(y) for y in range(3)]
print list_with_nested_loops_2
```

    [0, 0, 0, 1, 1, 1]


[The article](http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/) gives an example of how to flatten a matrix using this trick. Semantically, one would using


```python
matrix = [[11,12],[21,22]]
row = [1,2]
wrong_flatten_of_matrix = [x for x in row for row in matrix]
print "matrix is", matrix
print "flattened matrix is", wrong_flatten_of_matrix
```

    matrix is [[11, 12], [21, 22]]
    flattened matrix is [1, 1, 2, 2]


which is obviously **WRONG**. The correct code is given by the author as


```python
right_flatten_of_matrix = [x for row in matrix for x in row]
print "matrix is", matrix
print "flattened matrix is", right_flatten_of_matrix
```

    matrix is [[11, 12], [21, 22]]
    flattened matrix is [11, 12, 21, 22]


**The key is to write the nested loops in a list as the normal nested loops.**

With this possible confusion, the author proposed a line breaking solution


```python
right_flatten_of_matrix_line_breaking = [
    x
    for row in matrix
        for x in row
]
print "matrix is", matrix
print "flattened matrix is", right_flatten_of_matrix_line_breaking
```

    matrix is [[11, 12], [21, 22]]
    flattened matrix is [11, 12, 21, 22]


which significantly improved the readability.
