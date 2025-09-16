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

# Create a lambda function that takes two numbers and returns their sum. Call it with 5 and 3.

adding = lambda a, b: a + b
print(adding(5, 3))

# Create a lambda function that takes a list of numbers and returns a new list containing only the numbers greater than a given threshold.
# Set the threshold to 10. Test the lambda with a list of numbers from 5 to 15.

numbers = list(range(1, 16))
greater_than_10 = lambda numbers: list(filter(lambda a: a > 10, numbers))
result = greater_than_10(numbers)
print(result)
# Write a lambda function that calculates the square of a number. Test it with the number 9.

squares = lambda a: a ** 2
print(squares(9))

# Use a lambda to check if a number is even. Test it with the number 8 and 7.

even_nums = lambda a: a % 2 == 0
print(even_nums(8))
print(even_nums(7))

# Create a list of numbers from 1 to 10, then use map() with a lambda to create a new list containing their squares.

nums = list(range(1, 11))
nums_1 = list(map(lambda x: x ** 2, nums))
print(nums_1)

# Use filter() with a lambda to filter out odd numbers from the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd = lambda the_list: list(filter(lambda x: x % 2 != 0, the_list))
res = odd(the_list)
print(res)


# Write a lambda function that concatenates two strings and use it to concatenate "Hello" and "World".

concatenate = lambda a, b: a + " " + b
print(concatenate("Hello", "World"))


# Create a list of words, then use sorted() with a lambda to sort the list by word length.

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

sorting = lambda x: sorted(x, key=len)
resulz = sorting(words)
print(resulz)
from functools import reduce

# Use reduce() from functools with a lambda to compute the product of all numbers in the list [1, 2, 3, 4, 5].

nums11 = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, (1, 2, 3, 4, 5))
print(product)

# Create a lambda that takes a list of tuples (name, age) and returns the list sorted by age. Test it with a few sample tuples.

people = [
    ("Alice", 30),
    ("Bob", 25),
    ("Charlie", 35),
    ("Diana", 28)
]

age_sorting = lambda lst: sorted(lst, key= lambda person: person[1])
print(age_sorting(people))

# Write a lambda function that swaps the elements of a list of two items, e.g. [1, 2], and test it.

swapped = lambda x: [x[1], x[0]]
print(swapped([1, 2]))