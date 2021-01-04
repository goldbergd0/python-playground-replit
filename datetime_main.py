import datetime

def parse(s):
  return datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S.%f'), 'from s', 'another test'

now = datetime.datetime.now()
print('Start: {}'.format(now))
all_td = datetime.timedelta()
for i in range(10):
  print(all_td)
  td = datetime.timedelta(minutes=(10*i))
  all_td += td
  print('added td: {}'.format(td))
print('finish td: {}'.format(all_td))

try:
  timestamp = datetime.datetime.strptime('1234-51-12 15124014', '%Y-%m-%d')
except ValueError as e:
  print(e)

print('Datetime timedelta:')
dt = datetime.datetime.now()
dt2 = datetime.datetime.now()
print((dt2-dt).days)