---
layout: til
title: "The Great Chrome Dev Tool"
date: 2016-09-28
modified: 2016-09-28
author: Lei Ma
comments: true
categories:
- programming
tags:
- Web
- Front-end
summary: How to use the chrome dev tool wisely
---

Chrome dev tool is not only super useful for front-end dev but also helpful to users.

## contentEditable

By setting

```
document.body.contentEditable = true
```

one can just start editing the content of the whole web page.

## Display Data in a Table

Reading nested lists can be painful. Suppose we have an array

```
var arraydata = [{a:1,b:2},{a:2,c:5},{b:4,e:1}]
```

the function

```
console.table(arraydata)
```

give us a table that is associated with the array.



{{< figure src="../assets/programming/chrome-dev-tools-console.table.png" caption="console.table()" >}}


## Clear the Output

Simple and easy

```
clear()
```


## inspect()

```
inspect($('.sidebar'))
```

will list all the element that has class `sidebar`.

{{< figure src="../assets/programming/chrome-dev-tools-inspect.png" caption="inspect($('.sidebar'))" >}}



## dir()

List out all the properties of a element using

```
dir($("div"))
```

{{< figure src="../assets/programming/chrome-dev-tool-dir.png" caption="div($('div'))" >}}


## And more

1. [Things you probably didn’t know you could do with Chrome’s Developer Console](https://medium.freecodecamp.com/10-tips-to-maximize-your-javascript-debugging-experience-b69a75859329#.cj9742xlv)
2. [中文版：天啦噜！原来Chrome自带的开发者工具还能这么用！](https://zhuanlan.zhihu.com/p/22665710)
