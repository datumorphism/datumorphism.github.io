---
layout: til
title: "Start a Simple Server"
date: 2016-09-17
author: Lei Ma
category:
- 'programming'
- 'basics'
tags:
- 'Python'
- 'Web'
summary: With one line of python command
---

Sometimes we debug html locally but run into the error

> XMLHttpRequest cannot load file:///xxx/xxx/xxxx.html. Cross origin requests are only supported for protocol schemes: http, data, chrome, chrome-extension, https, chrome-extension-resource.


The solution is to run a very simple static web server locally by using a python one-liner

```
python -m SimpleHTTPServer 8000
```
