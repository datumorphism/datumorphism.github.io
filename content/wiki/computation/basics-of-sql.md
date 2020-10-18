---
title: "Basics of SQL"
excerpt: "Essential knowledge of programming"
date: '2018-11-19'
toc: true
category:
- 'Computation'
tag:
- 'Programming'
- 'Basics'
notify: 'I am transitioning from a physicist to a data scientist. While I am exploring the world of data, I find that I need to know some basics about computers.'
weight: 5
---


<div class="notes--info" markdown="1">
Adding a new field to data:

1. Relational: requires a new column
2. Non-Relational: just add the field to one single document, thus can be easily decentralized.
</div>


## Basics and Background


1. SQL: Structured Query Language
2. Relational Database:

   1. usually in tables
   2. rows are called records
   3. columns are certain types of data. Data type of rows are specified:
      1. INTEGER
      2. TEXT
      3. DATE
      4. REAL, real numbers
      5. NULL
      6. ...

3. RDBMS: Relational Database Management System, most RDBMS use SQL as the query language. SQLite is one of the RDBMS.
   1. SQLite: open source and minimal
   2. MySQL: powerful and popular, also open source, controlled by Oracle, not really scalable.
   3. PostgreSQL: open source, even slower than MySQL.
   4. OracleDB: not open source
   5. SQL Server: from Microsoft, not open source, and only on windows.



## SQL


<div class="notes--warning" markdown="1">
Semicolon in SQL is a statement terminator. Just use it.
</div>

<div class="notes--info" markdown="1">
**Capitalization Strategy**

For readablilty

1. Capitalize clauses
2. Capitalize table names etc

On stackoverflow: [stackoverflow](https://stackoverflow.com/questions/608196/why-should-i-capitalize-my-sql-keywords)
</div>

## Statements for Manipulation


1. Create table

   ```SQL

      CREATE TABLE table_name (
          column_1 data_type,
          column_2 data_type,
          column_3 data_type
        );
   ```

   Constraints can be included when creating tables. I am using the example from [CodeAcademy](https://www.codecademy.com/courses/learn-sql-manipulation/lessons/manipulation/exercises/delete).

   ```SQL

      CREATE TABLE awards (
      --id should be integer, and is the primary key
         id INTEGER PRIMARY KEY,
      --recipient should be text and can not be null
         recipient TEXT NOT NULL,
      --default values for a column
         award_name TEXT DEFAULT "Grammy"
      );
   ```

   As mentioned in the basics section, primary keys should be unique to identify the specific row.

2. Insert new row

   ```SQL
      INSERT INTO table_name (column_1, column_2, column_3)
      VALUES (some_value_1, some_value_2, some_value_3);
   ```

3. Update some values

   ```SQL
      -- Specify the table
      UPDATE table_name
      -- choose column to be updated
      SET column_1 = some_other_value_1
      -- specify row location
      WHERE column_2 = some_specific_value_to_locate_the_row;
   ```

4. Add new columns

   ```SQL
      -- speficy table
      ALTER table_name
      -- add column and specify data type, here I use TEXT
      ADD COLUMN column_4 TEXT
   ```

5. Delete rows

   ```SQL
      DELETE FROM celebs
      -- I use column_4 as an example
      -- Delete every row if column_4 has NULL values
      WHERE column_4 IS NULL;
   ```



## Statements for Queries



1. Select from table; select returns *result set* which is a new table.

   ```SQL
      -- Select out everything from table
      SELECT * FROM table_name;
      -- Select out the values of a specific column
      SELECT column_1 FROM table_name;
   ```

2. Select specific columns

   ```SQL
      SELECT column_1, column_2
      FROM table_name;
   ```

3. `AS` keyword: allows you to select the column and return it as the specified new name of the column; the database is NOT modified.

   ```SQL
      SELECT column_1 AS 'A NEW NAME'
      FROM table_name;
   ```


4. Select and show only the distinct values of the column

   ```SQL
      SELECT DISTINCT column_1
      FROM table_name;
   ```

5. `WHERE` key: using operators such as `=, !=, >, <, >=, <=` to filter results

   ```SQL
      SELECT * FROM table_name
      WHERE column_1 = 0;
   ```

6. `LIKE` key: patern specified like `AA_B` where `_` is for a single character.

   ```SQL
      SELECT * FROM table_name
      WHERE column_1 LIKE `AA_B`
   ```

   Wildcards: `_`, `%` for 0 or more characters.

7. `BETWEEN`, `AND`, `OR`:

   ```SQL
      SELECT *
      FROM movies
      WHERE name BETWEEN 'D%' AND 'G%';
   ```


8. `SORT BY`: Can be either `DESC` or `ASC` and goes after where

   ```SQL
      SELECT * FROM movies
      WHERE year > 2014
      ORDER BY name DESC;
   ```

9. `LIMIT`

   ```SQL
      SELECT *
      FROM movies
      ORDER BY imdb_rating DESC
      LIMIT 3;
   ```

10. `CASE`:

    ```SQL
       SELECT name,
        CASE
          WHEN genre = 'romance' THEN 'fun'
          WHEN genre = 'comedy' THEN 'fun'
          ELSE 'serious'
        END
       FROM movies;
   ```



## Aggregate



1. `COUNT`:

   ```SQL
      SELECT COUNT(*)
      FROM tabe_name;
   ```

2. `SUM`:

   ```SQL
      SELECT SUM(column_1)
      FROM table_name;
   ```

3. `MAX` and `MIN`:

   ```SQL
      SELECT MAX(column_1)
      FROM table_name;
   ```

4. `AVG`: average

   ```SQL
      SELECT AVG(column_1)
      FROM table_name;
   ```

5. `ROUND`: round to specified decimals

   ```SQL
      --round the price to integers
      SELECT name, ROUND(price,0)
      FROM fake_apps;

      --round the price to integers
      --even with other keys as arguments
      SELECT name, ROUND(AVG(price),0)
      FROM fake_apps;
   ```

6. `GROUP BY`: group by column values


   ```SQL
      SELECT price, COUNT(*)
      FROM fake_apps
      WHERE downloads > 20000
      GROUP BY price;
   ```

   or

   ```SQL
      SELECT category, SUM(downloads)
      FROM fake_apps
      GROUP BY category;
   ```

   References can be used in `GROUP BY`

   ```SQL
      SELECT category, SUM(downloads)
      FROM fake_apps
      GROUP BY 1;
      --1 here is identical to category
   ```


7. `HAVING`: The problem with `WHERE` is that it goes before `GROUP BY`. What if we need to filter the groups?

   ```SQL
      SELECT price, ROUND(AVG(downloads))
      FROM fake_apps
      GROUP BY price
      HAVING COUNT(price) > 9;
   ```


## Multiple Tables


The **normalization** is explained in [DB Normalization](../basics-of-database/#normalization).

1. `JOIN`: Join tables with specified column

   ```SQL
      SELECT *
      FROM orders
      JOIN subscriptions
      ON orders.subscription_id = subscriptions.subscription_id
      WHERE description = 'Fashion Magazine';
   ```

2. Inner Join: only join the rows that have common values on the specified join columns.

   ```SQL
      SELECT COUNT(*)
      FROM newspaper;
      --Output 60

      SELECT COUNT(*)
      FROM online;
      --Output 65

      SELECT COUNT(*)
      FROM newspaper
      JOIN online
      ON online.id = newspaper.id;
      --Output 50 <= 60 or 65
   ```

3. Left Join: simply plug all the right table onto left tables, where the values of the specified column match. The number of rows will be the number of rows for the left table.

   ```SQL
      SELECT *
      FROM newspaper
      LEFT JOIN online
      ON newspaper.id=online.id
      WHERE online.id IS NULL;
   ```

4. Cross join: combine all the information


   ```SQL
      SELECT month,
      COUNT(*) as subscribers
      FROM months
      CROSS JOIN newspaper
      WHERE months.month > newspaper.start_month AND months.month < newspaper.end_month
      GROUP BY months.month;
   ```

5. `UNION`: stack tables

   ```SQL
      SELECT *
      FROM newspaper
      UNION
      SELECT *
      FROM online;
   ```

6. `WITH`: create a result with alias





## References and Notes



1. [What is a Relational Database Management System (RDBMS)?](https://www.codecademy.com/articles/what-is-rdbms-sql)
2. [List of SQL commands](https://www.codecademy.com/articles/sql-commands)