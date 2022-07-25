# Generators are function that return object that can be iterated over, they generate the items inside object only one at a time and only when asked
# most memory efficicent

def myGenerator():
    yield 1
    yield 2
    yield 3
    yield 5
    yield 4

G = myGenerator()
print(G)
for i in G:
    print(i)

value = next(G)
print(value)    # print 1

value = next(G)
print(value)    # print 2

value = next(G)
print(value)    # print 3



print(sum(G))
print(sorted(G))






# Execution of a Generator function

def Countdown(num):
    print('Starting...')
    while num > 0:
        yield num
        num -= 1

cd = Countdown(5)
value = next(cd)
print(value)
print(next(cd))
print(next(cd))
print(next(cd))



 
# Advantage of Generator
import sys

# First method takes more memory


def FirstN(N):
    nums = []
    num = 0
    while num < N:
        nums.append(num)
        num += 1
    return nums


print(sum(FirstN(10)))


# Second method using Generator
def First_Generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(sum(First_Generator(10)))


# Analyse Memory usage of both methods

print(f'Memory Occupied by first Method : {sys.getsizeof(FirstN(1000000))} bits')
print(f'Memory Occupied by Second Method : {sys.getsizeof(First_Generator(1000000))} bits')


# Example
def fib(limit):
    # 0 1 1 2 3 5 8 13 . . . . 
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
f = fib(30)
for i in f:
    print(i, end=" ")

# generator Expressions
import sys

my = (i for i in range(1000000) if i % 2 == 0)
myList = [i for i in range(1000000) if i % 2 == 0]

# Analyse the Memory Size
print(f'size of Generator : {sys.getsizeof(my)} bits')
print(f'size of List : {sys.getsizeof(myList)} bits')












