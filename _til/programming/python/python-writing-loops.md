---
layout: til
title: "Python Various Ways of Writing Loops"
date: 2015-12-04
author: Lei Ma
category:
- 'programming'
- 'basics'
tag:
- 'Python'
excerpt: Python Various Ways of Writing Loops
---




1. List Comprehension

{% highlight python %}
[2*x+3 for x in list]
{% endhighlight %}


2. `map`

{% highlight python %}
map(function, list)
{% endhighlight %}

A function can also be defined on the fly.

{% highlight python %}
map(lambda x: function of x, list)
{% endhighlight %}


For multivariable,

{% highlight python %}
map(lambda x,y:x+y, xlist, ylist)
{% endhighlight %}


3. `zip` and `map`

`zip` is useful in a map of multivariable function.

{% highlight python %}
map(functionofxy, zip(xlist,ylist))
{% endhighlight %}

As given in the reference link, one good example is

{% highlight python %}
map(sum,zip(A,B,C))
{% endhighlight %}


4. `map` and list comprehension



{% highlight python %}
[map(lambda x: x+3, list) for list in shape2by2list]
{% endhighlight %}




Ref. [Great Python Tricks for avoiding unnecessary loops in your code](http://forums.udacity.com/questions/1002566/great-python-tricks-for-avoiding-unnecessary-loops-in-your-code)
