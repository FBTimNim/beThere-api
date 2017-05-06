"""Provides the routes for the application."""

from datetime import datetime

from flask import Flask, jsonify, request, send_from_directory, url_for

import secure
from flask_sqlalchemy import SQLAlchemy

# Run the application.
app = Flask(__name__)
DEBUG = True
