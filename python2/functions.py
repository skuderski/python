# # def add(a: int, b: int) -> int:
# #     return a + b
# #
# # multiply = lambda a, b: a * b
# #
# # print(add(10, 5))
# # print(multiply(2, 5))
# #
# # lambda a, b: a * b(10, 5)
# #
# # operation = add
# #
# # print(operation(1, 5))
# #
# # operation = multiply
# #
# # print(operation(2, 10))
# #
# from typing import Any, Callable
# #
# # def calculate(operation: Callable) -> int:
# #     result = operation(2, 5)
# #     return result
# #
# # print(calculate(multiply))
# #
# # def calc(callback: Callable) -> int:
# #     result = callback(2, 20)
# #     return result
# #
# # print(calc(add))
#
# def show(x: Any) -> None:
#     print(x)
#
# def test(f: Callable) -> None:
#     f(123)
#     return f
# # print(test(1))
# # print(test(show(1)))
# # print(test(None))
# # print(test(show))
# print(test(show))
# res = test(show)
# print(res(1))
# print(res(1234))
#                                     lambda
import math

# Create a lambda function that takes two numbers and returns their sum. Call it with 5 and 3.

# adding = lambda a, b: a + b
# print(adding(5, 3))
#
# # Create a lambda function that takes a list of numbers and returns a new list containing only the numbers greater than a given threshold.
# # Set the threshold to 10. Test the lambda with a list of numbers from 5 to 15.
#
# numbers = list(range(1, 16))
# greater_than_10 = lambda numbers: list(filter(lambda a: a > 10, numbers))
# result = greater_than_10(numbers)
# print(result)
# # Write a lambda function that calculates the square of a number. Test it with the number 9.
#
# squares = lambda a: a ** 2
# print(squares(9))
#
# # Use a lambda to check if a number is even. Test it with the number 8 and 7.
#
# even_nums = lambda a: a % 2 == 0
# print(even_nums(8))
# print(even_nums(7))
#
# # Create a list of numbers from 1 to 10, then use map() with a lambda to create a new list containing their squares.
#
# nums = list(range(1, 11))
# nums_1 = list(map(lambda x: x ** 2, nums))
# print(nums_1)
#
# # Use filter() with a lambda to filter out odd numbers from the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
#
# the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# odd = lambda the_list: list(filter(lambda x: x % 2 != 0, the_list))
# res = odd(the_list)
# print(res)
#
#
# # Write a lambda function that concatenates two strings and use it to concatenate "Hello" and "World".
#
# concatenate = lambda a, b: a + " " + b
# print(concatenate("Hello", "World"))
#
#
# # Create a list of words, then use sorted() with a lambda to sort the list by word length.
#
# words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
#
# sorting = lambda x: sorted(x, key=len)
# resulz = sorting(words)
# print(resulz)
# from functools import reduce
#
# # Use reduce() from functools with a lambda to compute the product of all numbers in the list [1, 2, 3, 4, 5].
#
# nums11 = [1, 2, 3, 4, 5]
# product = reduce(lambda x, y: x * y, (1, 2, 3, 4, 5))
# print(product)
#
# # Create a lambda that takes a list of tuples (name, age) and returns the list sorted by age. Test it with a few sample tuples.
#
# people = [
#     ("Alice", 30),
#     ("Bob", 25),
#     ("Charlie", 35),
#     ("Diana", 28)
# ]
#
# age_sorting = lambda lst: sorted(lst, key= lambda person: person[1])
# print(age_sorting(people))
#
# # Write a lambda function that swaps the elements of a list of two items, e.g. [1, 2], and test it.
#
# swapped = lambda x: [x[1], x[0]]
# print(swapped([1, 2]))

# Create a function that takes a number and another function.
# The function applies the passed-in function to the number and returns the result. Test it with a lambda that doubles a number.
# from typing import Any, Callable
# def some(one: int, f: Callable):
#     result = f(one)
#     return result
#
# print(some(5, lambda x: x * 2))
#
# # Create a function that takes a string and another function.
# # The function applies the passed-in function to the string and returns the result. Test it with a lambda that reverses the string.
#
# def somet(word: str, func: Callable):
#     result = func(word)
#     return result
#
# print(somet("Sergiusz", lambda x: x[::-1]))
#
# # Create a function that takes a list of integers and another function.
# # The function applies the passed-in function to the entire list and returns the result.
# # Test it with a lambda that calculates the sum of the list elements.
#
# def something(integers: list, func: Callable):
#     result = func(integers)
#     return result
#
# print(something([1, 2, 3, 4, 5], lambda x: sum(x)))
#
# # Create a function that takes a list of strings and a function.
# # The function applies the passed-in function to each string in the list (like map) and returns a new list of the transformed strings.
# # Test it with a lambda that converts each string to uppercase.
#
# def someth(strings: list, func: Callable):
#     result = [func(s) for s in strings]
#     return result
#
# print(someth(["Sergiusz", "Kuderski", "kocha"], lambda x: x.upper()))
#
# # Create a function that takes a list of integers and a function.
# # The function applies the passed-in function to each integer in the list (like map) and returns a new list of the results.
# # Test it with a lambda that computes the square root of each number (use math.sqrt).
# import math
# def somethi(integers: list, func: Callable):
#     result = [func(i) for i in integers]
#     return result
#
# print(somethi([1, 2, 3, 4, 5, 6, 7, 8, 9], lambda x: math.sqrt(x)))
#
# # Write a function that takes two numbers and a comparison function (e.g., max, min, or a custom lambda).
# # The function should return the result of applying the comparison function to the two numbers.
#
# def twonums(one: int, two: int, func: Callable):
#     result = func(one, two)
#     return result
#
# print(twonums(2, 2, lambda x, y: x ** (y * 2)))
#
# # Create a function that takes two strings and a function. The function applies the passed-in function to these two strings
# # (for example, concatenating or comparing them) and returns the result.
# # Test it with a lambda that concatenates the two strings with a space in between.
#
#
# def somethink(one: str, two: str, func: Callable):
#     result = func(one, two)
#     return result
#
# print(somethink("Sergiusz", "Kuderski", lambda a, b: a + " " + b))
#
# # Create a function that takes a list and a function,
# # and returns a new list with the function applied to each element (like map). Test with a lambda that adds 10 to each number.
#
# def lel(one: list, func: Callable):
#     result = [func(i) for i in one]
#     return result
#
# print(lel([1, 2, 3, 4, 5], lambda x: x + 10))
#
# # Create a function that takes a list of strings and a function.
# # The function applies the passed-in function only to strings that start with a vowel (A, E, I, O, U), leaving the others unchanged.
# # Return the new list. Test it with a lambda that converts strings to uppercase.
#
# def somesin(strings: list, func: Callable):
#     vowels = "aeiouAEIOU"
#     result = [func(s) for s in strings if s[0] in vowels]
#     return result
#
# print(somesin(["Sergiusz", "Kuderski", "zly", "armageddon"], lambda x: x.upper()))
#
# # Create a function that takes a list of strings and a function.
# # The function should apply the passed-in function only to strings that contain the letter 'a' (case-insensitive), leaving other strings unchanged.
# # Return the new list. Test it with a lambda that converts strings to lowercase.
#
# def check(strings: list, func: Callable):
#     result = [func(s) for s in strings if "a" in s.lower()]
#     return result
#
# print(check(["Sergiusz", "Kuderski", "Alpha"], lambda a: a.lower()))
#
#
# # Write a function that takes a string and a function, applying the function to transform the string (like changing case)
# # and returning the result. Test with a lambda that converts the string to uppercase.
#
# def transforming(word: str, func: Callable):
#     result = func(word)
#     return result
#
# print(transforming("Sergiusz", lambda x: x.upper()))
#
#
# # Create a higher-order function that takes a list of strings and a function to filter the list, returning the filtered list.
# # Test with a lambda that keeps only strings longer than 3 characters.
#
# def highorder(strings: list, func: Callable):
#     result = list(func(strings))
#     return result
#
# print(highorder(["Sergiusz", "Kuderski", "Wiesiek", "da"], lambda x: filter(lambda s: len(s) > 3, x)))
#
# # Create a higher-order function that takes a list of numbers and a function, then applies the function to each number,
# # returning a new list of the results. Test it with a lambda that computes the factorial of each number.
#
# def high(numbers: list, func: Callable):
#     result = [func(n) for n in numbers]
#     return result
#
# print(high([1, 2, 3, 4, 5], lambda x: math.factorial(x)))
#
#
# # Write a function that takes two lists and a function, applying the function to combine elements pairwise (like zip but with a custom operation).
# # For example, sum the pairs or concatenate strings.
#
# def twolists(one: list, two: list, func: Callable):
#     result = func(one, two)
#     return result
#
# print(twolists([1, 2, 3], [4, 5, 6], lambda x, y: [a + b for a, b in zip(x, y)]))
#
# # Create a function that takes a list of numbers and a function, and returns the sum of applying the function to each number.
# # Test with a lambda that squares each number before summing.
#
# def zipet(numbers: list, func: Callable):
#     total = 0
#     for n in numbers:
#         total += func(n)
#     return total
#
# print(zipet([1, 2, 3, 4, 5], lambda x: x ** 2))
#
# # Create a function that takes a list of strings and a function.
# # The function should apply the passed-in function to each string only if the string length is greater than 3,
# # then sum the lengths of the resulting strings. Return this total length.
# # Test it with a lambda that converts strings to uppercase before considering their length.
#
# def stringsz(strings: list, func: Callable):
#     total = 0
#     for s in strings:
#         if len(s) > 3:
#             transformed = func(s)
#             total += len(transformed)
#     return total
#
# print(stringsz(["Sergiusz", "Kuderski"], lambda x: x.upper()))
#
#
#
# # Write a function that accepts a list and a function, and applies the function only to elements satisfying a certain condition
# # (e.g., only even numbers).
#
# def functioning(one: list, func: Callable):
#     result = [func(i) for i in one if i % 2 == 0]
#     return result
#
# print(functioning([1, 2, 3, 4, 5], lambda x: x * 2))
#
# # Write a function that accepts a list and another function,
# # then applies the function to each element of the list that is greater than a specified threshold value.
# # The function should ignore elements that do not meet this condition.
#
# def accepting(one: list, func: Callable, threshold: int):
#     result = [func(i) for i in one if i > threshold]
#     return result
#
# print(accepting([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], lambda x: x - 1, 4))
#
#
# # Create a function that takes a list of strings and a sorting function, then returns the list sorted according to that function.
# # Test with sorted() and a lambda that sorts by string length.
#
#
# def sorting(strings: list, func: Callable):
#     result = list(sorted(strings, key=func))
#     return result
#
# print(sorting(["apple", "banana", "kiwi"], lambda x: len(x)))
#
#
# #
# # Write a function that takes a number and a list of functions, applying each function to the number and collecting the results into a list.
#
# def combinat(one: int, functions: Callable):
#     result = [func(one) for func in functions]
#     return result
# def square(x):
#     return x * x
#
# def double(x):
#     return x * 2
#
# def add_ten(x):
#     return x + 10
#
# function_list = [square, double, add_ten]
# print(combinat(5, function_list))
#
#
#                                                         # """global and local variables"""
#
# def printer():
#     global s
#     s += " how are you?"
#     print(s)
# s = "Hello, mate"
# printer()
# print("s:", s)

# Basic Scope: Write a function that declares a local variable and modifies it. Show that the global variable remains unchanged.
x = 10
def basic():
    x = 5
    x += 1
    return x

print(x)
print(basic())

# Task: Write a function that creates a local variable with the same name as a global variable,
# modifies the local variable, and then print both to show that they are independent.
y = 5
def localizing():
    y = 10
    y *= 2
    print("inside function:", y)
    return y

print("outside function:", y)
localizing()

# Task:
# Create a global list variable. Write two functions:
#
# One function should create a local list with the same name, modify it (e.g., add some elements), and print it.
# The other function should modify the global list directly (e.g., append an element to it) without creating a local list.
# In the main program:
#
# Call the first function and print the list afterward.
# Call the second function and print the list afterward.


the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def modi():
    the_list = [1, 2, 3, 4, 5]
    the_list.append(6)
    print(f"inside function: {the_list}")

def modif():
    the_list.append(6)

modi()
print(the_list)
modif()
print(the_list)

# Task:
# Create a global dictionary variable. Write three functions:
#
# One function should create a local dictionary with the same name and add some key-value pairs to it. Print the local dictionary.
# A second function should modify the global dictionary by adding or updating some key-value pairs without creating a local variable.
# A third function should attempt to modify the global dictionary by reassigning it to a new dictionary object, and observe what happens.

dictionary = {"one": 1, "two": 2, "three": 3}

def modi_dic():
    dictionary = {"four": 4, "five": 5}
    print(dictionary)

def modi_dict():
    dictionary["four"] = 4

def modi_dict_q():
    dict_modi = dictionary
    print(dict_modi)
    return dict_modi
modi_dic()
print(dictionary)
modi_dict()
print(dictionary)
modi_dict_q()
print(dictionary)


# Global Keyword: Create a global variable and a function that modifies it using the global keyword.

q = 10

def change():
    global q
    q = 15
    print(q)
    return q

print(q)
change()
print(q)

# Task:
# Create a global counter variable initialized to 0. Write three functions:
#
# One function should increment the global counter by a specified value (passed as a parameter) using the global keyword.
# A second function should decrement the global counter by a specified value, also using global.
# A third function should reset the global counter to zero, but this time, it should not use the global keyword;
# instead, explore how to reassign or modify the global variable indirectly.

counter = 0

def increment(one):
    global counter
    counter += one

def decrement(two):
    global counter
    counter -= two


print(counter)
increment(2)
print(counter)
decrement(3)
print(counter)


# Nested Functions: Write a nested function that modifies a variable from the outer function's scope.

def outer():
    x = 2
    def inner():
        nonlocal x
        x += 2
    inner()
    return x

print(outer())

# Task:
# Write a function called outer_counter() that:
#
# Initializes a local variable count to 0.
# Contains a nested function called increment() that increases count by 1 each time it is called.
# The outer_counter() function should return the increment() function itself, so that it can be called multiple times to increment the counter.
# Your goal is to use nonlocal inside increment() to modify the count variable from the outer scope.

def outer_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
counter = outer_counter()
print(counter())
print(counter())
print(counter())
# Variable Shadowing: Demonstrate how a local variable can shadow a global variable with the same name.

z = 10
def add():
    z = 2
    print(f"z inside function: {z}")
add()
print(f"z outside of function: {z}")

# Using globals(): Use the globals() dictionary to modify a global variable inside a function.

num = 100

def globaling():
    globals()["num"] = 50
    return num
print(f"before:", num)
globaling()
print(f"after:", num)

# Local vs Global Output: Write a program that prints the value of a variable before and after modification inside a function.

n = 99

def changing_n():
    global n
    n += 9
print(f"before function: {n}")
changing_n()
print(f"after function: {n}")



# Task:
# Write a program with a global variable score initialized to 50. Create two functions:
#
# add_points()
#
# Uses the global keyword to increase score by a given number.
# Prints the value of score after the update.
# subtract_points()
#
# Attempts to decrease score by a given number without using the global keyword.
# Inside this function, explore how to modify the global score indirectly, for example, by modifying a mutable object or using globals().


score = 50

def add_points(n):
    global score
    score += n
    print(score)

def subtract_points(n):
    globals()["score"] -= n
    print(globals()["score"])

print(score)
add_points(5)
subtract_points(10)

# Counter with Global Variable: Create a global counter variable that increments each time a function is called.

the_counter = 0

def incrementing():
    global the_counter
    the_counter += 1
    return the_counter
incrementing()
print(the_counter)
incrementing()
print(the_counter)

# Task:
# Create a global list called log. Write a function log_event() that:
#
# Uses the global keyword to access the list.
# Appends a timestamped message (like "Event number X" where X is the event count) to the list each time it's called.
# The message should include the current call count to track how many times the function has been executed.
# In your main program:
#
# Call log_event() multiple times.
# After each call, print the entire log list to see the sequence of logged events with timestamps.

log = []
event_count = 1
def log_event():
    global log, event_count
    log.append(f"Event {event_count}")
    event_count += 1
    return event_count
log_event()
print(log)
log_event()
print(log)
log_event()
print(log)

# Attempt to Modify Global Variable: Create a function that tries to modify a global variable without the global keyword and observe the result.

v = 10

def modify():
    global v
    v += 10
    return v
modify()

# Global List Modification: Use a global list and modify it inside a function by appending or removing elements.

some_list = [1, 2, 3, 4, 5]

def modi_list():
    global some_list
    some_list.remove(3)
    return some_list

print(some_list)
modi_list()
print(some_list)

def print_msg(msg):
    def printer():
        print(msg)

    return printer

another = print_msg("Hello")
another()


def make_multiplier_of(n):

    def multiplier(x):
        return x * n
    return multiplier

times_3 = make_multiplier_of(3)

print(times_3(2))

times_4 = make_multiplier_of(4)

print(times_4(3))

print(times_4(times_3(2)))

def calculate_taxes(percentage):
    def taxes(sum_of_money):
        return sum_of_money * percentage / 100
    return taxes

five = calculate_taxes(5)
ten = calculate_taxes(10)

print(five(10000))
print(ten(10000))

from typing import Callable

def produce(device_name: str) -> Callable:
    count = 0
    def device():
        nonlocal count
        count += 1
        print(f"{device_name} launch {count}")

    return device

cell = produce("Cell Phone")

cell()
cell()
cell()
cell()

# Your task:
# Write a function named make_greetings that:
#
# Takes a list of person names as input.
# Creates an inner function that takes a message type (like "hello", "meeting", "bye").
# The inner function should:
# Print a personalized message embedding the list of people.
# The messages should vary based on the message type, similar to your example.
# The outer function should return this inner function, enabling you to generate customized greeting functions for different groups of people.

def make_greetings(people: list):
    joined_people = ", ".join(people)

    def inner(message):
        if message == "yes":
            print(f"{joined_people} can.")
        elif message == "no":
            print(f"{joined_people} unfortunately can't.")
    return inner

result = make_greetings(["Sergiusz", "Inga"])
result("yes")
result("no")

# Write a function create_notifier(recipients: list, notification_type: str) that:
#
# Sets up a personalized message context:
#
# Joins the list of recipients into a single string (e.g., "Alice, Bob").
# Creates an inner function that:
#
# Accepts additional parameters (like time, location, or subject) to customize the message.
# Uses the notification_type (e.g., "reminder", "alert", "update") to determine the message content.
# Formats and returns or prints a notification message incorporating recipient names and any additional parameters.
# Returns the inner function, so it can be called later to send notifications tailored for that group and notification type.

def create_notifier(recipients: list, notification_type: str):
    joined_recipients = ", ".join(recipients)

    def inner(location, time):
        if notification_type == "reminder":
            print(f"Kind reminder - {joined_recipients}, tomorrow you have to be up at {time} at {location}")
        elif notification_type == "alert":
            print(f"{joined_recipients}, please evacuate the premises")
        elif notification_type == "update":
            print(f"{joined_recipients} are kindly asked to show up at {location} to update their data")
    return inner

result = create_notifier(["Sergiusz", "Inga"], "reminder")
result("Warsaw", 7.00)

# type annotations
from typing import Any, Callable
def validate_length(data: str, max_length: int = 10):
    return len(data) <= max_length

print(validate_length("Sergiusz"))

def validate_lowercase(data: str):
    return data.lower() == data

print(validate_lowercase("Sergiusz"))

def validate_no_extra_space(data: str):
    return data.strip() == data

def validate(validators = list[Callable]):
    a = 1
    b = 2
    return a + b

print(validate(validate_lowercase("Sergiusz")))

# Task: Create a Flexible String Processing Pipeline
# Objective:
# Write a function string_pipeline that:
#
# Takes a list of strings (strings) as input.
# Accepts three optional callable parameters:
# pre_process: a function that receives a string and performs some manipulation (e.g., strip whitespace, convert to lowercase).
# process: a function that analyzes or transforms the string (e.g., check if it contains a certain substring, count characters).
# post_process: a function that outputs or logs the final string or analysis result.
# Applies these functions in sequence for each string in the list.
# Details to include:
#
# Use Callable from typing for type annotations of the function parameters.
# Make default functions for each step that, for example:
# default_pre_process: trims whitespace and converts to lowercase.
# default_process: counts characters and prints the length.
# default_post_process: prints the final string or result.
# Allow the user to pass custom functions for each step to customize behavior.

def pre_process(string: str):
    return string.strip().lower()

def process(string: str):
    return len(string)

def post_process(string: str):
    print(f"Character count: {string}")




def string_pipeline(strings: list, pre_process: Callable = pre_process, process: Callable = process, post_process: Callable = post_process):
    for ch in strings:
        processed_str = pre_process(ch)
        result = process(processed_str)
        post_process(result)

strings = ["  Hello World  ", "Python is fun!", "  OpenAI GPT "]
string_pipeline(strings)

# Task: Create a Modular Number Processing Pipeline
# Objective:
# Write a function number_pipeline that:
#
# Takes a list of numbers (numbers) as input.
# Accepts three optional callable functions:
# pre_process: a function that takes a number and pre-processes it (e.g., rounds it, filters it).
# process: a function that analyzes or transforms the number (e.g., compute square, check if positive).
# post_process: a function that outputs or logs the result (e.g., print the number, log to a file).
# Implementation Details:
#
# Define default functions for each step:
#
# default_pre_process: e.g., rounds each number.
# default_process: e.g., computes the square of each number.
# default_post_process: e.g., prints the transformed number.
# Apply these functions to each number in the list in sequence.
#
# Allow the user to pass custom functions for each step by overriding the defaults.

def pre_process1(number: float):
    return round(number, 2)

def process1(number: float):
    return math.sqrt(number)

def post_process1(number: float):
    print(f"The number is: {number}")


def number_pipeline(numbers: list, pre_process: Callable = pre_process1, process: Callable = process1, post_process: Callable = post_process1):
    for n in numbers:
        rounded_n = pre_process(n)
        result = process(rounded_n)
        post_process(result)
numbers = [1.2, 3.7, 4.5, 8.9]
number_pipeline(numbers)

# Task: Create a Flexible Data Transformation Pipeline
# Objective:
# Write a function data_transformer that:
#
# Accepts a list of numerical data (integers or floats).
#
# Accepts three optional callable parameters:
#
# pre_process: a function to preprocess each data point (e.g., normalize, filter).
# transform: a function to transform each data point (e.g., square, log, convert to percentage).
# post_process: a function to handle the output (e.g., print, save to file, collect in a list).
# Applies these functions sequentially to each data point, similar to your previous example.
#
# Implementation requirements:
#
# Use type annotations (Callable) for the parameters.
# Provide default functions:
# default_pre_process: identity or normalization.
# default_transform: square the number.
# default_post_process: print the result.
# Make the pipeline flexible to accept custom functions.

def pre_process11(data: list):
    return sorted(data)

def transform11(data: list):
    return [i * 2 for i in data]

def post_process11(data: list):
    print(f"The processed list is {data}.")


def data_transformer(data: list[int],
                     pre_process: Callable = pre_process11,
                     transform: Callable = transform11,
                     post_process: Callable = post_process11):
        sorted_data = pre_process(data)
        result = transform(sorted_data)
        post_process11(result)

data = [3, 1, 4, 2]
data_transformer(data)

# Objective:
# Create a function string_pipeline that:
#
# Accepts a list of strings.
#
# Has three optional callable parameters:
#
# pre_process: a function to preprocess each String (e.g., strip whitespace, convert to lowercase).
# transform: a function to transform the String (e.g., replace characters, reverse, get length).
# post_process: a function to handle or display the final result (e.g., print, log, collect).
# Inside the pipeline, apply the functions to each string in sequence, just like your data pipeline.
#
# Implementation instructions:
# Use default functions like:
# default_pre_process: trim whitespace and make lowercase.
# default_transform: get the string length or reverse the string.
# default_post_process: print the result.
# Make sure your string_pipeline() function calls the callable parameters, not the default functions directly.

def pre_process_one(string: str):
    return string.strip()

def transform_one(string: str):
    return string.title()

def post_process_one(string: str):
    print(f"The processed string is: {string}")

def string_pipeline(strings: list[str], pre_process: Callable = pre_process_one, transform: Callable = transform_one, post_process: Callable = post_process_one):
    for i in strings:
        processed_str = pre_process(i)
        result = transform(processed_str)
        post_process(result)

sample_strings = [
    "  Hello, World!  ",
    "Python is Awesome",
    "  ChatGPT AI assistant  ",
    " OpenAI GPT-4 "
]

string_pipeline(sample_strings)

# Simple Counter Closure:
# Create a function that returns another function which, when called, increments and returns an internal counter variable.

def outer(n):
    counter = 0

    def inner():
        nonlocal counter
        counter += n
        return counter
    return inner

result = outer(2)
print(result())
print(result())

# Objective:
# Write a function make_step_counter(step) that:
#
# Takes an initial step value (e.g., 3, 5, or 10).
# Returns a function that, each time called, adds that step value to an internal counter.
# The internal counter should start at Zero when the closure is created.
# Each call to the returned function should return the new total.

def make_step_counter(step):
    counter = 0
    def inner():
        nonlocal counter
        counter += step
        return counter
    return inner

result = make_step_counter(5)
print(result())


# Task: Create a Flexible Subtracting Counter
# Objective:
# Write a function make_subtract_counter(subtract_value) that:
#
# Accepts a number subtract_value.
# Returns a function that, each time called, decreases an internal counter by that value.
# The internal counter should start at 0 when the closure is created.
# Each subsequent call should return the current total after subtraction.

def make_subtract_counter(subtract_value):
    counter = 0

    def inner():
        nonlocal counter
        counter -= subtract_value
        return counter
    return inner

result = make_subtract_counter(3)
print(result())
result()
print(result())

# Persistent Multipliers:
# Write a function that takes a number n and returns a new function that multiplies its input by n, "remembering" n through closure.

def outer(n):
    def inner(x):
        return n * x
    return inner
res = outer(2)
print(res(2))

# Objective:
# Write a function make_adder(n) that:
#
# Takes a number n.
# Returns a new function that adds its input to n.
# The inner function should remember the value of n via closure.

def make_adder(n):
    def inner(y):
        return y + n
    return inner
ress = make_adder(5)
print(ress(5))

# Objective:
# Write a function make_power(p) that:
#
# Takes an exponent p (like 2 for square, 3 for cube).
# Returns a new function that takes a number x and raises it to the power p.
# The inner function should remember the value of p via closure, so you can create multiple functions for different powers.

def make_power(p):
    def inner(x):
        return x ** p
    return inner

result = make_power(3)
print(result(4))

# Objective:
# Write a function make_discount(percentage) that:
#
# Takes a discount percentage (e.g., 10, 20, 50).
# Returns a new function that takes a price and applies that discount to it.
# The inner function should remember the discount percentage via closure.

def make_discount(percentage):
    def inner(n):
        return n * (1 - percentage / 100)
    return inner

percentage_10 = make_discount(10)
print(percentage_10(96))

# Objective:
# Write a function make_tip_calculator(tip_percentage) that:
#
# Takes a tip percentage (e.g., 10, 15, 20).
# Returns a new function that takes a bill amount and calculates the total amount including the tip.
# The inner function should “remember” the tip percentage via closure.

def make_tip_calculator(tip_percentage):
    def inner(n):
        return n + (n * (tip_percentage / 100))
    return inner

percentage_22 = make_tip_calculator(22)
print(percentage_22(900))


# Accumulator Function:
# Implement a function that creates an accumulator; each call adds a given number to an internal total, which persists across calls.

def accumulator():
    total = 0
    def inner():
        nonlocal total
        total += 1
        return total
    return inner

result = accumulator()
result()
print(result())

# Objective:
# Write a function make_limited_counter(max_value) that:
#
# Takes a maximum value max_value.
# Returns a function that:
# Increments an internal counter each time it’s called.
# Stops incrementing once it reaches max_value.
# Continues to return the max_value after reaching or exceeding it.
# The counter should start at 0 when created.

def make_limited_counter(max_value):
    count = 0
    def inner():
        nonlocal count
        if count < max_value:
            count += 1
        return count
    return inner

result = make_limited_counter(2)
print(result())
print(result())
print(result())


# List Append Closure:
# Create a closure that maintains a list, providing a function to add items to it and another to retrieve the list.

def outer():
    ls = []
    def add_item(item):
        ls.append(item)

    def get_list():
        return ls

    return add_item, get_list

add, get = outer()
add(5)
add(10)
print(get())

# Objective:
# Write a function make_observable_list() that:
#
# Maintains a private list.
# Returns three functions:
# add_item(item) — adds an item to the list.
# remove_item(item) — removes an item from the list if it exists.
# get_list() — returns the current state of the list.
# This way, you can perform multiple operations on the list, and all functions share access to the same list via closure.

def make_observable_list():
    ls = []

    def add_item(item):
        ls.append(item)

    def remove_item(item):
        ls.remove(item)

    def get_list():
        return ls

    return add_item, remove_item, get_list

add, rm, get = make_observable_list()

add(1)
add(2)
add(3)
rm(2)
print(get())

# Objective:
# Write a function make_history(max_size) that:
#
# Maintains an internal list (the history).
# Limits the history list to a maximum size (max_size).
# Returns three functions:
# add_entry(entry) — adds a new entry to the history; if the list exceeds max_size, remove the oldest entry.
# remove_entry(entry) — removes a specific entry if it exists.
# get_history() — returns the current list of entries.

def make_history(max_size):
    the_history = []

    def add_entry(entry):
        the_history.append(entry)
        if len(the_history) > max_size:
            the_history.pop(0)

    def remove_entry(entry):
        if entry in the_history:
            the_history.remove(entry)

    def get_history():
        return the_history
    return add_entry, remove_entry, get_history

add, rm, get = make_history(2)
add(2)
rm(2)
add(2)
add(3)
add(4)
add(5)
rm(4)
print(get())

# Nested Closure:
# Make a function that returns another function, which in turn returns a third function. Chain them and demonstrate how each level remembers variables.

def outer():
    variable = 2
    def inner():
        variable2 = 0
        def inner2():
            variable3 = 5
            def inner3():
                return variable, variable2, variable3
            return inner3
        return inner2
    return inner

result = outer()
inner2_func = result()
inner3_func = inner2_func()
print(inner3_func())

# Objective:
# Build a function make_chain() that:
#
# Returns a chain of three nested functions.
# Each nested function remembers a variable from its enclosing scope:
# The outermost function holds a number a.
# The middle function holds a number b.
# The innermost function holds a number c.
# When you call the innermost function, it returns the sum of a, b, and c.

def make_chain(a):

    def middle(b):

        def inner(c):
            return a + b + c
        return inner
    return middle
first = make_chain(2)
second = first(3)
print(second(7))


# Closure with Configuration:
# Make a function that accepts configuration parameters
# and returns a closure that uses those parameters to modify its behavior (e.g., thresholds, messages).

def config(threshold, message):
    def check(num):
        if num > threshold:
            return message
        else:
            return "Nothing to worry about"
    return check

res = config(5, "Alert")
print(res(6))

# Objective:
# Write a function make_discount_or_bonus(discount_percentage=0, bonus_amount=0) that:
#
# Accepts two configuration parameters:
# discount_percentage: a percentage discount to apply.
# bonus_amount: a fixed bonus amount to add.
# Returns a nested function that takes a price and:
# Applies the discount (if any).
# Adds the bonus (if any).
# Returns the final price after these modifications.
# The inner function remembers the configuration via closure.

def make_discount_or_bonus(discount_percentage = 0, bonus_amount=0):
    def inner(price):
        discounted_price = price * (1 - discount_percentage / 100)
        final_price = price - discounted_price + bonus_amount
        return final_price
    return inner

result = make_discount_or_bonus(8, 100)
print(result(300))



# Timer Closure:
# Build a closure that acts as a stopwatch: it records the start time when created and, when called, returns elapsed time.

# import time
# def timer():
#     start_time = time.time()
#     def inner():
#         current_time = time.time()
#         difference = current_time - start_time
#         return difference
#     return inner
#
# result = timer()
# time.sleep(1.1)
# print(result())

# Task: Create a Multi-Stage Stopwatch
# Objective:
# Build a closure that acts as a stopwatch with the following features:
#
# When initialized, it records the start time.
# When called the first time, it returns the elapsed time since start.
# When called the second time, it resets the start time to the current time without returning anything.
# When called again after reset, it returns the new elapsed time since the reset.

# def timer_watch():
#     start_time = time.time()
#     is_reset = False
#     def stopwatch():
#         nonlocal start_time, is_reset
#         if not is_reset:
#             return time.time() - start_time
#         else:
#             start_time = time.time()
#             is_reset = False
#             return None
#     return stopwatch
#
# result = timer_watch()
# time.sleep(2)
# print(result())
# result()
# time.sleep(.5)
# print(result())

# File Writer Closure:
# Write a function that takes a filename and returns a function which, when called, appends data to that file,
# maintaining a persistent file handle using closure.

def outer(file):
    def inner(data):
        return file + data
    return inner

result = outer("s")
print(result("e"))

# Example: Greeting Generator with Closure
# Objective:
# Create a function make_greeting(greeting) that:
#
# Takes a greeting word or phrase (like "Hello" or "Hi").
# Returns a function that takes a name and outputs a personalized greeting using the captured greeting.

def make_greeting(greeting):
    def inner(name):
        return f"{greeting}, {name}."
    return inner

result = make_greeting("Hello")
print(result("Sergiusz"))

# Objective:
# Write a function make_chatbot_response(greeting, farewell) that:
#
# Accepts two parameters:
# greeting: a greeting message (e.g., "Hi").
# farewell: a farewell message (e.g., "Goodbye").
# Returns two nested functions:
# say_hello(name): returns a personalized greeting using the captured greeting.
# say_goodbye(name): returns a personalized farewell using the captured farewell.

def make_chatbot_response(greeting, farewell):

    def say_hello(name):
        return f"{greeting}, {name}."

    def say_goodbye(name):
        return f"{farewell}, {name}."

    return say_hello, say_goodbye

hello, goodbye = make_chatbot_response("Hello", "Bye")

print(hello("Sergiusz"))
print(goodbye("Inga"))

# Objective:
# Write a function make_notifier(welcome_message, alert_message, farewell_message) that:
#
# Takes three message templates as parameters.
# Returns three functions:
# welcome(name): returns a personalized welcome message using the welcome_message template.
# alert(name): returns an alert message using the alert_message template.
# goodbye(name): returns a farewell message using the farewell_message template.

def make_notifier(welcome_message, alert_message, farewell_message):

    def welcome(name):
        return f"{welcome_message}, {name}."

    def alert(name):
        return f"{name}!!! {alert_message}."

    def goodbye(name):
        return f"{farewell_message}, {name}."

    return welcome, alert, goodbye

hi, alert, bye = make_notifier("Welcome to the kingdom", "Please evacuate", "Farewell young padawan")

print(hi("Sergiusz"))
print(alert("Martyna"))
print(bye("Irena"))


# Function Factory:
# Create a closure that generates multiple specialized functions, such as different power functions (square, cube, etc.),
# demonstrating how each remembers its exponent.

def factory(n):

    def square():
        return n ** 2

    def cube():
        return n ** 3

    def quartic():
        return n ** 4

    return square, cube, quartic

sq, c, quar = factory(2)

print(sq())
print(c())
print(quar())

def outer(n, p):
    def inner():
        return n ** p
    return inner

result = outer(2, 3)
print(result())

# Objective:
# Create a function make_multi_power(n, exponents) that:
#
# Accepts a base number n.
# Accepts a list of exponents, e.g., [2, 3, 4].
# Returns a dictionary of functions, where each key is the exponent (as a string or number),
# and its value is a function that computes n raised to that exponent.

def make_multi_power(n, exponents):
    functions = {}
    for i in exponents:
        def raising(power = i):
            return n ** power
        functions[i] = raising
    return functions

powers = make_multi_power(2, [2, 4, 6])
print(powers[2]())
print(powers[4]())
print(powers[6]())


# Closure with State Reset:
# Implement a closure that counts how many times it has been called, with an internal reset method to reset its count to zero.

def internal():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count

    def reset():
        nonlocal count
        count = 0
        return count

    inner.reset = reset
    return inner

c = internal()
print(c())
print(c())
c.reset()
print(c())

# Objective:
# Write a function make_paused_counter() that:
#
# Maintains an internal count.
# Provides two main functions:
# increment(): increases the count by 1, unless paused.
# pause(): pauses the counter (stops incrementing).
# resume(): resumes the counter.
# Attach pause() and resume() as methods to the main counter function.
# When paused, calls to increment() should not increase the count but should still return the current value.

def make_paused_counter():
    count = 0
    is_paused = False

    def increment():
        nonlocal count, is_paused
        if is_paused:
            return count
        else:
            count += 1
            return count

    def pause():
        nonlocal count, is_paused
        is_paused = True

    def resume():
        nonlocal is_paused
        is_paused = False
    return increment, pause, resume

counter, pause, resume = make_paused_counter()
print(counter())
print(counter())
pause()
print(counter())
resume()
print(counter())