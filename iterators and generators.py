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