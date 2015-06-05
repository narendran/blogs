import rethinkdb as r
import time

def get_time():
	return time.time() * 1000 * 1000

connection = r.connect( "localhost", 28015)
try:
	r.db_drop("test_db").run(connection)
	r.db("test_db").table_drop("test_table").run(connection)
except r.RqlRuntimeError, e:
	pass # Ignoring non-existent table drop

r.db_create("test_db").run(connection)
r.db("test_db").table_create("test_table").run(connection)
r.db("test_db").table("test_table").insert([{"a" : 1, "b" : "name", "c" : True}]).run(connection)

i = 0
while i < 1:
	start = get_time()
	r.db("test_db").table("test_table").insert([{"a" : 1, "b" : "name", "c" : True}]).run(connection)
	time_taken = get_time() - start
	print time_taken
	i += 1