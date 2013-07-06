from src import auth
from src import html
import sys, cgi, json, subprocess

form = cgi.FieldStorage()
try:
	fb_token = form['fb_token']
except KeyError, e:
	fb_token = False

result = auth.verify()
htmlData = '<h1>Nej du!</h1>'
proc = subprocess.Popen('fswebcam -d /dev/video0 -r 640x480 /var/www/motion/cam.jpg', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, htmlData = proc.communicate()
if result:
        #subprocess.call(['/var/www/script/take_picture.sh'])
	htmlData = html.load('main')

jsonData = {'result': result, 'html': htmlData}

print 'Content-Type: application/json\n\n'
print json.dumps(jsonData)

