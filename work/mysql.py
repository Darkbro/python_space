#!/usr/bin/env python
#coding utf-8
import MySQLdb
connection = MySQLdb.connect(user="root",passwd="root",host="localhost",db="test")
cursor=connection.cursor()
sql = "INSERT INTO python VALUES('1','ZXC'),('45','CC')"
cursor.execute("SELECT * FROM python")
cursor.execute(sql)
sql = "SELECT * FROM python"
cursor.execute(sql)
print "The info:",cursor.rowcount
for row in cursor.fetchall():
	print ":",row
cursor.close()
