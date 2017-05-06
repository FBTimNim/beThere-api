"""Libs for uploading to the server."""
import hashlib
import os
import random
import string
from datetime import datetime

HASHTYPE = hashlib.sha256()


def genRandomString():
    """Generate a random string."""
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))


def hashFile(filename):
    """Hash a filename depending on filename and datetime."""
    utcTime = str(datetime.utcnow()) + genRandomString()
    inputStr = filename.split('.')[0] + utcTime
    HASHTYPE.update(inputStr.encode())

    return HASHTYPE.hexdigest()[:16] + '.' + filename.split('.')[1]
