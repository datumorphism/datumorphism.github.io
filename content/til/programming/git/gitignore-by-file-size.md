---
layout: til
title: "gitignore by file size"
date: 2015-12-04
author: Lei Ma
comments: true
category:
- programming
tags:
- Git
excerpt: gitignore by file size
---

http://stackoverflow.com/questions/4035779/gitignore-by-file-size


```
find . -size +1G | cat >> .gitignore
```

For the actual application purpose, I would prefer to overwrite the .gitignore file, which only requires single `>`

```
find . -size +50M | cat > .gitignore
```
