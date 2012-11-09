#!/usr/bin/python
#Filename:auto_bak.py
import os
import sys
def get_dir(path):
	print path,'\n'
	return os.listdir(path)
def bak_file(path,path_bak):
	list = os.listdir(path)
for l in list:
	file_path = os.path.join(path,l)
	file_path_bak = os.path.join(path_bak,l)
	print file_path
#if os.path.isdir(file_path):
if not os.path.isdir(file_path_bak):
	create_com = '''mkdir -p '%s' '''%(file_path_bak)
if os.system(create_com == 0):
	print create_com
else:
	print 'create file failure!'
	os.exit(0)
bak_file (file_path,file_path_bak)
#else:
if os.path.isfile(file_path_bak):
	stat_bak = os.stat(file_path_bak)
	stat_source = os.stat(file_path)
if stat_sorce.st_mtime <= stat_bak.st_mtime:
#	continue
	cp_com = '''cp '%s' '%s' '''%(file_path,file_path_bak)
if os.system(cp_com ==0 ):
	print cp_com
else:
	print 'create folder failure !'
	os.exit(0)
path = '/etc/my.cnf'
path_bak = '/tmp/bak'
bak_file(path,path_bak)
