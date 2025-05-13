numbers = [4, 2, 7, 10]

squares = {}

for num in numbers:
    if num % 2 == 0:
        squares[num] = num ** 2

print(squares)

squares2 = {num: num **2 for num in numbers if num % 2 == 0}
print(squares2)

set_of_squares = {num **2 for num in numbers if num % 2 == 0}
print(set_of_squares)

word = "hello"

symbols = {}

for char in word:
    if char not in symbols:
        symbols[char] = 1
    else:
        symbols[char] += 1
print(symbols)

"""ONE LINERS"""

def sum_if_three():
    return sum([i for i in range(100) if "3" in str(i)])

print(sum_if_three())

def make_uppercase(words: str):
    return " ".join([word.upper() for word in words.split(" ") if len(word) > 5])

print(make_uppercase("Sergiusz to fajny gosc"))
"""IMPORTANT EXAMPLE TO GO OVER"""
attendance = [
    ["Monday", "Wednesday", "Friday"],
    ["Tuesday", "Thursday"],
    ["Monday", "Tuesday", "Wednesday"],
    ["Wednesday", "Friday"]
]

def get_count_attendance(attendance: list):
    return {day: sum(attendance, []).count(day) for day in set(sum(attendance, []))}

print(get_count_attendance(attendance))

# Create a dictionary mapping numbers from 1 to 10 to their squares.

squares = {num: num ** 2 for num in range(1, 11)}
print(squares)

#
# Given a list of words, create a dictionary with words as keys and their lengths as values.

words = ["ocean", "mountain", "forest", "desert", "river", "valley", "canyon", "beach", "island", "volcano"]

words_dict = {word: len(word) for word in words}
print(words_dict)


# From a list of numbers, create a dictionary where the keys are the numbers and the values are True if the number is even, False otherwise.

numbers = [3, 7, 10, 15, 22, 30, 42]

numbers_dictionary = {num: True if num % 2 == 0 else False for num in numbers}
print(numbers_dictionary)


# Generate a dictionary of vowels as keys (a, e, i, o, u) and their ASCII codes as values.
vowels = ["a", "e", "i", "o", "u"]
vowels_ASCII = {vowel: ord(vowel) for vowel in vowels}
print(vowels_ASCII)




# Given a list of strings, create a dictionary where each string is the key and the value is the string reversed.

names = [
    "Alexander", "Benjamin", "Catherine", "Diana", "Eleanor",
    "Frederick", "Gabriella", "Harrison", "Isabella", "Jonathan",
    "Katherine", "Leonardo", "Madeline", "Nicholas", "Olivia"
]

dictionary_of_names_reversed = {name: name[::-1] for name in names}
print(dictionary_of_names_reversed)



# Create a dictionary from a list of names, assigning each name a default score of 0.

names1 = [
    "Sophia", "Jackson", "Olivia", "Liam", "Emma",
    "Aiden", "Ava", "Lucas", "Mia", "Caden",
    "Aria", "Grayson", "Ella", "Ethan", "Harper"
]

default_names = {name: 0 for name in names1}
print(default_names)



# Invert a dictionary: given a dictionary, create a new dictionary where keys are values, values are keys. (Assume all values are unique.)

fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple",
    "orange": "orange",
    "kiwi": "brown",
    "lemon": "yellow"
}

inverted = {color: fruit for fruit, color in fruit_colors.items()}
print(inverted)


# From a list of tuples (city, temperature), create a dictionary mapping each city to its temperature.

city_temperatures = [
    ("New York", 75),
    ("Los Angeles", 85),
    ("Chicago", 70),
    ("Houston", 90),
    ("Phoenix", 105),
    ("Philadelphia", 78),
    ("San Antonio", 88),
    ("San Diego", 77),
    ("Dallas", 83),
    ("San Jose", 72)
]

dictionary_of_temperatures = {city: temperature for city, temperature in city_temperatures}

print(dictionary_of_temperatures)


# Create a dictionary that maps each letter (a-z) to its position in the alphabet.

alphabet = "abcdefghijklmnopqrstuvwxyz"

mapping_to_position = {letter: index for index, letter in enumerate(alphabet, start = 1)}

print(mapping_to_position)


# Filter a dictionary to include only items where the key is an even number.


random_numbers_dict = {
    237: "A mysterious code",
    459: "A random number",
    782: "Another value",
    591: "Sample data",
    403: "Sample data",
    888: "Lucky number",
    123: "Simple number"
}

even_keys = {key: random_numbers_dict[key] for key in random_numbers_dict if key % 2 == 0}
print(even_keys)

# Create a dictionary where keys are the numbers from 10 to 20,
# and values are the cubes of those numbers, but only include entries where the number is odd.

numbers_from_ten_to_twenty = {num: num**3 for num in range(10, 21) if not num % 2 == 0}
print(numbers_from_ten_to_twenty)

# Given a list of temperatures in Celsius, create a dictionary that maps each temperature to its Fahrenheit equivalent.

celsius_temperatures = [3.5, -7.2, 15.0, 22.8, -12.4, 37.6, 0.0, 45.3]
fahrenheit_temps = {celsius: celsius * 9/5 + 32 for celsius in celsius_temperatures}
print (fahrenheit_temps)

# Given a dictionary of products and their prices, create a new dictionary that includes only the products with prices greater than $50.

products_prices = {
    "laptop": 999.99,
    "smartphone": 699.99,
    "book": 15.50,
    "headphones": 85.75,
    "coffee mug": 12.30,
    "monitor": 250.00,
    "keyboard": 45.00,
    "chair": 120.50,
    "desk lamp": 35.00,
    "smartwatch": 199.99
}

products_over_fifty = {key: value for key, value in products_prices.items() if products_prices[key] > 50}

print(products_over_fifty)

# Create a dictionary where the keys are the integers from 1 to 10, and the values are their factorials.

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

random_dictionary = {num: factorial(num) for num in range(1, 11)}

print(random_dictionary)

# Create a dictionary where the keys are the first 10 lowercase letters (a to j), and the values are the ASCII codes of those letters.
letters = "abcdefghij"
ten_letters = {letter: ord(letter) for letter in letters}
print(ten_letters)

