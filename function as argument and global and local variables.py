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

# Greeting Machine: Create a function that takes a name
# and another function (a greeting function) as arguments. The greeting function should generate a personalized greeting.
# Try it with different greetings like "Hello," "Good morning," and "Hey."

# def greeting(customized, name, age):
#     return customized(name, age)
#
# def customized(name, age):
#     print(f"Good morning, {name}, you are {age} years old.")
#
# greeting(customized,"Sergiusz", 30)
#
# # Number Processor: Create a function that takes a list of numbers and another function (a number operation function) as arguments.
# # The number operation function could square the number, double it, or add 5 to it.
#
# def numbers(operation, lst):
#     processed_numbers = []
#     for item in lst:
#         processed_numbers.append(operation(item))
#     return processed_numbers
#
# def func(x):
#     return x ** 2
# some_list = [1, 2, 3, 4, 5]
# doubled = numbers(func, some_list)
#
# print(doubled)
# def triple(x):
#     return x ** 3
#
# tripled = numbers(triple, some_list)
#
# print(tripled)
# some_other_list = [2, 5, 6]
# def quadruple(x):
#     return x ** 4
#
# quadrupled = numbers(quadruple, some_other_list)
# print(quadrupled)



# String Modifier: Create a function that takes a list of strings and another function (a string manipulation function) as arguments.
# The string manipulation function could convert the string to uppercase, add an exclamation point, or calculate its length.


# def string_modifier(modification, strings):
#     modified_strings = []
#     for string in strings:
#         modified_strings.append(modification(string))
#     return modified_strings
#
# def uppercase(x):
#     return x.upper()
#
# some_strings = ["sergiusz", "wiesiek", "irena"]
#
# uppercase_strings = string_modifier(uppercase, some_strings)
# print(uppercase_strings)

# Create a function called string_transformer that takes a list of strings and another function (a string operation function) as arguments.
# The string_transformer function should apply the string operation function to each string in the list
# and return a new list containing the transformed strings.


# def string_transformer(operation, the_list):
#     transformed = []
#     for item in the_list:
#         transformed.append(operation(item))
#     return transformed
#
# def add_exclamation(i):
#     return i + "!"
#
# def first_letter(i):
#     return i[0].upper() + i[1:]
#
# def add_parentheses(i):
#     return ", ".join(i)
#
# my_list = ["jestem", "milym", "chlopcem"]
#
# def move_by_one(i):
#     return i[1:] + i[0]
#
# print(string_transformer(add_exclamation, my_list))
# print(string_transformer(first_letter, my_list))
# print(string_transformer(add_parentheses, my_list))
# print(string_transformer(move_by_one, my_list))
#
#
# # Filter List: Create a function that takes a list of items (numbers, strings, etc.) and another function (a filtering function) as arguments.
# # The filtering function determines whether an item should be included in the result.
# # For example, filter out even numbers or strings longer than 5 characters.
#
#
# def filter_list(filtering, numbers):
#     filtered_list = []
#     for number in numbers:
#         if filtering(number):
#             filtered_list.append(number)
#     return filtered_list
#
# def is_even(x):
#     return x % 2 == 0
#
# numbers = [1, 2, 3, 4, 5]
#
# def is_odd(x):
#     return x % 2 != 0
#
# other_numbers = [1, 2, 7, 3, 9, 11]
#
# print(filter_list(is_even, numbers))
# print(filter_list(is_odd, other_numbers))
#
# def filtering(function, strings):
#     list_of_strings = []
#     for string in strings:
#         if function(string):
#             list_of_strings.append(string)
#     return list_of_strings
#
# def length_of_strings(x):
#     return len(x) > 5
#
# the_strings = ["sergiusz", "irena", "wiesiek"]
#
# print(filtering(length_of_strings, the_strings))
#
# # Apply Discount: Create a function that takes a list of prices and another function (a discount function) as arguments.
# # The discount function calculates the discount based on the price. Try different discount strategies (e.g., percentage-based, fixed amount).
#
# def apply_discount(discount, prices):
#     discounted_prices = []
#     for price in prices:
#         discount_amount = discount(price)
#         discounted_price = price - discount_amount
#         discounted_prices.append(discounted_price)
#     return discounted_prices
#
# def discount(price, percentage):
#     return price * (percentage / 100)
#
# original_prices = [100, 200, 350, 170]
#
# print(apply_discount(lambda price: discount(price, 20), original_prices))
#
#
# # Process User Input: Create a function that takes user input and another function (a validation function) as arguments.
# # The validation function checks if the input is valid (e.g., a number within a range, a valid email address).
#
# def process_user_input(input_prompt, validation_function):
#
#     user_input = input(input_prompt)
#
#     if validation_function(user_input):
#         return user_input
#
#     else:
#         return None
#
# def is_valid_input(input_string):
#     lowercased_string = input_string.lower()
#
#     return bool(lowercased_string)
#
# input_prompt = "Please enter something "
# result = process_user_input(input_prompt, is_valid_input)
#
# if result:
#     print(f"You entered {result}")
# else:
#     print("No valid input.")

# Calculate Grade: Create a function that takes a score and another function (a grading function) as arguments.
# The grading function determines the letter grade based on the score. Try different grading scales.


# def calculate_grade(calculation, scores):
#     grades = []
#     for score in scores:
#         grade = calculation(score)
#         grades.append(grade)
#     return grades
#
# def score(x):
#     if x > 80:
#         return "A"
#     elif 60 < x <= 80:
#         return "B"
#     else:
#         return "C"
#
# the_scores = [100, 50, 65, 70, 90]
#
# print(calculate_grade(score, the_scores))

# String Repeater:
#
# Create a function called string_repeater that takes two arguments: func and string.
# func should be a function that takes a string as input and an integer as input and returns the string repeated that many times.
# The string_repeater function should call the func function with the string and the number 3 as arguments and return the result.
# Create a function called repeat_string that takes a string s and an integer n and returns the string s repeated n times.
# Call string_repeater with the repeat_string function and a string (e.g., "hello") and print the result. The output should be "hellohellohello".

# def string_repeater(func, string):
#     return func(string, 3)
#
# def repeat_string(s, n):
#     return s * n
#
# result = string_repeater(repeat_string, "hello")
# print(result)


# Greeting with Title:
#
# Create a function called greet_with_title that takes two arguments: func and name.
# func should be a function that takes a title and a name and returns a greeting string.
# The greet_with_title function should call the func function with the title "Dr." and the name as arguments and return the result.
# Create a function called titled_greeting that takes a title and a name and returns the string "Hello, [title] [name]!".
# Call greet_with_title with the titled_greeting function and a name (e.g., "Alice") and print the result. The output should be "Hello, Dr. Alice!".

# def greet_with_title(func, name):
#     return func("Dr.", name)
#
# def titled_greeting(title, name):
#     return f"Hello, {title} {name}"
#
# print(greet_with_title(titled_greeting, "Alice"))


#
# Execute with Timing: Create a function that takes another function (the function to execute) as an argument.
# Before executing the function, record the start time. After executing the function, record the end time.
# Print the time it took to execute the function.

# Apply Math Operation with Constant:
#
# Create a function called apply_math_operation that takes two arguments: func and number.
# func should be a function that takes a number and a constant as input and returns the result of a mathematical operation.
# The apply_math_operation function should call the func function with the number and the constant 5 as arguments and return the result.
# Create a function called add_constant that takes a number x and a constant c and returns the sum of x and c.
# Call apply_math_operation with the add_constant function and a number (e.g., 10) and print the result. The output should be 15.

# def apply_math_operation(func, number):
#     return func(number, 5)
#
# def add_constant(x, c):
#     return x + c
#
# print(apply_math_operation(add_constant, 10))


# Apply String Operation with Constant
#
# Create a function called apply_string_operation that takes two arguments: func and string_value.
# func should be a function that takes a string and a constant string, and returns a modified string.
# The apply_string_operation function should call func with string_value and the constant " World" as arguments and return the result.
# Create a function called append_string that takes a string s and a constant string c and returns the concatenation of s and c.
# Call apply_string_operation with append_string and your own string (e.g., "Hello") and print the result.

# def apply_string_operation(func, string_value):
#     return func(string_value, " World")
#
# def append_string(s, c):
#     return s + c
#
# print(apply_string_operation(append_string, "Hello"))


# Apply List Transformation with Constant
#
# Create a function called apply_list_transform that takes two arguments: func and list_input.
# func should be a function that takes a list and a constant integer, and returns a new list.
# The apply_list_transform should call func with list_input and the number 3.
# Create a function called double_elements_plus_constant that takes a list lst and an integer c and returns a list where each element is doubled plus c.
# Call apply_list_transform with double_elements_plus_constant and a list of integers (e.g., [1, 2, 3]) and print the result.
# (Expected output: [3, 5, 7])

# def apply_list_transform(func, list_input):
#     return func(list_input, 2)
#
# def double_elements_plus_constant(lst, c):
#     some_list = []
#     for i in lst:
#         some_list.append(i * 2 + c)
#     return some_list
#
# result = apply_list_transform(double_elements_plus_constant, [1, 2, 3])
# print(result)


# Task 3: Apply Boolean Logic with Constant
#
# Create a function called apply_boolean_logic that takes two arguments: func and a boolean value.
# func should be a function that takes a boolean and a constant boolean, returning a boolean result.
# The apply_boolean_logic function should call func with the input boolean and the constant True.
# Create a function called logical_and_with_true that takes two booleans and returns their logical AND.
# Call apply_boolean_logic with logical_and_with_true and False and print the result.
# (Expected output: False)

# def apply_boolean_logic(func, boolean):
#     return func(boolean, True)
#
#
#
# def logical_and_with_true(one, two):
#     return one and two
#
# result = apply_boolean_logic(logical_and_with_true, True)
# print(result)

# Create a function apply_numeric_operation that accepts two arguments: a function and a number.
# The function should call the passed-in function with the number and a fixed value, then return the result.
#
# Define a function add_fixed_value that takes a number and adds 10 to it.
# Use apply_numeric_operation to apply add_fixed_value to your own number and print the output.

# def apply_numeric_operation(func, num):
#     return func(num, 10, 15)
#
# def add_fixed_value(n, c, b):
#     return n + c + b
#
# output = apply_numeric_operation(add_fixed_value, 5)
# print(output)


# Create a function apply_combined_operation that accepts two arguments: a function and a starting value.
# The function should call the passed-in function with the starting value and two fixed numbers, then return the result.
#
# Define a function compute_sum that takes three numbers and returns their sum.
#
# Use apply_combined_operation to apply compute_sum to your own number and two fixed numbers, then print the output.

# def apply_combined_operation(func, starting_value):
#     return func(starting_value, 1, 2)
#
# def compute_sum(a, b, c):
#     return a + b + c
#
# output = (apply_combined_operation(compute_sum, 5))
# print(output)


# Create a function apply_power_operation that takes two arguments: a function and a base number.
# The function should call the passed-in function with the base number and two fixed exponents, then return the result.
#
# Define a function calculate_power_sum that takes three numbers and returns the sum of the first number raised to the second power
# and the third number raised to the fourth power.
#
# Use apply_power_operation with calculate_power_sum and a base number of your choice, then print the result.


# def apply_power_operation(func, base_number, third_number):
#     return func(base_number, 4, third_number)
#
# def calculate_power_sum(a, b, c):
#     return (a ** 2) + (c ** 4)
#
# the_result = apply_power_operation(calculate_power_sum, 10, 5)
#
# print(the_result)

# Define a function that takes three arguments: a function and two numbers. Inside this function, call the passed-in function with the first number,
# a fixed value, and the second number. Then, create a separate function to perform some operation on these arguments.
# Use the first function to apply your operation with specific inputs and display the result.


# def some_fun_function(func, two, three):
#     return func(20, three)
#
# def doing_stuff(a, b):
#     return (a ** 10) + (b ** 3)
#
# output = some_fun_function(doing_stuff, 2, 3)
# print(output)



# Create a function that takes four arguments: a function, two initial numbers, and a fixed exponent.
# Inside the function, call the passed-in function with the first number, the second number, and the fixed exponent.
# Define the inner function to perform an operation combining these inputs, such as raising one number to the power of the fixed exponent
# and multiplying by the other.
# Use your outer function with specific values and display the result.

# def my_cool_function(func, two, three, four):
#     return func(two, three, four)
#
# def calculating(a, b, c):
#     first = a ** c
#     second = a * b
#     return first, second
#
# def multiply_and_add(a, b, c):
#     return (a * b) + c
#
# result = my_cool_function(calculating, 2, 4, 3)
# print(result)
# result2 = my_cool_function(multiply_and_add, 2, 5, 7)
# print(result2)


# Design a function that accepts at least three arguments: a function and two numbers.
# The function should invoke the passed-in function with the two numbers and a fixed operation or value.
# Create helper functions to perform different calculations on these inputs. Demonstrate switching between these helper functions with specific inputs.

# def my_cute_function(func, one, two):
#     return func(one, two, 13)
#
# def helper(a, b, c):
#     return (a - c) ** b
#
# def another_helper(a, b, c):
#     return (a * b) ** c
#
# result = my_cute_function(helper, 20, 10)
#
# print(result)
#
# result2 = my_cute_function(another_helper, 2, 3)
# print(result2)

# Create a function that accepts three arguments: a transformation function, a list of items, and a fixed multiplier.
# The function should apply the transformation to each item in the list, passing the item and the fixed multiplier to it.
# Write at least two different transformation functions that perform different calculations using the item and the multiplier.
# Use your main function to process a specific list with each helper function and display the results.


# def my_function(func, lst, multiplier):
#     the_list = []
#     for item in lst:
#         result = func(item, multiplier)
#         the_list.append(result)
#     return the_list
#
# def transformation(a, b):
#     return a * b
#
# some_list = [2, 3, 4, 5, 6, 7]
#
# print(my_function(transformation, some_list, 5))


"""GLOBAL and LOCAL variables"""

# def printer():
#     global s
#     s += " How are you?"
#     print(s)
#
# s = "Hello, mate."
# printer()
# print(s)

# def print_msg(msg):
#
#     def printer():
#         print(msg)
#
#     printer()
#
# print_msg("Hello")
#
# def print_msg(msg):
#
#     def printer():
#         print(msg)
#
#     return printer
#
# another = print_msg("Hello")
#
# another()

def make_multiplier_of(n):

    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier_of(3)
print(times3(3))

times5 = make_multiplier_of(5)
print(times5(5))

print(times5(times3(3)))
print(times5(times3(3)))


from typing import Callable


def produce(device_name: str) -> Callable:
    count = 0

    def device():
        nonlocal count
        count += 1
        print(f"{device_name} launch {count}")
    return device

cell_phone = produce("Cell Phone")

cell_phone()
cell_phone()
cell_phone()
cell_phone()
cell_phone()