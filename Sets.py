# Sets : Unoredered, mutable, no Duplicates
mySet = {1, 4, 4, 1, 3, 6}
print(mySet)

mySet = set("Hello")
print(mySet)

mySet.add(10)
mySet.add(20)
mySet.add(30)
print(mySet)

mySet.remove(10)
""" mySet.remove(5) """
print(mySet)


odds = {1, 3, 5, 7, 9}
even = {2, 4, 6, 8, 0}
primes = {2, 3, 5, 7}

# Union
U = odds.union(even)
print(U)

# Intersection
I = odds.intersection(even)
print(I)

I = odds.intersection(primes)
print(I)


# Difference
diff = odds.difference(primes)
print(diff)

diff = odds.symmetric_difference(primes)
print(diff)


# Update
odds.update(primes)
print(odds)

even.intersection_update(primes)
print(even)

primes.difference_update(even)
print(primes)

even.symmetric_difference_update(primes)
print(even)

# Subset
print(even.issubset(primes))
print(even.issuperset(odds))

# Disjoints
print(even.isdisjoint(primes))

# Copy sets
odds = even # points to same set
print(odds)

even = odds.copy()
print(even)

even = set(odds)
print(even)

# Frozen set : immutable
a = frozenset([1, 2, 4, 5])
a.add(3)
a.remove(2)
print(a)