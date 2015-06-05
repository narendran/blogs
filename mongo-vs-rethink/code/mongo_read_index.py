from bson.objectid import ObjectId
import pymongo
import time

client = pymongo.MongoClient()
db = client.test_db
coll1 = db.test_collection1
coll = db.test_collection

def get_time():
	return time.time() * 1000 * 1000

i = 0
while i < 1000:
	docs = list(coll1.find()) # To avoid cache hits while reading test_collection
	count = len(docs) # Confirm load to memory
	start = get_time()
	coll.find({"_id" : ObjectId("5571b95544b7942d5246bf92")}) # Reading from another collection
	time_taken = get_time() - start
	print time_taken
	i += 1

client.close()

