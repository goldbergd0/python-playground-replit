import json



class ConnectedComponent(object):
  def __init__(self, label, x, y, distance = 0):
    self._x_map = {x: set([y])}
    # self._y_map = {y: set([x])}
    self._x_sum = x
    self._y_sum = y
    self._x2_sum = x*x
    self._y2_sum = y*y
    self.count = 1
    self.points = [(x,y)]
    self.label = label
    self.min_x = x
    self.min_y = y
    self.max_x = x
    self.max_y = y
    self._last_x = x
    self._last_y = y
    self._distance_squared = distance*distance
    self.distance = distance
    self.name = 'base'
    self.properties = {}


  def as_dict(self):
    d = self.__dict__
    for x in self._x_map:
      set_of_y = self._x_map[x]
      self._x_map[x] = []
      for y in set_of_y:
        self._x_map[x].append(y)
    return d


  def from_dict(self, d):
    self.__dict__ = d
    for x in self._x_map:
      list_of_y = self._x_map[x]
      self._x_map[x] = set()
      for y in list_of_y:
        self._x_map[x].add(y)
    for i in range(len(self.points)):
      self.points[i] = tuple(self.points[i])


c = ConnectedComponent(1, 20, 20)
print(c.__dict__)
j = json.dumps(c, default = lambda comp: comp.as_dict())
c2 = ConnectedComponent(1, 1000, 10000)
c2.from_dict(json.loads(j))
print(c2.__dict__)