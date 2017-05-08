beThere-api
===========

REST API backend for the beThere application.

> Tied third place at Facebook Melbourne Hackathon 2017!

Installation
------------

You first need to setup your database. We use MySQL though any relational DBMS will work as long as you pass in the right credentials. The user should have CRUD permissions and the ability to create and drop tables. Note down the credentials and DB information for your application.

The database schema is shown in the `backend.py` file.

After you have done this, you will need to edit the contents of the `secure.py` file. Move it from `secure.py.example` if it doesn't yet exist.

Finally, ensure you have a working API key for your clientside applications. Do this by running `python run.py newapikey`. Make sure to note down what it prints. You can also `cat api.keys` at any time to see all the valid API keys.

You can start the server (to test) using the command line:

```bash
python run.py start 0.0.0.0:8080
```

This will start a server on 0.0.0.0:8080.

API Documentation
-----------------

To get photos and videos use one of the following API calls:

-	Get any media:
	-	METHOD: GET
	-	ROUTE: /api/media/<filename> PARAMETERS: None.
-	Upload any media:
	-	METHOD: POST
	-	ROUTE: /api/upload
	-	PARAMS:
		-	media: The file.
		-	apikey: Your API key.
		-	lat: Latitude.
		-	lon: Longitude.
		-	uid: Facebook user id of authenticated user.
		-	type: The type of the file. Must be "photo" or "video".
		-	delay: Number of hours to delay posting the video.
		-	duration: Number of hours to keep the video alive.
	-	RESPONSE: Simple JSON object.
-	Get relevant media:
	-	METHOD: POST
	-	ROUTE: /api/getRelevant
	-	PARAMS:
		-	apikey: Your API key.
		-	withinTime: Number of hours to check back for photos. I suggest a default of 1. This will round up!
		-	Right now this is heavily hardcoded but obviously would need some sort of processing in the future.
	-	RESPONSE: JSON response object:
		-	url: URL of the media.
		-	thumbUrl: URL of the circle thumbnail.
		-	type: Media type. Must be "photo" or "video".
		-	lat: Latitude.
		-	lon: Longitude.
		-	uid: User ID of the person who posted the image.
