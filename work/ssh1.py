#!/usr/bin/env python
#coding utf-8

import pexpect
import os,os.path
import sys

def usage():
	print "Get the ip user passwd :"
	info = ("ip","user","passed")
	fd = open('/tmp/test.txt','r')
	line = fd.readline()
	line.split()
	strin = raw_input()
	if strin == ip:
	ssh_login()
	else:
		print "the %s is not exists:",strin	
def ssh_login(ip, user, passwd):
	child = pexpect.spwan('ssh -l %s %s'%(user,ip))
	
		
