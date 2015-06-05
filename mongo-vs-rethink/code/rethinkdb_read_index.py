import rethinkdb as r
import time

def get_time():
	return time.time() * 1000 * 1000

connection = r.connect( "localhost", 28015)

i = 0
while i < 1000:
	# docs = list(r.db("test_db").table("test_table1").run(connection))
	# count = len(docs)
	start = get_time()
	r.db("test_db").table("test_table").get("00ff4bf6-9f4a-487b-92e1-cb4c8d81263d").run(connection)
	time_taken = get_time() - start
	print time_taken
	i += 1