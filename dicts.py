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

items_categories = {
    "apple": "fruit",
    "carrot": "vegetable",
    "salmon": "fish",
    "broccoli": "vegetable",
    "banana": "fruit",
    "chicken": "meat",
    "blueberry": "fruit",
    "potato": "vegetable"
}
inverted_dict = {}

for key, value in items_categories.items():
    if value not in inverted_dict:
        inverted_dict[value] = []
    inverted_dict[value].append(key)

print(inverted_dict)

# Calculate the total value of a dictionary of items and prices by summing all the prices.

items_prices = {
    "bread": 2.50,
    "milk": 3.00,
    "eggs": 2.00,
    "cheese": 5.50,
    "apple": 0.75,
    "chicken": 8.00,
    "rice": 1.20,
    "orange juice": 3.50
}

print(sum(items_prices.values()))

# From a dictionary of country populations, find all countries where the population is over 50 million.

random_countries_population = {
    "Norway": 5378857,
    "Kenya": 53771296,
    "Portugal": 10295909,
    "Vietnam": 97338583,
    "Australia": 25687041,
    "Finland": 5540720,
    "Greece": 10715549,
    "Thailand": 69799978,
    "Latvia": 1901548,
    "Peru": 32971874
}

over_fifty = []

for key, value in random_countries_population.items():
    if value > 50000000:
        over_fifty.append(key)
print(over_fifty)


# Create a dictionary from a list of words, with the word as the key and the length of the word as the value.

cute_words = ["bunny", "kitten", "cupcake", "snuggle", "peach", "butterfly", "cloud", "daisy", "pudding", "sparkle"]

dix = {}

for word in cute_words:
    dix[word] = len(word)
print(dix)


# Given a dictionary where keys are student names and values are their scores, create a new dictionary with only students who scored below 60.

student_scores = {
    "Alice": 92,
    "Bob": 85,
    "Charlie": 78,
    "David": 88,
    "Eve": 95,
    "Frank": 55,
    "Grace": 73,
    "Helen": 81
}

diksee = {}

for key, value in student_scores.items():
    if value < 60:
        diksee[key] = value

print(diksee)


# Create a dictionary from a list of numbers where keys are the numbers and values are the number squared, but only include numbers divisible by 3.

random_numbers = [12, -5, 7, 0, 23, -14, 5.5, 8, -2, 15]

dictzzz = {}

for n in random_numbers:
    if n % 3 == 0:
        dictzzz[n] = n ** 2
print(dictzzz)


# From a dictionary of country populations, create another dictionary mapping countries to "developed" or "developing"
# based on whether their population exceeds 100 million (yes for developed, no for developing).

europe_populations = {
    "Russia": 145912025,
    "Germany": 83783942,
    "United Kingdom": 67886011,
    "France": 65273511,
    "Italy": 60461826,
    "Spain": 46754778,
    "Ukraine": 43733762,
    "Poland": 37887452,
    "Romania": 19237582,
    "Netherlands": 17134872
}

developed_developing = {}

for key, value in europe_populations.items():
    if value > 50_000_000:
        developed_developing[key] = "developed"
    else:
        developed_developing[key] = "developing"
print(developed_developing)


# Given a dictionary where keys are words and values are their definitions,
# swap keys and values to create a new dictionary. (Assume all definitions are unique).


word_definitions = {
    "apple": "A fruit that is round and typically red, green, or yellow.",
    "book": "A set of written, printed, or blank pages bound together.",
    "car": "A vehicle with four wheels used for transporting people.",
    "dog": "A domesticated carnivorous mammal that typically has a long snout.",
    "elephant": "A large mammal with a trunk native to Africa and Asia.",
    "flower": "A plant cultivated for its blooms or blossoms.",
    "guitar": "A musical instrument with strings played by plucking or strumming.",
    "hat": "A shaped covering for the head, typically with a brim.",
    "ice": "Frozen water.",
    "jungle": "A dense tropical forest."
}

swapparooni = {}

for key, value in word_definitions.items():
    swapparooni[value] = key

print(swapparooni)

