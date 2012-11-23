#!/usr/bin/python

import pymongo
import random

conn = pymongo.Connection("127.0.0.1",27017)
db = conn.tage
db.authenticate("admin","admin")
db.user.drop()
db.user.save({'id':1,'name':'kaka','sex':'male'})
for id in range(2,10):
    name = random.choice(['steve','koby','owen','tody','rony'])
    sex = random.choice(['male','female'])
    db.user.insert({'id':id,'name':name,'sex':sex}) 
content = db.user.find()
for i in content:
    print i

