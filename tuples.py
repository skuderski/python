# Tuple Creation: Create a tuple containing the first five even numbers. Print the tuple.

# def even_numbers(numbers: tuple):
#     even = []
#     for n in numbers:
#         if n == 0:
#             continue
#         if n % 2 == 0:
#             even.append(n)
#         if len(even) == 5:
#             break
#     t = tuple(even)
#     print(type(t))
#     return t
#
# print(even_numbers((2, 5, 8, 1, 6, 9, 4, 7, 0, 3, 10, 12, 11)))

# Tuple Packing/Unpacking: Create a function that takes two numbers as input and returns them as a tuple.
# Then, unpack the tuple into two separate variables and print them.

# def tuple_unpacking(one: int, two: int):
#     the_tuple = (one, two)
#     x, y = the_tuple
#     print(x, y)
#
# tuple_unpacking(1, 5)

# Accessing Elements: Given a tuple of names, access and print the third name in the tuple.

def access_elements(names:tuple):
    return names[2]

print(access_elements(("Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace")))


# Tuple Slicing: Given a tuple of numbers,
# create a new tuple containing only the elements from the 2nd to the 5th position (inclusive).

def tuple_slicing(numbers: tuple):
    new_tuple = numbers[1:5]
    return new_tuple

print(tuple_slicing((1, 2.5, 3, 4.7, 5, 1, 6)))

# Tuple Length: Write a function that takes a tuple as input and returns its length.

def tuple_length(names: tuple):
    return len(names)

print(tuple_length(("Kenji Tanaka", "Aisha Khan", "Mateo Rodriguez", "Linh Nguyen")))
# Tuple Concatenation: Create two tuples. Concatenate them into a single tuple and print the result.

def tuple_concatenation(names: tuple, surnames: tuple):
    combined_tuples = names + surnames
    return combined_tuples

print(tuple_concatenation(("Alice", "Bob", "Charlie", "David", "Eve"), ("Smith", "Johnson", "Williams", "Brown", "Davis")))
# Tuple Repetition: Create a tuple and repeat it three times. Print the resulting tuple.

def tuple_repetition(hairstyles: tuple):
    return 3 * hairstyles

print(tuple_repetition(("messy bun", "sleek ponytail", "loose waves", "tight curls", "spiky hair")))
# Tuple Membership: Write a function that takes a tuple and a value as input.
# It should return True if the value is present in the tuple and False otherwise.

def tuple_membership(names: tuple, value: any):
    if value in names:
        return True
    else:
        return False

print(tuple_membership(("sergiusz", "vodka"), "vodka"))

# Finding the Index: Given a tuple and a value, find the index of the first occurrence of that value in the tuple.
# (Hint: Use a loop). If not present, return -1.

def find_index(names: tuple, value: any):
    for i in range(len(names)):
        if names[i] == value:
            return i
    return -1

print("the index is: " + str(find_index((1, 2, 3, 5), 1)))


# Tuple to String: Given a tuple of strings, concatenate them into a single string with spaces in between. Print the string.

def tuple_to_string(strings: tuple):
    stringinho = " ".join(strings)
    return stringinho

print(tuple_to_string(("The quick brown fox.", "Jumps over the lazy dog.", "How now, brown cow?")))
