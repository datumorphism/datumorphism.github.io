---
layout: til
title: "== and is in Python"
date: 2020-04-01
author: Lei Ma
category:
- programming
- basics
tags:
- Python
excerpt: == and is are different
---

The operator `==` is true if the values of the objects are the same while the operar `is` is true if their id are the same.

In Python, immutable objects are usually cached in memory, meaning they all point to the same thing in memory. For example, two tuples with the same values `(1,2,3)` will share the same id. Thus the operator `is` and `==` will give us the same results.


```python
def compare(a, b):
    print("=======================================")
    print(f"values: {a}, {b}")
    print(f"ids: {id(a)}, {id(b)}")
    if a is b:
        print(f"is: True")
    else:
        print(f"is: False")

    if a == b:
        print(f"==: True")
    else:
        print(f"==: False")

none_1 = None
none_2 = None
int_1 = 42
int_2 = 42
int_3 = 42
int_4 = 43
list_1 = [1,2,3]
list_2 = [1,2,3]
list_3 = [4,5,6,7]
list_4 = []
list_5 = []
dict_1 = {"key_1": 1}
dict_2 = {"key_1": 1}
dict_3 = {"key_2": 2}
dict_4 = {}
dict_5 = {}
tuple_1 = (1,2,3)
tuple_2 = (1,2,3)
tuple_3 = ()

compare(none_1, none_2)
compare(int_1, int_2)
compare(int_3, int_4)
compare(tuple_1, tuple_2)
compare(tuple_2, tuple_3)
compare(list_1, list_2)
compare(list_2, list_3)
compare(list_4, list_5)
compare(dict_1, dict_2)
compare(dict_2, dict_3)
compare(dict_4, dict_5)
compare(list_4, none_1)
compare(dict_4, none_1)
```

The above code prints

```
=======================================
values: None, None
ids: 140018300629504, 140018300629504
is: True
==: True
=======================================
values: 42, 42
ids: 140018300782112, 140018300782112
is: True
==: True
=======================================
values: 42, 43
ids: 140018300782112, 140018300782144
is: False
==: False
=======================================
values: (1, 2, 3), (1, 2, 3)
ids: 140018221295360, 140018221295360
is: True
==: True
=======================================
values: (1, 2, 3), ()
ids: 140018221295360, 140018222882880
is: False
==: False
=======================================
values: [1, 2, 3], [1, 2, 3]
ids: 140018221864512, 140018220932416
is: False
==: True
=======================================
values: [1, 2, 3], [4, 5, 6, 7]
ids: 140018220932416, 140018221075264
is: False
==: False
=======================================
values: [], []
ids: 140018221071040, 140018220932672
is: False
==: True
=======================================
values: {'key_1': 1}, {'key_1': 1}
ids: 140018222297856, 140018222821504
is: False
==: True
=======================================
values: {'key_1': 1}, {'key_2': 2}
ids: 140018222821504, 140018222067648
is: False
==: False
=======================================
values: {}, {}
ids: 140018221072576, 140018220887744
is: False
==: True
=======================================
values: [], None
ids: 140018221071040, 140018300629504
is: False
==: False
=======================================
values: {}, None
ids: 140018221072576, 140018300629504
is: False
==: False
```


<iframe height="400px" width="100%" src="https://repl.it/@emptymalei/None-in-Python?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>