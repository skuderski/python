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

# def inc(x):
#     return x + 1
#
# def dec(x):
#     return x - 1
#
# def operation(func, x):
#     result = func(x)
#     return result
#
# operation(inc, 5)
#
# operation(dec, 5)
#
# def decorate(func):
#     def inner():
#         print("Decorated before")
#         func()
#         print("Decorated after")
#     return inner
# def printer():
#     print("Hello")
#
# decorated_printer = decorate(printer)
#
# decorated_printer()
#
# @decorate
# def printer():
#     print("Hello")
#
#
# def my_dec(func):
#     def wrapper():
#         print("Before calling the function.")
#         func()  # Call the original function
#         print("After calling the function.")
#     return wrapper
#
# @my_dec
# def say_hello():
#     print("Hello!")
#
# say_hello()
#
# def add_fudge(func):
#     def wrapper():
#         print("You add fudge")
#         func()
#     return wrapper
#
# @add_fudge
# def get_ice_cream():
#     print("Here is your ice cream")
#
# get_ice_cream()

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

# def goodbye(func):
#     def wrapper(x, y):
#         func(x, y)
#         print("Goodbye from the decorator!")
#         result = func(x, y)
#         return result
#     return wrapper
#
# @goodbye
# def subtract(x, y):
#     return x - y
#
# print(subtract(5, 2))
#
#
# # uppercase_decorator: Write a decorator that converts the result of a function to uppercase. Assume the function returns a string.
#
# def uppercase(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         result = func(*args, **kwargs)
#         return result.upper()
#     return wrapper
# @uppercase
# def some_function(string):
#     return string
#
# print(some_function("sergiusz"))
#
# # exclaim_decorator: Write a decorator that adds an exclamation mark ("!") to the end of the string returned by a function.
# # Assume the function returns a string.
#
# def exclaim(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result + "!"
#     return wrapper
#
# @exclaim
# def some_function(s):
#     return s
#
# print(some_function("sergiusz"))
#
# # greeting_decorator: Write a decorator that takes a greeting string (e.g., "Hi", "Welcome") as an argument.
# # The decorator should print the greeting before the decorated function is executed.
#
# def greeting_decorator_factory(greeting):
#     def greeting_decorator(func):
#         def wrapper(*args, **kwargs):
#             print(greeting)
#             result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return greeting_decorator
#
# @greeting_decorator_factory("Hi there!")
# def the_function():
#     return "Function called"
#
# print(the_function())
#
#
# # repeat_decorator: Write a decorator that takes an integer n as an argument. The decorator should execute the decorated function n times.
#
# def repeat_decorator(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @repeat_decorator(3)
# def something(name):
#     print( f"Called {name}")
#
# something("Sergiusz")
#
#
# # bold_decorator: Write a decorator that surrounds the string returned by a function with HTML <b> and </b> tags (making it bold in HTML).
#
# def bold_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return f"<b>{result}</b>"
#
#     return wrapper
# @bold_decorator
# def get_name():
#     return "John Doe"
#
# print(get_name())
#
# # italic_decorator: Write a decorator that surrounds the string returned by a function with HTML <i> and </i> tags (making it italic in HTML).
#
# def italic_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return f"<i>{result}</i>"
#     return wrapper
#
# @italic_decorator
# def get_age(num):
#     return str(num * 2)
#
# print(get_age(2))
#
# # print_args_decorator: Write a decorator that prints the arguments passed to the decorated function before the function is executed.
#
# def print_args_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Positional arguments:", args)
#         print("Keyword arguments:", kwargs)
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
#
# @print_args_decorator
# def some_cool_funcjone(*args, **kwargs):
#     return 1
#
# print(some_cool_funcjone(2, 4, name = "Sergiusz", age = 30))
#
#
#
# # multiply_by_two_decorator: Write a decorator that multiplies the number returned by a function by 2. Assume the function returns a number.
#
# def multiply_by_two_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result * 2
#     return wrapper
#
# @multiply_by_two_decorator
# def multiply(num):
#     return num
#
# print(multiply(2))
#
# # Write a function called multiplier_decorator(multiplier). This function should take a number multiplier as input and return a decorator.
# # The decorator should then multiply the result of the decorated function by the given multiplier.
# # Assume the decorated function returns a number.
#
# def multiplier_decorator_factory(multiplier):
#     def multiplier_decorator(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             return result * multiplier
#         return wrapper
#     return multiplier_decorator
# @multiplier_decorator_factory(3)
# def add(x):
#     return x * 2
#
# print(add(2))

# Task: Simple Logging Decorator
#
# Write a decorator called log_calls that does the following:
#
# It takes a function as input.
# Before calling the decorated function, it prints the name of the function being called.
# It then calls the decorated function and returns its result.

# def log_calls(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__}")
#         result = func(*args, *kwargs)
#         return result
#     return wrapper
# @log_calls
# def add(x, y):
#     return x + y
#
# print(add(2, 5))

# print_name_decorator: Write a decorator that prints the name of the function being called after the function has executed.
# (Similar to what you did before, but printing after).

# def print_name_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(func.__name__)
#         return result
#     return wrapper
#
# @print_name_decorator
# def adding(x, y, z):
#     return x * y * z
#
# print(adding(1, 2, 3))
#
# # multiply_result_by_3: Write a decorator that multiplies the result of a function (that returns a number) by 3.
#
# def multiply_result_by_3(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result * 3
#     return wrapper
# @multiply_result_by_3
# def multiply(x):
#     return x
#
# print(multiply(5))
#
# # add_stars: Write a decorator that surrounds the string returned by a function with asterisks (*).
#
# def add_stars(func):
#     def wrapper(*args):
#         result = ([f"*{arg}*" for arg in args])
#         return " ".join(result)
#     return wrapper
#
# @add_stars
# def star(*names):
#     return names
#
# print(star("Sergiusz", "Kuderski"))
#
# # force_positive: Write a decorator that takes the absolute value of the number returned by a function.
#
# def force_positive(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return abs(result)
#     return wrapper
#
# @force_positive
# def absolute(x):
#     return x * 2
#
# print(absolute(-2))
#
# # say_hello: Write a decorator that has the decorator print "Hello!". (The decorated function shouldn't print anything).
#
# def say_hello(func):
#     def wrapper(*args, **kwargs):
#         print("Hello")
#         return func(*args, **kwargs)
#     return wrapper
#
# @say_hello
# def add(x, y):
#     return x + y
#
# print(add(2, 3))
#
# # add_10: A decorator which adds 10 to a result.
#
# def add_10(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result + str(10)
#     return wrapper
#
# @add_10
# def add(data):
#     return data["name"]
#
# data_dict = {"name": "Sergiusz"}
# print(add(data_dict))
#
#
# # make_question: A decorator that adds a question mark to the end of a result.
#
# def make_question(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result + "?"
#     return wrapper
#
# @make_question
# def sentence(sent):
#     return sent.upper()
#
# print(sentence("what's up"))
#
# # negate: A decorator that flips the sign of a number.
#
# def negate(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return -result
#     return wrapper
# @negate
# def add(x, y):
#     return x + y
#
# print(add(2, 3))
#
#
# # to_the_power_of_2: Write a decorator that raises the result to the power of 2.
#
# def to_the_power_of_2(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result ** 2
#     return wrapper
# @to_the_power_of_2
# def powered_up(x, y):
#     return x ** y
#
# print(powered_up(2, 2))
#
#
# # apply_function: Write a decorator takes a function (such as uppercase, or bold). The result should apply the function from the decorator.
#
# def apply_function(func):
#     def decorator(apply_func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             return apply_func(result)
#         return wrapper
#     return decorator
#
# def uppercase(text):
#     return text.upper()
#
# def bold(text):
#     return f"<b>{text}</b>"
#
# @apply_function(uppercase)
# def writing(name):
#     return name[0:2].lower() + name[2:]
#
# print(writing("sergiusz"))
# @apply_function(bold)
# def writing_bold(name):
#     return name[0:2].lower() + name[2:]
#
#
# print(writing_bold("sergiusz"))
#
# def repeat_twice(func):
#     def inner(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#     return inner
#
# @repeat_twice
# def double_num(num: int):
#     print(num)
#     return num * 2
#
# print(double_num(4))

# Print "Hello" before calling any function.
#
# Create a decorator that prints "Hello" every time a function is called.
# Add a message after the function runs.

# def greeting(func):
#     def wrapper(*args, **kwargs):
#         print("Hello")
#         return func(*args, **kwargs)
#     return wrapper
# @greeting
# def hello():
#     pass
#
# hello()


#
# Write a decorator that, after executing the function, prints "Function finished!"
# Count how many times a function is called.

# def finished(func):
#     count = 0
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         count += 1
#         result = func(*args, **kwargs)
#         print("Function finished")
#         print(f"The function has been called {count} times")
#         return result
#     return wrapper
# @finished
# def sayhello(name):
#     print(f"Hello {name}")
#
# sayhello("Sergiusz")
# sayhello("Adam")

# Create a decorator that counts how many times a specific function has been called and prints the count each time.
# Make a decorator that adds parentheses around a string output.

# def counter(func):
#     count = 0
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         count += 1
#         result = func(*args, **kwargs)
#         print(f"The function has been called {count} times.")
#         return f"({result})"
#     return wrapper
# @counter
# def name(name):
#     return (f"Hello, {name}")
#
# print(name("Sergiusz"))
#
#
# # Create a decorator that converts a number to its square.
# # The decorated function returns a number, and the decorator should return its square.
#
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result ** 2
#     return wrapper
# @decorator
# def number(x):
#     return x
#
# print(number(3))
#
# # Create a decorator that ensures a function receives only positive numbers.
# # If the number is negative, change it to positive before passing it to the function.
#
# def deco(func):
#     def wrapper(*args, **kwargs):
#         new_args = []
#         for arg in args:
#             if isinstance(arg, (int, float)) and arg < 0:
#                 new_args.append(-arg)
#             else:
#                 new_args.append(arg)
#         return func(*new_args, **kwargs)
#     return wrapper
# @deco
# def number(num):
#     return num
#
# print(number(-5))
# print(number(10))
# print(number(-9))
#
# # Write a decorator that measures and prints how long a function takes to run.
# # (Hint: Use time module)
#
# import time
#
# def counting_time(func):
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         end = time.perf_counter()
#         print(f"Elapsed time: {end - start} seconds")
#         return result
#     return wrapper
# @counting_time
# def counteeink():
#     for i in range(1000000):
#         pass
#
# counteeink()
#
# # Create a decorator that reverses the string output of a function.
# # The function returns a string, and the decorator should reverse that string.
#
# def some_cute_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result[::-1]
#     return wrapper
# @some_cute_decorator
# def hello(name):
#     return name
#
# print(hello("Sergiusz"))
#
#
# # Make a decorator that adds a warning if a function takes longer than 1 second.
# # Print a message if the function runs too long.
# import time
# def warning(func):
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         end = time.perf_counter()
#         elapsed = end - start
#         result = func(*args, **kwargs)
#         print(f"Elapsed time: {elapsed}")
#         if elapsed > 1:
#             print("Function taking too long")
#         return result
#     return wrapper
#
# @warning
# def times():
#     for i in range(10000000):
#         pass
# times()
#
# # Create a decorator that prints the name of the function when it is called.
# # Show the function's name before it runs.
# import functools
# def creators(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(func.__name__)
#         return func(*args, **kwargs)
#     return wrapper
# @creators
# def add(x, y):
#     return x + y
#
# add(2, 5)
#
# from typing import Callable
# import pickle
#
#
# def cache(func: Callable) -> Callable:
#     cache_dictionary = {}
#
#     def wrapper(*args) -> Callable:
#         key = pickle.dumps(args)
#         if key in cache_dictionary:
#             print("Getting from cache")
#             return cache_dictionary[key]
#         else:
#             print("Calculating new result")
#             result = func(*args)
#             cache_dictionary[key] = result
#             return result
#     return wrapper
# @cache
# def add(x, y):
#     return x + y
#
# add(2, 3)
# add(2, 3)

# Add Logging of Function Arguments
# Create a decorator that prints out the function's name and the arguments it receives each time it's called.

def logging_of_function(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__}")
        print(f"args = {args}, kwargs = {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper
@logging_of_function
def add(x, y, name = None):
    return x + y

print(add(2, 3, name = "sergiusz"))


# 2. Cache Decorator with Limited Size
# Write a decorator that caches results of a function but limits the cache size to, say, 3 entries.
# When the cache exceeds this size, remove the oldest entry.

def cache_decorator(func):
    caching = {}
    def wrapper(*args):
        key = args
        if key in caching:
            print(f"Getting from cache for args: {args}")
            return caching[key]
        else:
            print(f"Calculating for args: {args}")
            result = func(*args)
            caching[key] = result
            # Optional: show cache size after inserting
            print(f"Cache size: {len(caching)}")
            if len(caching) > 3:
                oldest_key = next(iter(caching))
                print(f"Removing oldest cache entry for args: {oldest_key}")
                del caching[oldest_key]
            return result
    return wrapper

@cache_decorator
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))




# 3. Print Function Name and Return Value
# Make a decorator that prints the name of the function and its return value every time the function is called.

def print_function(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper
@print_function
def add(x, y):
    return x + y

add(2, 5)



# 4. Run Function Only Once
# Create a decorator that ensures the decorated function runs only once, no matter how many times it's called afterward.

def decor(func):
    has_run = False
    result = 0
    def wrapper(*args, **kwargs):
        nonlocal has_run, result
        if not has_run:
            result = func(*args, **kwargs)
            has_run = True
        return result
    return wrapper
@decor
def subtract(x, y):
    return x - y

print(subtract(2, 3))
print(subtract(3, 5))



# 5. Convert Output to String
# Write a decorator that converts whatever the function returns into a string, regardless of its original type.