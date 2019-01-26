---
layout: til
title: "Python Map vs For in Python"
date: 2015-12-04
author: OctoMiao
category:
- 'programming'
- 'basics'
tag:
- Python
excerpt: Python Map vs For in Python
---



`map` is sometimes more convinient instead of for. The code

{% highlight python %}
newlist = []
for word in oldlist:
    newlist.append(word.upper())
{% endhighlight %}

can be reformed using `map`

{% highlight python %}
newlist = map(str.upper, oldlist)
{% endhighlight %}

`for` loop is sometimes slow because the dot evaluation inside is evaluated for each loop. Thus the following code is more efficient.

{% highlight python %}
upper = str.upper
newlist = []
append = newlist.append
for word in oldlist:
    append(upper(word))
{% endhighlight %}
