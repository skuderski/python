# Check for Numeric Types:
# Write a function that takes an argument and returns True if it is an int or float, and False otherwise.

def numeric_types(argument):
    return isinstance(argument, (int, float))

print(numeric_types(22))


# Identify String or List:
# Write a program that takes an input and prints whether it is a str, list, or something else.

def identify_string_list(input):
    if isinstance(input, str):
        print("It is a string")
    elif isinstance(input, list):
        print("It is a list")
    else:
        print("It is neither a string nor a list.")

identify_string_list("Sergiusz")
identify_string_list(123)

# Determine if Object is Callable:
# Create a function that checks if an object is callable (like a function or method).

def object_is_callable(obj):
    return callable(obj)

print(object_is_callable(len))
# Validate Data Types in a List:
# Given a list of mixed types, filter and return all items that are of type dict or set.

def validate_data(mixed: list):
    dict_or_set = []
    for item in mixed:
        if isinstance(item, (dict, set)):
            dict_or_set.append(item)
    return dict_or_set

print(validate_data([42, "hello", [1, 2, 3], {'a': 1, 'b': 2}, 3.14, {1, 2, 3}, True, (4, 5, 6)]))

# Check for Boolean Values:
# Write a function that returns True if the given argument is of type bool, and False otherwise.

def boolean_values(argument):
    return isinstance(argument, bool)

print(boolean_values(True))


# Create a function that takes an object and returns a string describing its type.
# The function should check if the object is an int, float, str, list, dict, set, bool, or NoneType, and return the name of the type as a string.
# If it doesn't match any of these, return "Unknown type".

def checking(something):
    if isinstance(something, (int, float, str, list, dict, set, bool, type(None))):
        return type(something).__name__
    else:
        print("Unknown type")

print(checking(25))

# Type Check for Tuples of Numbers:
# Write a function that takes an argument and returns True if it is a tuple containing only numeric types (int or float).

def check_for_tuples(something):
    if not isinstance(something, tuple):
        return False
    return all(isinstance(item, (int, float)) for item in something)

print(check_for_tuples((25, 33)))



# Create a function that takes a list of mixed objects and returns a new list containing only the objects that are strings or booleans.

def mixed_objects(mixed: list):
    str_bool = []
    for item in mixed:
        if isinstance(item, (str, bool)):
            str_bool.append(item)

    return str_bool

print(mixed_objects([42, "hello", True, 3.14, False, "world", [], {}, 0]))


# Filter Numeric Types in a Dictionary:
# Given a dictionary with mixed value types, create a new dictionary containing only key-value pairs where the value is an int or float.

def filtering(dictionary: dict):
    new_dictionary = {}
    for key, value in dictionary.items():
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            new_dictionary[key] = value
    return new_dictionary

print(filtering({
    'age': 30,
    'name': 'Alice',
    'height': 5.7,
    'is_student': False,
    'hobbies': ['reading', 'swimming'],
    'profile': {'city': 'New York', 'zip': 10001},
    'score': None,
    'birth_year': 1990
}))