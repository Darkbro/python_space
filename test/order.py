#!/usr/bin/python
#Filename:order.py
import os
import sys
def get_dir(path):
	list = os.listdir(path)
	return os.listdir(path)
#for l in list :
#	print the_path.join(path,l)
path = '/home'
print get_dir(path)
print path
print list
#print path.join(path,get_dir(path))
