import collections

def get_line(s):
  for i in s:
    yield i

prev_lines = collections.deque()
lines = ['10000', '20000', '30000', '40000', '50000', '60000']
prev_lines.appendleft('d')
prev_lines.appendleft('c')
prev_lines.appendleft('b')
prev_lines.appendleft('a')
test = [i + '_dan' for i in prev_lines]
print(test)

for l in get_line(lines):
  for pl in prev_lines:
    l += '\n' + pl
  print(l)
for l in reversed(lines):
  print(l)

try:
  with open('asdflk') as test:
    print("don't care")
except IOError as e:
  print(e)