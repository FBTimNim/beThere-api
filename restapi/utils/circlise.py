"""Make images circles."""

import base64
from io import BytesIO
from urllib import request

from PIL import Image, ImageDraw, ImageOps

from . import upload


def getProfilePic(userID):
    """Return compressed version of a user's profile pic."""
    # Get profile image from Facebook.
    try:
        response = request.urlopen('http://graph.facebook.com/' +
                                   str(userID) + '/picture?type=square')
    except Exception as e:
        return ""

    # Make the image a circle.
    im = Image.open(BytesIO(response.read()))
    bigsize = (im.size[0] * 3, im.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(im.size, Image.ANTIALIAS)
    im.putalpha(mask)

    fn = upload.hashFile('hardcoding_hullo.png')

    # Save the file as a base 64 string.
    im.save('/media/thumbs/' + fn, format="PNG")

    return "/media/thumbs/" + fn
