---
title: "PySpark: Beware of Python Mutable Objects"
description: "We should be careful when dealing with python mutable objects. For example, make copies of python mutable objects in pyspark udfs."
date: "2022-04-20"
authors:
  - "Lei Ma"
categories:
  - "data"
tags:
  - "PySpark"
  - "Python"
---


{{< rawhtml >}}
<style>
.file {
  display: block
}
</style>
{{< /rawhtml >}}

I created [this example notebook](https://gist.github.com/emptymalei/07ba6716d0e2d815ebb64adce25dee72) to demonstrate the potential danger when dealing with mutable objects in pyspark udfs.

{{< gist emptymalei 07ba6716d0e2d815ebb64adce25dee72 >}}

https://gist.github.com/emptymalei/07ba6716d0e2d815ebb64adce25dee72


In the above notebook, we can see that python lists in udfs are behaving like just pointers. For group in the aggregation, we see that the lists in the same values in column `b` are behaving like the same list, thus pointer like.

To solve this problem, we can do a few things.

1. Cache the dataframe after aggregation.

   ```python
   sdf_2 = sdf.groupby("language", "b").agg(F.max("b").alias("combined")).cache()
   ```

2. Make a copy of the mutable object.

   ```python
   sch = T.ArrayType(T.IntegerType())

   @F.udf(returnType=sch)
   def add_one(data):
       b = data["b"].copy()
       b[0] = b[0] + 1

       return b
   ```
