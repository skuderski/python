# # create a list with values from 0 to 99
#
# print(list(range(100)))
#
# # create a list with values from 0 to 99 if "3" is in value
#
# result_list = []
#
# for num in range(100):
#     if "3" in str(num):
#         result_list.append(num)
#
# print(result_list)
#
# print([num for num in range(100)])
#
# print([num for num in range(100) if "3" in str(num)])
#
# # create a list of squares
#
# # squares = []
# # numbers = [3, 6, 9, 12, 4]
#
# for num in numbers:
#     squares.append(num ** 2)
#
# print(squares)
#
# for index, num in enumerate(numbers):
#     numbers[index] = num ** 2
# print(numbers)
#
# nums = [2, 3, 11, 14, 15]
# print(id(nums))
# nums = [num ** 2 for num in nums]
# print(id(nums))
# print(nums)
#
# list_of_names = [
#     ['Alice', 'Bob', 'Charlie'],
#     ['David', 'Eve', 'Frank'],
#     ['Grace', 'Heidi', 'Ivan']
# ]
#
# print([
#     [student + " - Python" for student in group]
#     for group in list_of_names
#  ])
#
# print([
# [
#     [student + " - Python" for student in group]
#     for group in list_of_names
#  ]
#
#     for _ in range(100)
# ])

"""LIST COMPREHENSION AND NESTED LIST COMPREHENSION"""

# Create a list of squares for numbers 0 to 9.

squares = [number ** 2 for number in range(10)]
print(squares)

# Filter even numbers from a list of integers from 1 to 20.

even_numbers = [num for num in range(1, 21) if num % 2 == 0]
print(even_numbers)

# Generate a list of tuples (x, x^2) for x in range 1 to 10.

list_of_tuples = [(x, x**2) for x in range(1, 11)]
print(list_of_tuples)

# Flatten a nested list: Given a list of lists, combine all elements into a single list.

list_of_lists = [
    [1, 2, 3],
    ['a', 'b', 'c'],
    [True, False, True],
    [10.5, 20.5, 30.5]
]

combined_list = [item for sublist in list_of_lists for item in sublist]
print(combined_list)


# Convert a list of strings to uppercase using list comprehension.

string_list = ["apple", "banana", "cherry", "date", "elderberry"]

uppercase_strings = [word.upper() for word in string_list]
print(uppercase_strings)


# Create a list of only the positive numbers from a list of mixed integers, including negatives and zeros.

integer_list = [-10, -5, 0, 3, 7, -2, 0, 15]

positive_numbers = [num for num in integer_list if num > 0]
print(positive_numbers)



# Extract the first letter of each word in a sentence (split into words).

sentence = "The quick brown fox jumps over the lazy dog."

words = sentence.split()
first_letter = [item[0] for item in words]
print(first_letter)


# Create a list of booleans indicating whether each number in a list is a prime number.
import math

numbers = [10, -5, 0, 42, 3.14, -7.2, 100, 5]

prime_numbers = [False if n < 2 else all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1)) for n in numbers]
print(prime_numbers)



# Create a list of counts of vowels in each string in a list of words.

words = ["apple", "banana", "cherry", "date", "elderberry"]

vowels = [sum(1 for ch in word if ch.lower() in "aeiou") for word in words]
print(vowels)


# Generate a list of numbers from 1 to 50 that are divisible by either 3 or 5.

three_or_five = [num for num in range(1, 51) if (num % 3 == 0) or (num % 5 == 0)]
print(three_or_five)

# Create a list of strings where each string is the original string reversed.

cities = ["New York", "Paris", "Tokyo", "Berlin", "Sydney"]

reversed_cities = [city[::-1] for city in cities]

print(reversed_cities)


# Create a list of integers from 1 to 20, but only include the ones that are divisible by 4 or 6.

four_six = [i for i in range(1, 21) if (i % 4 == 0) or (i % 6 == 0)]
print(four_six)


# Create a list of all the uppercase letters in the alphabet.

all_uppercase = [char for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
print(all_uppercase)



# Generate a list of strings where each string is the original word plus its length, e.g., "apple5".

funny_strings = [
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "Did you hear about the cheese factory that exploded? There was nothing left but de-brie.",
    "Why don’t scientists trust atoms? Because they make up everything!",
    "I told my computer I needed a break, and now it won’t stop sending me vacation ads!"
]

original_plus_length = [string + str(len(string)) for string in funny_strings]
print(original_plus_length)


# From a list of integers, create a new list containing only the numbers that are perfect squares.
import math
integers = [4, 10, 12, 15, 18, 20, 22, 25]

perfect_squares = [num for num in integers if math.sqrt(num).is_integer()]


# Make a list of all the vowels found in a sentence, with each vowel only appearing once (no duplicates).

sentence = "Learning Python can be both fun and very rewarding as you explore new programming skills."

vowels = [char for index, char in enumerate(sentence.lower()) if char in "aeiou" and char not in sentence.lower()[:index]]

print(vowels)

# Create a list of tuples (number, square) for all numbers between 1 and 10, but only include those whose square is greater than 20.


greater_than_twenty = [(n, n ** 2) for n in range(1, 11) if n ** 2 > 20]
print(greater_than_twenty)


# Create a list of all the words in a sentence that start with a vowel.

start_with_vowel = [word for word in sentence.split() if word.lower()[0] in "aeiou"]
print(start_with_vowel)

"Create a list of all the words in a sentence that have more than 5 characters."

sentence_check = "Creativity is intelligence having fun."

more_than_five = [word for word in sentence_check.split() if len(word) > 5]
print(more_than_five)

# Create a list of strings where each string contains the word "Python" repeated a number of times equal to its position in the list.

pytka = ["Python" * n for n in range(1, 11)]
print(pytka)