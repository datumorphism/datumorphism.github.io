---
title: "Basics of Redis"
description: "Redis is an in-memory nosql data structure server"
date: 2021-01-08
authors:
  - "LM"
categories:
  - "Computation"
tags:
  - "dev"
  - "Database"
  - "cache"
  - "Basics"
references:
  - name: "Redis Tutorial - A Brief Introduction to Redis"
    link: "https://www.youtube.com/watch?v=qr4FVhBTq0I"
  - name: "Redis with Python for Data Science"
    link: "https://www.youtube.com/watch?v=Koh6piVaYh0"
weight:
links:
  - "wiki/computation/basics-of-mongodb.md"
---


## Basics

Redis is:
- NoSQL
- KeyValue
- In memory
- Data Structure Server
  - binary safe strings
  - lists, sets, sorted sets, hashes
  - bitmaps, hyperloglogs
- Open source

Redis is:
- Fast
- Low CPU Requirement
- Scalable


Redis can be used as:
- Cache
- Analytics
- Leaderboard
- Queues
- Cookie storage
- Expiring data
- Messaging
- High I/O workloads
- API throttlings


How to persist your data
- Snapshot
- AOF: Append Only File


Pros:
- Redis has both data store and job queue built in
- Redis is a data structure server so is has flexibe data structures
- Redis is fast

Cons:
- Redis used a lot of RAM
- Redis can be be queued by value

Comparisons
- SQL
- NoSQL
- Flat file
- Rabbit
- ActiveMQ

## How to Use it

Redis can be used as a handy data storage for data science projects. It can also be used as an API. Redis can be used on a medium data file. It can be used as a way to store medium size data file and also read out for analysis.



### Installation

- [Install redis on ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04)
- [install redis on Mac](https://gist.github.com/tomysmile/1b8a321e7c58499ef9f9441b2faa0aa8)


### Test

Invoke the command line
```
redis-cli
```


### Useful commands

- `set`: `set test "just a test"`
- `get`: `get test`


### Python

[redis on pypi](https://pypi.org/project/redis/)

```
import redis

r \= redis.Redis(host\='localhost', port\=6379, db\=0)

print("setting keys")
r.set('test', 'just a test in python')

print('getting values')
print(

r.get('test')

)
```