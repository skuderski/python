# task 1

"""Reverse a String: Write a function that takes a string and returns it reversed using slicing."""

def reverse_it(word: str) -> str:
    return word[::-1]

print(reverse_it("Sergiusz"))

# task 2
"""Extract Substring: Create a function that 
returns a substring from a string based on given start and end indices."""

def extraction(word: str) -> str:
    return word[0:3]

print(extraction("Sergiusz"))

# task 3

"""Get Even Index Characters: Write a function that 
returns a string containing characters from even indices of the input string."""

def even_index(word: str) -> str:
    return word[::2]

print (even_index("Sergiusz"))

# task 4

"""Get Last N Characters: Implement a function that takes a string and an integer N, and 
returns the last N characters from the string."""

def lastn(word: str, n: int) -> str:
    return word[-n:]

print(lastn("Sergiusz", 3))

# task 5

"""Remove First and Last N Characters: Write a function that removes the first N and last N characters 
from a string based on an input integer N."""

def first_last(word: str, n: int) -> str:
    if n >= len(word) // 2:
        return ""
    else:
        return word[n:-n]

print(first_last("Sergiusz", 3))

# task 6

"""Duplicate and Reverse: Create a function that takes a string, duplicates it, and 
reverses the duplicated string."""

def dup_rever(word: str) -> str:
    duplication = word + word
    return duplication[::-1]

print(dup_rever("Sergiusz"))

# task 7

"""Extract Every Second Character: Write a function that 
returns every second character of a string using slicing."""

def every_second(word: str) -> str:
    return word[::2]

print(every_second("Sergiusz"))

# task 8

"""Check Palindrome Using Slicing: 
Implement a function that checks if a given string is a palindrome using slicing."""

def palindrome(word: str) -> bool:
    return word.lower() == word[::-1].lower()

print(palindrome("ANNA"))

# task 9

"""Get Middle Character(s): Write a function that returns the middle character of a string. 
If the string has an even length, return the two middle characters."""

def middle_char(word: str) -> str:
    if len(word) % 2 == 0:
        mid = len(word) // 2
        return word[mid - 1: mid + 1]
    elif len(word) % 2 == 1:
        mid = len(word) // 2
        return word[mid]
print(middle_char("Kaja"))

# task 10

"""Rotate a List: Create a function that rotates a list to the left 
by a specified number of positions using slicing."""

def rotating(some_list: list, n: int) -> list:
    rotato = some_list[n:] + some_list[:n]
    return rotato

print(rotating(["Sergiusz", "Martyna", "Wiesiek", "Zolw"], 3))
