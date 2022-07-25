# Iter-tools : product, permutations, combinations, accumulate, groupby, and infinite iteration

# Product
from itertools import product
a = [1, 2]
b = [4, 5]
prod = product(a, b)
print(list(prod))   # Cartesian Product of a, b

b = [4]
prod = product(a, b, repeat=2)
print(list(prod))


# Permutation
from itertools import permutations
a = [1, 2, 3]
perm1 = permutations(a, 1)
perm2 = permutations(a, 2)
perm3 = permutations(a, 3)
print(list(perm1))  # Permutation of 1 numbsers at a time
print(list(perm2))  # Permutation of 2 numbsers at a time
print(list(perm3))  # Permutation of 3 numbsers at a time



# Combination
from itertools import combinations, combinations_with_replacement
a = [1, 2, 3, 4]
com1 = combinations(a, 1)   # Combination of 1 numbers at a time without repeatation
com2 = combinations(a, 2)   # Combination of 2 numbers at a time without repeatation
com3 = combinations(a, 3)   # Combination of 3 numbers at a time without repeatation
print(list(com1))
print(list(com2))
print(list(com3))

a = [1, 2, 3]
comb_wr1 = combinations_with_replacement(a, 1)   # Combination of 1 numbers at a time with repeatation
comb_wr2 = combinations_with_replacement(a, 2)   # Combination of 2 numbers at a time with repeatation
comb_wr3 = combinations_with_replacement(a, 3)   # Combination of 3 numbers at a time with repeatation
print(list(comb_wr1))
print(list(comb_wr2))
print(list(comb_wr3))



# Accumulate
from itertools import accumulate
import operator
a = [1, 2, 3, 4]
acc = accumulate(a) # by default it is func = add
print(a)
print(list(acc))

acc1 = accumulate(a, func=operator.mul)
acc2 = accumulate(a, func=operator.add)
acc3 = accumulate(a, func=max)
print(list(acc1))
print(list(acc2))
print(list(acc3))




# groupby
from itertools import groupby

def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))



# infinite Iteration
from itertools import count, cycle, repeat
for i in count(10):
    print(i)
    if i == 15:
        break

a = [1, 2, 3]
for i in repeat(a, 4):
    print(i)

for i in cycle(a):
    print(i)




