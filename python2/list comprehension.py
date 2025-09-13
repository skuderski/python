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

# Create a 3x3 matrix filled with zeros.

matrix = []

for _ in range(3):
    row = []
    for _ in range(3):
        row.append(0)
    matrix.append(row)
print(matrix)

mat = [[0 for _ in range(3)]
       for _ in range(3)
       ]

print(mat)

# Create a 4x4 matrix filled with ones.


matrix4 = [[1 for _ in range(4)]
    for _ in range(4)
]


# Create a 5x5 matrix filled with the number 7 using nested loops or list comprehension.

matrix5 = [[7 for _ in range(5)]
           for _ in range(5)
]

print(matrix5)

# Create a 6x4 matrix where each element is the product of its row and column indices (starting from 0).

matrix6x4= [[row * column for column in range(4)]
 for row in range(6)]

print(matrix6x4)

# Create a 7x3 matrix where each element is the sum of its row and column indices (starting from 0).

matrix7x3= [[row + column for column in range(3)]
for row in range(7)
]

print(matrix7x3)


# Create a 4x6 matrix where each element is the difference between its row and column indices (starting from 0).
matrix4x6 = [[row - column for column in range(6)]
for row in range(4)
]
print(matrix4x6)


# Create a 5x5 matrix where each element
# is the square of the sum of its row and column indices (starting from 0).

five = [[((row + column) ** 2) for column in range(5)]
for row in range(5)
]


print(five)
print(matrix4)
# Create a 4x4 identity matrix (1s on the diagonal, 0s elsewhere).

identity_matrix = [[1 if i == j else 0 for j in range(4)]
                    for i in range(4)
]
print(identity_matrix)
# Create a 5x5 identity matrix (1s on the diagonal, 0s elsewhere) using nested list comprehension.


# identy = [[1 if i == j else 0 for j in range(5)]
#           for i in range(5)]
#
# print(identy)

# Create a 6x6 matrix where each element is 1 if the sum of its row and column indices is even, and 0 otherwise.

matrix6 = [[1 if (i + j) % 2 == 0 else 0 for j in range(6)]
            for i in range(6)]

print(matrix6)

# Create a 3x3 matrix where each element is 1 if the row number is greater than the column number,
# and 0 otherwise.

matrix3 = [[1 if i > j else 0 for j in range(3)]
            for i in range(3)]

print(matrix3)

# Create a 4x4 matrix where each element is 1 if the column number is even, and 0 if the column number is odd.

matrix4 = [[1 if j % 2 == 0 else 0 for j in range(4)]
           for i in range(4)]
print(matrix4)

# Create a 5x5 matrix where each element is 2 if the sum of its row and column indices is divisible by 3,
# and 0 otherwise.


mat5 = [[2 if (i + j) % 3 == 0 else 0 for j in range(5)]
            for i in range(5)]

print(mat5)

# Generate a 3x3 matrix where each element is the sum of its row and column indices.

ma3 = [[i + j for j in range(3)]
        for i in range(3)]

print(ma3)

# Create a 4x4 matrix where each element is the difference between its row and column indices.

ma4 = [[i - j for j in range(4)]
for i in range(4)]

print(ma4)

# Create a 5x5 matrix where each element is 1 if the product of its row and column indices is even,
# and 0 otherwise.

ma5 = [[1 if (i * j) % 2 == 0 else 0 for j in range(5)]
for i in range(5)]
print(ma5)

# Create a 6x6 matrix where each element is 1 if the sum of its row and column indices is divisible by 3,
# and 0 otherwise.


matr6 = [[1 if (i + j) % 3 == 0 else 0 for j in range(6)]
for i in range(6)]

print(matr6)

# Create a 5x5 multiplication table where each element is the product of its row and column indices.


s = [[i * j for j in range(5)]
for i in range(5)]

print(s)

# Create a 6x6 matrix where each element is the sum of its row and column indices.

ss = [[o + j for j in range(6)]
for o in range(6)]

print(ss)

# Create a 2x3 matrix filled with the number 7.

sss = [[7 for _ in range(3)]
for _ in range(2)]

print(sss)

# Create a 3x5 matrix where each element is the difference between 10 and its row and column indices.
x = [[10 - (i + j) for j in range(5)]
for i in range(3)]

print(x)

# Create a 4x4 matrix where each element is the product of 2 and its row index, plus the column index.

ssss = [[(2 * i) + j for j in range(4)]
for i in range(4)]

print(ssss)

# Create a 5x5 matrix where each element is the square of the sum of its row and column indices.

asdsa = [[(i + j) ** 2 for j in range(5)]
         for i in range(5)]
print(asdsa)

# Generate a 4x4 matrix with values decreasing from 16 to 1 in row-major order.
values = [i for i in range(16, 0, -1)]
aaa = [[values[i *4:(i + 1) * 4]
for i in range(4)]]

print(aaa)

# Create a 3x3 matrix with alternating 0s and 1s like a checkerboard pattern.
#
# Generate a list of lists where each inner list contains the first 5 natural numbers, repeated 3 times.
#
# Create a 2x5 matrix with each row being the sequence of numbers from 1 to 5, multiplied
# by the row number (i.e., row 0 all 0s, row 1 all 1s, etc.).
#
# Generate a 4x4 matrix with elements equal to the product of the row and column indices,
# but only for even row indices.


# x = "ABC"
# y = "123"
# z = "abc"
# comb = []
# for i in x:
#     for j in y:
#         for k in z:
#             comb.append(i + j + k)
# print(comb)
#
# w = [i + j + k for i in x for j in y for k in z
#
# ]
# print(w)

# Create a dictionary from a list of numbers where each key is the number and the value is its square.

numberss = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dicti = {num: num ** 2 for num in numberss}
print(dicti)

# Given a list of words, create a dictionary mapping each word to its length.

wordz = ["Sergiusz", "Kuderski", "age", "30"]
words_di = {word: len(word) for word in wordz}
print(words_di)

# Create a dictionary with keys being numbers 1 through 5 and values being those numbers multiplied by 10.

ranger = {i: i * 10 for i in range(1, 6)}
print(ranger)


# Given a string, create a dictionary counting how many times each character appears.

stringo = "Sergiusz Kuderski"

stringo_d = {i: stringo.count(i) for i in stringo}
print(stringo_d)


# Create a dictionary from two lists: one with names and another with ages, mapping names to ages.

one = ["Sergiusz", "Irena", "Wiesiek"]
two = [31, 62, 69]
three = {name:age for name, age in zip(one, two)}
print(three)


# Generate a dictionary where keys are numbers from 1 to 10 and values are the cubes of those numbers.

some_dicti = {i: i ** 3 for i in range(1, 11)}
print(some_dicti)


# Create a dictionary with words as keys and their uppercase versions as values, given a list of words.

some_other_dicti = {word: word.upper() for word in wordz}
print(some_other_dicti)

# From a list of tuples (name, score), create a dictionary mapping names to scores.

list_of_te = [("Sergiusz", 30), ("Irena", 62), ("Wiesiek", 69)]
dics = {l[0]: l[1] for l in list_of_te}
print(dics)

# Create a 3x3 matrix filled with zeros.

sa = [[0 for _ in range(3)]
    for _ in range(3)
]
print(sa)

# Create a 5x5 matrix filled with ones.
fi = [[1 for _ in range(5)]
for _ in range(5)]

print(fi)

# Create a 4x4 matrix where each element is the sum of its row and column indices,
# but only include elements where the sum is an even number; otherwise, fill with zero.


fourxfour = [[(row + column) if (row + column) % 2 == 0 else 0 for column in range(4)]
                for row in range(4)]

print(fourxfour)

# Create a 5x5 matrix where each element is the product of its row and column indices,
# but only if the product is an odd number; otherwise, fill the cell with zero.
fivexfive = [[(row * column) if (row * column) % 2 != 0 else 0 for column in range(5)]
                for row in range(5)]

print(fivexfive)


# Create a 6x6 matrix where each element is the difference between its row and column indices,
# but only include the difference if it's an odd number; otherwise, fill with zero.

sixxsix = [[(row - column) if (row - column) % 2 != 0 else 0 for column in range(6)]
            for row in range(6)]

print(sixxsix)

# Create a 4x4 identity matrix (1s on the diagonal, 0s elsewhere).

iden = [[1 if i == j else 0 for j in range(4)]
        for i in range(4)]

print(iden)

# Create a 5x5 matrix where the element is 1
# if the sum of its row and column indices is divisible by 3, and 0 otherwise.

sada = [[(row + col) if (row + col) % 3 == 0 else 0 for col in range(5)]
        for row in range(5)]

print(sada)
# Generate a 3x3 matrix where each element is the sum of its row and column indices.

leesa = [[r + c for c in range(3)]
         for r in range(3)]

print(leesa)

# Create a 4x4 matrix where each element is the difference between its row and column indices.

dif = [[row - col for col in range(4)]
       for row in range(4)]
print(dif)

# Create a 5x5 multiplication table where each element is the product of its row and column indices.

multipa = [[(row * col) for col in range(5)]
            for row in range(5)]

print(multipa)

# Create a 2x3 matrix filled with the number 7.

seven = [[7 for _ in range(3)]
            for _ in range(2)]

print(seven)

# Create a 3x4 matrix where each element is the product of its row and column indices,
# but only include the product if it is an odd number; otherwise, fill the cell with zero.

asdasdas = [[(row * column) if (row * column) % 2 != 0 else 0 for column in range(4)]
for row in range(3)]
print(asdasdas)
# Generate a 4x4 matrix with values decreasing from 16 to 1 in row-major order.

sixteen = [[num for num in range(16, 10, -1)]
           for _ in range(4)]
print(sixteen)

# Create a 3x5 matrix where each row contains the numbers from 20 down to 16.
twooo = [[num for num in range(20, 15, -1)]
for _ in range(3)]
print(twooo)

# Create a 3x3 matrix with alternating 0s and 1s like a checkerboard pattern.

al = [[1 if col % 2 == 0 else 0 for col in range(3)]
      for _ in range(3)]
print(al)

# Create a 4x4 matrix where each element is 1 if the row index plus the column index is divisible by 3,
# and 0 otherwise.

print([[1 if (row + col)% 3 == 0 else 0 for col in range(4)]
for row in range(4)])

# Generate a list of lists where each inner list contains the first 5 natural numbers, repeated 3 times.

natural = [[x for x in range(1, 6)] for _ in range(3)]
print(natural)

# Create a list of 4 inner lists, where each inner list contains the squares of numbers from 1 to 4.
# Use nested list comprehension.

squares = [[x ** 2 for x in range(1, 5)] for _ in range(4)]
print(squares)

# Create a 2x5 matrix with each row being the sequence of numbers from 1 to 5, multiplied by the row number
# (i.e., row 0 all 0s, row 1 all 1s, etc.).

xcas= [[row * num for num in range(1, 6)] for row in range(2)]
print(xcas)
# Create a 3x4 matrix where each row is the sequence of numbers from 0 to 3,
# multiplied by the row number (i.e., first row all 0s, second row all 1s, and third row all 2s).

aasfa = [[row * num for num in range(4)] for row in range(3)]
print(aasfa)


# Generate a 4x4 matrix with elements equal to the product of the row and column indices,
# but only for even row indices.

asfasfas = [[(row * col) if row % 2 == 0 else 0 for col in range(4)]
    for row in range(4)]

print(asfasfas)

# Create a list of squares for numbers 1 through 10.

squares = [num ** 2 for num in range(1, 11)]
print(squares)

# Task:
# Create a list of tuples (number, square, cube) for numbers from 1 to 10,
# but only include the tuples where the number is divisible by 2 or 3.

squares_tuples = [(num, num ** 2, num ** 3) for num in range(1, 11) if num % 2 == 0 or num % 3 == 0]
print(squares_tuples)

# Task:
# Create a list of tuples (number, sum of digits) for numbers from 1 to 50,
# but only include those where the sum of the digits is greater than 10.
# (For example, 29 has digits 2 and 9, sum is 11, so it should be included.)

list_of_tuples_ = [(num, sum(int(digit) for digit in str(num))) for num in range(1, 51) if sum(int(digit) for digit in str(num)) > 10]
print(list_of_tuples_)

# Task:
# Create a list of tuples (number, product of digits) for numbers from 10 to 99,
# but only include those where the product of digits is divisible by 3.

list2 = [
    (num,
     [int(d) * int(d) for d in str(num)])
             for num in range(10, 100)
    if any((int(d) * int(d)) % 3 == 0 for d in str(num))]
print(list2)
# Generate a list of all even numbers from 0 to 20.

even_n = [n for n in range(21) if n % 2 == 0]
print(even_n)

# Create a list of all odd numbers from 1 to 50 using list comprehension.

odd_n = [n for n in range(1, 51) if n % 2 != 0]
print(odd_n)

# Create a list of squares of all numbers from 1 to 50, but only include those squares that are divisible by 3 or 5.

squares1 = [n ** 2 for n in range(1, 51) if n ** 2 % 3 == 0 or n ** 2 % 5 == 0]
print(squares1)

# Create a list of numbers from 1 to 100 where the number is divisible by 3 or 5,
# but exclude numbers where the number's digit sum is greater than 10.

num100 = [n for n in range(1, 100) if (n % 3 == 0 or n % 5 == 0) and sum(int(d) for d in str(n)) <= 10]
print(num100)

# Create a list of numbers from 200 to 300 that are divisible by 4 or 6,
# but exclude numbers where the product of their digits is greater than 30.
import math
num200 = [n for n in range(200, 301) if (n % 4 == 0 or n % 6 == 0) and math.prod(int(d) for d in str(n)) <= 30]
print(num200)

# Create a list of strings, where each string is 'Number X' for numbers 1 to 5.

list_str = [f"Number {n}" for n in range(1, 6)]
print(list_str)

# Create a list of strings where each string is 'Item Y' for numbers 10 to 15.

list_y = [f"Item {n}" for n in range(10, 16)]
print(list_y)

# Create a list of strings where each string is 'Product N: $X', for numbers 20 to 25, 
# with the price being calculated as N * 10 + 99. For example, for N=20, the string should be 'Product 20: $299'.


listzz = [f"Product {n}: ${n * 10 + 99}" for n in range(20, 26)]
print(listzz)

# Create a list of strings 'Item N: Price $X' for N from 30 to 35,
# where the price X is calculated as N * 15 + 50. Use a list comprehension with proper string formatting.

listaaz = [f"Item {n}: Price ${(n * 15) + 50}" for n in range(30, 36)]
print(listaaz)

# Create a list of strings 'Product N: Discounted Price $Y' for N from 40 to 45, where:
#
# The original price X is calculated as N * 20 + 100.
# The discount price Y is 20% less than the original price.

asfas = [f"Product {n}: Discounted Price ${round((n * 20 + 100) * .8, 2)}" for n in range(40, 46)]
print(asfas)

# Generate a list of strings 'Item N: Price $X' for N from 100 to 105.
#
# The original price X should be calculated as N * 10 + 50.
# The discounted price should be 15% less than the original price.
# Use formatted strings (with two decimal places) to display the price.


wgqw = [f"Item {n}: Price ${round((n * 10 + 50) * .85, 2)}" for n in range(100, 106)]
print(wgqw)

# Create a list of the lengths of each word in a list of words.

words = ["apple", "banana", "cherry", "date", "elderberry",
         "fig", "grape", "honeydew", "kiwi", "lemon"]

len_word = [len(word) for word in words]
print(len_word)

# Create a list of the uppercase versions of each word in a list of words.

upper_words = [word.upper() for word in words]
print(upper_words)

# Given a list of words, create a list of strings where each string contains the original word repeated as many times as its length,
# separated by hyphens (-).
#
# For example, if the word is "hi", which has length 2, the string should be "hi-hi".


list_sttring = ["-".join([word] * len(word)) for word in words]
print(list_sttring)

# Given a list of words,
# create a new list where each element is a string containing the first letter of the word repeated as many times as the length of the word,
# separated by asterisks (*).

asfwgqg = ["*".join([word[0]] * len(word)) for word in words]
print(asfwgqg)

# Generate a list of tuples (number, square) for numbers 1 to 10.

tuples = [(n, n ** 2) for n in range(1, 11)]
print(tuples)

# Create a list of tuples (number, cube) for numbers from 5 to 15, but only include tuples where the cube is divisible by 4.

tuples2 = [(num, num ** 3)  for num in range(5, 16) if num ** 3 % 4 == 0]
print(tuples2)
# Create a list of tuples (number, square root of the number rounded to 2 decimal places) for numbers from 10 to 50.
# # Include only those tuples where the square root is an even integer or a perfect square (i.e., the square root is an integer).
import math
def is_perfect_square(n):
    sqrt_n = math.sqrt(n)
    return int(sqrt_n) ** 2 == n
safa = [(n, round(math.sqrt(n), 2)) for n in range(10, 51) if round(math.sqrt(n), 2) % 2 == 0 or is_perfect_square(n)]
print(safa)

# Create a list of the first 10 Fibonacci numbers.

def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


print(fibonacci(10))

# Create a list of lowercase letters from 'a' to 'z'.

lowercase = [chr(n) for n in range(97, 123)]
print(lowercase)

# Create a list of the uppercase letters from 'A' to 'Z' using their ASCII codes.
# Think about the ASCII range for uppercase letters and how to convert those codes into characters.

upep = [chr(n).upper() for n in range(97, 123)]
print(upep)

# Generate a list of all possible pairs (x, y) where x is from 0 to 2 and y is from 0 to 2.

x_y_flat = [(x, y) for x in range(3) for y in range(3)]
print(x_y_flat)

x_y = [(x, y) for y in range(0, 3) for x in range(0, 3)]

print(x_y)

# Generate a list of all possible ordered triples (x, y, z) where each variable ranges from 1 to 3.
# Think about using nested list comprehensions to cover all combinations.

ordered_triples = [(x, y, z ) for x in range(1, 4) for y in range(1, 4) for z in range(1, 4)]
print(len(ordered_triples))
print(ordered_triples)

# Create a list of the absolute values of numbers from -5 to 5.

list_absolute = [abs(n) for n in range(-5, 6)]
print(list_absolute)

# Create a list of the absolute values of numbers from -10 to 10, but only include those absolute values that are greater than 5.
# Make sure to use the abs() function in your list comprehension.

absolutes = [abs(n) for n in range(-10, 11) if abs(n) > 5]
print(absolutes)


# Create a list of prime numbers from 2 to 50 (use a helper function to check if a number is prime).

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes2 = [n for n in range(2, 51) if is_prime(n)]
print(primes2)