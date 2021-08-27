---
title: "Postgres Timezone Conversions"
summary: "Pitfals of timezone conversion in Postgres"
date: 2021-08-27
authors:
  - Lei Ma
categories:
  - "data"
references:
  - name: "kadkaz. Postgres AT TIME ZONE function shows wrong time? In: Stack Overflow [Internet]. [cited 27 Aug 2021]. Available: https://stackoverflow.com/questions/27938857/postgres-at-time-zone-function-shows-wrong-time"
    link: "https://stackoverflow.com/questions/27938857/postgres-at-time-zone-function-shows-wrong-time"
  - name: "8.5. Date/Time Types. In: PostgreSQL Documentation [Internet]. 12 Aug 2021 [cited 27 Aug 2021]. Available: https://www.postgresql.org/docs/current/datatype-datetime.html"
    link: "https://www.postgresql.org/docs/current/datatype-datetime.html"
  - name: "Time Zones. (2012, January 1). PostgreSQL Documentation. https://www.postgresql.org/docs/7.2/timezones.html"
    link: "https://www.postgresql.org/docs/7.2/timezones.html"
  - name: "Momjian B. Postgres AT TIME ZONE Explained. In: EDB [Internet]. 7 Nov 2019 [cited 27 Aug 2021]. Available: https://www.enterprisedb.com/postgres-tutorials/postgres-time-zone-explained"
    link: "https://www.enterprisedb.com/postgres-tutorials/postgres-time-zone-explained"
tags:
  - "Postgres"
  - "Warehouse"
---

By default, string representations of the datetime without time zone information is ambiguous. To properly convert such string representations to different time zones, we can clean it up by converting it to a timestamp, then attach the actual timezone to the strings, and convert it to the desired time zone.

For example, we have a string `'2021-07-29 14:48'` for UTC time. We would like to convert it to PST. The safest method would be convert it to a timestamp without timezone information, convert it to UTC time, then convert it to PST, i.e.,

```sql
'2021-07-29 14:48'::timestamp AT TIME ZONE 'UTC' AT TIME ZONE 'PST'
```

In this case, we do not need to set the time zone using `SET` (e.g., `set time zone -8;`, `set time zone UTC;`) nor do we need to know the actual time zone settings.



## I know the TIME ZONE Setting

If the time zone setting of the server is clear, or one would like to set the time zone up front, we can also directly using the string.

```sql
set time zone UTC;
SELECT
'2021-07-29 14:48' AS "raw",
'2021-07-29 14:48' AT TIME ZONE 'UTC' AS "direct_utc",
'2021-07-29 14:48' AT TIME ZONE 'PST' AS "direct_pst"
```

| raw              | direct_utc       | direct_pst       |
|------------------|------------------|------------------|
| 2021-07-29 14:48 | 2021-07-29 14:48 | 2021-07-29 06:48 |


## The Strange Thing


```sql
SELECT
'2021-07-29 14:48' AS "raw",
'2021-07-29 14:48' AT TIME ZONE 'UTC' AS "direct_utc",
'2021-07-29 14:48' AT TIME ZONE 'PST' AS "direct_pst",
'2021-07-29 14:48' AT TIME ZONE 'UTC' AT TIME ZONE 'PST' AS "direct_utc_pst", --  PST -08:00	Pacific Standard Time
'2021-07-29 14:48'  AT TIME ZONE 'PST' AT TIME ZONE 'UTC' AS "direct_pst_utc",
'2021-07-29 14:48'::timestamp AT TIME ZONE 'UTC' AT TIME ZONE 'PST' AS "ts_utc_pst",
'2021-07-29 14:48'::timestamp  AT TIME ZONE 'PST' AT TIME ZONE 'UTC' AS "ts_pst_utc"
```

| Raw String | direct_utc | direct_hst | utc_hst | ts_utc_hst | hst_utc | ts_hst_utc |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 2021-07-29 14:48 | 2021-07-29 14:48 | 2021-07-29 04:48 | 2021-07-30 00:48 | 2021-07-29 04:48 | 2021-07-29 04:48 | 2021-07-30 00:48 |



```sql
set time zone 3;
SELECT
'2021-07-29 14:48' AS "raw",
'2021-07-29 14:48' AT TIME ZONE 'UTC' AS "direct_utc",
'2021-07-29 14:48' AT TIME ZONE 'PST' AS "direct_pst",
'2021-07-29 14:48' AT TIME ZONE 'PST' AT TIME ZONE 'PST' AS "direct_pst_pst",
'2021-07-29 14:48' AT TIME ZONE 'UTC' AT TIME ZONE 'PST' AS "direct_utc_pst", --  PST -08:00	Pacific Standard Time
'2021-07-29 14:48' AT TIME ZONE 'HST' AS "direct_hst",
'2021-07-29 14:48' AT TIME ZONE 'HST' AT TIME ZONE 'PST' AS "direct_hst_pst",
'2021-07-29 14:48'  AT TIME ZONE 'PST' AT TIME ZONE 'UTC' AS "direct_pst_utc",
'2021-07-29 14:48'::timestamp AT TIME ZONE 'UTC' AS "ts_utc",
'2021-07-29 14:48'::timestamp AT TIME ZONE 'UTC' AT TIME ZONE 'PST' AS "ts_utc_pst",
'2021-07-29 14:48'::timestamp  AT TIME ZONE 'PST' AT TIME ZONE 'UTC' AS "ts_pst_utc"
```


| raw              | direct_utc       | direct_pst       | direct_pst_pst   | direct_utc_pst   | direct_hst       | direct_hst_pst   | direct_pst_utc   | ts_utc           | ts_utc_pst       | ts_pst_utc       |
|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|
| 2021-07-29 14:48 | 2021-07-29 11:48 | 2021-07-29 03:48 | 2021-07-29 14:48 | 2021-07-29 22:48 | 2021-07-29 01:48 | 2021-07-29 12:48 | 2021-07-29 06:48 | 2021-07-29 17:48 | 2021-07-29 06:48 | 2021-07-29 22:48 |


{{< message title="If we do not convert strings to timestamps" class="warning" >}}
If we do not convert strings to timestamps, the query result will try to use the system defined timezone to show the results.

For example, if the time zone of the system is UTC, then any time zone conversions based on strings will be converted back to UTC in the end.

- `'2021-07-29 14:48'  AT TIME ZONE 'UTC'` will always return the same result if the system is configured to UTC by default.
- `'2021-07-29 14:48' AT TIME ZONE 'PST'` will attach timezone PST (GMT-08) to the string then convert it back to UTC. The result will be `'2021-07-29 06:48'`.
- `'2021-07-29 14:48' AT TIME ZONE 'UTC' AT TIME ZONE 'PST'`. The result is `'2021-07-29 22:48'`.

The third result seems to be a backward conversion. Instead of -8, it added 8 hours. It is a conversion from PST to UTC.

{{< /message >}}