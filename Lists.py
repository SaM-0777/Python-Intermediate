# List : Ordered, mutable, allows duplicate elements

myList = ['banana', 'cherry', 5, 2.3, 5+2.4j, True]
print(myList)
print(myList[0], myList[-2])
for i in myList:
    print(i)

if True in myList:
    print("Yes")
else:
    print("No")

myList.append("Lemon")

myList.insert(1, "Berry")
print(myList)

myList.remove(5)
print(myList)

item = myList.pop()
print(item)

""" item = myList.clear()
print(item) """

""" newList = sorted(myList) """    # Error

""" myList.sort() """   # Error

""" print(newList) """

newList = ['M'] * 8
print(newList)

# Slicing
List = [4, 7, 8, 0, 12, 5, 6]
a = List[:5]
b = List[5:]
print(a, "\t", b)

c = List[::]
print(c)
c = List[::-1]
print(c)
c = List[1:5:2] # start, stop, step
print(c)

c = list(List)
print(c)    # Copy List

c = [x ** 2 for x in List]
print(c)

pos = c.index(3)
print(pos)