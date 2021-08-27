---
title: "Basics of MongoDB"
description: "MongoDB is a document based database"
date: 2018-10-03
categories:
- 'Computation'
tags:
- 'Database'
- 'Basics'
references:
  - name: "MongoDB Cheatsheet"
    link: https://gist.github.com/emptymalei/8c6b4fbbf0d92ba0ffb856439ec9cc64
weight: 6
links:
  - "wiki/computation/basics-of-redis.md"
---

This [MongoDB Cheatsheet](https://gist.github.com/emptymalei/8c6b4fbbf0d92ba0ffb856439ec9cc64) is my best friend.

## MongoDB Concepts

1. Documents
2. Collections: just like tables in SQL.
3. Database

## MongoShell

Some examples:

```
// show the databases
show dbs

// show collections
show collections

//set any database to current database
use database_name

// insert entry
db.database_name.insert( an_object_2_be_the_entry )

// read document
db.database_name.findOne({'some_field':'value_of_field'})
db.database_name.fidn()

// prettify
db.database_name.find().pretty()
```

