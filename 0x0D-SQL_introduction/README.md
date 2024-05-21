# INTRODUCTION TO SQL
## Brief overview
###DATABASES
============
Storing data in your application (in memory) has the obvious shortcoming that, whatever the technology you’re using, your data dies when your server stops. Some programming languages and/or frameworks take it even further by being stateless, which, in the case of an HTTP server, means your data dies at the end of an HTTP request. Whether the technology you’re using is stateless or stateful, you will need to persist your data somewhere. That’s what databases are for.

# Basic SQL STATEMENTS: DDL and DML
SQL statements are divided into two major categories: data definition language (DDL) and data manipulation language (DML). Both of these categories contain far more statements than we can present here, and each of the statements is far more complex than we show in this introduction. If you want to master this material, we strongly recommend that you find a SQL reference for your own database software as a supplement to these pages.

## A solid database is expected to to be acid i.e;
** Atomicity: transactions are atomic, which means if a transaction fails, the result will be like it never happened.
Consistency: you can define rules for your data, and expect that the data abides by the rules, or else the transaction fails.
Isolation: run two operations at the same time, and you can expect that the result is as though they were ran one after the other. That’s not the case with the JSON file storage you built: if 2 insert operations are done at the same time, the later one will fetch an outdated collection of users because the earlier one is not finished yet, and therefore overwrite the file without the change that the earlier operation made, totally ignoring that it ever happened.
Durability: unplug your server at any time, boot it back up, and it didn’t lose any data.

## TWO+ KINDS OF DATABASES
When people talk about databases, they’re usually referring to relational databases (such as PostgreSQL, MySQL, Oracle, …); but there are many other kinds of databases used in the industry, which are globally referred to as “NoSQL” databases, even though they can be very different from each other, and serve very various purposes. Also, the name “NoSQL” comes from SQL, which is the name of the syntax used to give orders (CRUD operations, creating and deleting tables, …) to a relational databases; however, some non-relational databases, which are referred to as “NoSQL” give the option to use the SQL syntax. Therefore, the term “NoSQL” is quite controversial to refer to non-relational databases, but it is still widely used.
