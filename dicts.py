# # Create a Dictionary: Create a dictionary that stores the names and ages of three people.
#
# people = {"Sergiusz": 30, "Irena": 62, "Piotr": 39}
# print(people)
# # Access Values: Given a dictionary of book titles and their authors,
# # write a function to retrieve the author of a given book title. Handle the case where the book is not in the dictionary.
#
# books = {
#     "The Lord of the Rings": "J.R.R. Tolkien",
#     "Pride and Prejudice": "Jane Austen",
#     "1984": "George Orwell",
#     "To Kill a Mockingbird": "Harper Lee",
#     "The Great Gatsby": "F. Scott Fitzgerald"
# }
#
# def retrieve_author(books: dict, book_title: str):
#     if book_title in books:
#         return books[book_title]
#     else:
#         return "Author not found"
#
# print(retrieve_author({
#     "The Lord of the Rings": "J.R.R. Tolkien",
#     "Pride and Prejudice": "Jane Austen",
#     "1984": "George Orwell",
#     "To Kill a Mockingbird": "Harper Lee",
#     "The Great Gatsby": "F. Scott Fitzgerald"}, "1984"))
#
# # Add and Update Key-Value Pairs: Create an empty dictionary.
# # Then, add key-value pairs representing the names and phone numbers of five contacts.
# # Next, update the phone number for one of the existing contacts.
#
# my_dict = {}
# initial_contact = {
#     "Sergiusz": 12512,
#     "Irena": 212112,
#     "Wiesiek": 211151,
#     "Piotr": 10555210,
#     "Magda": 1522255234
# }
# my_dict.update(initial_contact)
#
# my_dict.update({"Sergiusz": 21512512})
#
# print(my_dict)
#
# # Iterate Through a Dictionary: Given a dictionary of student names and their scores,
# # iterate through the dictionary and print each student's name along with their score.
#
# student_scores = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 95,
#     "Eve": 88
# }
#
# for key, value in student_scores.items():
#     print(f"{key}: {value}")
#
# # Check for Key Existence: Write a function that takes a dictionary and a key as input.
# # The function should return True if the key exists in the dictionary and False otherwise.
#
# def key_existence(name: dict, key: any):
#     return key in name
#
# print(key_existence({
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 95,
#     "Eve": 88
# }, "Eve"))
#
#
# # Count Word Occurrences: Write a function that takes a string as input and
# # returns a dictionary where the keys are the words in the string, and the values are the number of times each word appears.
# # (This is a classic example).
# def count_word_occurrences(word: str):
#     count = {}
#     words = word.lower().split()
#     for wordz in words:
#         if wordz not in count:
#             count[wordz] = 1
#         else:
#             count[wordz] += 1
#     return count
#
# print(count_word_occurrences("sergiusz kuderski sergiusz"))
#
#
# # Merge Two Dictionaries: Given two dictionaries, write a function to merge them into a single dictionary.
# # If there are any common keys, the value from the second dictionary should overwrite the value from the first dictionary.
#
#
# def merge_two_dics(first: dict, second: dict):
#     first.update(second)
#     return first
#
# print(merge_two_dics({
#     "name": "Alice Smith",
#     "age": 30,
#     "city": "New York",
#     "occupation": "Software Engineer"
# }, {
#     "apple": 100,
#     "banana": 50,
#     "orange": 75,
#     "grape": 120
# }))
# #
# # Find the Maximum Value: Given a dictionary where the keys are strings and the values are numbers,
# # find the key associated with the maximum value.
# def find_maximum(some_dict: dict):
#     maximum_key = next(iter(some_dict))
#     maximum = some_dict[maximum_key]
#     for key, value in some_dict.items():
#         if value > maximum:
#             maximum = value
#             maximum_key = key
#
#     return maximum_key
#
# print(find_maximum({"a": 10, "b": 5, "c": 12, "d": 8}))
#
#
# # Value Sum: Given a dictionary where the keys are strings and the values are numbers,
# # write a function that calculates the sum of all the values in the dictionary.
#
#
# def value_sum(dix: dict):
#     sum_of_values = 0
#     for value in dix.values():
#         sum_of_values += value
#     return sum_of_values
#
# print(value_sum({
#     "USD_to_EUR": 0.92,
#     "USD_to_GBP": 0.79,
#     "USD_to_JPY": 147.50
# }))
# # Key Lengths: Given a dictionary where the keys are strings and the values are anything,
# # write a function that creates a new dictionary where the keys are the same as the original dictionary,
# # but the values are the lengths of the original keys.
#
# def key_lengths(some_dict: dict):
#     d = {}
#     for key, value in some_dict.items():
#         d[key] = len(key)
#     return d
#
# print(key_lengths({
#     "string_key": "Hello",
#     "integer_key": 123,
#     "float_key": 3.14,
#     "boolean_key": True,
#     "list_key": [1, 2, 3],
#     "tuple_key": (4, 5, 6),
#     "dictionary_key": {"a": 1, "b": 2}
# }))
#
# def count_marks(class_register: dict) -> dict:
#     marks = {}
#     for v in class_register.values():
#         if v not in marks:
#             marks[v] = 1
#         else:
#             marks[v] += 1
#     return marks
# print(count_marks({
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 85,
#     "Eve": 88
# }))

# def create_dictionary(*args) -> dict:
#     some_dict = {}
#     for index, arg in enumerate(args):
#         if isinstance(arg, (list, dict, set)):
#             print(f"Cannot add {arg} to the dict!")
#         else:
#             some_dict[arg] = index
# 
#     return some_dict
# 
# print(create_dictionary(10, [1, 2], "hello", {'a': 1}, 3.14, set([1,2]), 2))


# Create a dictionary that maps each letter in the string "python" to its position in the string (starting from 1).
# some_string = "python"
# dict = {}
# for index, letter in enumerate(some_string, start = 1):
#     dict[letter] = index
# print(dict)
#
# # Given a dictionary of student names and their scores, create a new dictionary with only the students who scored above 80.
#
# students_scores = {
#     "Alice": 92,
#     "Bob": 85,
#     "Charlie": 78,
#     "David": 88,
#     "Eva": 95,
#     "Frank": 67,
#     "Grace": 73,
#     "Helen": 81
# }
#
# scores_above_80 = {}
#
# for key, value in students_scores.items():
#     if value > 80:
#         scores_above_80[key] = value
#
# print(scores_above_80)
#
# # Invert a dictionary: given a dictionary where keys are items and values are categories,
# # create a new dictionary where categories are keys and items are lists of items belonging to each category.

# items_categories = {
#     "apple": "fruit",
#     "carrot": "vegetable",
#     "salmon": "fish",
#     "broccoli": "vegetable",
#     "banana": "fruit",
#     "chicken": "meat",
#     "blueberry": "fruit",
#     "potato": "vegetable"
# }
# inverted_dict = {}
#
# for key, value in items_categories.items():
#     if value not in inverted_dict:
#         inverted_dict[value] = []
#     inverted_dict[value].append(key)
#
# print(inverted_dict)
#
# # Calculate the total value of a dictionary of items and prices by summing all the prices.
#
# items_prices = {
#     "bread": 2.50,
#     "milk": 3.00,
#     "eggs": 2.00,
#     "cheese": 5.50,
#     "apple": 0.75,
#     "chicken": 8.00,
#     "rice": 1.20,
#     "orange juice": 3.50
# }
#
# print(sum(items_prices.values()))
#
# # From a dictionary of country populations, find all countries where the population is over 50 million.
#
# random_countries_population = {
#     "Norway": 5378857,
#     "Kenya": 53771296,
#     "Portugal": 10295909,
#     "Vietnam": 97338583,
#     "Australia": 25687041,
#     "Finland": 5540720,
#     "Greece": 10715549,
#     "Thailand": 69799978,
#     "Latvia": 1901548,
#     "Peru": 32971874
# }
#
# over_fifty = []
#
# for key, value in random_countries_population.items():
#     if value > 50000000:
#         over_fifty.append(key)
# print(over_fifty)
#
#
# # Create a dictionary from a list of words, with the word as the key and the length of the word as the value.
#
# cute_words = ["bunny", "kitten", "cupcake", "snuggle", "peach", "butterfly", "cloud", "daisy", "pudding", "sparkle"]
#
# dix = {}
#
# for word in cute_words:
#     dix[word] = len(word)
# print(dix)
#
#
# # Given a dictionary where keys are student names and values are their scores, create a new dictionary with only students who scored below 60.
#
# student_scores = {
#     "Alice": 92,
#     "Bob": 85,
#     "Charlie": 78,
#     "David": 88,
#     "Eve": 95,
#     "Frank": 55,
#     "Grace": 73,
#     "Helen": 81
# }
#
# diksee = {}
#
# for key, value in student_scores.items():
#     if value < 60:
#         diksee[key] = value
#
# print(diksee)
#
#
# # Create a dictionary from a list of numbers where keys are the numbers and values are the number squared, but only include numbers divisible by 3.
#
# random_numbers = [12, -5, 7, 0, 23, -14, 5.5, 8, -2, 15]
#
# dictzzz = {}
#
# for n in random_numbers:
#     if n % 3 == 0:
#         dictzzz[n] = n ** 2
# print(dictzzz)
#
#
# # From a dictionary of country populations, create another dictionary mapping countries to "developed" or "developing"
# # based on whether their population exceeds 100 million (yes for developed, no for developing).
#
# europe_populations = {
#     "Russia": 145912025,
#     "Germany": 83783942,
#     "United Kingdom": 67886011,
#     "France": 65273511,
#     "Italy": 60461826,
#     "Spain": 46754778,
#     "Ukraine": 43733762,
#     "Poland": 37887452,
#     "Romania": 19237582,
#     "Netherlands": 17134872
# }
#
# developed_developing = {}
#
# for key, value in europe_populations.items():
#     if value > 50_000_000:
#         developed_developing[key] = "developed"
#     else:
#         developed_developing[key] = "developing"
# print(developed_developing)
#
#
# # Given a dictionary where keys are words and values are their definitions,
# # swap keys and values to create a new dictionary. (Assume all definitions are unique).
#
#
# word_definitions = {
#     "apple": "A fruit that is round and typically red, green, or yellow.",
#     "book": "A set of written, printed, or blank pages bound together.",
#     "car": "A vehicle with four wheels used for transporting people.",
#     "dog": "A domesticated carnivorous mammal that typically has a long snout.",
#     "elephant": "A large mammal with a trunk native to Africa and Asia.",
#     "flower": "A plant cultivated for its blooms or blossoms.",
#     "guitar": "A musical instrument with strings played by plucking or strumming.",
#     "hat": "A shaped covering for the head, typically with a brim.",
#     "ice": "Frozen water.",
#     "jungle": "A dense tropical forest."
# }
#
# swapparooni = {}
#
# for key, value in word_definitions.items():
#     swapparooni[value] = key
#
# print(swapparooni)


# Count the number of occurrences of each character in a string.

# random_string = "Skyfall clouds drift gently in the spring breeze."
#
# count_occurrences = {}
#
# for c in random_string:
#     if c not in count_occurrences:
#         count_occurrences[c] = 1
#     else:
#         count_occurrences[c] += 1
#
# print(count_occurrences)
#
# # Create a dictionary from two lists, one of keys and one of values.
# # (e.g., keys = ["a", "b", "c"], values = [1, 2, 3])
#
# keys = ["name", "age", "country", "favorite_color"]
# values = [5, 3, 7, 2]
# zipped =zip(keys, values)
# zipped_dict = (dict(zipped))
# combined_dict = {}
#
# for key, value in zipped_dict.items():
#     combined_dict[key] = value
#
# print(combined_dict)
#
# # Given a dictionary of student names and their scores,
# # create a new dictionary mapping students to "pass" or "fail" based on whether their score is above or below 60.
#
# student_scores = {
#     "Alice": 92,
#     "Bob": 85,
#     "Charlie": 78,
#     "Diana": 50,
#     "Ethan": 95,
#     "Fiona": 67,
#     "George": 73,
#     "Hannah": 44
# }
#
# pass_or_fail = {}
#
# for key, value in student_scores.items():
#     if value < 60:
#         pass_or_fail[key] = "fail"
#     else:
#         pass_or_fail[key] = "pass"
#
# print(pass_or_fail)
#
# # Join two dictionaries into one.
#
# student_grades1 = {
#     "Alice": 92,
#     "Bob": 85,
#     "Charlie": 78
# }
#
# country_population = {
#     "USA": 331000000,
#     "India": 1380004385,
#     "Brazil": 213993437
# }
#
# merged_dictionaries = {**student_grades1, **country_population}
#
# merged = student_grades1 | country_population # union of dictionaries
#
# print(merged_dictionaries)
# print(merged)
#
# # Create a dictionary that maps each even number from 1 to 20 to its square, and only include these entries in the dictionary.
#
# dictionary_of_squares = {}
#
# for num in range(1, 21):
#     if num % 2 == 0:
#         dictionary_of_squares[num] = num ** 2
#
# print(dictionary_of_squares)
#
# # Create a dictionary that maps each number from 1 to 50 to its cube, but only include the entries where the cube's last digit is 5 or 0.
#
# dictionary_of_cubes = {}
#
# for num in range(1, 51):
#     if num % 10 == 5 or num % 10 == 0:
#         dictionary_of_cubes[num] = num ** 3
#
# print(dictionary_of_cubes)
#
# # Create a dictionary that maps each integer from 1 to 100 to its factorial, but only include entries where the factorial's last digit is 0.
#
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
# factorial_dictionary = {}
#
# for num in range(1, 101):
#     fact = factorial(num)
#     if fact % 10 == 0:
#         factorial_dictionary[num] = fact
#
# print(factorial_dictionary)
#
# # Create a dictionary where the keys are strings representing numbers ("one", "two", "three") and the values are their numerical equivalents.
#
# list_of_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
# list_of_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# zippt = dict(zip(list_of_strings, list_of_integers))
#
# print(zippt)
#
# # Create a dictionary that maps each character in a sentence to its ASCII code.
#
# sentence = "The wind whispered softly through the ancient trees."
# list_of_character = []
# character_to_ASCII = []
#
# for c in sentence:
#     list_of_character.append(c)
#
# for c in list_of_character:
#     character_to_ASCII.append((c, ord(c)))
#
# print(character_to_ASCII)
#
# # In a student grades dictionary, increase everyone's grade by 5 points, but cap the maximum grade at 100.
#
# student_grades = {
#     "Alice": 92,
#     "Bob": 85,
#     "Charlie": 78,
#     "Diana": 88,
#     "Ethan": 95,
#     "Fiona": 97,
#     "George": 73,
#     "Hannah": 81
# }
#
#
# for key, value in student_grades.items():
#     student_grades[key] = min(student_grades[key] + 5, 100)
#
# print(student_grades)
#
#
# # Given a dictionary of temperatures in Celsius, decrease each temperature by 3 degrees, but do not allow any temperature to go below 0°C.
#
# temperatures = {
#     "New York": 10,
#     "Tokyo": 1,
#     "Paris": 15,
#     "Sydney": 18,
#     "Cairo": 3,
#     "Moscow": 5,
#     "Rio de Janeiro": 30,
#     "London": 12,
#     "Beijing": 20,
#     "Delhi": 2
# }
#
# for key, value in temperatures.items():
#     temperatures[key] = max(temperatures[key] -3, 0)
#
# print(temperatures)
#
# # Given a dictionary of student test scores (with scores possibly exceeding 100),
# # increase each score by 10 points, but cap the score at 120 (the maximum possible score).
#
# student_scorez = {
#     "Anna": 88,
#     "Ben": 105,
#     "Cara": 92,
#     "Derek": 118,
#     "Ella": 73,
#     "Frank": 104,
#     "Grace": 99,
#     "Hugo": 117
# }
#
# for key, value in student_scorez.items():
#     student_scorez[key] = min(student_scorez[key] + 10, 120)
#
# print(student_scorez)
#
# # Given a dictionary of scores, increase each score by 50 points only if the score is less than 85. After increasing,
# # cap the score at 130 to prevent exceeding that maximum, even if the increased score would be larger.
#
# student_scorsese = {
#     "Alice": 85,
#     "Bob": 82,
#     "Charlie": 92,
#     "Diana": 88,
#     "Ethan": 93,
#     "Fiona": 78,
#     "George": 84,
#     "Hannah": 90
# }
#
# for key, value in student_scorsese.items():
#     if value <= 85:
#         student_scorsese[key] = min(student_scorsese[key] + 50, 130)
# print(student_scorsese)
#
# # Given a dictionary of stock prices for different companies, increase each stock price by 10%, but only if the current price is below $240.
# # After increasing, ensure that the final price does not exceed $250 using the min() function.
#
# stock_prices = {
#     "Tesla": 150,
#     "Apple": 235,
#     "Amazon": 199,
#     "Google": 180,
#     "Microsoft": 250,
#     "NVIDIA": 190,
#     "Facebook": 145,
#     "Netflix": 238,
#     "Samsung": 222,
#     "Intel": 195
# }
#
# for key, value in stock_prices.items():
#     if value <= 240:
#         stock_prices[key] = min(stock_prices[key] + (stock_prices[key] * 0.1), 250)
#
# print(stock_prices)
#
# # Given a dictionary of airline ticket prices for various routes,
# # increase each price by 10% if the current price is below the average price of all routes.
# # After increasing, ensure that no price exceeds $500 using min().
#
# flight_prices = {
#     "NYC-LAX": 450,
#     "LHR-JFK": 450,
#     "SYD-LA": 499,
#     "PEK-HKG": 450,
#     "DXB-DEL": 440,
#     "SFO-ORD": 440,
#     "FRA-MEX": 435,
#     "JNB-CPT": 435,
#     "MIA-CHI": 452,
#     "VIE-ZRH": 440
# }
# average_price = sum(flight_prices.values()) / len(flight_prices)
# print(average_price)
# for key, value in flight_prices.items():
#     if value < average_price:
#         flight_prices[key] = min(flight_prices[key] + flight_prices[key] * 0.15, 500)
#
# print(flight_prices)
#
# # Given a dictionary of airline ticket prices, increase each price by 20% if:
# #
# # The current price is below twice the average price of all routes, and
# # The current price is not already above $400.
# # After increasing, cap each price at $500 using min().
#
# flight_prices2 = {
#     "NYC-LAX": 450,
#     "LHR-JFK": 480,
#     "SYD-LA": 520,
#     "PEK-HKG": 390,
#     "DXB-DEL": 410,
#     "SFO-ORD": 430,
#     "FRA-MEX": 370,
#     "JNB-CPT": 385,
#     "MIA-CHI": 495,
#     "VIE-ZRH": 392
# }
# avg = sum(flight_prices2.values()) / len(flight_prices2)
# for key, value in flight_prices2.items():
#     if value < (avg * 2) and value < 400:
#         flight_prices2[key] = min(flight_prices2[key] + flight_prices2[key] * 0.2, 500)
#
# print(flight_prices2)

# Given a dictionary of airline ticket prices, for each route:
#
# Increase the price by 30% if:
# The price is less than the average price of all routes, and
# The price is less than $300.
# If the price after increase exceeds $600, cap it at $600.
# Additionally, if after the increase the price is more than 80% of the original price,
# apply a discount to reduce it back to 80% of its original pre-increase value (but don’t go below $250).

# flight_p = {
#     "NYC-LAX": 450,
#     "LHR-JFK": 470,
#     "SYD-LA": 580,
#     "PEK-HKG": 290,
#     "DXB-DEL": 310,
#     "SFO-ORD": 340,
#     "FRA-MEX": 275,
#     "JNB-CPT": 250,
#     "MIA-CHI": 595,
#     "VIE-ZRH": 260
# }
# before_increase = {}
# for key, value in flight_p.items():
#     before_increase[key] = value
# print(before_increase)
#
# average = sum(flight_p.values()) / len(flight_p)
#
# for key, value in flight_p.items():
#     if value < average and value < 300:
#         flight_p[key] = min(flight_p[key] + flight_p[key] * 0.3, 600)
#
# for key in flight_p:
#     original_price = before_increase[key]
#     current_price = flight_p[key]
#     if current_price > original_price * 0.8:
#         flight_p[key] = max(original_price * 0.8, 250)
# print(flight_p)
#
#
# # Count how many words in a paragraph start with each letter, resulting in a dictionary where keys are letters,
# # and values are counts of words starting with that letter.
#
# paragraph = "The sun dipped below the horizon, casting a warm golden hue across the sky. The gentle breeze carried the sweet scent of blooming flowers, creating a peaceful atmosphere."
# words = paragraph.split(" ")
# print(words)
#
# count_of_letter = {}
#
# for word in words:
#     first_letter = word[0].lower().strip(".,")
#     if first_letter not in count_of_letter:
#         count_of_letter[first_letter] = 1
#     else:
#         count_of_letter[first_letter] += 1
#
# print(count_of_letter)



# Dictionary Summation
# Given a dictionary of numbers, write a function to return the sum of all values.

numbers_dict = {
    'a': 10,
    'b': 25,
    'c': 7,
    'd': 30,
    'e': 15
}

total_sum = sum(numbers_dict.values())
print(total_sum)

# 2. Invert a Dictionary
# Create a function that takes a dictionary and returns a new dictionary with keys and values swapped. Assume all values are unique.

def invert_dictionary(dictionary: dict):
    new_dictionary = {value:key for key, value in dictionary.items()}
    return new_dictionary

print(invert_dictionary({
    'a': 10,
    'b': 25,
    'c': 7,
    'd': 30,
    'e': 15
}))
# 3. Merge Two Dictionaries
# Write a function that merges two dictionaries into one. If keys overlap, sum their values.

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}

def merging(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key not in result:
            result[key] = value
        else:
            result[key] += value
    return result

print(merging({'a': 10, 'b': 20, 'c': 30}, {'b': 5, 'c': 15, 'd': 25} ))

merged_dicts = merging(dict1, dict2)
print(merged_dicts)

# 4. Count Occurrences
# Given a list of items, create a dictionary that counts how many times each item appears.

def count_occurrences(items):
    dictionary = {}
    for item in items:
        if item not in dictionary:
            dictionary[item] = 1
        else:
            dictionary[item] += 1
    return dictionary

print(count_occurrences(['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'kiwi', 'orange']))

# 5. Find Keys by Value
# Create a function that, given a dictionary and a value, returns a list of all keys that map to that value.

def finding_keys(dictionary, v):
    keys = []
    for key, value in dictionary.items():
        if value == v:
            keys.append(key)
    return keys

print(finding_keys({'a': 10, 'b': 20, 'c': 10, 'd': 30}, 10))

# 6. Filter Dictionary
# Given a dictionary, create a new one containing only items where the value meets a condition (e.g., value > 10).

the_dictionary = {'a': 10,
    'b': 25,
    'c': 7,
    'd': 30,
    'e': 15}

new_dict = {}

for key, value in the_dictionary.items():
    if value > 15:
        new_dict[key] = value
print(new_dict)


# 7. Dictionary Keys to List
# Write a function that takes a dictionary and returns a list of all its keys sorted alphabetically.

def sorted_function(dictionary: dict):
    list_of_keys = []
    for key in dictionary:
        list_of_keys.append(key)
    sorted_list = sorted(list_of_keys)
    return sorted_list

print(sorted_function({
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'hobbies': ['reading', 'hiking', 'coding']
}))
# 8. Dictionary with Tuple Keys
# Create a dictionary where keys are tuples, e.g., (x, y),
# and values are their sum (x + y). Generate this for all pairs (x, y) where x and y are in a list.

dict_of_tuples = {}

number_tuples = [(1, 10), (2, 20), (3, 30), (4, 40)]

for i in number_tuples:
    dict_of_tuples[i] = i[0] + i[1]

print(dict_of_tuples)



# 9. Remove Duplicates Values
# Given a dictionary, remove all key-value pairs where the value appears more than once, leaving only the first occurrence.

duplicates_dict = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 2,
    'f': 4
}

seen_values = set()
new_dict = {}

for key, value in duplicates_dict.items():
    if value not in seen_values:
        new_dict[key] = value
        seen_values.add(value)

print(new_dict)


# 10. Nested Dictionary Access
# Given a nested dictionary (a dictionary inside a dictionary),
# write a function that retrieves a value at a specific nested key path, e.g., ['key1']['key2']['key3'].

nested_dict1 = {
    'user': {
        'name': 'Alice',
        'details': {
            'age': 30,
            'location': {
                'city': 'New York',
                'country': 'USA'
            }
        }
    },
    'preferences': {
        'colors': ['red', 'blue'],
        'food': {
            'breakfast': 'pancakes',
            'lunch': 'sandwich'
        }
    }
}

def get_nested_value(nested_dict, key_path):
    current_value = nested_dict
    for key in key_path:
        current_value = current_value[key]
    return current_value

print(get_nested_value(nested_dict1, ['preferences','food', 'breakfast']))
print(get_nested_value(nested_dict1, ['user', 'details', 'age']))
