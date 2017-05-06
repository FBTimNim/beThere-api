beThere-api
===========

REST API backend for the beThere application.

Installation
------------

You first need to setup your database. We use MySQL though any relational DBMS will work as long as you pass in the right credentials. The user should have CRUD permissions and **nothing more**. Note down the credentials and DB information for your application.

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
	-	ROUTE: /api/<filename> PARAMETERS: None.
-	Upload any media:
	-	METHOD: POST
	-	ROUTE: /api/upload
	-	PARAMS:
		-	media: The file.
		-	apikey: Your API key.
		-	lat: Latitude.
		-	lon: Longitude.
		-	type: The type of the file. Must be "photo" or "video".
		-	delay (optional): Number of hours to delay posting the video.
		-	duration (optional): Number of hours to keep the video alive.
