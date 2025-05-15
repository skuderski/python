# def add(a: int, b: int) -> int:
#     return a + b
#
# multiply = lambda a, b: a * b
#
# add(10, 5)
#
# multiply(10, 5)
#
# (lambda a, b: a * b)(10, 5)
#
# operation = add
#
# operation (10, 5)
#
# operation2 = multiply
#
# operation2 (10, 5)

# from typing import Callable
#
# def calculate(operation2: Callable) -> int:
#     result = operation2(10, 5)
#     return result

# calculate(multiply)
#
# def calculate(callback: Callable) -> int:
#     result = callback(10, 5)
#     return result
#
# calculate(add)

# def greet(name):
#     print("Hello, " + name + "!")
#
# def process_user_input(callback):
#     name = input("Enter your name: ")
#     callback(name)  # Call the callback function and pass the name
#
# # Pass the 'greet' function as a callback
# process_user_input(greet)

# Apply Function:
# Create a function call_twice(func, x) that calls func(x) two times and returns the sum.

# def func(x):
#     return x * 2
#
# def call_twice(func: Callable, x):
#     result1 = func(x)
#     result2 = func(x)
#     return result1 + result2
# print(call_twice(func, 3))

# Write a function apply_twice(func, x) that:
#
# Takes a function func and a number x.
# Calls func(x) twice.
# Returns the sum of those two results.

# def func(x):
#     return x
#
#
# def apply_twice(func: Callable, x):
#     first = func(x)
#     second = func(x)
#     return first + second
#
# print(apply_twice(func, 2))


# Create a function called execute_callback(callback) that:
#
# Takes a function callback as an argument.
# Calls that callback function without any arguments.

# def execute_callback(callback):
#     return callback()
#
#
# def add():
#     return 2 + 3
#
# print(execute_callback(add))

# Create a function called run_callback(callback) that:
#
# Takes a function named callback as a parameter.
# Calls the callback function.
# The callback function should print a message like "Callback function executed!".

# def run_callback(callback):
#     return callback()
#
# def execution():
#     print("Callback function executed.")
#
# run_callback(execution)

# Create a function called execute_twice(func) that:
#
# Takes another function func as an argument.
# Calls the func() two times.

# def execute_twice(func):
#     func()
#     func()
#
# def func():
#     print("Hi")
#
# execute_twice(func)


# Create a function called run_multiple_times(func, n) that:
#
# Takes a function func and a number n.
# Calls func() exactly n times.
from typing import Callable
# def func():
#     print("Hello")
#
# def run_multiple_times(func, n):
#     for _ in range(n):
#         func()
#
# run_multiple_times(func, 3)


# Create a function called call_three_times(func) that:
#
# Takes a function func as an argument.
# Calls the func() three times in a row.

# def call_three_times(func):
#     for _ in range(10):
#         func()
# def func():
#     print("WTF")

# call_three_times(func)


# Create a function called repeat_until_success(func, times) that:
#
# Takes a function func and an integer times.
# Calls func() repeatedly, up to times.
# Stops early if func() returns True (indicating success).
# import random
#
# def repeat_until_success(func, times: int):
#     for _ in range(times):
#         if func():
#             break
# def func():
#     result =  random.choice([True, False])
#     print(f"Function returned: {result}")
#     return result
#
# repeat_until_success(func, 5)

# Write a function call_once(func) that:
#
# Takes another function func as an argument.
# Calls func() once.
# Make sure to define a simple function like say_hello() that prints "Hello!".
# Pass it to call_once() and see the message printed.

# def call_once(func):
#     for _ in range(3):
#         func()
#         func()
#
# def say_hello():
#     print("Hello")
#
# call_once(say_hello)

# Create a function called call_n_times(func, n) that:
#
# Accepts a function func and an integer n.
# Calls the function n times in a loop.

# def call_n_times(func, n):
#     for _ in range(n):
#         func()
#
# def func():
#     print("kocham Siebie")
#
# call_n_times(func, 10)

# Create a function call_n_times_with_delay(callback, n, delay) that:
#
# Calls the function callback() exactly n times.
# Waits for delay seconds between each call.
# import time
# def call_n_times_with_delay(callback, n, delay):
#     for _ in range(n):
#         callback()
#         time.sleep(delay)
#
# def callback():
#     print("WTFF")
#
# call_n_times_with_delay(callback, 5, 2)

# Create a function called call_with_args(callback, args) that:
#
# Accepts a function callback and a tuple args.
# Calls callback() with those arguments unpacked.
# import time
# def add(a, b, c):
#     time.sleep(5)
#     print(a * b * c)
#
# def call_with_args(add, args):
#     add(*args)
#
# call_with_args(add, (2, 4, 5))

# Create a function called apply_function_to_list(func, lst) that:
#
# Accepts a function func and a list lst.
# Applies func() to each element of lst.
# Returns a new list containing the results.

# def apply_function_to_list(func, lst):
#     the_list = []
#     for item in lst:
#         result = func(item)
#         the_list.append(result)
#     return the_list
#
# def func(x):
#     return x * 2
#
# my_list = [33, 44, 55]
# result = apply_function_to_list(func, my_list)
# print(result)


# def func(word):
#     return word.upper()
#
# def uppercase(func, word):
#     result = func(word)
#     return result
#
# print(uppercase(func, "zdzisiek"))

# Create a function called apply_function that takes two arguments: a list of numbers and a function.
# Your task is to apply the given function to
# each element in the list and return a new list of the results.

# def apply_function(func, lst):
#     some_f_list = []
#     for item in lst:
#         result = func(item)
#         some_f_list.append(result)
#     return some_f_list
#
# def func(x):
#     return x ** 3
#
# the_list = [2, 4, 7, 13]
# voilla = apply_function(func,the_list)
# print(voilla)

"""GLOBAL and LOCAL variables"""

# def printer():
#     global s
#     s += " How are you?"
#     print(s)
#
# s = "Hello, mate."
# printer()
# print(s)