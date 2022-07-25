import json

Person = {"name": "Soumya", "age": 20, "city": "Balangir",
          "haschildren": False, "titles": ["engineer", "programmer", "student"]}

# separators = (': ', '= ')
PersonJSON = json.dumps(Person, indent=4, sort_keys=True)
print(PersonJSON)

with open('Person.json', "w") as file:
    json.dump(Person, file, indent=4)


# Convert json file to Python Dict with loads func
Person1 = json.loads(PersonJSON)
print(Person1)

# Read the json file / decode json file
f = open('Person.json', 'r')
print(json.load(f))
f.close()



class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Soumya", 20)
print(type(user))

# Encode the data
def encode_User(o):
    if isinstance(o, User):
        return {'name' : o.name, 'age' : o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of  type User is not JSON serializable")


userJSON = json.dumps(user, default=encode_User)
print(userJSON)

# Custom Encoder
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name' : o.name, 'age' : o.age, o.__class__.__name__ : True}
        return JSONEncoder.default(self, o)

UserJSON_class = json.dumps(user, cls=UserEncoder)
print(UserJSON_class)
# OR
UserJSON_class = UserEncoder().encode(user)
print(UserJSON_class)


# Decode
user = json.loads(UserJSON_class)
print(user)

# custom decoding method
def decode_User(dict):
    if User.__name__ in dict:
        return User(name=dict['name'], age=dict['age'])
    return dict


user = json.loads(UserJSON_class, object_hook=decode_User)
print(type(user))   #
print(user.name)




