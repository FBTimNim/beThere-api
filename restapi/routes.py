"""Provides the routes for the application."""

from datetime import datetime

from flask import Flask, jsonify, request, send_from_directory, url_for
from flask_sqlalchemy import SQLAlchemy

import models
import secure

# Run the application.
app = Flask(__name__)
DEBUG = False

# Directories for uploading media.
app.config['PHOTO_FOLDER'] = 'media/photos'
app.config['VIDEO_FOLDER'] = 'media/videos'
app.config['MUSIC_FOLDER'] = 'media/music'

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = secure.DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app, use_native_unicode=True)

# API Views, main route logic.


@app.route("/api/test")
def testConnection():
    """Display simple test route for the API."""
    if request.method == "GET":
        return "You sent a GET request and we received it. Congrats!"
    elif request.method == "POST":
        return "You sent a POST request and we received it. Congrats!"


@app.route('/api/photo/<filename>', methods=["GET"])
def getPhoto(filename):
    """Return photo of an event."""
    return send_from_directory(app.config['PHOTO_FOLDER'], filename)


@app.route('/api/video/<filename>', methods=["GET"])
def getVideo(filename):
    """Return video of an event."""
    return send_from_directory(app.config['VIDEO_FOLDER'], filename)


@app.route('/api/music/<filename>', methods=["GET"])
def getMusic(filename):
    """Return music of an event."""
    return send_from_directory(app.config['MUSIC_FOLDER'], filename)

@app.route('/api/uploadMedia', methods=["POST"])
def uploadMedia():
	"""create an event and upload media to the host. return error if fails"""

	mediaType = request.form['mediaType']
	lat = request.form['lat']
	lon = request.form['lng']
	mediaID = request.form['mediaID']
	media = request.files['media']

	return 'Nothing.'
