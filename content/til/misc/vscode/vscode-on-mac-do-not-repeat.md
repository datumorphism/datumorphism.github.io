---
layout: til
title: VSCode on Mac Long Press Keys Not Repeating
date: 2018-12-31
author: Lei Ma
comments: true
categories:
  - "misc"
tags:
  - "VSCode"
  - "IDE"
  - "Programming"
garden:
  - "evergreen"
summary: "Enable your key repeat in vscode on mac in the terminal"
references:
  - name: "jjcm. How do I press and hold a key and have it repeat in VSCode? In: Stack Overflow [Internet]. [cited 28 Mar 2022]. Available: https://stackoverflow.com/questions/39972335/how-do-i-press-and-hold-a-key-and-have-it-repeat-in-vscode"
    link: "https://stackoverflow.com/questions/39972335/how-do-i-press-and-hold-a-key-and-have-it-repeat-in-vscode"
    key: "jjcm"
---

## Solution

In some versions of vscode on Mac, when we long press a key, it does not repeat.

To ENABLE REPEAT on Mac[^jjcm]:

```bash
defaults write com.microsoft.VSCode ApplePressAndHoldEnabled -bool false
```

## Reason

Apple has this ApplePressAndHold function, where we can long press a key to type alternative characters. This is very useful in many cases, e.g., typing `öü` on a English keyboard. This is enabled by default on Mac.

We can disable it for some certain applications to enable repeating. The above solution will disable it for vscode.

There are examples for other applications too. For example, to disable it for sublime, we can follow this gist: https://gist.github.com/leesmith/8029019


[^jjcm]: {{< cite key="jjcm" >}}