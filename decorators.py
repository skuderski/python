"""import time
#
# def timer(func):
#     def inner():
#         start = time.time()
#         result = func()
#         end = time.time()
#         print(f"Elapsed: {end - start}")
#         return result
#     return inner
#
# @timer
# def long_function():
#     return sum(range(50_000_000))
#
# long_function()"""
import time



# from simple_exercises import hello
#
#
# # from typing import Callable, Any
# #
# #
# # def create_permissions(users: list) -> None:
# #     for user in users:
# #         print(f'Creating permissions for {user["username"]}')
# #
# #
# # def only_admin(func: Callable[[list], Any]) -> Callable[[list], Any]:
# #     def wrapper(users: list) -> Any:
# #         true_list = []
# #         for user in users:
# #             if user.get("is_admin") is True:
# #                 true_list.append(user)
# #         return func(true_list)
# #     return wrapper
# #
# # @only_admin
# # def process_users(users: list) -> Any:
# #     create_permissions(users)
# #
# # users_data = [
# #     {"username": "Alice", "is_admin": True},
# #     {"username": "Bob", "is_admin": False},
# #     {"username": "Charlie", "is_admin": True}
# # ]
# # process_users(users_data)
#
#
# # def taxes(sum_of_money):
# # 	months = 9
# # 	def calculate_taxes(percentage):
# # 		return sum_of_money * percentage / 100 * months
# # 	return calculate_taxes
# # taxes_5 = taxes(1000)
# # print(taxes_5(20))
#
# # def inc(x):
# #     return x + 1
# #
# # def dec(x):
# #     return x - 1
# #
# # def operation(func, x):
# #     result = func(x)
# #     return result
# #
# # operation(inc, 5)
# #
# # operation(dec, 5)
# #
# # def decorate(func):
# #     def inner():
# #         print("Decorated before")
# #         func()
# #         print("Decorated after")
# #     return inner
# # def printer():
# #     print("Hello")
# #
# # decorated_printer = decorate(printer)
# #
# # decorated_printer()
# #
# # @decorate
# # def printer():
# #     print("Hello")
# #
# #
# # def my_dec(func):
# #     def wrapper():
# #         print("Before calling the function.")
# #         func()  # Call the original function
# #         print("After calling the function.")
# #     return wrapper
# #
# # @my_dec
# # def say_hello():
# #     print("Hello!")
# #
# # say_hello()
# #
# # def add_fudge(func):
# #     def wrapper():
# #         print("You add fudge")
# #         func()
# #     return wrapper
# #
# # @add_fudge
# # def get_ice_cream():
# #     print("Here is your ice cream")
# #
# # get_ice_cream()
#
# # hello_decorator: Write a decorator that prints "Hello from the decorator!" before the decorated function is executed.
#
# # def hello_decorator(func):
# #     def wrapper(x, y):
# #         print("Hello from the decorator!")
# #         result = func(x, y)
# #         return result
# #     return wrapper
# #
# # @hello_decorator
# # def add(x, y):
# #     return x + y
# #
# # print(add(2, 3))
#
#
# # goodbye_decorator: Write a decorator that prints "Goodbye from the decorator!" after the decorated function is executed.
#
# # def goodbye(func):
# #     def wrapper(x, y):
# #         func(x, y)
# #         print("Goodbye from the decorator!")
# #         result = func(x, y)
# #         return result
# #     return wrapper
# #
# # @goodbye
# # def subtract(x, y):
# #     return x - y
# #
# # print(subtract(5, 2))
# #
# #
# # # uppercase_decorator: Write a decorator that converts the result of a function to uppercase. Assume the function returns a string.
# #
# # def uppercase(func):
# #     def wrapper(*args, **kwargs):
# #         func(*args, **kwargs)
# #         result = func(*args, **kwargs)
# #         return result.upper()
# #     return wrapper
# # @uppercase
# # def some_function(string):
# #     return string
# #
# # print(some_function("sergiusz"))
# #
# # # exclaim_decorator: Write a decorator that adds an exclamation mark ("!") to the end of the string returned by a function.
# # # Assume the function returns a string.
# #
# # def exclaim(func):
# #     def wrapper(*args, **kwargs):
# #         result = func(*args, **kwargs)
# #         return result + "!"
# #     return wrapper
# #
# # @exclaim
# # def some_function(s):
# #     return s
# #
# # print(some_function("sergiusz"))
# #
# # # greeting_decorator: Write a decorator that takes a greeting string (e.g., "Hi", "Welcome") as an argument.
# # # The decorator should print the greeting before the decorated function is executed.
# #
# # def greeting_decorator_factory(greeting):
# #     def greeting_decorator(func):
# #         def wrapper(*args, **kwargs):
# #             print(greeting)
# #             result = func(*args, **kwargs)
# #             return result
# #         return wrapper
# #     return greeting_decorator
# #
# # @greeting_decorator_factory("Hi there!")
# # def the_function():
# #     return "Function called"
# #
# # print(the_function())
# #
# #
# # # repeat_decorator: Write a decorator that takes an integer n as an argument. The decorator should execute the decorated function n times.
# #
# # def repeat_decorator(n):
# #     def decorator(func):
# #         def wrapper(*args, **kwargs):
# #             for _ in range(n):
# #                 func(*args, **kwargs)
# #         return wrapper
# #     return decorator
# #
# # @repeat_decorator(3)
# # def something(name):
# #     print( f"Called {name}")
# #
# # something("Sergiusz")
# #
# #
# # # bold_decorator: Write a decorator that surrounds the string returned by a function with HTML <b> and </b> tags (making it bold in HTML).
# #
# # def bold_decorator(func):
# #     def wrapper(*args, **kwargs):
# #         result = func(*args, **kwargs)
# #         return f"<b>{result}</b>"
# #
# #     return wrapper
# # @bold_decorator
# # def get_name():
# #     return "John Doe"
# #
# # print(get_name())
# #
# # # italic_decorator: Write a decorator that surrounds the string returned by a function with HTML <i> and </i> tags (making it italic in HTML).
# #
# # def italic_decorator(func):
# #     def wrapper(*args, **kwargs):
# #         result = func(*args, **kwargs)
# #         return f"<i>{result}</i>"
# #     return wrapper
# #
# # @italic_decorator
# # def get_age(num):
# #     return str(num * 2)
# #
# # print(get_age(2))
# #
# # # print_args_decorator: Write a decorator that prints the arguments passed to the decorated function before the function is executed.
# #
# # def print_args_decorator(func):
# #     def wrapper(*args, **kwargs):
# #         print("Positional arguments:", args)
# #         print("Keyword arguments:", kwargs)
# #         result = func(*args, **kwargs)
# #         return result
# #     return wrapper
# #
# # @print_args_decorator
# # def some_cool_funcjone(*args, **kwargs):
# #     return 1
# #
# # print(some_cool_funcjone(2, 4, name = "Sergiusz", age = 30))
# #
# #
# #
# # # multiply_by_two_decorator: Write a decorator that multiplies the number returned by a function by 2. Assume the function returns a number.
# #
# # def multiply_by_two_decorator(func):
# #     def wrapper(*args, **kwargs):
# #         result = func(*args, **kwargs)
# #         return result * 2
# #     return wrapper
# #
# # @multiply_by_two_decorator
# # def multiply(num):
# #     return num
# #
# # print(multiply(2))
# #
# # # Write a function called multiplier_decorator(multiplier). This function should take a number multiplier as input and return a decorator.
# # # The decorator should then multiply the result of the decorated function by the given multiplier.
# # # Assume the decorated function returns a number.
# #
# # def multiplier_decorator_factory(multiplier):
# #     def multiplier_decorator(func):
# #         def wrapper(*args, **kwargs):
# #             result = func(*args, **kwargs)
# #             return result * multiplier
# #         return wrapper
# #     return multiplier_decorator
# # @multiplier_decorator_factory(3)
# # def add(x):
# #     return x * 2
# #
# # print(add(2))
#
# # Task: Simple Logging Decorator
# #
# # Write a decorator called log_calls that does the following:
# #
# # It takes a function as input.
# # Before calling the decorated function, it prints the name of the function being called.
# # It then calls the decorated function and returns its result.
#
# # def log_calls(func):
# #     def wrapper(*args, **kwargs):
# #         print(f"Calling {func.__name__}")
# #         result = func(*args, *kwargs)
# #         return result
# #     return wrapper
# # @log_calls
# # def add(x, y):
# #     return x + y
# #
# # print(add(2, 5))
#
# # print_name_decorator: Write a decorator that prints the name of the function being called after the function has executed.
# # (Similar to what you did before, but printing after).
#
# # def print_name_decorator(func):
# #     def wrapper(*args, **kwargs):
# #         result = func(*args, **kwargs)
# #         print(func.__name__)
# #         return result
# #     return wrapper
# #
# # @print_name_decorator
# # def adding(x, y, z):
# #     return x * y * z
# #
# # print(adding(1, 2, 3))
# #
# # # multiply_result_by_3: Write a decorator that multiplies the result of a function (that returns a number) by 3.
# #
# # def multiply_result_by_3(func):
# #     def wrapper(*args, **kwargs):
# #         result = func(*args, **kwargs)
# #         return result * 3
# #     return wrapper
# # @multiply_result_by_3
# # def multiply(x):
# #     return x
# #
# # print(multiply(5))
# #
# # # add_stars: Write a decorator that surrounds the string returned by a function with asterisks (*).
# #
# # def add_stars(func):
# #     def wrapper(*args):
# #         result = ([f"*{arg}*" for arg in args])
# #         return " ".join(result)
# #     return wrapper
# #
# # @add_stars
# # def star(*names):
# #     return names
# #
# # print(star("Sergiusz", "Kuderski"))
# #
# # # force_positive: Write a decorator that takes the absolute value of the number returned by a function.
# #
# # def force_positive(func):
# #     def wrapper(*args, **kwargs):
# #         result = func(*args, **kwargs)
# #         return abs(result)
# #     return wrapper
# #
# # @force_positive
# # def absolute(x):
# #     return x * 2
# #
# # print(absolute(-2))
# #
# # # say_hello: Write a decorator that has the decorator print "Hello!". (The decorated function shouldn't print anything).
# #
# # def say_hello(func):
# #     def wrapper(*args, **kwargs):
# #         print("Hello")
# #         return func(*args, **kwargs)
# #     return wrapper
# #
# # @say_hello
# # def add(x, y):
# #     return x + y
# #
# # print(add(2, 3))
# #
# # # add_10: A decorator which adds 10 to a result.
# #
# # def add_10(func):
# #     def wrapper(*args, **kwargs):
# #         result = func(*args, **kwargs)
# #         return result + str(10)
# #     return wrapper
# #
# # @add_10
# # def add(data):
# #     return data["name"]
# #
# # data_dict = {"name": "Sergiusz"}
# # print(add(data_dict))
# #
# #
# # # make_question: A decorator that adds a question mark to the end of a result.
# #
# # def make_question(func):
# #     def wrapper(*args, **kwargs):
# #         result = func(*args, **kwargs)
# #         return result + "?"
# #     return wrapper
# #
# # @make_question
# # def sentence(sent):
# #     return sent.upper()
# #
# # print(sentence("what's up"))
# #
# # # negate: A decorator that flips the sign of a number.
# #
# # def negate(func):
# #     def wrapper(*args, **kwargs):
# #         result = func(*args, **kwargs)
# #         return -result
# #     return wrapper
# # @negate
# # def add(x, y):
# #     return x + y
# #
# # print(add(2, 3))
# #
# #
# # # to_the_power_of_2: Write a decorator that raises the result to the power of 2.
# #
# # def to_the_power_of_2(func):
# #     def wrapper(*args, **kwargs):
# #         result = func(*args, **kwargs)
# #         return result ** 2
# #     return wrapper
# # @to_the_power_of_2
# # def powered_up(x, y):
# #     return x ** y
# #
# # print(powered_up(2, 2))
# #
# #
# # # apply_function: Write a decorator takes a function (such as uppercase, or bold). The result should apply the function from the decorator.
# #
# # def apply_function(func):
# #     def decorator(apply_func):
# #         def wrapper(*args, **kwargs):
# #             result = func(*args, **kwargs)
# #             return apply_func(result)
# #         return wrapper
# #     return decorator
# #
# # def uppercase(text):
# #     return text.upper()
# #
# # def bold(text):
# #     return f"<b>{text}</b>"
# #
# # @apply_function(uppercase)
# # def writing(name):
# #     return name[0:2].lower() + name[2:]
# #
# # print(writing("sergiusz"))
# # @apply_function(bold)
# # def writing_bold(name):
# #     return name[0:2].lower() + name[2:]
# #
# #
# # print(writing_bold("sergiusz"))
# #
# # def repeat_twice(func):
# #     def inner(*args, **kwargs):
# #         func(*args, **kwargs)
# #         func(*args, **kwargs)
# #     return inner
# #
# # @repeat_twice
# # def double_num(num: int):
# #     print(num)
# #     return num * 2
# #
# # print(double_num(4))
#
# # Print "Hello" before calling any function.
# #
# # Create a decorator that prints "Hello" every time a function is called.
# # Add a message after the function runs.
#
# # def greeting(func):
# #     def wrapper(*args, **kwargs):
# #         print("Hello")
# #         return func(*args, **kwargs)
# #     return wrapper
# # @greeting
# # def hello():
# #     pass
# #
# # hello()
#
#
# #
# # Write a decorator that, after executing the function, prints "Function finished!"
# # Count how many times a function is called.
#
# # def finished(func):
# #     count = 0
# #     def wrapper(*args, **kwargs):
# #         nonlocal count
# #         count += 1
# #         result = func(*args, **kwargs)
# #         print("Function finished")
# #         print(f"The function has been called {count} times")
# #         return result
# #     return wrapper
# # @finished
# # def sayhello(name):
# #     print(f"Hello {name}")
# #
# # sayhello("Sergiusz")
# # sayhello("Adam")
#
# # Create a decorator that counts how many times a specific function has been called and prints the count each time.
# # Make a decorator that adds parentheses around a string output.
#
# # def counter(func):
# #     count = 0
# #     def wrapper(*args, **kwargs):
# #         nonlocal count
# #         count += 1
# #         result = func(*args, **kwargs)
# #         print(f"The function has been called {count} times.")
# #         return f"({result})"
# #     return wrapper
# # @counter
# # def name(name):
# #     return (f"Hello, {name}")
# #
# # print(name("Sergiusz"))
# #
# #
# # # Create a decorator that converts a number to its square.
# # # The decorated function returns a number, and the decorator should return its square.
# #
# #
# # def decorator(func):
# #     def wrapper(*args, **kwargs):
# #         result = func(*args, **kwargs)
# #         return result ** 2
# #     return wrapper
# # @decorator
# # def number(x):
# #     return x
# #
# # print(number(3))
# #
# # # Create a decorator that ensures a function receives only positive numbers.
# # # If the number is negative, change it to positive before passing it to the function.
# #
# # def deco(func):
# #     def wrapper(*args, **kwargs):
# #         new_args = []
# #         for arg in args:
# #             if isinstance(arg, (int, float)) and arg < 0:
# #                 new_args.append(-arg)
# #             else:
# #                 new_args.append(arg)
# #         return func(*new_args, **kwargs)
# #     return wrapper
# # @deco
# # def number(num):
# #     return num
# #
# # print(number(-5))
# # print(number(10))
# # print(number(-9))
# #
# # # Write a decorator that measures and prints how long a function takes to run.
# # # (Hint: Use time module)
# #
# # import time
# #
# # def counting_time(func):
# #     def wrapper(*args, **kwargs):
# #         start = time.perf_counter()
# #         result = func(*args, **kwargs)
# #         end = time.perf_counter()
# #         print(f"Elapsed time: {end - start} seconds")
# #         return result
# #     return wrapper
# # @counting_time
# # def counteeink():
# #     for i in range(1000000):
# #         pass
# #
# # counteeink()
# #
# # # Create a decorator that reverses the string output of a function.
# # # The function returns a string, and the decorator should reverse that string.
# #
# # def some_cute_decorator(func):
# #     def wrapper(*args, **kwargs):
# #         result = func(*args, **kwargs)
# #         return result[::-1]
# #     return wrapper
# # @some_cute_decorator
# # def hello(name):
# #     return name
# #
# # print(hello("Sergiusz"))
# #
# #
# # # Make a decorator that adds a warning if a function takes longer than 1 second.
# # # Print a message if the function runs too long.
# # import time
# # def warning(func):
# #     def wrapper(*args, **kwargs):
# #         start = time.perf_counter()
# #         result = func(*args, **kwargs)
# #         end = time.perf_counter()
# #         elapsed = end - start
# #         result = func(*args, **kwargs)
# #         print(f"Elapsed time: {elapsed}")
# #         if elapsed > 1:
# #             print("Function taking too long")
# #         return result
# #     return wrapper
# #
# # @warning
# # def times():
# #     for i in range(10000000):
# #         pass
# # times()
# #
# # # Create a decorator that prints the name of the function when it is called.
# # # Show the function's name before it runs.
# # import functools
# # def creators(func):
# #     @functools.wraps(func)
# #     def wrapper(*args, **kwargs):
# #         print(func.__name__)
# #         return func(*args, **kwargs)
# #     return wrapper
# # @creators
# # def add(x, y):
# #     return x + y
# #
# # add(2, 5)
# #
# # from typing import Callable
# # import pickle
# #
# #
# # def cache(func: Callable) -> Callable:
# #     cache_dictionary = {}
# #
# #     def wrapper(*args) -> Callable:
# #         key = pickle.dumps(args)
# #         if key in cache_dictionary:
# #             print("Getting from cache")
# #             return cache_dictionary[key]
# #         else:
# #             print("Calculating new result")
# #             result = func(*args)
# #             cache_dictionary[key] = result
# #             return result
# #     return wrapper
# # @cache
# # def add(x, y):
# #     return x + y
# #
# # add(2, 3)
# # add(2, 3)
#
# # Add Logging of Function Arguments
# # Create a decorator that prints out the function's name and the arguments it receives each time it's called.
#
# # def logging_of_function(func):
# #     def wrapper(*args, **kwargs):
# #         print(f"{func.__name__}")
# #         print(f"args = {args}, kwargs = {kwargs}")
# #         result = func(*args, **kwargs)
# #         return result
# #     return wrapper
# # @logging_of_function
# # def add(x, y, name = None):
# #     return x + y
# #
# # print(add(2, 3, name = "sergiusz"))
# #
# #
# # # 2. Cache Decorator with Limited Size
# # # Write a decorator that caches results of a function but limits the cache size to, say, 3 entries.
# # # When the cache exceeds this size, remove the oldest entry.
# #
# # def cache_decorator(func):
# #     caching = {}
# #     def wrapper(*args):
# #         key = args
# #         if key in caching:
# #             print(f"Getting from cache for args: {args}")
# #             return caching[key]
# #         else:
# #             print(f"Calculating for args: {args}")
# #             result = func(*args)
# #             caching[key] = result
# #             # Optional: show cache size after inserting
# #             print(f"Cache size: {len(caching)}")
# #             if len(caching) > 3:
# #                 oldest_key = next(iter(caching))
# #                 print(f"Removing oldest cache entry for args: {oldest_key}")
# #                 del caching[oldest_key]
# #             return result
# #     return wrapper
# #
# # @cache_decorator
# # def fibonacci(n):
# #     if n <= 1:
# #         return n
# #     else:
# #         return fibonacci(n - 1) + fibonacci(n - 2)
# #
# # print(fibonacci(5))
# # print(fibonacci(6))
# # print(fibonacci(7))
# # print(fibonacci(8))
# #
# #
# #
# #
# # # 3. Print Function Name and Return Value
# # # Make a decorator that prints the name of the function and its return value every time the function is called.
# #
# # def print_function(func):
# #     def wrapper(*args, **kwargs):
# #         result = func(*args, **kwargs)
# #         print(f"{func.__name__} returned: {result}")
# #         return result
# #     return wrapper
# # @print_function
# # def add(x, y):
# #     return x + y
# #
# # add(2, 5)
# #
# #
# #
# # # 4. Run Function Only Once
# # # Create a decorator that ensures the decorated function runs only once, no matter how many times it's called afterward.
# #
# # def decor(func):
# #     has_run = False
# #     result = 0
# #     def wrapper(*args, **kwargs):
# #         nonlocal has_run, result
# #         if not has_run:
# #             result = func(*args, **kwargs)
# #             has_run = True
# #         return result
# #     return wrapper
# # @decor
# # def subtract(x, y):
# #     return x - y
# #
# # print(subtract(2, 3))
# # print(subtract(3, 5))
# #
# #
# #
# # # 5. Convert Output to String
# # # Write a decorator that converts whatever the function returns into a string, regardless of its original type.
# #
# # def decoratorato(func):
# #     def wrapper(*args, **kwargs):
# #         result = func(*args, **kwargs)
# #         result_str = str(result)
# #         print(type(result_str))
# #         return result_str
# #     return wrapper
# #
# # @decoratorato
# # def addeenk(x, y):
# #     s = x + y
# #     return s
# #
# # print(addeenk( 1, 5))
# #
# # # 1. Decorator for Uppercasing Output
# # # Create a decorator that modifies any function returning a string so that the output is always uppercase.
# #
# # def dec(func):
# #     def wrapper(*args, **kwargs):
# #         result = func(*args, **kwargs)
# #         return result.upper()
# #     return wrapper
# #
# # @dec
# # def greeting(name):
# #     return f"Hello, {name}"
# #
# # print(greeting("Sergiusz"))
#
# # Create a decorator that modifies any function so that:
# #
# # If the function returns a string, it should be converted to uppercase.
# # If the function returns a list of strings, each string should be uppercase.
# If the function returns any other type, leave it unchanged.

# def decorazorro(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result, str):
#             return result.upper()
#         elif isinstance(result, list):
#             new_list = []
#             for s in result:
#                 if isinstance(s, str):
#                     new_list.append(s.upper())
#                 else:
#                     new_list.append(s)
#             return new_list
#         else:
#             return result
#     return wrapper
# @decorazorro
# def get_greeting():
#     return "hello"
# @decorazorro
# def get_fruits():
#     return ["banana", "apple", "cherry"]
#
# print(get_greeting())
#
# print(get_fruits())

# Create a decorator that modifies any function so that:
#
# If the function returns a string, it reverses the string.
# If the function returns a list of strings, it reverses each string in the list.
# If the function returns a number, it adds 100 to the number.
# Otherwise, it just returns the original result unchanged.

# def complex_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result, str):
#             return result[::-1]
#         elif isinstance(result, list):
#             the_list = []
#             for s in result:
#                 if isinstance(s, str):
#                     the_list.append(s[::-1])
#                 else:
#                     the_list.append(s)
#             return the_list
#         elif isinstance(result, (int, float)):
#             return result + 100
#         else:
#             return result
#     return wrapper
# @complex_decorator
# def name():
#     return "Sergiusz Kuderski"
#
#
# print(name())
# @complex_decorator
# def sports():
#     return ["football", "volleyball", "basketball"]
#
# print(sports())
#
# @complex_decorator
# def add():
#     return 10
# print(add())
#
# # Create a decorator that modifies any function so that:
# #
# # If the function returns a string, it converts the string to title case (.title()).
# # If the function returns a list of strings, it title-cases each string in the list.
# # If the function returns a dictionary, it title-cases all string values inside it (but leaves non-string values unchanged).
# # If the function returns a number, it multiplies the number by 2.
# # Otherwise, it just returns the original result unchanged.
#
# def some_cool_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result, str):
#             return result.title()
#         elif isinstance(result, list):
#             return [s.title() if isinstance(s, str) else s for s in result]
#         elif isinstance(result, dict):
#             return {k: v.title() if isinstance(v, str) else v for k, v in result.items()}
#         elif isinstance(result, (float, int)):
#             return result * 2
#         else:
#             return result
#     return wrapper
# @some_cool_decorator
# def data():
#     return {
#         "name": "john doe",
#         "age": 30,
#         "city": "new york"
#     }
# @some_cool_decorator
# def list_of_names():
#     return ["alice", "bob", "carol"]
# @some_cool_decorator
# def get_number():
#     return 45
#
#
# print(data())
# print(list_of_names())
# print(get_number())
#
# # Create a decorator that modifies any function's output based on its type, with these rules:
# #
# # If the function returns a string, convert it to sentence case (first letter capitalized, remaining lowercase).
# # If it returns a list of strings, convert each string in the list to sentence case.
# # If it returns a dictionary, recursively title-case all string values inside it — including nested dictionaries or lists.
# # If it returns a number, divide it by 2.
# # If it returns any other data type, leave it unchanged.
# # Additionally, if the returned value is a list or dictionary, sort the list or dictionary keys in ascending order before processing or return.
#
# def process_string(s):
#     return s.capitalize()
#
# def process_list(lst):
#     new_list = []
#     for s in lst:
#         if isinstance(s, str):
#             new_list.append(process_string(s))
#         elif isinstance(s, list):
#             new_list.append(process_list(s))
#         elif isinstance(s, dict):
#             new_list.append(process_dict(s))
#         else:
#             new_list.append(s)
#     return sorted(new_list)
#
# def process_dict(dct):
#     new_dict = {}
#     for k in sorted(dct.keys()):
#         v = dct[k]
#         if isinstance(v, str):
#             new_dict[k] = process_string(v)
#         elif isinstance(v, list):
#             new_dict[k] = process_list(v)
#         elif isinstance(v, dict):
#             new_dict[k] = process_dict(v)
#         else:
#             new_dict[k] = v
#     return new_dict
#
# def very_cool_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result, str):
#             return process_string(result)
#         elif isinstance(result, list):
#             return sorted(process_list(result))
#         elif isinstance(result, dict):
#             return process_dict(result)
#         elif isinstance(result, (int, float)):
#             return result / 2
#         else:
#             return result
#     return wrapper
#
# @very_cool_decorator
# def get_data():
#     return {
#         "name": "john doe",
#         "scores": [70, 80, 90],
#         "details": {
#             "city": "new york",
#             "hobbies": ["reading", "swimming"]
#         },
#         "rating": 4.8,
#         "misc": ["apple", "banana"]
#     }
#
# print(get_data())
#
# # Create a decorator that modifies any function's output based on its type:
# #
# # If the function returns a string, convert it to lowercase.
# # If it returns a list of strings, convert each string in the list to lowercase.
# # If it returns a dictionary, convert all string values (but not nested dictionaries or lists) inside it to lowercase. Leave other types unchanged.
# # If it returns a number, subtract 5 from it.
# # Otherwise, just return the result unchanged.
#
# def modi_deco(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result, str):
#             return result.lower()
#         elif isinstance(result, list):
#             return [s.lower() if isinstance(s, str) else s for s in result]
#         elif isinstance(result, dict):
#             return {k: v.lower() if isinstance(v, str) else v for k, v in result.items()}
#         elif isinstance(result, (float, int)):
#             return result - 5
#         else:
#             return result
#     return wrapper
#
# @modi_deco
# def get_string():
#     return "Hello World"
#
# @modi_deco
# def get_list():
#     return ["Apple", "BANANA", "Cherry"]
#
# @modi_deco
# def get_dict():
#     return {"Name": "Alice", "Age": 30, "City": "New York"}
#
# @modi_deco
# def get_number():
#     return 20
#
# print(get_string())
# print(get_list())
# print(get_dict())
# print(get_number())
#
# # Simple Timing Decorator
# # Write a decorator that measures how long a function takes to run and prints the duration (use time.perf_counter()).
# import time
# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         end = time.perf_counter()
#         print(f"Elapsed time of {func.__name__} function is {end - start}")
#         return result
#     return wrapper
# @timing_decorator
# def ranging():
#     for _ in range(99999999):
#         pass
#
# ranging()
#
# # Create a decorator that measures the execution time of a function and logs that information to a file (e.g., 'timing.log')
# # instead of printing it to the console.
# #
# #
# # It should record the start and end times using time.perf_counter().
# # Write the function name, duration, and timestamp into 'timing.log'.
# # Append to the log file if run multiple times, keeping all logs.
# # Use a timestamp (like datetime.now()) to record when the function was called.
# import time
# from datetime import datetime
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         end = time.perf_counter()
#         duration = end - start
#         log_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {func.__name__} took {duration} seconds"
#         with open('timing.log', 'a') as log_file:
#             log_file.write(log_entry)
#             return result
#     return wrapper
# @decorator
# def example():
#     time.sleep(1)
#
# example()
#
# # 3. Decorator to Count Function Calls
# # Keep track of how many times a function has been called. Each call should print the current count.
#
# def decorator(func):
#     count = 0
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         result = func(*args, **kwargs)
#         count += 1
#         print(f"Current count of the function called {func.__name__}: {count}")
#         return result
#     return wrapper
#
# @decorator
# def add(x, y):
#     return x ** y
#
# print(add(2, 3))
# print(add(3, 4))
#
# # Create a decorator that tracks how many times a specific function has been called during the lifetime of the program
# # and prints the count each time the function is called.
# #
# # But here's the twist:
# #
# # The count is shared across all decorated functions, by function name.
# # So, if two different functions with the same name are decorated, they share the same count (not separate).
# count = 0
# def tracking(func):
#     def wrapper(*args, **kwargs):
#         global count
#         result = func(*args, **kwargs)
#         count += 1
#         print(f"Current count of the function is: {count}")
#         return result
#     return wrapper
# @tracking
# def add(x, y):
#     return x + y
# @tracking
# def multiply(x, y):
#     return x * y
#
# print(add(2, 5))
# print(add(3, 6))
# print(multiply(2, 4))
# print(multiply(1, 5))
#
# # Create a decorator that tracks the number of times a particular function has been called during the program's lifetime, but:
# #
# # It also tracks the number of calls for all functions with the same name across different modules or pieces of code.
# # So, if two separate functions with the same name are decorated somewhere, they share the same count (by name),
# # regardless of which module they are in.
# # Each call prints the current count for that function name across all modules.
# count = 0
# dict_count = {}
# def decorator(func):
#     global dict_count
#     def wrapper(*args, **kwargs):
#         if func not in dict_count:
#             dict_count[func] = 0
#         dict_count[func] += 1
#         global count
#         count += 1
#         print(f"{func.__name__} was called {dict_count[func]} times and all functions have been called {count} times.")
#         return func(*args, **kwargs)
#     return wrapper
# @decorator
# def adding(x, y):
#     return x + y
# @decorator
# def substracting(x, y):
#     return x - y
# @decorator
# def multiplying(x, y):
#     return x * y
# @decorator
# def diving(x, y):
#     return x // y
#
# print(adding(10, 5))
# print(adding(2, 5))
# print(substracting(10, 5))
# print(multiplying(10, 5))
# print(diving(10, 5))
#
# # Create a decorator that tracks the total runtime of each function with a given name across all modules during the program's lifetime.
# #
# # Each time a function with a name is called, it accumulates the execution time.
# # When the function finishes, it prints the total accumulated runtime for all functions sharing that name.
# # Notes:
# # The decorator must share timing data across all functions with the same name, even if they are defined in different modules.
# # It should not track per-instance or per-function call; only cumulative time per function name.
# import time
# total_runtime = {}
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         end = time.perf_counter()
#         duration = end - start
#         global total_runtime
#         if func.__name__ not in total_runtime:
#             total_runtime[func.__name__] = 0
#         total_runtime[func.__name__] += duration
#         print(f"The duration for all '{func.__name__}': {total_runtime[func.__name__]}")
#         return result
#     return wrapper
# @decorator
# def one():
#     for _ in range(10000):
#         pass
# @decorator
# def two():
#     for _ in range(20000):
#         pass
#
# one()
# two()
# two()
#
# # Create a decorator that counts how many times each specific function was called during the entire program's lifetime, but:
# #
# # The count is shared per function name across all modules (so if functions with the same name are in different files, they share the count).
# # Each time a function is called, print the function's name and the total call count so far.
# # This way, you only need to:
# #
# # Use a global dictionary keyed by function name.
# # Increment and print the count on each call.
#
# calls_count = {}
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         if func.__name__ not in calls_count:
#             calls_count[func.__name__] = 0
#         calls_count[func.__name__] += 1
#
#         print(f"'{func.__name__}' has been called {calls_count[func.__name__]} times")
#
#         return func(*args, **kwargs)
#     return wrapper
# @decorator
# def add(x, y):
#     return x + y
# @decorator
# def subtract(x, y):
#     return x - y
#
# add(2, 5)
# subtract(3, 6)
# subtract(10, 3)
#
# # Add Logging of Arguments and Result
# # Create a decorator that logs the function name, input arguments, and the return value each time the function is called.
#
# def logging_of_args(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f"Function name: {func.__name__}, input arguments: {args}, {kwargs}, value: {result}")
#         return result
#     return wrapper
# @logging_of_args
# def add(x, y):
#     return x + y
#
# add(6, 5)
#
# # Create a decorator that logs detailed information each time the function is called, including:
# #
# # The function name
# # The input arguments (both positional and keyword arguments)
# # The type of each argument
# # The return value and its type
# # Additionally, log the execution time of the function call
# import time
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         end = time.perf_counter()
#         duration = end - start
#         print(f"The name of the function is '{func.__name__}'.")
#         print(f"The input arguments are: {args} and {kwargs}. Argument types: ")
#         for i, arg in enumerate(args):
#             print(f"args[{i}] ({arg}) type: {type(arg)}")
#         for key, value in kwargs.items():
#             print(f"  kwargs['{key}'] ({value}) type: {type(value)}")
#         print(f"The return value is: {result} and its type is {type(result)}.")
#         print(f"The execution time of the function is: {duration:.6f} seconds..")
#         return result
#     return wrapper
#
# @decorator
# def add(x, y):
#     return x + y
#
# print(add(5, 2))

# 5. Run a Function Only After N Calls
# Implement a decorator that only allows the function to run once it has been called N times;
# before that, it just prints a message saying "Not yet!".

def run_a_function_after_n_calls(n):
    def decorator(func):
        counter = 0
        def wrapper(*args, **kwargs):
            nonlocal counter
            counter += 1
            if counter <= n:
                print("Not yet!")
                return None

            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator

@run_a_function_after_n_calls(3)
def add(x, y):
    return x + y

print(add(2, 3))
print(add(3, 5))
print(add(4, 7))
print(add(5, 2))

# Create a decorator that only allows the decorated function to run on every nth call.
#
# On all other calls, it should just print "Waiting..." and not run the function.
# When the call number reaches a multiple of n, it runs the function as normal and resets the count.

def factory(n):
    def decorator(func):
        counter = 0
        run_count = 0
        def wrapper(*args, **kwargs):
            nonlocal counter, run_count
            counter += 1
            if counter % n == 0:
                run_count += 1
                print("here we go")
                return func(*args, **kwargs)
            else:
                print(f"Waiting call counts: {counter}. {run_count} executions so far.")
                return "Function is waiting to be called again"
        return wrapper
    return decorator

@factory(3)
def add(x, y):
    return x + y

print(add(2, 3))
print(add(2, 3))
print(add(2, 3))
print(add(2, 3))
print(add(2, 3))
print(add(2, 3))
print(add(2, 3))
print(add(2, 3))
print(add(2, 3))
print(add(2, 3))

# Create a simple decorator that caches the result of a function only if the function takes one argument and that argument is hashable.
#
# If the result for the argument is already in the cache, return the cached value instead of recomputing.
# If not, compute and store the result in the cache.
import pickle
def simple_decor(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = pickle.dumps(args)
        if key in cache:
            print("Fetching from cache")
            return cache[key]
        else:
            result = func(*args, **kwargs)
            cache[key] = result
            print("Caching result")
            return result
    return wrapper

@simple_decor
def multiply(x, y):
    return x * y

multiply(2, 2)
multiply(2, 2)
multiply(3, 2)

# Create a decorator that caches the results of functions only if the function takes two arguments, both of which are hashable.
#
# If the result for a specific pair of arguments exists in the cache, return the cached value.
# Otherwise, compute the result, store it, and then return it

def cute_decorator(func):
    dictionary = {}
    def wrapper(arg1, arg2):
        try:
            key = (arg1, arg2)
            hash(key)
        except TypeError:
            raise ValueError("Both arguments must be hashable")

        if key in dictionary:
            return dictionary[key]
        result = func(arg1, arg2)
        dictionary[key] = result
        return result
    return wrapper

# Decorator for Adding Authentication (Simulated)
# Implement a decorator that checks a "logged_in" boolean before allowing a function to run. If not logged in, print "Access denied."
def authentication(auth_state):
    def auth(func):
        def wrapper(*args, **kwargs):
            if not auth_state['logged_in']:
                print("Access denied.")
                return "Not logged in"
            else:
                print("Logged in")
                return func(*args, **kwargs)

        return wrapper
    return auth


auth_state = {'logged_in': False}

@authentication(auth_state)
def add(x, y):
    return x + y

add(2, 3)


auth_state['logged_in'] = True

add(2, 3)
