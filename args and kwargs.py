# Sum All Numbers:
#
# Write a function called sum_all that accepts any number of numerical arguments using *args.
# The function should return the sum of all the numbers passed to it.

def sum_all(*arg):
    return sum(arg)

print(sum_all(1, 2, 3, 4, 5))


# Print Profile:
#
# Write a function called print_profile that accepts a name as a regular argument and any number of keyword arguments using **kwargs.
# The function should print the name, followed by each key-value pair from the kwargs dictionary, formatted as "key: value".

def print_profile(name, **kwargs):
    print(f"Name: {name}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_profile("Sergiusz", age = 30, city = "New York")

# Combine Lists:
#
# Write a function called combine_lists that accepts any number of list arguments using *args.
# The function should return a new list that contains all the elements from all the input lists, concatenated together.
# Create Dictionary:

def combine_lists(*args):
    new_list = []
    for arg in args:
        new_list.extend(arg)
    return new_list

print(combine_lists([1, 2, 3], [4, 5, 6]))

# Write a function called create_dictionary that accepts any number of keyword arguments using **kwargs.
# The function should return a new dictionary that contains all the key-value pairs from the kwargs dictionary, but only if the keys are strings. Skip any key-value pairs where the key is not a string.

def create_dictionary(**kwargs):
    dictio = {}
    for key, value in kwargs.items():
        if isinstance(key, str):
            dictio[key] = value
    return dictio

print(create_dictionary(age = 30, city = "New York", num = 123))

# Multiply with a Factor:
# Write a function called multiply_with_factor that accepts a factor as a regular argument and any number of numerical arguments using *args.
# The function should return a new list that contains each number from args multiplied by the factor.

def multiply_with_factor(factor, *args):
    the_list = []
    for arg in args:
        multi = arg * factor
        the_list.append(multi)
    return the_list

print(multiply_with_factor(2,3, 4, 5, 6, 7, 8))