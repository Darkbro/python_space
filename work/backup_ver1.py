#!/usr/bin/python
#Filename:backup.py
import os
import time
source = [ '/home']
target_dir = '/tmp/backup/'
today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
comment = raw_input('Enter a comment -->')
if len(comment) == 0 :
	target = today + os.sep + now + '.tar.gz'
else:
	target = today + os.sep + now + '_' + comment.replace(' ','_') + '.tar.gz'
if not os.path.exists(today):
	os.mkdir(today)
	print 'MAKE '
#target = today + os.sep+ now + '.zip'
tar_command = " tar -zcvf '%s' %s" % (target, ' '.join(source))
if os.system(tar_command) == 0 :
	print 'Successful backup to ', target
else:
	print 'Failed'
