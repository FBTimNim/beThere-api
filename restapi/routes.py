"""Provides the routes for the application."""

from datetime import datetime

from flask import Flask, jsonify, request, send_from_directory, url_for

import secure
from flask_sqlalchemy import SQLAlchemy

# Run the application.
app = Flask(__name__)
DEBUG = True


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