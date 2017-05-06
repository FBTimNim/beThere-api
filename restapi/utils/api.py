"""API utils."""

import hashlib
import os
import random
import string
from datetime import datetime

HASHTYPE = hashlib.sha256()
APIKEY_FILE = "api.keys"
ENTROPY = 64


def checkApiKey(apikey):
    """Check if an api key provided is good."""
    with open(APIKEY_FILE, 'r') as f:
        for j in [str(i.rstrip()) for i in f.readlines()]:
            if j == apikey.rstrip():
                return True
        return False


def hashAPI(size):
    """Insecurely generate a random string of n size."""
    chooseFrom = string.ascii_uppercase + string.ascii_lowercase + \
        string.digits
    chars = [random.SystemRandom().choice(chooseFrom) for _ in range(size)]

    return str(''.join(chars))


def touch(fname):
    """Add empty file if it does not exist. Credit to SilentGhost on SO."""
    if os.path.exists(fname):
        os.utime(fname, None)
    else:
        open(fname, 'a').close()


def addApiKey():
    """Add an API key to the api key file."""
    touch(APIKEY_FILE)

    with open(APIKEY_FILE, "a") as f:
        key = hashAPI(ENTROPY)
        f.write(key + '\n')

        return key
