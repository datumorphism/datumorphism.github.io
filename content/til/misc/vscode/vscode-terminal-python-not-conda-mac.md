---
layout: til
title: "VSCode Terminal Python Can Not Activate Conda on Mac"
date: 2021-08-31
author: Lei Ma
categories:
    - misc
tags:
    - 'VSCode'
summary: Enable your key repeat in vscode on mac
---

In some versions of vscode, the built-in terminal does't use conda python. Instead it uses the system python. It does't matter what bash/zsh config you set. Conda just doesn't activate.

To fix this issue, add the config `terminal.integrated.env.osx` to `.vscode/settings.json` to fix the problem.


```json
{
    "terminal.integrated.env.osx": {
        "PATH": ""
    },
}
```