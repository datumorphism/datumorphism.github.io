---
layout: til
title: C++ int Multiplication
date: 2017-09-21
author: Lei Ma
comments: true
category:
- programming
tags:
- 'C++'
excerpt: int multiplication in C++ should be processed with caution.
---

{% highlight cpp %}

#include <iostream>

using namespace std;

int main(int argc, char *argv[]){

   // Check the number of parameters
   if (argc < 1) {
      // Tell the user how to run the program
      std::cerr << "Usage: " << argv[0] << " takes 1 parameter:  the value of int to be multiplied " << std::endl;
      return 1;
   }

   int a = stoi(argv[1]);
   long int b = stol(argv[1]);

   cout.precision(10);
   cout << "Multiple itself as int: " << a * a << endl;
   cout << "Multiple itself as long int: " << b * b << endl;

}

{% endhighlight %}

Compile and run the program using `-std=c++11`.

{% highlight bash %}

cpp-int-multiply ‹master*›  ./int-multiplication.out 1000
Multiple itself as int: 1000000
Multiple itself as long int: 1000000

cpp-int-multiply ‹master*›  ./int-multiplication.out 10000
Multiple itself as int: 100000000
Multiple itself as long int: 100000000

cpp-int-multiply ‹master*›  ./int-multiplication.out 100000
Multiple itself as int: 1410065408
Multiple itself as long int: 10000000000

cpp-int-multiply ‹master*›  ./int-multiplication.out 1000000
Multiple itself as int: -727379968
Multiple itself as long int: 1000000000000

{% endhighlight %}


The results seems to be weird because the multiplicated number exceeds the max of int.


Within for loops, the `int i = 0` should be used carefully. The calculation `i*i` is problematic even i is not exceeding the max. There are solutions to this. We could convert `i` to double `(double)i` in situ. Or we could simple use `long int`.

Source code at repl.it.

<script src="//repl.it/embed/L1FC/0.js"></script>

Results from asciinema.

<div style="width:100%;text-align:center;">
<script type="text/javascript" src="https://asciinema.org/a/138882.js" id="asciicast-138882" async></script>
</div>
