# Errors and Exception

# When a statement is syntaxly correct but gives an error when executed called Exception

# Raising an exception
""" x = -5
if x < 0:
    raise Exception("X should be Positive")

# OR

assert (x >= 0), "x is not an valid argument" """


try:
    a = 5 / 0
    b = a + 4
except ZeroDivisionError as e:
    print(e)
else:
    print("Successful")
finally:
    print('clening up...')

""" except Exception as e:
    print(e) """
""" except:
    print("An Error Occured") """


class ValueTooHighError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too High')

try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
except ValueTooHighError as e:
    print(e.message, e.value)




