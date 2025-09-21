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

# def my_decorator(func):
#     def wrapper():
#         print("Hello!")
#         func()
#         print("Bye")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("This is the original function")
#
# say_hello()
#
# # Write a decorator called add_prefix(prefix) that:
# # Takes a string prefix as an argument.
# # When used to decorate a function, it should print the prefix before calling the original function.
# # Use it to decorate a simple function that prints a message.
#
# def add_prefix(prefix):
#     def decorator(func):
#         def wrapper():
#             print(f"{prefix}")
#             func()
#         return wrapper
#     return decorator
#
# @add_prefix("Note:")
# def printing_message():
#     print("Original function")
#
# printing_message()
#
# # Write a decorator factory called repeat_times(n) that:
# # Takes an integer n.
# # When used to decorate a function, it runs that function n times every time it's called.
#
# def repeat_times(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             result = None
#             for _ in range(n):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator
# @repeat_times(3)
# def add(a, b):
#     return a + b
#
#
# print(add(2, 4))
#
# # Task:
# # Create a decorator called warn() that:
# #
# # When applied to a function, it prints "Warning: Function is about to run!" before executing the actual function.
# # Then it runs the original function.
#
# def warn(func):
#     def wrapper(*args, **kwargs):
#         print("Warning: Function is about to run!")
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
# @warn
# def add(a, b):
#     return a + b
#
# print(add(2, 4))

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

# def call_counter(func):
#     counter = 0
#     def wrapper(*args, **kwargs):
#         nonlocal counter
#         result = func(*args, **kwargs)
#         counter += 1
#         print(f"The function has been called {counter} times")
#         return result
#
#     return wrapper
# @call_counter
# def multiply(a, b):
#     return a * b
#
# print(multiply(2, 3))
# print(multiply(2, 3))
#
# # Task: Create a Timer with a Reset Function
# # Objective:
# # Design a decorator that:
# #
# # Measures how long a function takes to run.
# # Stores the total accumulated time across multiple calls.
# # Provides a method to reset the accumulated time.
# import time
# def outer(func):
#     elapsed_time = 0
#     def wrapper(*args, **kwargs):
#         nonlocal elapsed_time
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         elapsed = end - start
#         elapsed_time += elapsed
#         print(f"Total elapsed time: {elapsed_time}")
#         return elapsed
#     def reset():
#         nonlocal elapsed_time
#         elapsed_time = 0
#         print(f"Total elapsed time: {elapsed_time}")
#     wrapper.reset = reset
#     return wrapper
# @outer
# def some_task():
#     time.sleep(1.5)
#
# some_task()
# some_task()
# some_task.reset()
#
# # 2. Timing Decorator
# # Write a decorator that prints how long a function takes to execute.
# import time
# def timing(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time() - start
#         print(f"Took {end} seconds.")
#         return result
#     return wrapper
# @timing
# def do_dat():
#     time.sleep(3)
#
# do_dat()

# Task: Timing Decorator with Multiple Runs
# Objective:
# Create a decorator timed_repeats(n) that:
#
# Accepts an integer n, the number of times to run a function.
# When applied to a function, it runs the function n times.
# Measures the total time taken for all n executions.
# Prints out the total duration after all runs.
import time
# def timed_repeats(n):
#     def outer1(func):
#         def wrapper(*args, **kwargs):
#             start = time.time()
#             result = None
#             for _ in range(n):
#                 result = func(*args, **kwargs)
#             elapsed = time.time() - start
#             wrapper.total_time += elapsed
#             average_time = wrapper.total_time / n
#             print(f"total time for {n} runs: {wrapper.total_time:.3f} and average time for a run is {average_time:.3f}")
#             return result
#         wrapper.total_time = 0
#         def reset():
#             wrapper.total_time = 0
#             print("Total time has been reset")
#         wrapper.reset = reset
#         return wrapper
#     return outer1
# @timed_repeats(3)
# def do_something():
#     time.sleep(1.5)
#
# do_something()
# do_something.reset()
# do_something()
# do_something()

# 3. Print Function Name
# Decorator that prints the name of the function being called.

# def naming(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(func.__name__)
#         return result
#     return wrapper
#
#
# @naming
# def do():
#     print("1")
#
# do()
#
# # Task: Create a Decorator that Prints a Custom Message and Function Name
# # Objective:
# #
# # Write a decorator called announce() that:
# # Takes a string message as a parameter.
# # When applied to a function, it prints this message before calling the function.
# # Also prints the name of the function being called.
# def factory(message):
#     def announce(func):
#         def wrapper(*args, **kwargs):
#             print(f"the message: {message}")
#             print(f"function name: {func.__name__}")
#             return func(*args, **kwargs)
#         return wrapper
#     return announce
#
# @factory("Run away")
# def do_that():
#     print("1")
#
# do_that()
#
# # 4. Repeat Function Call
# # Decorator that makes a function run twice whenever called.
#
# def decorator(func):
#     def wrapper():
#         print("Calling the function twice below.")
#         func()
#         func()
#         print(f"the function \"{func.__name__}\" has been called twice above.")
#     return wrapper
#
# @decorator
# def do_something():
#     print("doing")
#
# do_something()
#
# # ask: Create a Repeat N Times Decorator
# # Objective:
# # Write a decorator factory repeat(n) that:
# #
# # Accepts a number n.
# # When used to decorate a function, it makes the function run n times every time you call it.
# # After the function runs n times, it prints a message saying it was repeated n times.
#
# def decorator_factory(n):
#     def decor(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 result = func(*args, **kwargs)
#             wrapper.total_calls += n
#             print(f"The function \"{func.__name__}\" was repeated {n} times this invocation, and {wrapper.total_calls} in total.")
#             return result
#         wrapper.total_calls = 0
#
#         def reset():
#             wrapper.total_calls = 0
#             print("Counter reset to 0")
#         wrapper.reset = reset
#         return wrapper
#     return decor
# @decorator_factory(3)
# def add(a, b):
#     print(a + b)
#
# add(2, 4)
# add(3, 5)
# add(3, 5)
# add.reset()
# add(4, 6)
#
# # 5. Add Pre/Post Messages
# # Decorator that prints "Start" before and "End" after the function runs.
#
# def dec(func):
#     def wrapper(*args, **kwargs):
#         print("Start")
#         res = func(*args, **kwargs)
#         print(f"{res}")
#         print("End")
#         return res
#     return wrapper
# @dec
# def subtract(a, b):
#     return a - b
#
# print(subtract(5, 3))
#
# # Task: Decorator for Logging Arguments
# # Objective:
# # Create a decorator log_args() that:
# #
# # When applied to a function, it prints all the arguments and keyword arguments the function is called with whenever it runs.
# # Then, it executes the original function normally.
#
# def log_args(func):
#     def wrapper(*args, **kwargs):
#         print(f"Arguments:", args)
#         print(f"Keyword arguments:", kwargs)
#         res = func(*args, **kwargs)
#         return res
#     return wrapper
# @log_args
# def adding(a, b):
#     return a + b
#
# result = adding(2, 2)
# print(result)
#
# @log_args
# def greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}!")
#
# greet("Alice", greeting="Hi")
# greet("Bob")
#
# # 6. Number of Calls
# # Decorator that keeps track of how many times a function has been called and prints the count each time.
#
# def decorator12(func):
#     count = 0
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         result = func(*args, **kwargs)
#         count += 1
#         print(f"The count is {count}")
#         return result
#     return wrapper
# @decorator12
# def doink():
#     print("the function is happening")
#
# doink()
# doink()
#
# # Objective:
# # Create a decorator log_calls() that:
# #
# # Every time the decorated function is called, it prints:
# #
# # The name of the function.
# # All positional arguments passed.
# # All keyword arguments passed.
# # Then, it runs the original function and returns its result.
#
#
# def log_calls(func):
#     def wrapper(*args, **kwargs):
#         print(f"{func.__name__} is the name of the function")
#         print(f"Arguments: {args}")
#         print(f"Keyword arguments: {kwargs}")
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
# @log_calls
# def multi(a, b, **kwargs):
#     return a * b
#
# print(multi(2, 4, name="Sergiusz"))
#
# # 7. Uppercase Output
# # Decorator for functions that return strings to convert the output to uppercase.
#
# def decor_upper(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         result = result.upper()
#         return result
#     return wrapper
# @decor_upper
# def write(a):
#     return a
#
# print(write("Sergiusz"))
#
# # Objective:
# # Create a decorator factory add_prefix(prefix) that:
# #
# # Accepts a string prefix.
# # When applied to a function, it:
# # Calls the original function (which returns a string).
# # Adds the prefix before the string.
# # Converts the entire string to uppercase.
# # Returns this modified string.
#
# def add_prefix(prefix):
#     def decor(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             result = f"{prefix} {result}"
#             result = result.upper()
#             return result
#         return wrapper
#     return decor
# @add_prefix("Sir")
# def text():
#     return "Sergiusz"
# print(text())
#
#
# # 8. Logging Decorator
# # Decorator that logs the arguments a function receives.
#
# def dec(func):
#     def wrapper(*args, **kwargs):
#         print("Arguments:", args)
#         print("Keyword arguments", kwargs)
#         result = func(*args, **kwargs)
#         print("The end")
#         return result
#     return wrapper
# @dec
# def dividing(a, b):
#     return a // b
#
# print(dividing(4, 2))
#
#
#
# # 9. Simple Validation
# # Decorator that checks if the arguments are positive numbers before calling the function.
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         for arg in args:
#             if arg <= 0:
#                 print("Arguments must be positive numbers.")
#         return func(*args, **kwargs)
#     return wrapper
#
# @decorator
# def square(x):
#     return x * x
#
# print(square(3))
#
#
# # 10. Decorator with Arguments
# # Write a decorator that takes an argument (like a prefix string) and adds it before the function's output.
#
#
# def factory(prefix):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             result = f"{prefix} {func(*args, **kwargs)}"
#             return result
#         return wrapper
#     return decorator
# @factory("Mr.")
# def upper(a):
#     return a.upper()
#
# print(upper("Sergiusz"))
#
# # 1. Basic Message Decorator
# # Create a decorator that prints "Function is about to run" before calling any function.
#
# def dec1(func):
#     def wrapper(*args, **kwargs):
#         print(f"Function is about to run")
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
#
# @dec1
# def add(a, b):
#     print(a + b)
#     return a + b
#
# add(1, 2)
#
# # Objective:
# # Build a decorator call_tracker() that:
# #
# # Keeps track of how many times each decorated function is called.
# # Prints the number of times that specific function has been called each time it runs.
# # Works with multiple functions independently, so the call count is maintained separately for each one.
#
# def call_tracker(func):
#     func.calls = 0
#     def wrapper(*args, **kwargs):
#         func.calls += 1
#         print(f"{func.__name__} has been called {func.calls} times.")
#         return func(*args, **kwargs)
#     return wrapper
# @call_tracker
# def subtract(a, b):
#     print(a - b)
#     return a - b
#
# subtract(2, 5)
# subtract(3, 5)
#
# @call_tracker
# def multiply(a, b):
#     print(a * b)
#     return a * b
#
# multiply(2, 5)

# Task: Create a Decorator that Tracks Call Counts and Total Execution Time (with Reset)
# Objective:
# Design a decorator factory called track_calls_and_time() that:
#
# When applied to a function, it:
# Counts how many times the function has been called.
# Records the total CPU time spent executing the function across all calls.
# Provides a method .reset() to reset both the call count and total time.
# Prints the current call count and total execution time each time the function is called.

# def track_calls_and_time():
#     def decorator(func):
#         func.calls = 0
#         func.total_time = 0
#         def wrapper(*args, **kwargs):
#             start = time.perf_counter()
#             result = func(*args, **kwargs)
#             end = time.perf_counter()
#
#             func.calls += 1
#             func.total_time += end - start
#             print(f"Current call count is: {func.calls} and elapsed time is: {end}")
#             return result
#
#         def reset():
#             func.calls = 0
#             func.total_time = 0
#             print("Counters and total time reset.")
#         wrapper.reset = reset
#         wrapper.calls = lambda: func.calls
#         wrapper.total_time = lambda: func.total_time
#         return wrapper
#     return decorator
#
# @track_calls_and_time()
# def do_smething():
#     time.sleep(0.5)
#
# do_smething()
# do_smething()
# print(f"Total calls: {do_smething.calls()}")
# print(f"Total time: {do_smething.total_time():.4f}")
# do_smething.reset()
# print(f"After reset - calls: {do_smething.calls()}, total: {do_smething.total_time()}")
#
#
#
# # 2. Timing Decorator
# # Write a decorator that measures and prints how long a function takes to execute.
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         end = time.perf_counter() - start
#         print(f"{func.__name__} took {end} seconds.")
#         return result
#     return wrapper
#
# @decorator
# def sleep():
#     time.sleep(5)
#
# sleep()

# Objective:
# Create a decorator measure_average_time(n) that:
#
# Accepts a number n, the number of times to run the decorated function each time it is called.
# Measures the total time taken to execute the function n times.
# Calculates and prints the average execution time per run after completing all n executions.
# Keeps a running total of the cumulative average time across multiple calls.
# Optionally, supports a reset() method to reset the total.

# def measure_average_time(n):
#     def decorator(func):
#         func.total_time = 0
#         func.total_runs = 0
#         def wrapper(*args, **kwargs):
#             start = time.perf_counter()
#             for _ in range(n):
#                 func(*args, **kwargs)
#             end = time.perf_counter()
#
#             elapsed = end - start
#
#             func.total_time += elapsed
#             func.total_runs += n
#
#             avg_time = func.total_time / func.total_runs
#             print(f"Average time over {func.total_runs} runs: {avg_time:.4f} seconds")
#             return
#         def reset():
#             func.total_time = 0
#             func.total_runs = 0
#             print("Counters have been reset.")
#
#         wrapper.reset = reset
#         return wrapper
#     return decorator
# @measure_average_time(2)
# def do():
#     time.sleep(2)
#
# do()
# do()
# do.reset()
# do()

# 3. Function Name Printer
# Create a decorator that prints the name of the function being called.

def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"The name of the function is: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@decorator
def add(a, b):
    print(a + b)
    return a + b

add(2, 4)


# 4. Repeat Call Decorator
# Make a decorator that runs a function twice every time it's called.

def decor(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        func(*args, **kwargs)
        return result
    return wrapper
@decor
def adding(a, b):
    print(a + b)
    return a + b

adding(2, 1)

# 5. Add Pre/Post Messages
# Create a decorator that prints "Start" before and "End" after the function runs.

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper
@decorator
def subtracting(a, b):
    print(a - b)
    return a - b

subtracting(5, 10)

# Objective:
# Write a decorator factory log_with_messages(pre_msg, post_msg) that:
#
# Accepts two strings, pre_msg and post_msg.
# When applied to a function:
# Prints pre_msg before the function runs.
# Prints post_msg after the function completes.
# Keeps track of how many times the function has been called.
# Each time the function runs, it also prints the call count.

def log_with_messages(pre_msg, post_msg):
    def decorator(func):
        func.calls = 0
        def wrapper(*args, **kwargs):
            print(f"{pre_msg}")
            result = func(*args, **kwargs)
            print(f"{post_msg}")
            func.calls += 1
            print(f"The number of calls: {func.calls}")
            return result
        def reset():
            func.calls = 0
            print("Call count has been reset.")
        wrapper.reset = reset
        return wrapper
    return decorator
@log_with_messages("Hello", "Bye")
def multi(a, b):
    print(a * b)
    return a * b

multi(2, 5)
multi(3, 6)
multi.reset()
multi(4, 4)
# 6. Call Counter
# Write a decorator that counts how many times a function has been called and prints the count each time.

def dec(func):
    func.total = 0
    def wrapper(*args, **kwargs):
        print("hey")
        result = func(*args, **kwargs)
        func.total += 1
        print(f"\"{func.__name__}\" has been called {func.total} times.")
        print("bye")
        return result
    return wrapper
@dec
def printing():
    print("Yes")

printing()
printing()

# 7. Uppercase Output
# Make a decorator for functions that return strings to always convert their output to uppercase.

def dec(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result = result.upper()
        return result
    return wrapper
@dec
def text():
    return "abc"

print(text())


# 8. Log Arguments
# Create a decorator that logs all arguments and keyword arguments passed to a function each time.

def decor(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments:", args,
              f"Keyword arguments:", kwargs)
        result = func(*args, **kwargs)
        return result
    return wrapper

@decor
def addx(a, b, **kwargs):
    print(a + b)
    print(kwargs)
    return a + b

addx(1, 5, name="Sergiusz")


# 9. Input Validation
# Build a decorator that checks if all numeric arguments are positive before running the function, giving a warning if not.

def decorator(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)):
                if arg <= 0:
                    print(f"{arg} not a positive number.")
                    return

        return func(*args, **kwargs)
    return wrapper
@decorator
def dividing(a, b):
    return a / b

print(dividing(4, 2))

# 10. Decorator with Arguments
# Write a decorator that accepts an argument (like a prefix string) and adds that prefix to the function's string output.

def factory(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, str):
                return f"{prefix} {result}"
            else:
                return f"{prefix} {str(result)}"
        return wrapper
    return decorator

@factory("Hey")
def addi(a, b):
    return a + b
print(addi(2, 5))