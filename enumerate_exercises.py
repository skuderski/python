# # Print List with Indices: Given a list of names, print each name along with its index in the list, starting the index at 1.
#
# def list_with_indices(names: list) -> None:
#     for i, name in enumerate(names, start = 1):
#         print(f"Index: {i}, Value: {name}")
# list_with_indices(["banana", "apple", "strawberry"])
#
#
# # Find Even Indexed Elements: Given a list of numbers, create a new list containing only the elements that have an even index.
#
# numbers = [2, 3, 5, 7, 11, 13]
# even_numbers = []
# for index, number in enumerate(numbers):
#     if index % 2 == 0:
#         even_numbers.append(number)
# print(even_numbers)
#
# # Modify Every Other Element: Given a list of strings, convert every other string to uppercase, starting with the element at index 0.
#
# words = ["apple", "banana", "cherry", "date", "fig", "watermelon"]
# converted_words = []
# for index, word in enumerate(words):
#     if index % 2 == 0:
#         converted_words.append(word.upper())
#     else:
#         converted_words.append(word)
# print(converted_words)

# Create a Dictionary from a List: Given a list of words,
# create a dictionary where the keys are the words and the values are their corresponding indices in the list.

# colors = ["red", "green", "blue", "yellow", "purple", "orange", "black", "white", "gray", "brown"]
# number_of_colors = {}
# for index, color in enumerate(colors):
#     number_of_colors[color] = index
#
# print(number_of_colors)

# Create a Dictionary of Reversed Words: Given a list of words,
# create a dictionary where the keys are the original words and the values are the reversed versions of those words.

# word_list = ["apple", "ocean", "mountain", "friendship", "courage", "harmony", "brilliant", "tranquility"]
#
# reversed_words = {}
#
#
# for index, word in enumerate(word_list):
#     reversed_words[word] = word[::-1]
#
# print(reversed_words)


# Print String with Character Positions: Given a string, print each character along with its position in the string.

# long_word = "supercalifragilisticexpialidocious"
# for index, c in enumerate(long_word):
#     print(f"{c}:{index}")

# Find the First Occurrence: Given a list of numbers and a target value,
# find the index of the first occurrence of the target value in the list.
# Return -1 if the target value is not found. (Use enumerate for this).

def first_occurance(numbers: list, target: int):
    for index, number in enumerate(numbers):
        if number == target:
            return index
    return -1
print(first_occurance([1, 10, 5, 22, 3, 8, 15, 42], 22))


# Print a Numbered Menu: Given a list of menu options, print a numbered menu to the console, starting the numbering at 1.

menu = ["Grilled Salmon with Roasted Vegetables", "Steak Frites", "Chicken Parmesan", "Vegetarian Pasta Primavera", "Mushroom Risotto"]

for index, item in enumerate(menu, start = 1):
    print(f"{index}:{item}")


# Reverse a List (with indices): Create a new list that is the reverse of the original list,
# but use enumerate to create the reversed list. Do not use the built in reverse or reversed functions

my_list = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
reversed_list = []
for index, item in enumerate(my_list):
    reversed_list.insert(0, item)
print(reversed_list)


# Conditional Modification: Given a list of numbers, multiply every even number by its index, but only if the index is also even.

nums = [8, 23, 97, 4, 52, 16, 71, 39, 6, 88]
for index, n in enumerate(nums):
    if n % 2 == 0 and index % 2 == 0:
        multi = n * index
        print(multi)

# Process Data with Skip: Given a list of data items, process every third item (starting with the first item) and print its index and value.
# Use enumerate and the modulo operator (%) to achieve this.

data_list = [10, 3.14,"Hello, world!", True, None, [1, 2, 3], {"name": "Alice", "age": 30}, (4, 5, 6), {7, 8, 9}]

for index, data in enumerate(data_list):
    if index % 3 == 0:
        print(f"{index}:{data}")

