"""Make images circles."""

import base64
from io import BytesIO
from urllib import request

from PIL import Image, ImageDraw, ImageOps


def getProfilePic(userID):
    """Return compressed version of a user's profile pic."""
    # Get profile image from Facebook.
    response = request.urlopen('http://graph.facebook.com/' +
                               str(userID) + '/picture?type=square')

    # Make the image a circle.
    im = Image.open(BytesIO(response.read()))
    bigsize = (im.size[0] * 3, im.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(im.size, Image.ANTIALIAS)
    im.putalpha(mask)

    # Save the file as a base 64 string.
    buffer = BytesIO()
    im.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue())

    return img_str
