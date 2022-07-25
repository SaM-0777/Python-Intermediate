import numpy as np
import random
import secrets  # used for password, account info

a = random.random()
print(a)

a = random.uniform(1, 5)
print(a)

a = random.randint(2, 6)
print(a)

a = random.normalvariate(0, 1)  # mu = 0, variance = 1
print(a)

myList = list("ABCDjkldflgs")
a = random.choice(myList)
print(a)
a = random.sample(myList, 3)    # number of unique elements
print(a)
a = random.choices(myList, k=2)  # same but data can repeat
print(a)

random.shuffle(myList)
print(myList)

random.seed(1)  # to reproduce the numbers
print(random.random())
print(random.randint(4, 40))
random.seed(2)
print(random.random())              # print the same numbers
print(random.randint(4, 40))

random.seed(1)
print(random.random())
print(random.randint(4, 40))
random.seed(2)
print(random.random())
print(random.randint(4, 40))


# secrets module
a = secrets.randbelow(10)   # true random -- 10 not included
print(a)

a = secrets.randbits(6)     # random number betwen 0-64
print(a)

myList = list("ksdhfsiuhfahfuegofafeu")
a = secrets.choice(myList)
print(a)


# numpy to make array of random numbers

a = np.random.rand(2, 3)    # 3x2 Array
print(a)


a = np.random.randint(0, 101, [3, 4])   # generate a 4x3 array of random integers between 0 and 100
print(a)

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
np.random.shuffle(a)

np.random.seed(1)
print(np.random.rand(3, 3))
# print the same array
np.random.seed(1)
print(np.random.rand(3, 3))



