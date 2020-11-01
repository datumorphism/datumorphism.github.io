---
layout: til
title: "Python Stupid numpy.piecewise"
date: 2015-12-04
author: Lei Ma
category:
- programming
- basics
tags:
- Python
excerpt: Python Stupid numpy.piecewise
---

The `piecewise()` function in numpy is not very good. Due to the writing of the function, one wouldn't be surprised to encounter the following error,

{% highlight python %}
if (n != n2):
    raise ValueError(
        "function list and condition list must be the same")
{% endhighlight %}

in which `n` is the length of condition list and `n2` is the length of function list.

To avoid it, the input should always be prepared as following

{% highlight python %}
x = np.asarray(x)
# The following is important to avoid the weird behavior of piecewise()
if not x.shape:
    x = np.asarray([x])
{% endhighlight %}
