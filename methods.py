# task 1

"""String Length: Write a function that takes a string and returns its length using the len() method."""

def length(word: str) -> int:
    return len(word)

print(length("Sergiusz Kuderski"))



# task 2
"""Uppercase Conversion: Implement a function that takes a string and 
returns it in uppercase using the upper() method."""

def uppercase(word: str) -> str:
    return word.upper()

print(uppercase("Sergiusz"))


# task 3
"""Check Substring: Create a function that checks if a specific substring exists in a string using the 
in keyword and returns a boolean."""

def checking(word: str, sub: str) -> bool:
    return sub in word.lower()

print(checking("Sergiusz", "ser"))


# task 4
"""Count Vowels: Write a function that counts the number of vowels 
in a string using the count() method for each vowel."""


def count_vowels(word: str) -> int:
    vowels = 0
    for letter in word:
        if letter in "aeiou":
            vowels += 1
    return vowels


print(count_vowels("Sergiusz"))

# task 5
"""
Join List of Strings: Create a function that takes a list of strings and 
combines them into a single string using the join() method."""

def joining(list_of_strings: list) -> str:
    return " ".join(list_of_strings)

print(joining(["Sergiusz", "kocha", "zycie", "i", "lubi", "picie."]))



#task 6
"""

Sort List: Write a function that takes a list of numbers (or strings) and 
returns a new list sorted in ascending order using the sorted() function."""


def sort_list(strings: list) -> list:
    return sorted(strings, key = len, reverse = True)

print(sort_list(["Sergiusz", "wodka", "labedz", "mocno", "wycieraczka"]))

# task 7
"""Find Minimum and Maximum: Implement a function that takes a list of numbers and 
returns the minimum and maximum values using the min() and max() methods."""

def minmaxx(numbers: list) -> int:
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum
print(minmaxx([1, 2, 3, 6, 9, 4]))



# task 8
"""Remove Whitespace: Create a function that removes leading and trailing whitespace 

from a string using the strip() method."""

def rm_whities(word: str) -> str:
    clean = word.strip()
    clean = clean.replace(" ", "")
    return clean


print(rm_whities(" Sergiuszek Kuderski "))


#task 9
"""Replace Substring: Write a function that replaces all occurrences of a specified substring 
within a string using the replace() method."""

def replacing_the_bad_guy(word: str, sub: str) -> str:
    modified = word.lower().replace(sub.lower(), "hehe")
    return modified

print(replacing_the_bad_guy("Sergiusz", "ser"))


# task 10
"""Reverse String: Create a function that reverses a string using slicing and returns the result."""

def reversing(word: str) -> str:
    return word[::-1]

print(reversing("Sergiusz"))

