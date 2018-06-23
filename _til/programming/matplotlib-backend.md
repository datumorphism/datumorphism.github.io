---
layout: til
title: "Some Tests on Matplotlib Backends"
date: 2017-05-23
author: OctoMiao
category:
- programming
tag:
- Python
- Matplotlib
excerpt: Matplotlib provides many different backends
---


Among the many matplotlib backends, what I found is that `TkAgg` and `WebAgg` works well on a mac.

Backends could either be set in your bashrc/zshrc files using

```
MPLBACKEND =
```

or a file located at `~/.matplotlib/matplotlibrc` using

```
backend =
```

A very useful customized backend is `itermplot` which displays plot result right in your iterm.
