from src import auth
from src import html
import sys, cgi, json

form = cgi.FieldStorage()
try:
	fb_token = form['fb_token']
except KeyError, e:
	fb_token = False

result = auth.verify()
htmlData = '<h1>Nej du!</h1>'
if result:
	htmlData = html.load('main')

jsonData = {'result': result, 'html': htmlData}

print 'Content-Type: application/json\n\n'
print json.dumps(jsonData)

