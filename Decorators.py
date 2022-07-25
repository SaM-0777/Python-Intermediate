# 2 diff decorator : class and function decorator

# func decorators
""" @mydecorator    # decorators are function which uses another function to perform task without modifying the original function i.e. doSomething()
def doSomething():
    pass
"""
import functools

def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):   # noe it can take as many arguments and key-argumeents as possible
        # before
        print("start")
        res = func(*args, **kwargs)
        # after
        print("end")
        return res
    return wrapper


@start_end_decorator
def print_name():
    print("Sam")


# print_name = start_end_decorator(print_name)  @start_end_decorator will do the samething
print_name()

# func with parametre


@start_end_decorator
def add5(x):
    return x + 5

print(add5(10))

print(help(add5))   # python gets confuse 
print(add5.__name__)


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                res = func(*args, **kwargs)
            return res
        return wrapper
    return decorator_repeat


@repeat(num_times=3)    # decorators with arguments
def greet(name):
    print(f'Hello {name}')

greet("Sam")


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args] # extract arguments from func
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()] # extract key-arguments from func
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"calling {func.__name__}{{signature}}")  # print func name and all args ang kwargs
        result = func(*args, **kwargs)                  # execute func
        print(f"{func.__name__!r} returned {result!r}") # print the return value fo func
        return result
    return wrapper


# Nested Decorator executed in order
@debug
@start_end_decorator
def say_hello(name):
    greet = f'Hello {name}'
    print(greet)
    return greet

say_hello("Soumya")






# class decorators

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    
    def __call__(self, *args, **kwargs):
        #print("Hi there !")
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)



@CountCalls
def say_hello():
    print('hello')

say_hello()
say_hello()




