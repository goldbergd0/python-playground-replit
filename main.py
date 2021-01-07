import sqlite3
import random



def create_insert_string(table_name, columns):
  names = '('
  names += ','.join(columns)
  names += ')'
  vals = '('
  vals += ','.join('?' for c in columns)
  vals += ')'
  return 'INSERT INTO {}{} VALUES {}'.format(table_name, names, vals)


c = sqlite3.connect('test.db', isolation_level=None).cursor()

c.execute('create table test2(test,another)')
c.execute('insert into test("# test", "# another") values (?, ?)', (1,random.randint(1,10),))
c.execute('select MAX(\"# another\") from test2 where \"# another\" > 2 order by \"# another\" ASC;')
r = c.fetchone()
while r:
  print(r[0])
  r = c.fetchone()

print(create_insert_string('TEST_NAME', ['col1', 'col2', 'col3']))