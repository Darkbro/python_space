#!/usr/bin/env python
#_*_coding: utf-8 _*_
import pexpect

def ssh_cmd(ip, passwd, cmd):
#	ret = -1
	ssh = pexpect.spwan('ssh root@%s' % (ip, cmd))
	i = ssh.expect(['password:','continue connecting (yes/no)?'], timeout=5)
	if i == 0 :
		ssh.sendline(passwd)
	elif i == 1 :
		ssh.sendline('yes\n')
		ssh.expect('password:')
		ssh.sendline(passwd)
	ssh.sendline(cmd)
	r = ssh.read()
	print r
#	ret = 0
#	expect pexpect.EOF:
	print "EOF"
	ssh.close()
	ret = -1
#	expect pexpect.TIMEOUT:
	print "TIMEOUT"
	ssh.close()
#		ret = -2
#	return ret
