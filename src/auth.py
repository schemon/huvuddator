from urllib2 import urlopen
import cgi, json, urllib2


def verify():
	form = cgi.FieldStorage()

	try:
        	fb_token = form['fb_token'].value
	except KeyError, e:
        	fb_token = False
	if fb_token:
		id = getFacebookId(fb_token)
	else:
		id = '0'
	whiteListed = ['601556797', '750142007']
        result = id in whiteListed
	return result

def getFacebookId(fb_token):
	try:	
		jsonStr = urlopen('https://graph.facebook.com/me?access_token=' +fb_token).read()
		content = json.JSONDecoder().decode(jsonStr)
		id = content['id']
	except TypeError as e:
		id = str(e)
	return id

