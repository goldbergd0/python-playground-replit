import sqlite3
import random



def create_insert_string(table_name, columns):
  names = '('
  names += ','.join(columns)
  names += ')'
  vals = '('
  vals += ','.join('?' for c in columns)
  vals += ')'
  return 'INSERT INTO {}{} VALUES {};'.format(table_name, names, vals)


c = sqlite3.connect('test.db', isolation_level=None).cursor()

# c.execute('create table test2(test,another)')
c.execute('insert into test("# test", "# another") values (?, ?);', [1,random.randint(1,10),])
c.execute('select rowid,* from test;')
r = c.fetchone()
while r:
  print(r)
  r = c.fetchone()
c.execute('SELECT name FROM sqlite_master WHERE type="table";')
print(c.fetchall())
c.execute('SELECT * FROM test LIMIT 1;')
for d in c.description:
  print(d[0])

print(create_insert_string('TEST_NAME', ['col1', 'col2', 'col3', 'COL4'.lower()]))