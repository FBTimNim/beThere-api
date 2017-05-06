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

	
<<<<<<< HEAD
class Media(db.Model):
	"""Media table."""
	id = db.Column(db.BigInteger, primary_key=True)
	expiryTime = db.Column(db.DateTime, nullable=False)
	filePath = db.Column(db.Text(), nullable=False)
	lat = db.Column(db.float, nullable=False)
	lon = db.Column(db.float, nullable=False)
	
	
	

=======
>>>>>>> refs/remotes/origin/master
