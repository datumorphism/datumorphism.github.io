---
title: "Basics of MongoDB"
excerpt: "MongoDB is a document based database"
date: 2018-10-03
toc: true
category:
- 'Computation'
tag:
- 'Database'
- 'Basics'
notify: 'I am transitioning from a physicist to a data scientist. While I am exploring the world of data, I find that I need to know some basics about computers and internet.'
weight: 6
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

