from bson.objectid import ObjectId
import pymongo
import time

client = pymongo.MongoClient()
db = client.test_db
coll1 = db.test_collection1
coll = db.test_collection
f = open('workfile', 'w')

def get_time():
    return time.time() * 1000 * 1000

i = 0
while i < 1000:
    # docs = list(coll1.find()) # To avoid cache hits while reading test_collection
    # docs = [docs] * 10
    # Ensuring no auto-optimizations are done.
    # f.write(str(docs))
    start = get_time()
    coll.find_one({"_id" : ObjectId("5572065f44b79464a3837e10")}) # Reading from another collection
    time_taken = get_time() - start
    print time_taken
    i += 1

client.close()

