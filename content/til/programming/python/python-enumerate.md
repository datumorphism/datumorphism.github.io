---
layout: til
title: "Python enumertate"
date: 2015-12-04
author: Lei Ma
category:
- programming
- basics
tags:
- Python
excerpt: Python enumertate function
---

[Code Style of Python Guide](http://docs.python-guide.org/en/latest/writing/style/)

`enumerate()` can be used to keep track of the index of the list.

{% highlight python %}
test = [None] * 5
for n, elem in enumerate( range(5,10) ):
    print n, elem
    test[n] = elem*2
{% endhighlight %}

Here we also used the technique of creating a list of length 5.
