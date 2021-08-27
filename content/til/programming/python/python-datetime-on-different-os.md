---
layout: til
title: "Python Datetime on Different OS"
date: 2018-12-31
author: Lei Ma
categories:
- programming
- basics
tags:
- Python
summary: Python datetime on different os behaves inconsistently
---

## Python datetime on Linux and Mac

For the same code

```python
from dateutil.parser import parse
from datetime import datetime

parse('18.09.197').strftime('%Y-%m-%d')
```

On Mac, we have `Python 3.6.5 :: Anaconda, Inc.`: `'0197-09-18'`

On REPL.it which is linux based, we have `Python 3.6.1 (default, Dec 2015, 13:05:11)` (the default python comes with the system on linux): `'197-09-18'`

On my ubuntu laptop with Python 3.6.3, Anaconda custom 64bit, I got

```
datetime.datetime(197,9,18).strftime('%Y-%m')
'197-09'
```

This is a difference between linux and mac.

There is another example: https://repl.it/@emptymalei/Strange-Datetime-Parser-in-Python


{{< repl url="https://repl.it/@emptymalei/Strange-Datetime-Parser-in-Python?lite=true" >}}

In case the repl.it embedding does not work, here is the code.

```
import dateutil.parser
import datetime

def check_and_convert_to_datetime(input_date):
    """
    Convert input to *datetime* object.

    This is the last effort of converting input to datetime.
    The order of instance check is

    1. datetime.datetime
    2. str
    3. float or int

    >>> handle_strange_dates(1531323212311)
    datetime(2018, 7, 11, 17, 33, 32, 311000)
    >>> handle_strange_dates(datetime(2085,1,1))
    datetime(2050, 1, 1)
    """

    if isinstance(input_date, datetime.datetime):
        cur_year = datetime.datetime.now().year
        if abs(input_date.year - cur_year) > 50:
            return datetime.datetime(2050, 1, 1)
        return input_date
    if isinstance(input_date, str):
        try:
            input_date = dateutil.parser.parse(input_date)
        except:
            return None

        cur_year = datetime.datetime.now().year
        if abs(input_date.year - cur_year) > 50:
            return datetime.datetime(2050, 1, 1)
        return input_date
    if isinstance(input_date, (float, int)):
        try:
            res = datetime.datetime.fromtimestamp(input_date / 1000)
        except:
            res = None
        return res

## The following code produces
## datetime.datetime(2018, 7, 11, 15, 33, 32, 311000)
## on linux
## but it produces
## datetime.datetime(2018, 7, 11, 17, 33, 32, 311000)
## on mac

print(
  check_and_convert_to_datetime(1531323212311)
)


##
## On Mac
## Python 3.6.1 |Continuum Analytics, Inc.| (default, May 11 2017, 13:04:09)
## Type 'copyright', 'credits' or 'license' for more information
## IPython 7.2.0 -- An enhanced Interactive Python. Type '?' for help.

## In [1]: import hl_etl_util.util as _util

## In [2]: _util.check_and_convert_to_datetime(1531323212311)
## Out[2]: datetime.datetime(2018, 7, 11, 17, 33, 32, 311000)
```


