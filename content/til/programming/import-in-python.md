---
layout: til
title: "Import in Python"
date: 2015-12-04
author: Lei Ma
comments: true
categories:
- programming
tags:
- Python
summary: Import in Python
---


As noted in [Structuring Your Project of Python Guide](http://docs.python-guide.org/en/latest/writing/structure/), `import` in python is rather tricky.

The style

```python
from neuosc import *
```

grabs everything in `neuosc` and put them in the global namespace which is more likely to override existing functions in the global namespace.

A better way is to import the exact function we need.

```python
from neuosc import par
```

Other good import methods are

```python
import neuosc
```

or

```python
import neuosc as ns
```
