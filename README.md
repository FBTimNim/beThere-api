beThere-api
===========

REST API backend for the beThere application.

Installation
------------

You first need to setup your database. We use MySQL though any relational DBMS will work as long as you pass in the right credentials. The user should have CRUD permissions and **nothing more**. Note down the credentials and DB information for your application.

The database schema is shown below:

```sql

DROP TABLE IF EXISTS `Media`;
CREATE TABLE IF NOT EXISTS `Media` (
  mediaId INT,
  lat DOUBLE,
  lon DOUBLE,
  path VARCHAR(300),
  type ENUM('photo', 'video', 'music')
);

```
