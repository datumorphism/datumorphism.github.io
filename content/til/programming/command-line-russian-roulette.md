---
layout: til
title: "Command Line Russian Roulette"
date: 2017-05-09
author: Lei Ma
comments: true
category:
- programming
tags:
- Linux
summary: Play russian roulette in your command line
---

Found a very funny comic on [commicstrip](http://www.commitstrip.com/en/2014/05/16/russian-roulette/).

{{< figure src="../assets/programming/russian-roulette-in-command-line.jpg" caption="Commic from [commicstrip](http://www.commitstrip.com/en/2014/05/16/russian-roulette/)." >}}

nixcraft has this article that explains these commands.

```
[ $[ $RANDOM % 6 ] == 0 ] && rm -rf / || echo *Click*
```

or

```
[ $[ $RANDOM % 6 ] == 0 ] && rm -rf --no-preserve-root / || echo *Click*
```

or a safer version

```
[ $[ $RANDOM % 6 ] == 0 ] && echo '*Oh nooo*' || echo '*Click*'
```

[On reddit someone saw an ad from infinum about this](https://www.reddit.com/r/ProgrammerHumor/comments/4ghiac/saw_this_on_my_way_to_uni_command_line_russian/).


{{< figure src="../assets/programming/russian-roulette-from-infinum.jpg" caption="[on reddit](https://www.reddit.com/r/ProgrammerHumor/comments/4ghiac/saw_this_on_my_way_to_uni_command_line_russian/)." >}}
