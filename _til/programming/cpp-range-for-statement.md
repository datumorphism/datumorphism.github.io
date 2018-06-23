---
layout: til
title: "C++ range-for-statement"
date: 2017-09-12T00:00:00.000Z
author: OctoMiao
category:
- programming
tag:
- 'C++'
excerpt: "In C++ we can use range-for-statement"
---

{% highlight cpp %}
# include <iostream>
using namespace std;
int main(){
    int v[] = {1,3,5,7};

    for( auto x:v)
    {
      cout << x << endl;
   }
}
{% endhighlight %}

What this does is to copy each element of array v into x and print it. For efficiency, we could use instead pointers.

{% highlight cpp %} for(auto& x : v) { cout << &x << endl; } {% endhighlight %}

<script src="//repl.it/embed/LAIt/5.js">
</script>
