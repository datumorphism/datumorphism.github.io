---
layout: til
title: "Switch statement in Python"
date: 2019-08-20
author: Lei Ma
category:
- programming
- basics
tag:
- Python
excerpt: Love switch statement? We can design a switch statement it in python.
references:
  - name: "Dispatch Tables in Python"
    link: https://medium.com/better-programming/dispatch-tables-in-python-d37bcc443b0b
---


We simply create a dispatch for the cases.

Here is the example from the references.

```python
import datetime

dispatch = {
  0: do_monday,
  1: do_tuesday,
  2: do_wednesday,
  3: do_thursday,
  4: do_friday,
  5: do_saturday,
  6: do_sunday
}

my_special_day = datetime.date(2019, 5, 25)

dispatch[my_special_day.weekday()]()
```
