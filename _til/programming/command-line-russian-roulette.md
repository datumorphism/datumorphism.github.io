---
layout: til
title: "Command Line Russian Roulette"
date: 2017-05-09
author: OctoMiao
comments: true
category:
- programming
tag:
- Linux
excerpt: Play russian roulette in your command line
---

Found a very funny comic on [commicstrip](http://www.commitstrip.com/en/2014/05/16/russian-roulette/).

<figure markdown="1">
![](../assets/programming/russian-roulette-in-command-line.jpg)
<figcaption markdown="1">
Commic from [commicstrip](http://www.commitstrip.com/en/2014/05/16/russian-roulette/).
</figcaption>
</figure>


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


<figure markdown="1">
![](../assets/programming/russian-roulette-from-infinum.jpg)
<figcaption markdown="1">
[on reddit](https://www.reddit.com/r/ProgrammerHumor/comments/4ghiac/saw_this_on_my_way_to_uni_command_line_russian/).
</figcaption>
</figure>
