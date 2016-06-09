from pymongo import MongoClient
from datetime import datetime
uri="mongodb://admin2:admin123@localhost/admin?authMechanism=SCRAM-SHA-1"
client=MongoClient(uri)
db=client.adj
i1=datetime.now()
cursor=db.full.find()
i=0
for doc in cursor:
	i=i+1
	if(i%1000==0):
		print i
	for n in doc['called']:
		curr=db.adj.find({"caller":n})
		if(curr.count()==0):
			db.full.insert({"caller":n,"leaf":1,"delete":0})
e1=datetime.now()
print "the start time ois {}".format(i1)
print "the enf ritme os {}".format(e1)
			
