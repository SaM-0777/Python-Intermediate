# lambda arguments : expression
add10 = lambda x: x + 10
print(add10(5))


mult = lambda x, y : x * y
print(mult(2, 4))

# Used when function take function as arg


Points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
Points2D_sorted = sorted(Points2D)

print(Points2D)
print(Points2D_sorted)

Points2D_sorted = sorted(Points2D, key=lambda x : x[1]) # Sort according to y
print(Points2D_sorted)

Points2D_sorted = sorted(Points2D, key=lambda x: x[0] + x[1])  # Sort according to x + y
print(Points2D_sorted)




# map(func, seq)
a = [1, 2, 3, 4, 5]
b = map(lambda x : x * 2, a)
print(list(b))

c = [x * 2 for x in a]
print(c)




# Filter(func, seq)   ===> func must return True or False
b = filter(lambda x : x % 2 == 0, a)
print(b)




# reduce(func, seq)
from functools import reduce
prod_a = reduce(lambda x, y : x * y, a)
print(prod_a)



