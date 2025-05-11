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

def create_dictionary(*args) -> dict:
    some_dict = {}
    for index, arg in enumerate(args):
        if isinstance(arg, (list, dict, set)):
            print(f"Cannot add {arg} to the dict!")
        else:
            some_dict[arg] = index

    return some_dict

print(create_dictionary(10, [1, 2], "hello", {'a': 1}, 3.14, set([1,2]), 2))