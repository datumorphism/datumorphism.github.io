---
layout: til
title: "C++ range-for-statement"
date: 2017-09-12T00:00:00.000Z
author: Lei Ma
category:
- programming
tags:
- 'C++'
summary: "In C++ we can use range-for-statement"
---

```cpp
# include <iostream>
using namespace std;
int main(){
    int v[] = {1,3,5,7};

    for( auto x:v)
    {
      cout << x << endl;
   }
}
```

What this does is to copy each element of array v into x and print it. For efficiency, we could use instead pointers.

```highlight cpp
for(auto& x : v) { cout << &x << endl; }
```

{{< repl url="https://repl.it/LAIt/5?lite=true" >}}