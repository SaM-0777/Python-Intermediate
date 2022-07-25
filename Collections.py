# Collections : Counter, namedtuple, OrderedDict, defaultDict, dequeue


# Counter
from collections import Counter
a = "aaaaaabbbbbbbbdddddddccccc"
my_Counter = Counter(a)
print(my_Counter.keys())
print(my_Counter.values())
print(my_Counter.most_common(2)[0][0])
print(list(my_Counter.elements()))


# NamedTuple
from collections import namedtuple
Point = namedtuple('Point', 'x, y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)


# Ordered Dict
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 2
ordered_dict['b'] = 3
ordered_dict['e'] = 4
ordered_dict['d'] = 1
print(ordered_dict)


# defultDict
from collections import defaultdict
d = defaultdict(int)    # Maybe float
d['a'] = 1
d['d'] = 5
d['c'] = 3
d['b'] = 4
print(d['c'], "\t", d['f'])


# Deqeue
from collections import deque
d = deque()

d.append(2)
d.append(5)
d.append(1)
print(d)

d.appendleft(4)
print(d)

print(d.pop())
print(d)

print(d.popleft())
print(d)

d.extend([7, 5, 6, 8, 10])
print(d)
d.extendleft([8, 1, 4, 6])
print(d)

d.rotate(1)
print(d)
d.rotate(2)
print(d)
d.rotate(-1)
print(d)
d.remove(4)
print(d)
d.clear()
print(d)