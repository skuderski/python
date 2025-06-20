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