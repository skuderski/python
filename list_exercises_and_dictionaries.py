# task 1
"""Write a function that takes a list of numbers and returns the sum of all the elements in the list."""
from typing import Any


def sum_of(numbers:list) -> int:
    return sum(numbers)

print(sum_of([1,2,3]))

# task 2
"""Create a function that finds and 
 the maximum value in a list of numbers without using the built-in max() function."""

def maximum_value(numbers: list) -> int:
    maximum_number = 0
    for number in numbers:
        if number > maximum_number:
            maximum_number = number
    return maximum_number

print(maximum_value([1,5,8,10]))


# task 3

"""Remove Duplicates:
Implement a function that takes a list and returns a new list with all duplicate elements removed."""

def duplicates(fruits:list) -> list:
    return list(tuple(fruits))

print (duplicates(["banana", "banana", "mango", "mango", "vodka"]))

# task 4
"""
Reverse a List: Write a function that takes a list 
and returns a new list that is the reverse of the original list."""

def reversed_list(numbers: list) -> list:
    return numbers[::-1]

print(reversed_list([1,2,5,7,2,3]))

# task 5

"""Count Occurrences: Create a function that takes a list and an element, 
and returns the count of how many times that element appears in the list."""

def occurences(fruits: list, element: Any) -> int:
    count = 0
    for fruit in fruits:
        if fruit == element:
            count += 1
    return count

print(occurences(["banana", 1, 3, 4, 1, 3 ], "banana"))

# task 6
"""Sort a List: Write a function that takes a list of numbers and
returns a new list sorted in ascending order without using the built-in sort() or sorted() functions."""

def asc_order(numbers: list) -> list:
    the_list = []
    while numbers:
        minimum = numbers[0]
        for number in numbers:
            if number < minimum:
                minimum = number
        the_list.append(minimum)
        numbers.remove(minimum)
    return the_list

print(asc_order([1,5,6,2,3,7,1,2]))

# task 7

"""
Merge Two Lists: Implement a function that takes two lists and 
returns a new list containing all elements from both lists, without duplicates, 
and in the order they were added."""

def merging(first_list: list, second_list: list):
    seen = set()  # To track seen elements
    result = []  # List to store the result

    for item in first_list + second_list:  # Iterate through the combined lists
        if item not in seen:  # Check if the item has been seen before
            seen.add(item)  # Add to seen set
            result.append(item)  # Append to the result list
    return result
print(merging([1,2,3,4,5,6,2,3,],[5,3,2,1,7,3,5,4,9]))

#task 8
"""List Comprehension: Use list comprehension to create a new list that contains the squares 
of all even numbers from a given list of integers."""

def squared(numbers: list) -> list:
    return [number**2 for number in numbers]

print(squared([2,4,6,8]))

#task 9
"""Flatten a Nested List: Write a function that takes a nested list (a list containing other lists) 
and returns a flat list containing all the elements."""

def flatten(nested_list: list) -> list:
    flat_list = []
    for i in nested_list:
        if isinstance(i, list):
            flat_list.extend(i)
        else:
            flat_list.append(i)
    return flat_list

print(flatten([[1, 2, 3], [4, 5]]))

# task 10

"""Find Index: Create a function that takes a list and an element, 
and returns the index of the first occurrence of the element in the list. 
If the element is not found, return -1."""

def first_occurence(some_list: list, element: Any ):
    for i in some_list:
        if i == element:
            return element

    return -1
print(first_occurence([1,2,3], 5))

#task 1
"""Create a Dictionary: Create a dictionary containing information about a person,
 including their name, age, and city. Print the dictionary."""

person = {"name": "Sergiusz", "age": 30, "city": "Warszawa"}
print(person)

# task 2
"""Accessing Values: Given a dictionary, print the value associated with a specific key. 
For example, access the age from the dictionary you created in Task 1."""

print(person["age"])

# task 3

"""Adding a New Key-Value Pair: Add a new key-value pair to your existing dictionary that 
stores the person's occupation."""
person["occupation"] = "unemployed"
print(person)

# task 4
"""Updating a Value: Change the value of an existing key in the dictionary. 
For instance, update the age to a new value."""

person["occupation"] = "software engineer"
print(person)

# task 5

"""Removing a Key-Value Pair: 
Use the pop() method to remove a key-value pair from the dictionary and print the updated dictionary."""

person.pop("age")
print(person)

#task 6

"""Looping Through Keys: Write a function that takes a dictionary and prints all the keys."""

def the_keys(dictionary: dict)-> list:
    return list(dictionary.keys())

print(the_keys(person))

# task 7

"""Looping Through Values: Write a function that takes a dictionary and prints all the values."""

def the_values(dictionary: dict):
    return list(dictionary.values())

print(the_values(person))

# task 8

"""
Looping Through Key-Value Pairs: Write a function that takes a dictionary and 
prints each key along with its associated value."""

def loopdidoo(dictionary: dict)-> list:
    return list(dictionary.items())

print(loopdidoo(person))

second_person = {"name":"Jahnn", "age": 25, "city":"Johannesburg", "occupation": "swimmer"}

# task 9
"""Merging Dictionaries: Create a second dictionary 
and write a function that merges the two dictionaries together, combining their key-value pairs."""

def merging(some_dictionary: dict, some_other_dictionary: dict)-> list:
    merged_list = []
    for key, value in some_dictionary.items():
        merged_list.append(value)
    for key, value in some_other_dictionary.items():
        merged_list.append(value)
    return merged_list

print(merging(some_dictionary=person, some_other_dictionary=second_person))

# task 10

"""Counting Occurrences: Create a function that takes a list of items and returns a dictionary where the keys are the items and 
the values are the counts of how many times each item appears in the list."""

def counting(the_list: list)-> dict:
    some_dictionary = {}
    for i in the_list:
        some_dictionary[i] = some_dictionary.get(i, 0) + 1
    return some_dictionary

print(counting(["john", "sally", "john"]))