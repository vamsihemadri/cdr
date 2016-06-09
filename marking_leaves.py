from pymongo import MongoClient
#uri=devuser@159.203.92.25/authenticationDatabase:admin
uri="mongodb://admin2:admin123@localhost/admin?authMechanism=SCRAM-SHA-1"
client=MongoClient(uri)
db=client.adj
with open("second_leaves.txt",'r') as f:
	content=f.read()
	liness=content.split("\n")
	i=0
	for lines in liness:
		i=i+1
		print (i)
		number=int(lines[1:11])
		print (number)
		curr=db.leaf.find({"caller":number})	
		for doc in curr:
			doc.update({"delete":1})
			db.leaf.save(doc)
	
