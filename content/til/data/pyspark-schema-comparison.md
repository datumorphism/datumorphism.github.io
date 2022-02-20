---
title: "PySpark: Compare Two Schemas"
date: 2022-02-14
authors:
  - Lei Ma
categories:
  - data
tags:
  - 'PySpark'
  - 'Python'
---

To compare two dataframe schemas in {{< c "wiki/tools/data-processing-spark.md" "PySpark" >}}, we can utilize the set operations in python.

```python
def schema_diff(schema1, schema2):

    return {
        'fields_in_1_not_2': set(schema1) - set(schema2),
        'fields_in_2_not_1': set(schema2) - set(schema1)
    }
```