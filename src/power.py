#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
import subprocess as s
import time
import auth
import json
import cgi
cgitb.enable()

def off():
	s.Popen(["/usr/local/bin/gpio", "-g", "mode", "2", "out"], stdout = s.PIPE)
	s.Popen(["/usr/local/bin/gpio", "-g", "write", "2", "0"], stdout = s.PIPE)
	time.sleep(0.1)
	s.Popen(["/usr/local/bin/gpio", "-g", "write", "2", "1"], stdout = s.PIPE)
	return True
def on():
	s.Popen(["/usr/local/bin/gpio", "-g", "mode", "3", "out"], stdout = s.PIPE)
	s.Popen(["/usr/local/bin/gpio", "-g", "write", "3", "0"], stdout = s.PIPE)
	time.sleep(0.1)
	s.Popen(["/usr/local/bin/gpio", "-g", "write", "3", "1"], stdout = s.PIPE)
	return True

def changeLight(action):
	if action == 'on':
		result = on()
	elif action == 'off':
		result = off()
	else:
		result = False
	return result

def getAction():
        form = cgi.FieldStorage()
        try:
                action = form['action'].value
        except KeyError, e:
                action = 'unknown'
	return action

action = getAction()
if auth.verify():
        result = changeLight(action)
else:
        result = False

jsonData = {'result': result, 'action': action}
print 'Content-Type: application/json\n\n'
print json.dumps(jsonData)

