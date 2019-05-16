---
layout: til
title: "Gridlines in Matplotlib"
date: 2016-9-26
author: Lei Ma
category:
- programming
tag:
- Python
- Matplotlib
excerpt: Adding gridlines in matplotlib
---

In matplotlib, enabling the gridlines would draw the lines according to the major and minor ticks. However, we need some gridlines at specified locations.

Adding a single gridline at location `10`:

{% highlight python %}
ax.axvline(10, linestyle='--', color='k')
{% endhighlight %}

When a bunch of lines are required, we define an array as the gridline locations then loop through the location to add in the grridlines.

{% highlight tex %}
gridlineslist = [1,2,3,4,5,6]

for gridline in gridlineslist:
    ax.axvline(gridline, linestyle='--', color='k')
{% endhighlight %}
