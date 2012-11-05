#!/usr/bin/python
#Filename:objvar.py
class Person():
	'''Represents a person'''
	population = 0 
	

	def __init__(self,name):
		'''Initialized the person's data'''
		self.name = name
		print '(Initialized  %s)' % self.name
		Person.population += 1
	def __del__(self):
		'''I am dying '''
		print '%s says bye ' % self.name
		Person.population -= 1
		if Person.population == 0:
			print ' I am the last one'
		else:
			print 'There are still %d people left' % Person.population
	def sayHi(self):


