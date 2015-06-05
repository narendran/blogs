import pymongo
import time

client = pymongo.MongoClient(w=1, j = True)
db = client.test_db
coll = db.test_collection

def get_time():
	return time.time() * 1000 * 1000

# Drop collection if exists. Create a single document to create the required files 
# because we want to capture real-world usage scenario.
coll.drop()
doc = {"a" : 1, "b" : "name", "c" : True}
coll.insert(doc)

i = 0
while i < 1000:
	# Reinitializing doc to avoid _id index conflict. pymongo stores the persisted document in "doc"
	doc = {"a" : 1, "b" : "name", "c" : True}
	start = get_time()
	coll.insert(doc)
	time_taken = get_time() - start
	print time_taken
	i += 1

client.close()