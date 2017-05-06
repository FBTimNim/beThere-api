from PIL import Image, ImageOps, ImageDraw

import requests
from io import BytesIO


def getProfilePic(userID):
	"""Return compressed version of a user's profile pic"""
	#response = requests.get('http://graph.facebook.com/' + userID + '/picture?type=square')

	response = requests.get('http://graph.facebook.com/' + userID + '/picture?type=square')

	im = Image.open(BytesIO(response.content))
	bigsize = (im.size[0] * 3, im.size[1] * 3)
	mask = Image.new('L', bigsize, 0)
	draw = ImageDraw.Draw(mask) 
	draw.ellipse((0, 0) + bigsize, fill=255)
	mask = mask.resize(im.size, Image.ANTIALIAS)
	im.putalpha(mask)
	#im.save('output.png')
	return im
	
#change
	




