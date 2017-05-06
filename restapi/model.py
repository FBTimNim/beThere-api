class Media(db.Model):
	"""Media table."""
	id = db.Column(db.BigInteger, primary_key=True)
	expiryTime = db.Column(db.DateTime, nullable=False)
	filePath = db.Column(db.Text(), nullable=False)
	lat = db.Column(db.float, nullable=False)
	lon = db.Column(db.float, nullable=False)
	