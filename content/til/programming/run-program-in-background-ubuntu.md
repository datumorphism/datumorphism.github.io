---
layout: til
title: "Run a program in the background on ubuntu"
date: 2015-12-04
author: Lei Ma
categories:
- 'programming'
- 'basics'
tags:
- 'Linux'
summary: Run a program in the background on ubuntu
---

1. Make it executable: `chmod +x program.py`
2. Use no hang up: `nohup /path/to/program.py &`. `nohup` keep the program running even in one closes the terminal. `python /path/to/program.py &` also keeps it running in the terminal in background. But it terminates the program if one logs out. To redirect the output to another file, `nohup comp-range-de.py > comp-range-de.out 2>&1&` or `nohup comp-range-de.py &> comp-range-de.out&` for short.
3. Check the process: `ps ax | grep program.py`. `ps -e` can list out all the running programs.

Source: [How to run the Python program in the background in Ubuntu machine? ](http://askubuntu.com/questions/396654/how-to-run-the-python-program-in-the-background-in-ubuntu-machine)

It is very important to understand the output of `ps`. Here is the man.

```bash
PROCESS STATE CODES
       Here are the different values that the s, stat and state output
       specifiers (header "STAT" or "S") will display to describe the state of
       a process.
       D    Uninterruptible sleep (usually IO)
       R    Running or runnable (on run queue)
       S    Interruptible sleep (waiting for an event to complete)
       T    Stopped, either by a job control signal or because it is being
            traced.
       W    paging (not valid since the 2.6.xx kernel)
       X    dead (should never be seen)
       Z    Defunct ("zombie") process, terminated but not reaped by its
            parent.

       For BSD formats and when the stat keyword is used, additional
       characters may be displayed:
       <    high-priority (not nice to other users)
       N    low-priority (nice to other users)
       L    has pages locked into memory (for real-time and custom IO)
       s    is a session leader
       l    is multi-threaded (using CLONE_THREAD, like NPTL pthreads do)
       +    is in the foreground process group
```

Meanwhile, another question is how to kill such a process.

```bash
xxx@ipython-notebook:~/abc/py$ ps -eaf | grep vacOsc4CompSSConvention-moretol.py
xxx    12921 11369 99 17:05 pts/0    00:04:49 python vacOsc4CompSSConvention-moretol.py
xxx    13040 11369  0 17:10 pts/0    00:00:00 grep --color=auto vacOsc4CompSSConvention-moretol.py
xxx@ipython-notebook:~/abc/py$ kill 12921
```
