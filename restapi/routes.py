"""Provides the routes for the application."""

from datetime import datetime

from flask import Flask, jsonify, request, send_from_directory, url_for
from flask_sqlalchemy import SQLAlchemy

import models
import secure

# Run the application.
app = Flask(__name__)
DEBUG = True

# Directories for uploading media.
app.config['PHOTOS_FOLDER'] = 'media/photos'
app.config['VIDEOS_FOLDER'] = 'media/videos'
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
