# user = "user"
#
# def post_article(text:str):
#     if user == "admin":
#         print(f"Article {text} was posted.")
#     else:
#         print("You don't have access to post articles.")
#
#
# def post_release(text:str):
#     if user == "admin":
#         print(f"Release {text} was posted.")
#     else:
#         print("You don't have access to post articles.")
#
# post_article("\"Hello, world!\"")
# post_article("\"Hello, mate!\"")
# post_release("Heyyy")

# 1. Basic Greeting Decorator
# Write a decorator that prints "Hello!" before calling any function.

def my_decorator(func):
    def wrapper():
        print("Hello!")
        func()
        print("Bye")
    return wrapper

@my_decorator
def say_hello():
    print("This is the original function")

say_hello()

# Write a decorator called add_prefix(prefix) that:
# Takes a string prefix as an argument.
# When used to decorate a function, it should print the prefix before calling the original function.
# Use it to decorate a simple function that prints a message.

def add_prefix(prefix):
    def decorator(func):
        def wrapper():
            print(f"{prefix}")
            func()
        return wrapper
    return decorator

@add_prefix("Note:")
def printing_message():
    print("Original function")

printing_message()

# Write a decorator factory called repeat_times(n) that:
# Takes an integer n.
# When used to decorate a function, it runs that function n times every time it's called.

def repeat_times(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
@repeat_times(3)
def add(a, b):
    return a + b


print(add(2, 4))

# Task:
# Create a decorator called warn() that:
#
# When applied to a function, it prints "Warning: Function is about to run!" before executing the actual function.
# Then it runs the original function.

def warn(func):
    def wrapper(*args, **kwargs):
        print("Warning: Function is about to run!")
        result = func(*args, **kwargs)
        return result
    return wrapper
@warn
def add(a, b):
    return a + b

print(add(2, 4))

# Objective:
# Create a decorator measure_time() that:
#
# When applied to any function, it measures how long that function takes to run.
# Prints the execution time in seconds before the function's result.
# import time
# def measure_time(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"Time elapsed: {end - start}")
#         return result
#     return wrapper
# @measure_time
# def square(a, b):
#     time.sleep(1)
#     return a * b
#
# print(square(4, 4))

# Objective:
# Create a decorator call_counter() that:
#
# Keeps track of how many times a decorated function has been called.
# Prints the number of times the function has been called each time the function executes.

def call_counter(func):
    counter = 0
    def wrapper(*args, **kwargs):
        nonlocal counter
        result = func(*args, **kwargs)
        counter += 1
        print(f"The function has been called {counter} times")
        return result

    return wrapper
@call_counter
def multiply(a, b):
    return a * b

print(multiply(2, 3))
print(multiply(2, 3))

# Task: Create a Timer with a Reset Function
# Objective:
# Design a decorator that:
#
# Measures how long a function takes to run.
# Stores the total accumulated time across multiple calls.
# Provides a method to reset the accumulated time.
import time
def outer(func):
    elapsed_time = 0
    def wrapper(*args, **kwargs):
        nonlocal elapsed_time
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        elapsed_time += elapsed
        print(f"Total elapsed time: {elapsed_time}")
        return elapsed
    def reset():
        nonlocal elapsed_time
        elapsed_time = 0
        print(f"Total elapsed time: {elapsed_time}")
    wrapper.reset = reset
    return wrapper
@outer
def some_task():
    time.sleep(1.5)

some_task()
some_task()
some_task.reset()

# 2. Timing Decorator
# Write a decorator that prints how long a function takes to execute.
# 3. Print Function Name
# Decorator that prints the name of the function being called.
# 4. Repeat Function Call
# Decorator that makes a function run twice whenever called.
# 5. Add Pre/Post Messages
# Decorator that prints "Start" before and "End" after the function runs.
# 6. Number of Calls
# Decorator that keeps track of how many times a function has been called and prints the count each time.
# 7. Uppercase Output
# Decorator for functions that return strings to convert the output to uppercase.
# 8. Logging Decorator
# Decorator that logs the arguments a function receives.
# 9. Simple Validation
# Decorator that checks if the arguments are positive numbers before calling the function.
# 10. Decorator with Arguments
# Write a decorator that takes an argument (like a prefix string) and adds it before the function's output.