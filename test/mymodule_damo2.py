#!/usr/bin/python
#Filename:mymodule_damo2.py
import sys
for i in sys.argv:
 	print i
from mymodule import sayhi,version
sayhi()
print 'Version', version
