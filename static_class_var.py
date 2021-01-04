class Test(object):
  print('this happens once!')
  counter = 0
  def __init__(self):
    self.counter = self.counter + 1
    print('this happens each time it\'s created: {}'.format(self.counter))

def tester(t):
  t.counter=10

d1 = Test()
print(d1.counter)
tester(d1)
print(d1.counter)
a = d1.counter if d1.counter > 10 else 100000
print(a)