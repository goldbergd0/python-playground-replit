import sqlite3
import random

c = sqlite3.connect('test.db', isolation_level=None).cursor()

# c.execute('create table test("# test","# another")')
c.execute('insert into test("# test", "# another") values (?, ?)', (1,random.randint(1,10),))
c.execute("select * from test where \"# another\" > 2 order by \"# another\" ASC;")
r = c.fetchone()
while r:
  print(r)
  r = c.fetchone()