# Dict : key-value pairs, Unordered, Mutable


myDict = {'Name' : 'Kanha', 'city' : 'Balangir'}
dict2 = dict(name= 'Mary', age=27, city='Boston')
print(dict2)
print(dict2['name'])

myDict['email'] = 'gmail@gmail.com'
print(myDict)

del myDict['Name']
print(myDict)
myDict.pop('city')
print(myDict)
myDict.popitem()
print(myDict)


for key, value in myDict.items():
    print(key, value)

dict1 = dict2 # point to same Memory location
dict1 = dict2.copy()
dict1 = dict(dict2)

# Merge 2 dict
dict1.update(dict2)

# keys
""" list = [0, 1]
mydict = {list : 15}
print(mydict) """
tuple = (1, 4)
mydict = {tuple : 10}
print(mydict)