---
layout: til
title: "List All Folders in Linux or Mac"
date: 2017-08-01
author: Lei Ma
comments: true
category:
- programming
tag:
- Linux
excerpt: Using ls and tree commands to list folders only
---

To list all folders, `ls` provides an option `-d`. Here is an example.

```
ls -ld */
```

The output is

```
drwxr-xr-x  44 doe  staff  1496 Jun  7 20:47 box-folder/
drwxr-xr-x  73 doe  staff  2482 Jun 23 17:16 another-folder/
drwxr-xr-x  60 doe  staff  2040 Jul  5 15:18 fake-folder-or-not/
```

In some special cases, a folder might start with `-`. `ls -d -- */` solves the problem. Here `--` means the end of the options for `ls`.


Another choice is `tree`.

```
tree -d .
```

which provides a output of the structures

```
.
├── box-folder-2
│   ├── export
│   │   └── allcomplex
│   └── fofomegak
│       └── export
├── export
│   └── unstable-regions
├── box-folder
└── two-beams
    └── export-np
```
