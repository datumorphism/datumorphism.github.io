---
layout: til
title: "Allocating Memory for Multidimensional Array in C++"
date: 2017-09-14
author: Lei Ma
comments: true
category:
- programming
tags:
- 'C++'
summary: Some caveats
---

```cpp
#include <iostream>
#include <typeinfo>

using namespace std;

int main() {

  int (*a0)[1000] = new int[10000][1000];
  int (*a1)[1000][10] = new int[10000][1000][10];
  int **a2;
  int *a3;
  int *a4 = new int[100];
  // int a5[]; // Commented out because we can not do this
  // a5 = new int[100];




  std::cout << typeid(a0).name() << endl;
  std::cout << typeid(a1).name() << endl;
  std::cout << typeid(a2).name() << endl;
  std::cout << typeid(a3).name() << endl;
  std::cout << typeid(a4).name() << endl;
  // std::cout << typeid(a5).name() << endl;

}
```

The outputs are

```txt
gcc version 4.6.3

PA1000_i
PA1000_A10_i
PPi
Pi
Pi
```

And multidimensional arrays by default are contiguous in memory.

<script src="//repl.it/embed/LHJd/46.js"></script>
{{< repl url="https://repl.it/@emptymalei/multidimensional-arrays?lite=true">}}
