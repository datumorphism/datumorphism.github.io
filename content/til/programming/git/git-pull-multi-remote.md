---
layout: til
title: "git pull multi remote"
date: 2016-11-22
author: Lei Ma
comments: true
categories:
- programming
tags:
- Git
summary: working with multi remote
---



`git pull` = `git pull origin HEAD`

So I can clearly pull from another remote or branch. For example, I can pull `gh-pages` branch from a remote `bitbucket` remote through

```
git pull bitbucket gh-pages
```
