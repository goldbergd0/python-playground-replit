import sqlite3

c = sqlite3.connect('test.db').cursor()

# c.execute('create table test("# test","# another")')
c.execute('insert into test("# test", "# another") values (?, ?)', (1,2,))
c.execute("select rowid,* from test")
for r in c.fetchall():
  print(r)