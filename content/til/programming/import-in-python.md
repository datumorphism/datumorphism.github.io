---
layout: til
title: "Import in Python"
date: 2015-12-04
author: Lei Ma
comments: true
category:
- programming
tags:
- Python
excerpt: Import in Python
---


As noted in [Structuring Your Project of Python Guide](http://docs.python-guide.org/en/latest/writing/structure/), `import` in python is rather tricky.

The style

{% highlight python %}
from neuosc import *
{% endhighlight %}

grabs everything in `neuosc` and put them in the global namespace which is more likely to override existing functions in global namespace.

A better way is to import the exact function we need.

{% highlight python %}
from neuosc import par
{% endhighlight %}

Other good import methods are

{% highlight python %}
import neuosc
{% endhighlight %}

or

{% highlight python %}
import neuosc as ns
{% endhighlight %}
