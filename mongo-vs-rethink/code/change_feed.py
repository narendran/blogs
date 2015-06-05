import rethinkdb as r

connection = r.connect( "localhost", 28015)

for change in r.db("test_db").table("test_table").changes().run(connection):
	print change

	