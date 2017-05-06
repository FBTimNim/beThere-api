"""Provides the routes for the application."""

from datetime import datetime, timedelta

from flask import Flask, jsonify, request, send_from_directory, url_for
from flask_sqlalchemy import SQLAlchemy

import models
import secure
from utils import api, dates, upload

# Run the application.
app = Flask(__name__)
DEBUG = False

# Directories for uploading media.
app.config['UPLOAD_FOLDER'] = 'media'

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = secure.DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database tables


class Media(db.Model):
    """Media table. Everything is required on create."""

    mediaID = db.Column(db.BigInteger, primary_key=True)

    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)

    path = db.Column(db.Text(), nullable=False)

    active = db.Column(db.Boolean, default=True, nullable=False)

    startDate = db.Column(db.DateTime, nullable=False, default=datetime.now)
    endDate = db.Column(db.DateTime, nullable=False, default=dates.getTomorrow)

# API Views, main route logic.


@app.route("/api/test")
def testConnection():
    """Display simple test route for the API."""
    if request.method == "GET":
        return "You sent a GET request and we received it. Congrats!"
    elif request.method == "POST":
        return "You sent a POST request and we received it. Congrats!"


@app.route('/api/<filename>', methods=["GET"])
def getPhoto(filename):
    """Return file."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/api/uploadMedia', methods=["POST"])
def uploadMedia():
    """Upload media to the host or return error on fail."""
    # Test API key.
    apikey = request.form['apikey']
    if not upload.checkApiKey(apikey):
        return "403 Forbidden: invalid API key.", 403

    # Get form params.
    mediaID = request.form['mediaID']

    lat = request.form['lat']
    lon = request.form['lon']

    try:
        duration = int(request.form['duration'])
    except Exception as e:
        printf("Error: Duration needs to be an int. Using default of 24.")
        duration = 24

    endDate = getIncrement(duration)

    # Get file that has been uploaded.
    media = request.files['media']

    # Filename must be nonempty to be valid.
    if media.filename == '':
        return "Forbidden: cannot upload file with no filename."

    # If there aren't any problems getting the file (empty file).
    if media:
        fn = upload.hashFile(media.filename)
        media.save(os.path.join(app.config['UPLOAD_FOLDER'], fn))

        # Upload renamed file to database.
        newPhoto = Photo(
            lat=lat,
            lon=lon,
            path=app.config['UPLOAD_FOLDER'] + "/" + fn,
            endDate=endDate,
        )

        # Finally, commit to the DB.
        db.session.add(newPhoto)
        db.session.commit()

        return url_for('uploadedFile', filename=fn)
    return "No file has been uploaded.", 400


# Create database tables and commit.
db.create_all()
db.session.commit()
