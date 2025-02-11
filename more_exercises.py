# task 1

"""Sum of Even Numbers: Write a function that takes a list of integers and
returns the sum of all even numbers."""

def sum_of_even(integers: list) -> int:
    count = 0
    for i in integers:
        if i % 2 == 0:
            count += i
    return count


print(sum_of_even([1,2,3,4,5]))

# task 2

"""Find Unique Elements: Create a function that returns a new list 
containing only unique elements from the provided list."""

def unique(some_list: list) -> list:
    return list(set(some_list))

print(unique([1, 1, 3, 4, 5, 6, 3]))

# task 3

"""Flatten a List: Write a function that takes a nested list (a list containing other lists) 
and flattens it into a single list containing all the elements."""

def flatten(nested_list: list) -> list:
    flattened_list = []
    for i in nested_list:
        if isinstance(i, list):
            flattened_list.extend(i)
        else:
            flattened_list.append(i)
    return flattened_list

print(flatten([1, 2, 3, 4, [5, 6, 7,], [2, 3, 4]]))

# task 4

"""Rotate a List: Implement a function that rotates a list to the right
 by a specified number of positions."""

def rotacjone(some_motherfucking_list: list, n: int) -> list:
    rotation = some_motherfucking_list[n:] + some_motherfucking_list[:n]
    return rotation

print(rotacjone([1, 2, 3, 4, 5], n = 3))

# task 5

"""Remove Specific Item(s): Write a function that takes a list and an item, 
and removes all occurrences of that item from the list."""

def removing(some_fun_list: list, an_item) -> list:
    some_fun_list.remove(an_item)
    return some_fun_list

print(removing([1, 3, 4, 11, 2, 34, 22], 3))

# task 6

"""Sorted List: Create a function that takes a list of numbers and returns a new list 
with the numbers sorted in descending order 
without using the built-in sort() or sorted() functions."""

def sorted_list(some_fun_list: list) -> list:
    the_list = []
    while some_fun_list:
        maximum = some_fun_list[0]

        for i in some_fun_list:
            if i > maximum:
                maximum = i
        the_list.append(maximum)

        some_fun_list.remove(maximum)

    return the_list

print(sorted_list([1, 5, 2, 3, 9, 4, 7, 2, 1]))

# task 7

"""List Intersection: Write a function that takes two lists and 
returns a new list containing the common elements between them."""

def intersection(first_list: list, second_list: list) -> list:
    first_set = set(first_list)
    second_set = set(second_list)
    return list(first_set.intersection(second_set))

print(intersection([1, 2, 3, 4, 5, 3, 2, 1], [3, 2, 9, 2, 1, 4, 6]))

# task 8

"""Count Character Frequencies: Create a function that counts 
how many times each character appears in a string and 
returns a list of tuples with characters and their counts."""

def char_freq(word: str) -> list:
    count = {}
    for letter in word.lower():
        count[letter] = count.get(letter, 0) + 1
    return list(count.items())
print(char_freq("Sergiuszek"))


# task 9

"""Find Minimum and Maximum: Write a function that finds both the minimum and maximum values in a list and 
returns them as a tuple."""

def minmaxxing(some_list: list) -> tuple:
    maximum = max(some_list)
    minimum = min(some_list)
    return (minimum, maximum)

print(minmaxxing([1, 2, 4, 5, 7, 9, 2, 33]))

# task 10

"""Create a List of Square Numbers: Implement a function that 
takes an integer n and returns a list of the first n square numbers (1, 4, 9, 16, ...)."""

def square_numbers(n: int) -> list:
    the_list = []
    for i in range(1, n + 1):
        the_list.append(i**2)
    return the_list

print(square_numbers(5))
