---
layout: til
title: "GNU Screen Key Conflict with Bash"
date: 2017-05-08
author: Lei Ma
comments: true
category:
- programming
tag:
- Linux
excerpt: GNU screen key conflict with bash can be solved
---

In Bash/zsh/etc, `CTRL+A` moves the cursor to the beginning of the lines, which significantly speeds up the workflow. However, as GNU screen is considered, `CTRL+A` is the prefix of all commands, such as `CTRL+A + D` to detach a screen. Inside screen, `CTRL+A` won't move the cursor around.

The solution is to replace all `CTRL` in the knowledge about bash/zsh/etc with `CTRL+A`. As an example, suppose we need to move the cursor to the beginning, we press `CTRL+A` first, then release, followed by `A`. The release of `CTRL+A` is critical otherwise we would excute some GNU screen command.
