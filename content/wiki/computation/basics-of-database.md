---
title: "Basics of Database"
description: "Essential knowledge of database"
date: 2018-10-03
categories:
- 'Computation'
tags:
- 'Database'
- 'Basics'
references:
  - link: "https://www.red-gate.com/simple-talk/sql/learn-sql-server/sql-server-index-basics/"
    name: "SQL Server Index Basics"
  - link: "https://apandre.wordpress.com/data/datacube/"
    name: "OLAP Cubes"
  - link: "https://app.enkipro.com/#/insight/5daefca67cef0ef7a1970975"
    name: "What is NoSQL"
  - link: "http://blog.knuthaugen.no/2010/03/the-nosql-landscape.html"
    name: "Analysis of the NoSQL Landscape"
weight: 4
links:
  - wiki/computation/basics-of-mongodb.md
  - wiki/computation/basics-of-redis.md
  - wiki/computation/basics-of-sql.md
---


## NoSQL

NoSQL = Not only SQL. The four main types of NoSQL databases are

- Key-value store: Amazon Dynamo, [memcached](http://memcached.org), Amazon SimpleDB
- Column-orient store: Google BigTable, Cassandra
- Graph database: Neo4j, VertexDB
- Document database: MongoDB
- Object database: [ZODB](http://www.zodb.org/)


## Database Operations


### Relations


1. Union: $A\cup B$
2. Intersection: $A\cap B$
3. $A - B$
4. Cartesian Product: $A \times B$


### Query

1. Union in database: will combine the data with matching common columns.
2. NaturalJoin and EquiJoin:

   ```SQL
    --EquiJoin where we specify what condition is used to join
    SELECT * FROM table1 JOIN table2 ON (table1.id = table2.id)
    --NaturalJoin where conditions are chosen by the database automatically
    SELECT * FROM table1 NATURAL JOIN table2
   ```
3. Procedural language: derived from structural programming, focuses on breaking tasks into variables, data structures, and subroutines.


### SQL

[Nice Article about Index](https://www.red-gate.com/simple-talk/sql/learn-sql-server/sql-server-index-basics/)

1. B-tree: nodes have subnodes; Read Wikipedia for more.
2. Index architectures:
   1. Clustered indices: sort data based on the key column, thus no row locator is needed.
   2. Non-clustered indices: store both column and row locator so that sorting is not needed.
3. "If the table has a clustered index, or the index is on an indexed view, the row locator is the clustered index key for the row." from HackerRank.
4. Leaf vs Non-leaf:
   1. Leaf level pages (nodes): the end of the search through B-tree;
   2. Non-leaf pages (nodes): root and intermediate
5. Fill factor: the leaf level pages are not always filled with data. You can specify some pages to be reserved for the future growth of data. The value is from 1 to 100 percent. Server-side default is usually 0 which means that all leaf pages are filled.
6. Composite index:

   ```sql
    CREATE INDEX index_name
    ON table_name(column1, column2);
   ```

### OLAP

OLAP Explained: [OLAP Cubes](https://apandre.wordpress.com/data/datacube/) explained the operations such as SLICE (slice by one dimension so that we get an N-1 subset of the data), DICE (slice more than two dimensions), DRILL DOWN/UP (navigate among levels of data), ROLL-UP (aggregate, consolidate, involves all the data relations for one or more dimensions), PIVOT (rotation).
{: .notes--info}

1. OLAP: Online analytical processing, with a core of OLAP cube (multidimensional cube, hypercube).
2. Aggregations: speed up time.
3. Both star schema and snowflake schema are the source of the cube metadata for OLAP.

4. About how those operations works, please find the quiz at [OLAP Operation Types @ HackerRank](https://www.hackerrank.com/challenges/olap-operation-types-2/forum)

   An example is

   ```text
    --Aggregation number of rows
    n1*n2*n3,
    --Rollup number of rows
    n1*n2*n3+n1+n1*n2+1
    --Cube number of rows
    n1*n2*n3+n1*n2+n2*n3+n1*n3+n1+n2+n3+1
   ```


### Relational Calculus

{{< message title="Operators">}}
Operators:
   1. ∀ = forall : https://en.wikipedia.org/wiki/Turned_A
   2. | = such that : https://en.wikipedia.org/wiki/Set-builder_notation
   3. ∧ = logical conjunction (and) : https://en.wikipedia.org/wiki/List_of_logic_symbols
   4. → = is a function

   Stolen from HackerRank: https://www.hackerrank.com/challenges/databases-relational-calculus/forum/comments/325506
{{< /message >}}


### Database Key

1. Primary key: unique values for each row of data; can not contain null values.

### Normalization

{{< message title="Dependency">}}
Dependency

   Dependency means a column that determines others.

   Partial dependency means that we have some column that depends on only some of the columns but has nothing to do with some other columns. In this case we can see some kind of redundancy. Hence in 2NF we remove partial dependency.

   Transitive dependency is that if x determines y, y determines z, then x determines z, which is the transitive dependency.
{{< /message >}}

1. NF: Normal Form,e.g., 1NF Rules, 2NF Rules, 3NF Rules. Refer to [this article](https://www.guru99.com/database-normalization.html). BCNF (Boyce-Codd normal form) please refer to wiki. 4NF is also explained well in [wiki](https://en.wikipedia.org/wiki/Fourth_normal_form).
2. [studytonight](https://www.studytonight.com/dbms/database-normalization.php)

   ```text
      1NF = can not be broken down into more elementary tables : Single value on each field; no repeating groups (for example table with multiple columns of products which are in principle the same is NOT 1NF)

      2NF = 1NF + no partial dependency: non-key columns depends on primary keys.

      3NF = 2NF + Transitive functional dependency of non-prime attribute on any super key should be removed.

      BCNF = A 3NF table that does not have multiple overlapping candidate keys is guaranteed to be in BCNF
   ```
3. [Superkey](https://en.wikipedia.org/wiki/Superkey):  set of attributes within a table whose values can be used to uniquely identify a tuple
4. Candidate key: column(s) to identify unique records
5. Nonkey Dependency: simply as the name indicates
