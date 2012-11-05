#!/usr/bin/python
#Filename
import os
import time
target_dir = '/tmp/'
source =  '/etc/my.cnf' 
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = "zip -qr '%s' %s " % ( target, source)
if os.system(zip_command) == 0:
  	print "Successful back up!",target
else:
	print "Back up FAILED"
