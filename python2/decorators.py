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

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"The name of the function is: {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper
#
# @decorator
# def add(a, b):
#     print(a + b)
#     return a + b
#
# add(2, 4)
#
#
# # 4. Repeat Call Decorator
# # Make a decorator that runs a function twice every time it's called.
#
# def decor(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         func(*args, **kwargs)
#         return result
#     return wrapper
# @decor
# def adding(a, b):
#     print(a + b)
#     return a + b
#
# adding(2, 1)
#
# # 5. Add Pre/Post Messages
# # Create a decorator that prints "Start" before and "End" after the function runs.
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Start")
#         result = func(*args, **kwargs)
#         print("End")
#         return result
#     return wrapper
# @decorator
# def subtracting(a, b):
#     print(a - b)
#     return a - b
#
# subtracting(5, 10)
#
# # Objective:
# # Write a decorator factory log_with_messages(pre_msg, post_msg) that:
# #
# # Accepts two strings, pre_msg and post_msg.
# # When applied to a function:
# # Prints pre_msg before the function runs.
# # Prints post_msg after the function completes.
# # Keeps track of how many times the function has been called.
# # Each time the function runs, it also prints the call count.
#
# def log_with_messages(pre_msg, post_msg):
#     def decorator(func):
#         func.calls = 0
#         def wrapper(*args, **kwargs):
#             print(f"{pre_msg}")
#             result = func(*args, **kwargs)
#             print(f"{post_msg}")
#             func.calls += 1
#             print(f"The number of calls: {func.calls}")
#             return result
#         def reset():
#             func.calls = 0
#             print("Call count has been reset.")
#         wrapper.reset = reset
#         return wrapper
#     return decorator
# @log_with_messages("Hello", "Bye")
# def multi(a, b):
#     print(a * b)
#     return a * b
#
# multi(2, 5)
# multi(3, 6)
# multi.reset()
# multi(4, 4)
# # 6. Call Counter
# # Write a decorator that counts how many times a function has been called and prints the count each time.
#
# def dec(func):
#     func.total = 0
#     def wrapper(*args, **kwargs):
#         print("hey")
#         result = func(*args, **kwargs)
#         func.total += 1
#         print(f"\"{func.__name__}\" has been called {func.total} times.")
#         print("bye")
#         return result
#     return wrapper
# @dec
# def printing():
#     print("Yes")
#
# printing()
# printing()
#
# # 7. Uppercase Output
# # Make a decorator for functions that return strings to always convert their output to uppercase.
#
# def dec(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         result = result.upper()
#         return result
#     return wrapper
# @dec
# def text():
#     return "abc"
#
# print(text())
#
#
# # 8. Log Arguments
# # Create a decorator that logs all arguments and keyword arguments passed to a function each time.
#
# def decor(func):
#     def wrapper(*args, **kwargs):
#         print(f"Arguments:", args,
#               f"Keyword arguments:", kwargs)
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
#
# @decor
# def addx(a, b, **kwargs):
#     print(a + b)
#     print(kwargs)
#     return a + b
#
# addx(1, 5, name="Sergiusz")
#
#
# # 9. Input Validation
# # Build a decorator that checks if all numeric arguments are positive before running the function, giving a warning if not.
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         for arg in args:
#             if isinstance(arg, (int, float)):
#                 if arg <= 0:
#                     print(f"{arg} not a positive number.")
#                     return
#
#         return func(*args, **kwargs)
#     return wrapper
# @decorator
# def dividing(a, b):
#     return a / b
#
# print(dividing(4, 2))
#
# # 10. Decorator with Arguments
# # Write a decorator that accepts an argument (like a prefix string) and adds that prefix to the function's string output.
#
# def factory(prefix):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             if isinstance(result, str):
#                 return f"{prefix} {result}"
#             else:
#                 return f"{prefix} {str(result)}"
#         return wrapper
#     return decorator
#
# @factory("Hey")
# def addi(a, b):
#     return a + b
# print(addi(2, 5))

# 1. Basic Print Message Decorator
# Create a decorator that prints "Function is about to run" before executing any function.

# def decor(func):
#     def wrapper(*args, **kwargs):
#         print("Function is about to run")
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
# @decor
# def adding(a, b):
#     print(a + b)
#     return a + b
#
# adding(2, 4)
#
# # Task: Create a Decorator that Logs Function Execution
# # Objective:
# # Make a decorator that:
# #
# # Prints "Starting execution of {function name}" before running.
# # Prints "Finished execution of {function name}" after the function completes.
# # Supports functions with any number of arguments and return a result.
#
# def decorator2(func):
#     def wrapper(*args, **kwargs):
#         print(f"Starting execution of \"{func.__name__}\"")
#         result = func(*args, **kwargs)
#         print(f"Finished execution of \"{func.__name__}\"")
#         return result
#     return wrapper
#
# @decorator2
# def do():
#     print(f"The funkcjone")
#
# do()
#
# # Objective:
# # Design a decorator factory called log_and_time(start_msg, end_msg) that:
# #
# # Accepts two string arguments for custom start and end messages.
# # When applied to a function:
# # Prints the custom start message before executing.
# # Measures and prints the execution time of the function.
# # Prints the custom end message after the function completes.
# # Supports functions with any arguments and preserves their return values.
#
# def log_and_time(start_msg, end_msg):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print(f"{start_msg}")
#             start = time.perf_counter()
#             result = func(*args, **kwargs)
#             end = time.perf_counter() - start
#             print(f"the time it took for the function: {end:.3f} seconds")
#             print(f"{end_msg}")
#             return result
#         return wrapper
#     return decorator
#
#
# @log_and_time("Starting", "Ending")
# def sleep():
#     time.sleep(2)
#
# sleep()
#
# # Objective:
# # Build a decorator factory track_stats() that:
# #
# # When applied to a function:
# # Tracks the total number of calls to that function.
# # Tracks the total execution time across all calls.
# # Prints the call count and total time each time the function is invoked.
# # Provides a .reset() method to reset both counters and total time.
#
#
# def track_stats():
#     def decorator(func):
#         func.total_calls = 0
#         func.total_execution_time = 0
#         def wrapper(*args, **kwargs):
#             start = time.perf_counter()
#             result = func(*args, **kwargs)
#             end = time.perf_counter() - start
#             func.total_execution_time += end
#             func.total_calls += 1
#             print(f"{func.__name__} has been called {func.total_calls} times and took {func.total_execution_time}.")
#             return result
#
#         def reset():
#             func.total_calls = 0
#             func.total_execution_time = 0
#             print("Both counters have been reset.")
#
#         wrapper.reset = reset
#         return wrapper
#     return decorator
#
# @track_stats()
# def printing():
#     time.sleep(0.5)
#     print("Hello")
#
# printing()


# 2. Timing a Function
# Write a decorator that measures how long a function takes to run and prints the elapsed time.

# def decor(func):
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         end = time.perf_counter() - start
#         print(f"Elapsed time is {end:.3f}")
#         return result
#     return wrapper
# @decor
# def power(a, b):
#     time.sleep(0.2)
#     print(a ** b)
#     return a ** b
#
# power(2, 2)
#
# # Objective:
# # Create a decorator factory measure_stats() that:
# #
# # When applied to a function, it:
# #
# # Measures the total execution time for each call.
# # Maintains a cumulative total of all execution times.
# # Counts how many times the function has been called.
# # After each call, it prints:
# # The latest execution time.
# # The cumulative total time.
# # The number of calls.
# # Supports a .reset() method that resets all these stats (call count, total time).
#
#
# def measure_stats():
#     def decorator(func):
#         func.last_run_time = 0
#         func.cumulative = 0
#         func.calls = 0
#         def wrapper(*args, **kwargs):
#             start = time.perf_counter()
#             result = func(*args, **kwargs)
#             end = time.perf_counter() - start
#             func.last_run_time = end
#             func.cumulative += end
#             func.calls += 1
#             print(f"Last run time is {func.last_run_time}. "
#                   f"Total cumulative time is {func.cumulative}. "
#                   f"The amount of calls are: {func.calls}.")
#             return result
#
#         def reset():
#             func.last_run_time = 0
#             func.cumulative = 0
#             func.calls = 0
#             print("The counts have been reset.")
#
#         wrapper.reset = reset
#         return wrapper
#     return decorator
#
# @measure_stats()
# def sleeping():
#     time.sleep(1)
#
# sleeping()
# sleeping()
# sleeping()
#
#
# # 3. Function Name Logger
# # Create a decorator that prints the name of each function before it executes.
#
# def name_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"\"{func.__name__}\" is the name of the function.")
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
# @name_decorator
# def calculating(a, b):
#     print(a ** b)
#     return a ** b
#
# calculating(2, 5)
#
# # Objective:
# # Write a decorator factory log_details(start_msg, end_msg) that:
# #
# # Accepts two string messages: start_msg and end_msg.
# # When applied to a function:
# # Prints start_msg along with the function name and arguments before running.
# # Prints end_msg after the function finishes.
# # Supports functions with any number and types of arguments.
# # The messages should be customizable, allowing you to specify your own log text.
#
# def log_details(start_msg, end_msg):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print(f"{start_msg} - function name: \"{func.__name__}\", Arguments: {args}, Keyword arguments: {kwargs}")
#             result = func(*args, **kwargs)
#             print(f"{end_msg}")
#             return result
#         return wrapper
#     return decorator
# @log_details("Yo men's", "Bye men's")
# def calc(a, b):
#     print(f"the sum of arguments is {a + b}")
#     return a + b
#
# calc(10, 15)
#
# # 4. Repeat Function Call
# # Make a decorator that calls the decorated function twice every time it’s invoked.
#
# def repeat_decor(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         res = func(*args, **kwargs)
#         return res
#     return wrapper
#
# @repeat_decor
# def sleeping():
#     time.sleep(2)
#     print("I just slept for 2 seconds.")
#
# sleeping()
#
# # Objective:
# # Write a decorator factory repeat_n_times(n) that:
# #
# # Accepts an integer n.
# # When applied to a function, it runs that function exactly n times every time it's called.
# # After executing, it prints:
# # How many total times the function has been called since the decoration (across all calls).
# # The total time spent executing the function across all calls.
# # Supports a .reset() method to reset both counters and total time.
#
# def repeat_n_times(n):
#     def dec(func):
#         func.total = 0
#         func.execution_time = 0
#         def wrapper(*args, **kwargs):
#             start = time.perf_counter()
#             for _ in range(n):
#                 result = func(*args, **kwargs)
#             elapsed = time.perf_counter() - start
#             func.total += n
#             func.execution_time += elapsed
#             print(f"total calls: {func.total}, time: {func.execution_time}")
#             return result
#         def reset():
#             func.total = 0
#             func.execution_time = 0
#             print("Counters reset")
#         wrapper.reset = reset
#         return wrapper
#     return dec
#
# @repeat_n_times(3)
# def sleepzzz():
#     time.sleep(0.3)
#     print("ZzZzZ")
#
# sleepzzz()
# sleepzzz()
# sleepzzz.reset()
# sleepzzz()
#
#
# # 5. Add Pre/Post Messages with Custom Text
# # Create a decorator that accepts custom messages to print before and after the function runs.
#
# def factory(pre, post):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print(f"{pre}")
#             result = func(*args, **kwargs)
#             print(f"{post}")
#             return result
#         return wrapper
#     return decorator
# @factory("welcome", "salutations")
# def adding(a, b):
#     print(a + b)
#     return a + b
#
# adding(1, 2)

# Objective:
# Write a decorator factory log_with_counts(pre_msg, post_msg) that:
#
# Accepts two custom messages (pre_msg, post_msg).
# When applied to a function:
# Prints the pre_msg before executing.
# Prints the post_msg after executing.
# Keeps track of how many times the function has been called since the decorator was applied.
# After each call, prints the total number of calls.

# def log_with_counts(pre_msg, post_msg):
#     def decorator(func):
#         func.total_calls = 0
#         def wrapper(*args, **kwargs):
#             print(f"This is the message that is to be shown before the function executes: {pre_msg}")
#             result = func(*args, **kwargs)
#             print(f"This is the message that is to be shown after the function executes: {post_msg}")
#             func.total_calls += 1
#             print(f"The amount of calls so far is: {func.total_calls}")
#             return result
#         return wrapper
#     return decorator
# @log_with_counts("Giasas", "Kalinixta")
# def do_something():
#     print("This is the message of the function.")
#
# do_something()
#
#
# # 6. Count How Many Times a Function Is Called
# # Decorator that keeps track of and prints how many times the function has been called.
#
# def dec(func):
#     func.calls = 0
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         func.calls += 1
#         print(f"The amount of calls is {func.calls}")
#         return result
#     return wrapper
# @dec
# def adding(a, b):
#     return a + b
#
# print(adding(2, 5))
#
#
# # 7. Convert String Outputs to Uppercase
# # Decorator for functions that return strings, transforming their output to uppercase.
#
# def upper_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.upper()
#     return wrapper
# @upper_decorator
# def printing_text(text):
#     return text
#
# print(printing_text("sergiusz"))
#
# # Objective:
# # Write a decorator factory transform_output(transformation) that:
# #
# # Accepts a transformation function (e.g., str.lower, str.replace, custom functions).
# # When applied to a function that returns a string, it:
# # Calls the original function.
# # Applies the transformation to the output.
# # Prints the transformed output.
# # Returns the transformed output.
#
# def transform_output(transformation):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             if not isinstance(result, str):
#                 result = str(result)
#             print(f"Before transformation: \"{result}\"")
#             transformed = transformation(result)
#             print(f"After transformation: \"{transformed}\"")
#             return transformed
#         return wrapper
#     return decorator
#
# @transform_output(str.title)
# def greet():
#     return "hello world"
#
# greet()
#
# # 8. Log Function Arguments
# # Create a decorator that logs all positional and keyword arguments passed to a function each time it’s called.
#
# def deco(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f"Positional arguments: {args}")
#         print(f"Keyword arguments: {kwargs}")
#         return result
#     return wrapper
# @deco
# def some(a, b, c):
#     return a + b + c
#
# print(some(2, 4, 6))
#
# # 9. Validate Numeric Arguments
# # Decorator that checks if all numeric arguments are positive before calling the function; if not, print a warning.
#
# def validate(func):
#     def wrapper(*args, **kwargs):
#         for arg in args:
#             if isinstance(arg, (int, float)):
#                 if arg <= 0:
#                     print("Not a positive number")
#                     return
#         return func(*args, **kwargs)
#     return wrapper
# @validate
# def adding(a, b):
#     return a + b
#
# print(adding(10, 15))
# print(adding(-2, -4))
#
#
#
# # 10. Decorator with Arguments
# # Write a decorator that accepts parameters (like a prefix string), and when decorating a function, adds the prefix to the function’s string output.
# def fact(prefix):
#     def dec_with_pars(func):
#         def wrapper(*args, **kwargs):
#             result = f"{prefix} {func(*args, **kwargs)}"
#             return result
#         return wrapper
#     return dec_with_pars
# @fact("Sir")
# def texting(text):
#     return text
# print(texting("Sergiusz"))
#
# # Objective:
# # Create a decorator factory log(msg) that:
# #
# # Accepts a string msg.
# # When applied to a function:
# # Prints a custom message before the function runs, including the function’s name.
# # Logs each call with timestamp and arguments.
# # Executes the function.
# # Prints a message after the function, including function's name and execution time.
#
# def factory_log(msg):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print(f"The message of {func.__name__} is {msg} at {time.strftime('%Y-%m-%d %H:%M:%S')}")
#             start = time.perf_counter()
#             result = func(*args, **kwargs)
#             end = time.perf_counter()
#             duration = end - start
#             print(f"Function {func.__name__} took {duration:.4f} seconds.")
#             return result
#         return wrapper
#     return decorator
# @factory_log("Hillo")
# def doink(a, b):
#     time.sleep(.1)
#     return a + b
#
# print(doink(2, 4))
#
# # Objective:
# # Write a decorator factory requires_permission(permission_name) that:
# #
# # Accepts a string permission_name.
# # When applied to a function expecting a user dictionary argument:
# # Checks if user has the specific permission in a list, e.g., user['permissions'].
# # If the user has the permission, execute the function.
# # If not, display a message: "Access denied: missing {permission_name} permission."
#
# def requires_permission(permission_name):
#     def decorator(func):
#         def wrapper(user: dict):
#             if permission_name in user["permissions"]:
#                 return func(user)
#             else:
#                 print(f"Access denied: missing {permission_name} permission")
#         return wrapper
#     return decorator
#
# @requires_permission("view_reports")
# def view_reports(user):
#     print(f"{user['name']} is viewing reports.")
#
#
# user1 = {'name': 'Alice', 'permissions': ['view_reports', 'edit_users']}
# user2 = {'name': 'Bob', 'permissions': ['edit_users']}
# view_reports(user1)
# view_reports(user2)
#
# # Objective:
# # Write a decorator factory require_permissions(*permissions) that:
# #
# # Accepts multiple permission strings.
# # When applied to a function expecting a user dictionary argument:
# # Checks if all specified permissions are present in user['permissions'].
# # If the user has all permissions, execute the function.
# # If any permission is missing, display: Access denied: missing {permission} for each missing permission.
#
# def require_permissions(*permissions):
#     def decorator(func):
#         def wrapper(user):
#             missing = [perm for perm in permissions if perm not in user["permissions"]]
#             if missing:
#                 for perm in missing:
#                     print(f"Access denied: missing {perm}")
#             else:
#                 func(user)
#         return wrapper
#     return decorator
#
# @require_permissions("view_reports", "edit_users")
# def edit_reports(user):
#     print(f"{user['name']} is editing reports.")
#
# user1 = {'name': 'Alice', 'permissions': ['view_reports', 'edit_users']}
# user2 = {'name': 'Bob', 'permissions': ['view_reports']}
#
# edit_reports(user1)
# edit_reports(user2)
#
# # Objective:
# # Write a decorator factory require_roles(*roles) that:
# #
# # Accepts multiple role strings (e.g., 'admin', 'editor', 'user').
# # When applied to a function expecting a user dictionary with a 'roles' list:
# # Checks if the user has at least one of the specified roles.
# # If yes, execute the function.
# # If no, print: "Access denied: insufficient roles".
#
# def require_roles(*roles):
#     def decorator(func):
#         def wrapper(user):
#             missing = [role for role in roles if role not in user["roles"]]
#             if missing:
#                 print(f"Access denied: missing roles: {', '.join(missing)}")
#             else:
#                 return func(user)
#         return wrapper
#     return decorator
# @require_roles("admin")
# def manage_content(user):
#     print(f"{user['name']} is managing the content")
#
# user1 = {'name': 'Alice', 'roles': ['user', 'editor']}
# user2 = {'name': 'Bob', 'roles': ['guest']}
# user3 = {'name': 'Eve', 'roles': ['admin']}
#
# manage_content(user1)
# manage_content(user2)
# manage_content(user3)
#
# # Objective:
# # Write a decorator factory require_roles_and_permissions(roles, permissions) that:
# #
# # Accepts two lists: one of required roles, and one of permissions.
# # When applied to a function expecting a user dict with 'roles' and 'permissions' lists:
# # Checks if the user has at least one of the required roles and at least one of the required permissions.
# # If both conditions are met, executes the function.
# # If either condition fails, prints: "Access denied: missing roles or permissions."
#
# def require_roles_and_permissions(roles, permissions):
#     def decorator(func):
#         def wrapper(user):
#             missing_roles = [role for role in roles if role not in user["roles"]]
#             missing_perms = [perm for perm in permissions if perm not in user["permissions"]]
#             if missing_roles or missing_perms:
#                 message_parts = []
#                 if missing_roles:
#                     message_parts.append(f"missing roles: {', '.join(missing_roles)}")
#                 if missing_perms:
#                     message_parts.append(f"missing permissions: {', '.join(missing_perms)}")
#                 print(f"Access denied: {', '.join(message_parts)}")
#                 return
#             else:
#                 return func(user)
#         return wrapper
#     return decorator
#
# @require_roles_and_permissions(['admin', 'editor'], ['write', 'delete'])
# def delete_content(user):
#     print(f"{user['name']} is deleting content.")
#
# user1 = {'name': 'Alice', 'roles': ['user', 'editor'], 'permissions': ['write']}
# user2 = {'name': 'Bob', 'roles': ['guest'], 'permissions': ['read']}
# user3 = {'name': 'Eve', 'roles': ['admin'], 'permissions': ['write', 'delete']}
#
# delete_content(user1)
# delete_content(user2)
# delete_content(user3)
#
# # Objective:
# # Write a decorator role_required(role: str) that:
# #
# # Checks if the user dictionary has the specified role in its 'roles' list.
# # If the user has that role, it allows executing the decorated function.
# # If not, it prints: "Access denied: missing role {role}".
#
# def role_required(role: str):
#     def decorator(func):
#         def wrapper(user):
#             if role in user["roles"]:
#                 return func(user)
#             else:
#                 print(f"Access denied: missing role {role}")
#         return wrapper
#     return decorator
#
# @role_required("admin")
# def sensitive(user):
#     print("Sensitive action performed.")
#
# user1 = {'name': 'Alice', 'roles': ['user', 'admin']}
# user2 = {'name': 'Bob', 'roles': ['user']}
#
# sensitive(user1)
# sensitive(user2)
#
# # Write a decorator login_required that checks if the user dictionary has a key 'logged_in' set to True.
# #
# # If the user is logged in, it allows executing the decorated function.
# # If not, it prints: "Please log in to access this feature.".
#
# def login_required(func):
#     def wrapper(user):
#         if user["logged_in"] is True:
#             return func(user)
#         else:
#             print("Please log in to access this feature.")
#     return wrapper
#
# @login_required
# def checking(user):
#     print("User successfully logged in")
#
# user1 = {'name': 'Charlie', 'logged_in': True}
# user2 = {'name': 'Dana', 'logged_in': False}
#
# checking(user1)
# checking(user2)
#
# # Write a decorator permission_required(permission) that checks if the user dictionary has the specified permission in its 'permissions' list.
# #
# # If the user has the permission, it allows executing the decorated function.
# # If not, it prints: "Permission '{permission}' required.".
#
# def permission_required(permission):
#     def decorator(func):
#         def wrapper(user):
#             if permission in user["permissions"]:
#                 return func(user)
#             else:
#                 print(f"Permission \"{permission}\" required")
#         return wrapper
#     return decorator
#
# @permission_required('edit')
# def edit_article(user):
#     print("Article edited successfully.")
#
# user1 = {'name': 'Eve', 'permissions': ['view', 'edit']}
# user2 = {'name': 'Frank', 'permissions': ['view']}
#
# edit_article(user1)
# edit_article(user2)
#
# # Write a decorator age_required(min_age) that checks if the user dictionary has an 'age' key with a value greater than or equal to min_age.
# #
# # If the user meets the age requirement, allow the decorated function to run.
# # If not, print: "Access denied: you must be at least {min_age} years old.".
#
# def age_required(min_age):
#     def decorator(func):
#         def wrapper(user):
#             if user["age"] >= min_age:
#                 return func(user)
#             else:
#                 print(f"Access denied: you must be at least {min_age} years old.")
#         return wrapper
#     return decorator
#
# @age_required(18)
# def access(user):
#     print("Welcome to the club")
#
# user1 = {'name': 'Grace', 'age': 20}
# user2 = {'name': 'Henry', 'age': 16}
#
# access(user1)
# access(user2)
#
# # Write a decorator filter_by_role(role: str) that filters a list of user dictionaries,
# # allowing only users with the specified role in their "roles" list to be processed by the decorated function.
# #
# # Details:
# #
# # The decorator should accept a role string.
# # The wrapper function should take a list of user dictionaries.
# # It filters only users who have that role in their "roles" list.
# # It then calls the decorated function with the filtered list.
#
# def filter_by_role(role: str):
#     def decorator(func):
#         def wrapper(user_list):
#             new_users = [user for user in user_list if role in user["roles"]]
#             func(new_users)
#         return wrapper
#     return decorator
#
# @filter_by_role('viewer')
# def process_editors(users):
#     for user in users:
#         print(f"Processing editor: {user['username']}")
#
# users_list = [
#     {'username': 'alice', 'roles': ['viewer', 'editor']},
#     {'username': 'bob', 'roles': ['viewer']},
#     {'username': 'carol', 'roles': ['editor', 'admin']}
# ]
#
# process_editors(users_list)
#
# # Write a decorator exclude_users_with_age(age_limit: int) that filters out users whose 'age' is less than or equal to the given age_limit.
# #
# # The decorator should accept an age limit.
# # The wrapper function should take a list of user dictionaries.
# # It filters out users whose 'age' is less than or equal to age_limit.
# # Then, it calls the decorated function with the filtered list.
#
# def exclude_users_with_age(age_limit: int):
#     def decorator(func):
#         def wrapper(user_list):
#             filtered = [user for user in user_list if user["age"] <= age_limit]
#             return func(filtered)
#         return wrapper
#     return decorator
#
# @exclude_users_with_age(25)
# def process_users(users):
#     for user in users:
#         print(f"Processing user: {user['username']} who is {user['age']} years old.")
#
# users_list = [
#     {'username': 'alice', 'age': 30},
#     {'username': 'bob', 'age': 22},
#     {'username': 'carol', 'age': 27},
#     {'username': 'dave', 'age': 24}
# ]
#
# process_users(users_list)
#
# # Write three decorators:
# #
# # uppercase_strings: Converts all string elements in a list to uppercase before passing to the decorated function.
# # filter_strings_by_length(length: int): Filters elements in the list, keeping only strings with length greater than the specified length.
# # append_suffix(suffix: str): Appends a suffix to each string element in the list before passing it to the decorated function.
# # Then, create a decorated function that:
# #
# # Accepts the processed list.
# # Returns a string describing the processed strings.
#
# def uppercase_strings(func):
#     def wrapper(items):
#         uppercase_list = [item.upper() for item in items]
#         return func(uppercase_list)
#     return wrapper
#
# def filter_strings_by_length(length: int):
#     def decorator(func):
#         def wrapper(items):
#             print("Before filter:", items)  # Debug
#             length_list = [item for item in items if len(item) > length]
#             print("After filter:", length_list)
#             return func(length_list)
#         return wrapper
#     return decorator
#
# def append_suffix(suffix):
#     def decorator(func):
#         def wrapper(items):
#             new_list = [item + " " + suffix for item in items]
#             return func(new_list)
#         return wrapper
#     return decorator
#
# @filter_strings_by_length(5)
# @append_suffix("hey")
# @uppercase_strings
# def process_strings(strings):
#     return f"Processed strings: {', '.join(strings)}"
#
#
# strings_list = ['apple', 'dog', 'banana', 'cat', 'kiwi']
# print(process_strings(strings_list))

# 1. Logging Decorator Stack
# Create three decorators:
#
# log_start: prints "Starting function..."
# log_args: prints the arguments passed
# log_end: prints "Function finished"
# Apply them to a simple function and observe the order of logs.

def log_start(func):
    def wrapper(*args, **kwargs):
        print("Starting function")
        result = func(*args, **kwargs)
        return result
    return wrapper

def log_args(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments passed: {args}")
        result = func(*args, **kwargs)
        return result
    return wrapper


def log_end(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Function finished")
        return result
    return wrapper

@log_end
@log_args
@log_start
def add(a, b):
    return a + b

print(add(2, 1))


# 2. Number Transformation Chain
# Create decorators:
#
# multiply_by_two: multiplies numeric inputs by 2
# add_five: adds 5 to numeric inputs
# convert_to_string: converts the result to a string
# Apply them to a function that takes a number and returns it.


def multiply_by_two(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs) * 2
        return result
    return wrapper

def add_five(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs) + 5
        return result
    return wrapper

def convert_to_string(func):
    def wrapper(*args, **kwargs):
        result = str(func(*args, **kwargs))
        return result
    return wrapper

@convert_to_string
@add_five
@multiply_by_two
def get_num():
    return 10

print(get_num())
print(type(get_num()))


# 3. String Reversal and Uppercase
# Decorators:
# to_upper: converts strings to uppercase
# reverse_string: reverses the string
# Apply to a function that processes a string.

def to_upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result = result.upper()
        return result
    return wrapper

def reverse_string(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result[::-1]
    return wrapper

@reverse_string
@to_upper
def texting(text):
    return text

print(texting("sergiusz"))

#
# 4. Access Control
# Create decorators:
# login_required: only proceeds if user['logged_in'] is True
# role_required(role): only proceed if role in user['roles']
# Apply both to a function that performs a sensitive action.

def login_required(func):
    def wrapper(user):
        if user["logged_in"] is True:
            return func(user)
        else:
            print(f"{user} not logged in")
    return wrapper

def role_required(role):
    def deco(func):
        def wrapper(user):
            if role in user["roles"]:
                return func(user)
            else:
                print(f"User {user['username']} does not have role '{role}'")
        return wrapper
    return deco

@role_required('admin')
@login_required
def sensitive_action(user):
    print(f"Sensitive action performed for {user['username']}")

user = {
    "username": "alice",
    "logged_in": True,
    "roles": ["user", "admin"]
}
sensitive_action(user)




# 5. Data Validation
# Create decorators:
# validate_type(expected_type): checks if input is of this type
# not_empty: ensures input list or string is not empty
# Chain them on a function that processes a list.

def validate_type(expected_type):
    def deco(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, expected_type):
                    print(f"Invalid type for argument {arg}. Expected {expected_type.__name__}.")
                    return

            for key, val in kwargs.items():
                if not isinstance(val, expected_type):
                    print(f"Invalid type for argument {key}: {val}. Excepted {expected_type.__name__}")
                    return
            return func(*args, **kwargs)
        return wrapper
    return deco

def not_empty(func):
    def wrapper(arg):
        if not arg:
            print("Input is empty")
            return
        return func(arg)
    return wrapper

@validate_type(list)
@not_empty
def process_list(lst):
    print("Processing list:", lst)

process_list([1, 2, 3])
process_list([])
process_list("not a list")




# 6. Performance Measurement
# Create decorators:
# start_timer: prints start time
# end_timer: prints end time and duration
# Apply both for measuring execution time of a heavy computation.
timing_data = {}
import time
def start_timer(func):
    def wrapper(*args, **kwargs):
        timing_data['start_time'] = time.time()
        print(f"Start time is: {timing_data['start_time']}")
        return func(*args, **kwargs)
    return wrapper

def end_timer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        start_time = timing_data.get('start_time')
        if start_time is None:
            print("Timing info not found.")
            return result
        end_time = time.time()
        duration = end_time - start_time
        print(f"End time: {end_time}")
        print(f"Duration: {duration}")
        return result
    return wrapper

@start_timer
@end_timer
def computation():
    time.sleep(2)

computation()

# 7. Output Formatting
# Create decorators:
# add_header: adds a header string before output
# add_footer: adds a footer after output
# Apply both to a function that returns data.

def add_header(header):
    def deco(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{header}\n{result}"
        return wrapper
    return deco

def add_footer(footer):
    def deco(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{result}\n{footer}"
        return wrapper
    return deco

@add_header("header")
@add_footer("footer")
def texting(text):
    return text

print(texting("sergiusz kuderski"))

# 8. Conditional Function Execution
# Create decorators:
#
# execute_if(condition): only execute if condition is met
# log_execution: logs every call
# Apply to a function that performs a task.
#
# 9. String Escaping and Sanitizing
# Decorators:
#
# escape_html: escapes HTML characters
# sanitize_input: removes dangerous characters
# Chain them on a function that processes user input.
#
# 10. Retry on Failure
# Create decorators:
#
# retry(times): retries the function up to times if it raises an exception
# log_attempt: logs each attempt
# Apply both on a function that randomly fails.