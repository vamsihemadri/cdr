from collections import OrderedDict
from pymongo import MongoClient
from datetime import datetime
uri="mongodb://admin2:admin123@localhost/admin?authMechanism=SCRAM-SHA-1"
client=MongoClient(uri)
st=datetime.now()
db=client.adj
i1=datetime.now()
cursor=db.adj9.find({"delete":0})
to_be_deleted=list()
d=[]	
i=0
for c in cursor:
	i=i+1
	if(i%1000==0):
		print (i)
	d=c['called']
	print (i)
	v=set()
	flag=0
	for f in d:
		v.add(f)
		k=f/1000000000
		k=int(k)
		find_leaf=db.leaf.find({"caller":f})
		if(not(find_leaf.count()==0)):
			for document in find_leaf:
				if(not(document['delete']==0)):
					flag=1
					to_be_deleted.append(c['caller'])
					break
				else:
					v.add(f)
		else:
			if (k==7):
				finder=db.adj7.find({"caller":f})
			#print("7")
			elif(k==8):
				finder=db.adj8.find({"caller":f})
			#print("8")
			else:
				finder=db.adj9.find({"caller":f})
			#print("9")
			for doc in finder:
				if (doc['delete']==0):
					numb=doc['called']
					for n in numb:
						v.add(n)
				elif( doc['delete']==1 or doc['delete']==2):
					c.update({'delete':3})
					to_be_deleted.append(c['caller'])
					flag=1
					break
		if(flag==1):
			break
                        #g1=g['called']
                        #db.rcb.update_one({"caller":c['caller']},{"$addToSet":{"called":{"$each":g1}}})
	s=list(v)
	c.update({'called':s})
	if(len(s)>10):
		to_be_deleted.append(c['caller'])
	c.update({'count':len(v)})
	db.adj8.save(c)
with open('numbers_to_delete9.txt','a+') as f:
        for v1 in to_be_deleted:
                f.write("{}\n".format(v1))
et1=datetime.now()
print ("the start time is {}".format(st))
print ("the start time for indexing is {}".format(i1))
#print ("the end time for indexing is {}".format(i2))
print ("the time to expand  is {}".format(et1))
#print ("the end time is {}".format(et))
