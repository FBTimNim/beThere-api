"""Provides the routes for the application."""

from datetime import datetime, timedelta

from flask import Flask, jsonify, request, send_from_directory, url_for
from flask_sqlalchemy import SQLAlchemy

import secure
from utils import api, dates, response, upload

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
    mediaType = db.Column(db.Text, nullable=False)

    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)

    filename = db.Column(db.Text(), nullable=False)
    uid = db.Column(db.Text(), nullable=False)

    active = db.Column(db.Boolean, default=True, nullable=False)

    startDate = db.Column(db.DateTime, nullable=False)
    endDate = db.Column(db.DateTime, nullable=False)

# API Views, main route logic.


@app.route('/api/<filename>', methods=["GET"])
def getPhoto(filename):
    """Return file."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/api/upload', methods=["POST"])
def uploadMedia():
    """Upload media to the host or return error on fail."""
    # Test API key.
    apikey = request.form['apikey']
    if not upload.checkApiKey(apikey):
        return jsonify(notOkay(403, "Access denied. Incorrect API key."))

    # Get form params.
    mediaID = request.form['mediaID']
    mediaType = request.form['type']

    lat = request.form['lat']
    lon = request.form['lon']

    try:
        delay = int(request.form['delay'])
        duration = int(request.form['duration'])
    except Exception as e:
        # Use defaults.
        delay = 0
        duration = 24

    startDate = getIncrement(delay)
    endDate = getIncrement(duration + delay)

    # Get file that has been uploaded.
    media = request.files['media']

    # Filename must be nonempty to be valid.
    if media.filename == '':
        return jsonify(notOkay(403, "Cannot upload without a filename."))

    # If there aren't any problems getting the file (empty file).
    if media:
        fn = upload.hashFile(media.filename)
        media.save(os.path.join(app.config['UPLOAD_FOLDER'], fn))

        # Upload renamed file to database.
        newPhoto = Photo(
            lat=lat,
            lon=lon,
            filename=fn,
            startDate=startDate,
            endDate=endDate,
        )

        # Finally, commit to the DB.
        db.session.add(newPhoto)
        db.session.commit()

        return {
            "code": 200,
            "message": "OK.",
            "data": []
        }, 200

    return jsonify(notOkay(400, "No file has been uploaded"))


@app.route('/api/getRelevant')
def getRelevant():
    """Return all of the relevant pins in the database."""
    returnVal = dict()
    allRelevant = list()

    for i in Media.query.filter_by(active == 1):
        print(i)  # Debug

        allRelevant.append(i)

    returnVal["code"] = 200
    returnVal["message"] = "OK."
    returnVal["data"] = allRelevant

    return jsonify(returnVal)


# Create database tables and commit.
db.create_all()
db.session.commit()
