# Tuple : Ordered, immutable, allows duplicate Elements

myTuple = ('Max', 25, "James", 'Sam', 5.2j, 4.59, False)
print(myTuple)

tuple = tuple([5, 8, 4, 'j'])
print(tuple)

print(tuple[2], tuple[-1])


# Same as List

name, age, city, Kanha = tuple  # Must match the item numbers in Tuple
print(name, age, city, Kanha)


# Comparing Liat and Tuple

# Memory Size
import sys
list = [0, 1, 2, "hello", True]
tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(list), "bytes")
print(sys.getsizeof(tuple), "bytes")

# Execution Time
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
