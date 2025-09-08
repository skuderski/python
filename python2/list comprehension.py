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