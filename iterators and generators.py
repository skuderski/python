from __future__ import annotations
from typing import Iterator

# #iterators
# #lists are iterable
# students = ["Alex", "John", "Anne", "Michael"]
#
# iterator = iter(students)
#
# print(next(iterator))
#
# print(next(iterator))
#
# print(iterator.__next__())
#
# print(next(iterator))



class NumberIterator:
    def __init__(self, numbers: list) -> None:
        self.numbers = numbers
        self.it = 0
    def __iter__(self) -> NumberIterator:
        self.it = 0
        return self

    def __next__(self) -> int:
        if self.it >= len(self.numbers):
            raise StopIteration
        result = self.numbers[self.it]
        self.it += 1
        return result


def fetch_numbers(iterator: Iterator, number: int) -> list:
    the_list = []
    for n in range(number):
        the_list.append(next(iterator))
    return the_list

num = NumberIterator([2, 5, 8, 13, 1, 6, 7, 8])
print(fetch_numbers(num, 5))

# Basic List Iteration:
# Create a list of numbers (e.g., [1, 2, 3, 4, 5]) and use an iterator to print each number one by one.

numbers = [1, 2, 3, 4, 5]

iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# Sum of Elements:
# Use an iterator to iterate through a list of integers and calculate their total sum.


integers = [1, 2, 3, 4, 5, 6, 7]

iterat = iter(integers)

total_sum = 0

try:
    while True:
        number = next(iterat)
        total_sum += number
except StopIteration:
    pass

print("Total sum:", total_sum)


# Iterate Over a String:
# Take a string (e.g., "hello") and use an iterator to print each character on a separate line.

hello = "hello"

iterator = iter(hello)

try:
    while True:
        letter = next(iterator)
        print(letter)
except StopIteration:
    pass

# Custom Iterable Class:
# Create a simple class that implements the __iter__() and __next__() methods to generate a sequence of numbers (like 0 to 4).

class IterableClass:
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 5:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration
numery = IterableClass()
for number in numery:
    print(number)


# For Loop vs Iterator:
# Compare using a for loop to iterate over a list with manually creating an iterator using iter() and iterating with next() until StopIteration.

some_cool_numbers = [2, 5, 10, 11, 15]
for n in some_cool_numbers:
    print(n)

iterator = iter(some_cool_numbers)
try:
    while True:
        print(next(iterator))
except StopIteration:
    pass

# Print elements in reverse:
# Create a list of words and use an iterator to print them in reverse order (you might want to reverse the list first, then iterate).

the_words = ["Sergiusz", "Wiesiek", "Anna"]

reversed_words = the_words[::-1]

iterator = iter(reversed_words)

try:
    while True:
        print(next(iterator))
except StopIteration:
    pass


# Filter even numbers:
# Use an iterator to go through a list of numbers and print only the even ones.

list_of_nums = [1, 2, 3, 4, 6, 10, 5]
iterator = iter(list_of_nums)
try:
    while True:
        num = next(iterator)
        if num % 2 == 0:
            print(num)
except StopIteration:
    pass


# Count occurrences of a specific element:
# Given a list and a target element, use an iterator to count how many times the element appears.

elements = [1, 2, 1, 3, 5, 8, 1]
element = 1
iterator = iter(elements)
the_count = 0
try:
    while True:
        current = next(iterator)
        if current == element:
            the_count += 1
except StopIteration:
    pass

print(f"Number of occurrences of {element}: {the_count}")

# Convert a string to uppercase:
# Use an iterator to go through each character of a string and build a new string with all characters in uppercase.

some_string = "sergiusz"

iterator = iter(some_string)
uppercase_iterator = ""
try:
    while True:
        letter = next(iterator)
        uppercase_iterator += letter.upper()
except StopIteration:
    pass


# Create an iterable class for Fibonacci sequence:
# Build a simple class that generates Fibonacci numbers up to a limit, using __iter__() and __next__().

class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.limit:
            raise StopIteration

        next_value = self.a
        self.a, self.b = self.b, self.a + self.b
        return next_value
fib_sequence = Fibonacci(20)
for num in fib_sequence:
    print(num)

# Task: Convert a list of words to lowercase
#
# Create a list of words.
# Use an iterator to go through each word in the list.
# Build a new list containing all words converted to lowercase.


words = ["SErgiusz", "Wiesiek", "IRENA"]
words_lower = []
iterator = iter(words)

try:
    while True:
        word = next(iterator)
        words_lower.append(word.lower())
except StopIteration:
    pass

print(words_lower)