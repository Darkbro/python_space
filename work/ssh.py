#!/usr/bin/python
#-*- coding: UTF-8 -*-
	
import pexpect
import os,os.path
import stat
import getpass
import sys
import getopt
import socket
from ConfigParser import ConfigParser
#import subprocess
	
def usage():
	print '\nUsage: ssh.py hostname'
	    system.exit(0)

	def load_config():
	    cfg_path = os.path.join(os.environ["HOME"], ".ssh.cfg")
	    cfg_temp = '''[connects]
	user   = 
	id_rsa = 
	'''
	    if not os.path.exists(cfg_path):
	        open(cfg_path, 'w').write(cfg_temp)
	#    os.chmod(cfg_path, stat.S_IREAD)
	    cfg = ConfigParser()
	    cfg.read(cfg_path)
	    user   = cfg.get('connects', 'user')
	    id_rsa = cfg.get('connects', 'id_rsa', 'True')
	    return (user,id_rsa)
	
	def ssh_login (user, host, id_rsa):
	    ssh_newkey = 'Are you sure you want to continue connecting'
	    try:
	        child = pexpect.spawn('ssh -l %s %s '%(user, host))
	        child.expect([pexpect.TIMEOUT, ssh_newkey, 'password: ', "id_rsa': "])
	        child.sendline(id_rsa)
	        # 预知chr(26)的含义,请查看ASCII码对照表,字符一列.
	        child.interact(chr(26))
	        print "\n"
	    except:
	        print "interact error"
	        sys.exit(0)
	
	def main ():
	    if len(sys.argv) == 1:
	        load_config()
	        usage()
	
	    # load file
	    user,id_rsa = load_config()
	
	    if user == '':
	        usage()
	    elif id_rsa == '':
	        usage()
	    else:
	        pass
	    #host    = raw_input('hostname: ')
	    host = sys.argv[1]
	#    print host
	    # use `ping` to check if the host is available now
	    # 用ping的方式测试主机是否存在
	    try:
	        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	        sock.settimeout(3)
	        sock.connect((host, 22))
	        sock.close()
	    except:
	        print 'ping: unknown host %s' % (host)
	        sys.exit(0)
	    # ssh 
	    ssh_login(user, host, id_rsa)
	
	if __name__ == '__main__':
	    try:
	        main()
	    except Exception, e:
	        print str(e)
 	        os._exit(1)

