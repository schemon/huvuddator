#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
import subprocess as s
import time
import json

cgitb.enable()


print json.dumps({"success":1})
s.Popen(["/usr/local/bin/gpio", "-g", "mode", "3", "out"], stdout = s.PIPE)
s.Popen(["/usr/local/bin/gpio", "-g", "write", "3", "0"], stdout = s.PIPE)
time.sleep(0.1)
s.Popen(["/usr/local/bin/gpio", "-g", "write", "3", "1"], stdout = s.PIPE)

