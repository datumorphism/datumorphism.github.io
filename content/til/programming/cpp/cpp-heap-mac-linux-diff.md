---
layout: til
title: "Heap on Mac and Linux"
date: 2017-09-26
author: Lei Ma
comments: true
categories:
- programming
tags:
- 'Linux'
- 'Mac'
- 'C++'
summary: Some caveats about heap on mac and linux
---

```cpp
#include <iostream>

int main() {

   double *a = new double[5];

   for(auto i = 0; i < 5; i++)
   {
     a[i] = i;
   }

   std::cout << a[-10] << std::endl;

}
```

This program runs on Mac without warning or error. However, it gives segmentation fault (core dump) error on ubuntu and cent os.

{{< repl url="https://repl.it/Lfne/7?lite=true">}}

