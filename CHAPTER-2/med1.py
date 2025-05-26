from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(2, 3)
print(p.x, p.y)  # Output: 2 3