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

After you have done this, you will need to edit the contents of the `secure.py` file. Move it from `secure.py.example` if it doesn't yet exist.

Finally, ensure you have a working API key for your clientside applications. Do this by running `python run.py newapikey`. Make sure to note down what it prints. You can also `cat api.keys` at any time to see all the valid API keys.

You can start the server (to test) using the command line:

```bash
python run.py start 0.0.0.0:8080
```

This will start a server on 0.0.0.0:8080.

Usage
-----

See API documentation below for API calls. For

API Documentation
-----------------

To get photos, videos, and music, use one of the following API calls:

-	Get any media:
	-	METHOD: GET
	-	ROUTE: /api/<filename> PARAMETERS: None.
