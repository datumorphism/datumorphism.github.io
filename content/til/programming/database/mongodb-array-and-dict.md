---
layout: til
title: "Arrays and Dicts in MongoDB"
date: 2019-08-14
author: Lei Ma
comments: true
category:
- programming
tags:
- 'MongoDB'
excerpt: Array of dictionaries becomes hard to update in MongoDB.
---


1. Array is easy to use if the elements are flat, e.g.,

   ```
   {
       "alternative_of_names": [
           "Jane Doe",
           "John Doe",
           "Tim Doe"
       ]
   }
   ```
   When updating with new values, we could simply use `$addToSet`.
2. Array of json objects becomes really hard to update.
   ```
   {
       "alternative_of_names": [
           {
               "source": "Magzine",
               "first": "Jane",
               "last": "Doe"
           },
           {
               "source": "TV",
               "first": "John",
               "last": "Doe"
           },
           {
               "source": "Ads",
               "first": "Tim",
               "last": "Doe"
           }
       ]
   }
   ```

   Suppose we would like to update the name from source "Ads", it becomes tedious.
3. For the above purpose, we could simply rewrite the database in the following way.
   ```
   {
       "alternative_of_names": {
           "Magzine":
                {
                    "first": "Jane",
                    "last": "Doe"
                },
           "TV":
                {
                    "first": "John",
                    "last": "Doe"
                },
           "Ads":
                {
                    "first": "Tim",
                    "last": "Doe"
                }
       }
   }
   ```
   Then we can update easily with `$set`.
