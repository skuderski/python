# Task: Check if All Players Have At Least One Win
# You have a list called game_results, which contains sublists for each player.
# Each sublist contains boolean values indicating whether the player won (True) or not (False) in each game.
# Write a function to determine if every player has at least one win.
import math


def all_players(game_results: list) -> bool:
    return all([any(player) for player in game_results])

print(all_players([[True, False, False],
                   [True, False],
                   [False]]))

# 1. Create a List of Squares
# Generate a list of squares for numbers 0 to 10.

squares = [i*i for i in range(11)]
print(squares)

# 2. Filter Even Numbers
# From a list of numbers, create a new list containing only even numbers.

nums = [1, 5, 9, 24, 41, 278, 2, 19, 18]
even_nums = [i for i in nums if i % 2 == 0]
print(even_nums)


# 3. Create a List of Lengths
# Given a list of words, create a list with the length of each word.

list_of_words = ["Sergiusz", "Kuderski", "wiek", "trzydziesci jeden", "lato", "plaza"]
length_of_words = [f"{i} - {len(i)}" for i in list_of_words]
print(length_of_words)


# 4. Convert Temperatures
# Convert a list of Celsius temperatures to Fahrenheit using the formula.

celcius_temps = [1, 5, 10, 20, 30, 40]
fahrenheit_temps = [(i * (9/5)) + 32 for i in celcius_temps]
print(fahrenheit_temps)


# 5. Flatten a List of Lists
# Given a list of lists, flatten it into one list.

list_of_lists = [[1, 2], [3, 4], [5, 6]]
flattened = [n for sublist in list_of_lists for n in sublist]
print(flattened)
# 6. Create a List of Tuples (Number, Square)
# List numbers 1-10 along with their squares as tuples.

list_of_tuples =[(n, n ** 2) for n in range(1, 11)]
print(list_of_tuples)


# 7. Capitalize Words
# From a list of lowercase words, create a list with words capitalized.

lowercase_words = ["sergiusz", "kuderski", "wiek"]
capitalized = [word.title() for word in lowercase_words]
print(capitalized)

# 8. Find Positive Numbers
# From a list of integers, create a list containing only positive numbers.

integers = [1, 2, 3, 4, 5, -10, -22, 0]
positive_ints = [n for n in integers if n > 0]
print(positive_ints)


# 9. Create a List of Characters
# From a string, such as "Hello", create a list of its characters.

text = "Hallo moto"
characters = [c for c in text]
print(characters)


# 10. Generate a List of Prime Numbers (simple)
# Using a basic method, generate a list of prime numbers up to 50.
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = 50
primes = [i for i in range(2, n + 1) if is_prime(i)]
print(primes)

# 1. Create a List of Odd Numbers
# Generate a list of all odd numbers from 1 to 50.

odd_numbers = [n for n in range(1, 51) if n % 2 != 0]
print(odd_numbers)
# 2. Create a List of Square Roots
# Given a list of numbers, generate a list of
# their square roots (rounded to 2 decimal places).

nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
square_roots = [math.sqrt(n) for n in nums1]
print(square_roots)


# 3. Generate a List of Cubes
# List cubes of numbers from 0 to 15.

cubes = [n ** 3 for n in range(16)]
print(cubes)

# 4. Filter Words Starting with a Vowel
# From a list of words, filter and create a new list containing only words starting
# with a vowel (a, e, i, o, u).

words1 = ["apple", "banana", "cherry", "date", "elderberry"]
voweld = [word for word in words1 if word[0].lower() in "aeiou"]
print(voweld)



# 5. Create a List of Multiples of 5
# List all multiples of 5 between 0 and 100.

multiplies = [i for i in range(101) if i % 5 == 0]
print(multiplies)
# 6. Extract the First Letter of Each Word
# Given a list of words, create a list of their first letters.

first_letters = [l[0] for l in words1]
print(first_letters)


# 7. Create a List of Absolute Values
# Given a list with both positive and negative numbers, create a list of their absolute values.

numms = [1, 2, 3, 5, -1, -10, 20, 69, 0, 22, -14]
absolute_nums = [abs(n) for n in numms]
print(absolute_nums)


# 8. Multiply Each Element by 10
# Given a list of numbers, create a new list where each number is multiplied by 10.

ten_multi = [(n * 10) for n in numms]
print(ten_multi)


# 9. Create a List Based on Conditions
# List numbers from 1 to 100 that are divisible by both 3 and 5.

multi_3_5 = [n for n in range(1, 101) if n % 3 == 0 and n % 5 == 0]
print(multi_3_5)

# 10. Create a List of Boolean Values
# From a list of numbers, produce a list of booleans indicating
# whether each number is even (True) or odd (False).

boolean_question_mark = [n % 2 == 0 for n in numms]
print(boolean_question_mark)

# Task: Find the Indexes of Expired Items
# You have a list called items, where each item is a dictionary containing
# "expiry_date" as an integer (e.g., year of expiry).
# Write a function that takes this list and a current year.
# Use list comprehension with enumerate() to return a list of indices of items
# that have already expired
# (i.e., expiry_date less than the current year).

def expiration(items: list, current_year = 2025) -> list:
    return [index for index, item in enumerate(items) if item["expiry_date"] < current_year]

print(expiration(items = [
    {"name": "milk", "expiry_date": 2023},
    {"name": "bread", "expiry_date": 2025},
    {"name": "eggs", "expiry_date": 2022},
    {"name": "cheese", "expiry_date": 2024},
    {"name": "butter", "expiry_date": 2025}
]
))

# Task: Find the Indexes of Items Expiring Before a Given Year
# Given a list of items, where each item is a dictionary with "name" and "expiry_year".
# Write a function that takes this list and a target year.
# Use enumerate() to return a list of indices of items that expire before the target year.

def expiring_before(items: list, target_year = 2020) -> list:
    return [index for index, item in enumerate(items) if item["expiry_year"] < target_year]

print(expiring_before(items= [
    {"name": "milk", "expiry_year": 2019},
    {"name": "bread", "expiry_year": 2025},
    {"name": "eggs", "expiry_year": 2018},
    {"name": "cheese", "expiry_year": 2024},
    {"name": "butter", "expiry_year": 2010}
]))

def even_odd(numbers: list) -> list:
    return ["even" if i % 2 == 0 else "odd" for i in numbers]

print(even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Task: Filter Stores with Minimum Sales
# You have a list of stores, where each store is a dictionary
# with "name" and "sales" (an integer).
# Write a function that, given this list
# and a minimum sales threshold, returns a list of sub-lists:
# Each sublist contains all stores from the original list whose sales meet
# or exceed the threshold.

def filter_stores(stores_list: list, minimum_sales = 200) -> list:
    return [
        [store for store in stores if store["sales"] >= minimum_sales

        ]
        for stores in stores_list
    ]
print(filter_stores(stores_list = [
    [{"name": "Store A", "sales": 150}, {"name": "Store B", "sales": 250}],
    [{"name": "Store C", "sales": 300}, {"name": "Store D", "sales": 180}]
]))

# Create a List of All Multiples of 7 from 0 to 100

multiples_of_7 = [i for i in range(101) if i % 7 == 0]
print(multiples_of_7)

# Create a list of all multiples of 7 or 11 from 0 to 200.

multiples_of_7_or_11 = [i for i in range(201) if i % 7 == 0 or i % 11 == 0]
print(multiples_of_7_or_11)

# Create a list of all numbers from 0 to 300 that are multiples of 3 or 5
# but exclude those that are multiples of 15.

m = [i for i in range(301) if (i % 3 == 0 or i % 5 == 0) and i % 15 != 0]
print(m)

# Create a list of numbers from 1 to 500 that are multiples of 2 or 3 but not multiples of 6,
# and also categorize them based on whether they are divisible by 2 or 3.

mn = {
    "divisible_by_2" : [i for i in range(1, 501) if i % 2 == 0  and i % 6 != 0],
    "divisible_by_3" : [i for i in range(1, 501) if i % 3 == 0 and i % 6 != 0]
}
print(mn)

# Generate a List of Boolean Values indicating whether numbers 1-50
# are even or odd (e.g., True for even, False for odd).

bolean_values = [True if i % 2 == 0 else False for i in range(1, 51)]
print(bolean_values)

# Create a list of integers from 1 to 100, and for each number,
# include a boolean value indicating whether it is a perfect square or not.

import math

perfect_square_list = [
    (i, True if int(math.sqrt(i)) ** 2 == i else False) for i in range(1, 101)
]

print(perfect_square_list)

# Create a list of numbers from 1 to 150, and for each number,
# include a string indicating whether the number is "small"
# if it's less than 50, "medium" if it's between 50 and 100,
# or "large" if it's greater than 100.

size = ["small" if i < 50 else
        "medium" if  50 <= i <= 100 else
        "large" for i in range(1, 150) ]
print(size)

# Create a List of Cubes of Odd Numbers from 1 to 20

cub = [i ** 3 for i in range(1, 21)]
print(cub)

# Filter Words Starting with 'a' or 'A' from a list of words.

words = ["apple", "Ant", "banana", "Apex", "art", "Alpha", "orange", "animal", "Sergiusz"]

filtered_words = [i for i in words if i[0] == "a" or i[0] == "A"]
print(filtered_words)

# Filter words from a list that start with either 'a' or 'A',
# but only include words whose length is greater than 3 characters.

filtr = [i for i in words if (i[0] == "a" or i[0] == "A") and len(i) > 3]
print(filtr)

# Filter words that start with 'a' or 'A' and contain the letter 'e' anywhere in the word.

fil = [i for i in words if (i[0] == "a" or i[0] == "A") and "e" in i]
print(fil)

# Create a list of words from the given list that start with 'a' or 'A',
# contain the letter 'e', and have a length between 4 and 7 characters inclusive.

filee_mou = [i for i in words if (i[0] == "a" or i[0] == "A") and "e" in i and 4 <= len(i) <= 7]
print(filee_mou)

# Create a List of the First Letters of words in a sentence.

first_l = [i[0] for i in words]
print(first_l)
# Create a list of the first letters of each word in a sentence, but only include the first letter
# if the word contains more than 3 characters and starts with a vowel (a, e, i, o, u).
sentence = "An elephant is often observed under a big umbrella."

new_list = [i[0] for i in sentence.split() if len(i) > 3 and any(vowel in i.lower() for vowel in "aeiou")]
print(new_list)

# Create a list of the first letters of each word in a sentence, but only include the first letter
# if the word is longer than 4 characters and contains at least two different vowels (a, e, i, o, u).
sentence2 = "An amazing experience often involves understanding the intricacies of language and communication."
lol = [i[0] for i in sentence2.split() if len(i) > 4 and len(set(vowel for vowel in i.lower() if vowel in "aeiou")) >= 2]
print(lol)
# Generate a List of Factorials for numbers 1-10 without importing math.
result = 1
factorial = [result := result * i for i in range(1, 11)]

                            # """ walrus operator := """
print(factorial)

# Generate a list of the cumulative sums of numbers from 1 to 20 using list comprehension,
# without importing any modules.
total = 0
cumul = [total := total + i for i in range(1, 21)]
print(cumul)

# Create a List of all Unique Characters in a string, case-insensitive, preserving order.

strin = "Sergiusz Kuderski"
seen = set()
unq = [i for i in strin if not (i.lower() in seen or seen.add(i.lower()))]
print(unq)
# Create a list of all characters in a string that are alphabetic characters (a-z or A-Z),
# case-insensitive, and unique, while preserving the order of their first appearance.

strinn = "Sergiuszek Kuderszczacki"
seen = set()
un = [char for char in strinn if char.isalpha() and not (char.lower() in seen or seen.add(char.lower()))]
print(un)


# Construct a List of Numbers that are divisible by 3 and 5 between 1 and 100.

divisible = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
print(divisible)
# Create a List of Strings representing the squares of the first 15 positive integers,
# formatted as 'Number: Square'.

positive = [f"{i}: {i * i}" for i in range(1, 16)]
print(positive)

# Create a list of strings for numbers 1 to 20, where each string indicates whether the number is 'Even' or 'Odd',
# formatted as 'Number: Even' or 'Number: Odd'. Use list comprehension.

even_oddi = [f"{i}: Even" if i % 2 == 0 else f"{i}: Odd" for i in range(1, 21)]
print(even_oddi)


# Generate a List of Reversed Words from a sentence.

sente = "sergiusz kocha wszystkich ludzi na swiecie"
li = [i[::-1] for i in sente.split()]
reversed_li = li[::-1]
print(li)
print(reversed_li)

# From a sentence,
# generate a list of all words reversed and reordered in descending order based on their original length.

words_info = [(i, i[::-1], len(i)) for i in sente.split()]
print(words_info)

sorted_words = sorted(words_info, key=lambda x: x[2], reverse=True)
print(sorted_words)

reversed_sorted_words = [item[1] for item in sorted_words]
print(reversed_sorted_words)

# Generate a multiplication table (from 1 to 5) as a list of lists —
# each sublist contains multiples of the row number.

table = [
    [1 * i for i in range(1, 6)],
    [2 * i for i in range(1, 6)],
    [3 * i for i in range(1, 6)],
    [4 * i for i in range(1, 6)],
    [5 * i for i in range(1, 6)],
]

print(table)
# Create a 3x3 matrix filled with zeros and ones, alternating — like a checkerboard pattern.

matrix = [[(row + col) % 2 for col in range(3)] for row in range(3)]
print(matrix)

# Create a 4x4 matrix filled with zeros.

matr = [
    [0 for _ in range(4)]
    for _ in range(4)
]
print(matr)

#
# Create a 3x3 matrix with values equal to the row number (all elements in a row are the same).

ma = [[row for _ in range(3)] for row in range(3)]
print(ma)


# Create a 3x3 matrix with values equal to the column number (all elements in a column are the same).

ms = [[column for column in range(3)] for _ in range(3)]
print(ms)

# Generate a 5x5 matrix where each element is the product of its row and column indices (starting from 0).


looping = [[row * col for row in range(5)] for col in range(5)]
print(looping)

# Create a 3x3 identity matrix (1s on the diagonal, 0s elsewhere).

identity = [[1 if i == j else 0 for j in range(3)]  for i in range(3)]
print(identity)


# Create a 2x4 matrix filled with the number 7.

seven = [[7 for _ in range(4)]for _ in range(2)]
print(seven)

# Generate a 3x3 matrix where each element is the sum of its row and column index.

sum_of = [[row + col for col in range(3)] for row in range(3)]
print(sum_of)


