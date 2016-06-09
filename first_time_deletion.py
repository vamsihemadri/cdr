from pymongo import MongoClient
from datetime import datetime
uri="mongodb://admin2:admin123@localhost/admin?authMechanism=SCRAM-SHA-1"
client=MongoClient(uri)
db=client.adj
i1=datetime.now()
i=0
cursor=db.full.find({"delete":2})
for doc in cursor:
	i=i+1
	if(i%500==0):
		print i
	doc.update({"delete":1})
	for numb in doc['called']:
		curr=db.full.find({"caller":numb})
		for doc1 in curr:
			doc1.update({"delete":2})
			db.full.save(doc1)
e1=datetime.now()
print i1
print e1		

		
		
			
