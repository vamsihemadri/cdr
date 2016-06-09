from pymongo import MongoClient
from datetime import datetime
uri="mongodb://admin2:admin123@localhost/admin?authMechanism=SCRAM-SHA-1"
client=MongoClient(uri)
db=client.adj
cir=db.leaf.find()
for doc in cir:
	print (doc)
