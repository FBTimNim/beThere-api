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
@app.route('/api/photo/<filename>', methods=["GET"])
def getPhoto(filename):
	"""return photo of an event"""
	return send_from_directory(app.config['PHOTO_FOLDER'], filename)
	
@app.route('/api/video/<filename>', methods=["GET"])
def getVideo(filename):
	"""return video of an event"""
	return send_from_directory(app.config['VIDEO_FOLDER'], filename)
	
@app.route('/api/music/<filename>', methods=["GET"])
def getMusic(filename):
	"""return music of an event"""
	return send_from_directory(app.config['MUSIC_FOLDER'], filename)
	
<<<<<<< HEAD
class Media(db.Model):
	"""Media table."""
	id = db.Column(db.BigInteger, primary_key=True)
	expiryTime = db.Column(db.DateTime, nullable=False)
	filePath = db.Column(db.Text(), nullable=False)
	lat = db.Column(db.float, nullable=False)
	lon = db.Column(db.float, nullable=False)
	
	
	
"""	
@app.route('/api/event', methods=["POST"])
def uploadMedia():
	""""""create an event and upload media to the host. return error if fails"""""""
	mediaType = request.form['mediaType']
	lat = request.form['lat']
	lon = request.form['lng']
	mediaID = request.form['mediaID']
	media = request.files['media']
	
	"""
=======
>>>>>>> refs/remotes/origin/master
