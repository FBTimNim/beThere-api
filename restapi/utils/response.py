"""Process responses for the route functions."""


def okay(obj, filetype, updir="media"):
    """Return okay python dict."""
    d = {
        "code": 200,
        "data": [
            {
                "url": "/" + updir + "/" + obj.filename,
                "message": "OK.",
                "type": obj.mediaType,
                "uid": obj.uid,
                "lat": obj.lat,
                "lon": obj.lon,
            }
        ]
    }

    return d


def notOkay(code, message):
    """Return failed python dict."""
    d = {
        "code": code,
        "message": message,
        "data": []
    }

    return d
