"""import time

def timer(func):
    def inner():
        start = time.time()
        result = func()
        end = time.time()
        print(f"Elapsed: {end - start}")
        return result
    return inner

@timer
def long_function():
    return sum(range(50_000_000))

long_function()"""

# from typing import Callable, Any
#
#
# def create_permissions(users: list) -> None:
#     for user in users:
#         print(f'Creating permissions for {user["username"]}')
#
#
# def only_admin(func: Callable[[list], Any]) -> Callable[[list], Any]:
#     def wrapper(users: list) -> Any:
#         true_list = []
#         for user in users:
#             if user.get("is_admin") is True:
#                 true_list.append(user)
#         return func(true_list)
#     return wrapper
#
# @only_admin
# def process_users(users: list) -> Any:
#     create_permissions(users)
#
# users_data = [
#     {"username": "Alice", "is_admin": True},
#     {"username": "Bob", "is_admin": False},
#     {"username": "Charlie", "is_admin": True}
# ]
# process_users(users_data)


# def taxes(sum_of_money):
# 	months = 9
# 	def calculate_taxes(percentage):
# 		return sum_of_money * percentage / 100 * months
# 	return calculate_taxes
# taxes_5 = taxes(1000)
# print(taxes_5(20))

def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operation(func, x):
    result = func(x)
    return result

operation(inc, 5)

operation(dec, 5)

def decorate(func):
    def inner():
        print("Decorated before")
        func()
        print("Decorated after")
    return inner
def printer():
    print("Hello")

decorated_printer = decorate(printer)

decorated_printer()

@decorate
def printer():
    print("Hello")


def my_dec(func):
    def wrapper():
        print("Before calling the function.")
        func()  # Call the original function
        print("After calling the function.")
    return wrapper

@my_dec
def say_hello():
    print("Hello!")

say_hello()

def add_fudge(func):
    def wrapper():
        print("You add fudge")
        func()
    return wrapper

@add_fudge
def get_ice_cream():
    print("Here is your ice cream")

get_ice_cream()

# hello_decorator: Write a decorator that prints "Hello from the decorator!" before the decorated function is executed.

# def hello_decorator(func):
#     def wrapper(x, y):
#         print("Hello from the decorator!")
#         result = func(x, y)
#         return result
#     return wrapper
#
# @hello_decorator
# def add(x, y):
#     return x + y
#
# print(add(2, 3))


# goodbye_decorator: Write a decorator that prints "Goodbye from the decorator!" after the decorated function is executed.

def goodbye(func):
    def wrapper(x, y):
        func(x, y)
        print("Goodbye from the decorator!")
        result = func(x, y)
        return result
    return wrapper

@goodbye
def subtract(x, y):
    return x - y

print(subtract(5, 2))


# uppercase_decorator: Write a decorator that converts the result of a function to uppercase. Assume the function returns a string.

def uppercase(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper
@uppercase
def some_function(string):
    return string

print(some_function("sergiusz"))

# exclaim_decorator: Write a decorator that adds an exclamation mark ("!") to the end of the string returned by a function.
# Assume the function returns a string.

def exclaim(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!"
    return wrapper

@exclaim
def some_function(s):
    return s

print(some_function("sergiusz"))

# greeting_decorator: Write a decorator that takes a greeting string (e.g., "Hi", "Welcome") as an argument.
# The decorator should print the greeting before the decorated function is executed.

def greeting_decorator_factory(greeting):
    def greeting_decorator(func):
        def wrapper(*args, **kwargs):
            print(greeting)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return greeting_decorator

@greeting_decorator_factory("Hi there!")
def the_function():
    return "Function called"

print(the_function())


# repeat_decorator: Write a decorator that takes an integer n as an argument. The decorator should execute the decorated function n times.

def repeat_decorator(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat_decorator(3)
def something(name):
    print( f"Called {name}")

something("Sergiusz")


# bold_decorator: Write a decorator that surrounds the string returned by a function with HTML <b> and </b> tags (making it bold in HTML).

def bold_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<b>{result}</b>"

    return wrapper
@bold_decorator
def get_name():
    return "John Doe"

print(get_name())

# italic_decorator: Write a decorator that surrounds the string returned by a function with HTML <i> and </i> tags (making it italic in HTML).

def italic_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<i>{result}</i>"
    return wrapper

@italic_decorator
def get_age(num):
    return str(num * 2)

print(get_age(2))

# print_args_decorator: Write a decorator that prints the arguments passed to the decorated function before the function is executed.

def print_args_decorator(func):
    def wrapper(*args, **kwargs):
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)
        result = func(*args, **kwargs)
        return result
    return wrapper

@print_args_decorator
def some_cool_funcjone(*args, **kwargs):
    return 1

print(some_cool_funcjone(2, 4, name = "Sergiusz", age = 30))



# multiply_by_two_decorator: Write a decorator that multiplies the number returned by a function by 2. Assume the function returns a number.

def multiply_by_two_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@multiply_by_two_decorator
def multiply(num):
    return num

print(multiply(2))

# Write a function called multiplier_decorator(multiplier). This function should take a number multiplier as input and return a decorator.
# The decorator should then multiply the result of the decorated function by the given multiplier.
# Assume the decorated function returns a number.

def multiplier_decorator_factory(multiplier):
    def multiplier_decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * multiplier
        return wrapper
    return multiplier_decorator
@multiplier_decorator_factory(3)
def add(x):
    return x * 2

print(add(2))

# Task: Simple Logging Decorator
#
# Write a decorator called log_calls that does the following:
#
# It takes a function as input.
# Before calling the decorated function, it prints the name of the function being called.
# It then calls the decorated function and returns its result.

def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, *kwargs)
        return result
    return wrapper
@log_calls
def add(x, y):
    return x + y

print(add(2, 5))