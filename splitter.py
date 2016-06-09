from datetime import datetime
from pymongo import MongoClient
uri="mongodb://admin2:admin123@localhost/admin?authMechanism=SCRAM-SHA-1"
client=MongoClient(uri)
i1=datetime.now()
db=client.adj
with open("tovamsi1.txt",'r') as f:
	content=f.read()
	liness=content.split('\n')
	for i,lines in enumerate(liness):
		print (i)
#		print (lines[i][0])
		if (lines[1]=='7'):
			#print("stark")
			curr=db.adj7.find({"caller":int(lines[1:11])})
			for doc in curr:
				doc.update({'delete':1})
				db.adj7.save(doc)
		elif (lines[1]=='8'):
                       # print("stark")
                        curr=db.adj8.find({"caller":int(lines[1:11])})
                        for doc in curr:
                                doc.update({'delete':1})
                                db.adj8.save(doc)
		elif (lines[1]=='9'):
                        #print("stark")
                        curr=db.adj9.find({"caller":int(lines[1:11])})
                        for doc in curr:
                                doc.update({'delete':1})
                                db.adj9.save(doc)
et=datetime.now()
print (et)
print (i1)
