#!/usr/bin/python
#Filename:func_doc.py
def printMax(x,y):
	'''Prints the maximum of two numbers.
	The teo values must be integer.'''
    	x = int(x)
 	y = int(y)
  	if x > y:
		print x
	else:
		print y
printMax(3,5)
print printMax.__doc__
