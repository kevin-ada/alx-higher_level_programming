## 0x0E. SQL - More queries
### General
1. How to create a new MySQL user
2. How to manage privileges for a user to a database or table
3. What’s a PRIMARY KEY
4. What’s a FOREIGN KEY
5. How to use NOT NULL and UNIQUE constraints
6. How to retrieve datas from multiple tables in one request
7. What are subqueries
8. What are JOIN and UNION

## Comments for your SQL file:
```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```
