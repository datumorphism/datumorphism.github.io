---
title: "Data Processing - (Py)Spark"
description: "Processing Data using (Py)Spark"
date: "2022-01-31"
categories:
  - "Data Engineering"
tags:
  - "Data Engineering"
  - "Spark"
  - "PySpark"
references:
  - name: "Introduction to PySpark on DataCamp"
    link: "https://www.datacamp.com/courses/introduction-to-pyspark"
    key: "DataCampPySparkIntro"
supplementary:
  - name: "Introduction to PySpark on DataCamp"
    link: "https://www.datacamp.com/courses/introduction-to-pyspark"
weight: 21
---

Spark uses Resilient Distributed Dataset (RDD).

## PySpark

PySpark provides

- `SparkContext`
  - `SparkSession`


A spark dataframe is immutable. This makes it tricky to update a dataframe.


### Useful Commands

#### Get Session

In pyspark, we can also get or create the session using the following method.

```python
pyspark.sql.SparkSession.builder.getOrCreate()
```

#### List all Tables

A [`pyspark.sql.SparkSession` has property `catalog`](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.sql.SparkSession.catalog.html#pyspark.sql.SparkSession.catalog) and can be used to list the tables.

```python
pyspark.sql.SparkSession.catalog.listTables()
```

#### Run SQL Query

Given a SQL query `query`, we can query the table using `.sql()` method of the session.

```python
query = ...
pyspark.sql.SparkSession.sql(query)
```


#### Convert Dataframe to Pandas Dataframe


```python
.toPandas()
```


#### Convert Pandas Dataframe to Spark Dataframe

To create a spark dataframe from a pandas dataframe,

```python
.createDataFrame(a_pandas_dataframe)
```

Note that the dataframe is not yet in the catalog of the session.
- It is only stored locally.
- SQL query doesn't work.


#### Use Query on local dataframe

To be able to query the dataframe, it has to be in the catalog. A dataframe has the method `.createOrReplaceTempView("a_table_name")`. This will create a table that can be used as long as the session is alive.

Once a table is in the catalog, we can create a dataframe using

```python
pyspark.sql.SparkSession.table("a_table_name")
```


### Updating Dataframe


#### Create and Add


```python
spark_df = spark_df.withColumn("a_new_col", df.existing_col * 3.14)
```

Contrary to our intuition, this will create a new dataframe with all the original columns and this new column `"a_new_col"`.

A comparison would be the `.select()` method of a dataframe.

#### Update the Type of a Column

```python
df.col_1.cast("integer")
```

PySpark can convert string representation of integers to integers. In the above example, it works even if `df.col_1` contains string representation of some integers.

#### `filter`

SQL Where clause

```python
.filter("sql query where clause")
```

or Python

```python
.filter(df.col_1 < 0)
```

#### Select a Newly Created Column


```python
.selectExpr("col_1 * 3.14 as col_1_mul_pi")
```

[`.selectExpr`](https://spark.apache.org/docs/3.1.1/api/python/reference/api/pyspark.sql.DataFrame.selectExpr.html?highlight=selectexpr#pyspark.sql.DataFrame.selectExpr) works similar to [`.select`](https://spark.apache.org/docs/3.1.1/api/python/reference/api/pyspark.sql.DataFrame.select.html?highlight=select#pyspark.sql.DataFrame.select), we can select other columns just like what we do in the SQL select clause

```python
.selectExpr("col_1", "col_2", "col_1 * 3.14 as col_1_mul_pi")
```


### Grouping

Use [`.groupBy`](https://spark.apache.org/docs/3.1.1/api/python/reference/api/pyspark.sql.DataFrame.groupBy.html?highlight=groupby#pyspark.sql.DataFrame.groupBy).

- `pyspark.sql.GroupedData` has some useful methods, e.g., `.avg`, `count`.
- Use `.agg(pyspark.sql.functions.x_y_z_function)` to aggregate.

### Joining Tables

[`.join`](https://spark.apache.org/docs/3.1.1/api/python/reference/api/pyspark.sql.DataFrame.join.html)


### ML on Spark

- `pyspark.ml`
  - `pyspark.ml.Transformer`
    - `pyspark.ml.Transformer.transform()`: input DataFrame, output DataFrame
  - `pyspark.ml.Estimator`
    - `pyspark.ml.Estimator.fit()`: input DataFrame, output model object.
  - `pyspark.ml.features`
  - `pyspark.ml.Pipeline`
    - `Pipeline(stages=[...])`
    - Once a pipeline is formed, we can `a_pipeline.fit(my_spark_df).transform(my_spark_df)`
  - `pyspark.ml.evaluation`
    - `pyspark.ml.evaluation.BinaryClassificationEvaluator()`
  - `pyspark.ml.tuning`
    - `pyspark.ml.tuning.ParamGridBuilder`
    - `pyspark.ml.tuning.CrossValidator`
- pyspark dataframe has the method `.randomSplit()`
