# # Sum All Numbers:
# #
# # Write a function called sum_all that accepts any number of numerical arguments using *args.
# # The function should return the sum of all the numbers passed to it.
#
# def sum_all(*arg):
#     return sum(arg)
#
# print(sum_all(1, 2, 3, 4, 5))
#
#
# # Print Profile:
# #
# # Write a function called print_profile that accepts a name as a regular argument and any number of keyword arguments using **kwargs.
# # The function should print the name, followed by each key-value pair from the kwargs dictionary, formatted as "key: value".
#
# def print_profile(name, **kwargs):
#     print(f"Name: {name}")
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# print_profile("Sergiusz", age = 30, city = "New York")
#
# # Combine Lists:
# #
# # Write a function called combine_lists that accepts any number of list arguments using *args.
# # The function should return a new list that contains all the elements from all the input lists, concatenated together.
# # Create Dictionary:
#
# def combine_lists(*args):
#     new_list = []
#     for arg in args:
#         new_list.extend(arg)
#     return new_list
#
# print(combine_lists([1, 2, 3], [4, 5, 6]))
#
# # Write a function called create_dictionary that accepts any number of keyword arguments using **kwargs.
# # The function should return a new dictionary that contains all the key-value pairs from the kwargs dictionary, but only if the keys are strings. Skip any key-value pairs where the key is not a string.
#
# def create_dictionary(**kwargs):
#     dictio = {}
#     for key, value in kwargs.items():
#         if isinstance(key, str):
#             dictio[key] = value
#     return dictio
#
# print(create_dictionary(age = 30, city = "New York", num = 123))
#
# # Multiply with a Factor:
# # Write a function called multiply_with_factor that accepts a factor as a regular argument and any number of numerical arguments using *args.
# # The function should return a new list that contains each number from args multiplied by the factor.
#
# def multiply_with_factor(factor, *args):
#     the_list = []
#     for arg in args:
#         multi = arg * factor
#         the_list.append(multi)
#     return the_list
#
# print(multiply_with_factor(2,3, 4, 5, 6, 7, 8))
#
# # Create a function concat_strings that takes any number of string arguments and returns a single string that concatenates all of them.
#
# def concat_strings(*args):
#     concataned = " ".join(args)
#     return concataned
#
# print(concat_strings("Sergiusz", "Wiesiek", "Irena"))
#
# # Implement a function print_kwargs that takes any number of keyword arguments and prints each key and value on a new line.
# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# print_kwargs(name = "Alice", age = 30, city = "New York", is_student = False)

# Write a function greet that accepts a greeting (regular argument), a name, and other optional parameters like title, punctuation via **kwargs.
# It should return a customized greeting message.

# def greet(greeting: str, name: str, title: str, **kwargs):
#     punctuation = kwargs.get("punctuation", "!")
#     return f"{greeting} {title} {name}{punctuation}"
#
# print(greet("Hello,", "Sergiusz", "Mista", punctuation = "."))

# Create a function describe_person that accepts *args for describing traits (e.g., "kind", "brave") and
# **kwargs for personal info (name, age, etc.).
# The function should print a sentence describing the person.

def describe_person(*args, **kwargs):
    gender = kwargs.get("gender", "-")
    name = kwargs.get("name", "---")
    age = kwargs.get("age", "not given")
    traits_list = ", ".join(args) if args else "a nice person"
    return f"{name} is {age}. {gender} is {traits_list}."

print(describe_person("kind", "brave", name = "Sergiusz", gender = "He", age = 30))

# Write a function product_description that takes:
#
# Any number of product features as positional arguments (*args), like "durable", "compact", "lightweight".
# Optional details about the product using keyword arguments (**kwargs), such as name, price, brand, color.
# The function should return a descriptive string that includes the product name, price, and a list of features.

def product_description(*args, **kwargs):
    name = kwargs.get("name", "-")
    price = kwargs.get("price", "-")
    list_of_features = ", ".join(args) if args else "cool"
    return f"The {name} costs {price} and is {list_of_features}."

print(product_description("strong", "durable", name = "Iphone", price = "300 EUR"))


# Sum All Arguments:
# Write a function that accepts any number of positional arguments and returns their sum.

def summing(*args):
    return sum(args)

print(summing(2, 3, 4, 5, 6))

# 2. Print Arguments:
# Create a function that prints all positional and keyword arguments with their names and values.

def printing_args_and_kwargs(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

printing_args_and_kwargs(1, 2, 3, name='sergiusz', age = 30, surname = 'kuderski')
# 3. Count Arguments:
# Write a function that accepts any number of args and kwargs, and returns the total number of arguments passed (positional + keyword).

def count_arguments(*args, **kwargs):
    count = 0
    for arg in args:
        count += 1
    for kwargs in kwargs:
        count += 1
    return count

print(count_arguments(1, 2, 3, name='sergiusz', age = 30, surname = 'kuderski'))



# 4. Merge Dictionaries:
# Create a function that accepts any number of dictionaries as keyword arguments and merges them into one dictionary.

def merging_dictionaries(**kwargs):
    merged = {}
    for dictionary_name, dictionary in kwargs.items():
        merged.update(dictionary)
    return merged

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'a': 5, 'e': 6}

merged_dict = merging_dictionaries(first = dict1, second = dict2, third = dict3)
print(merged_dict)

# 5. Dynamic Greeting:
# Write a function that takes a greeting string (kwargs) and any number of names as positional arguments,
# then prints personalized greetings for each.

def dynamic_greeting(*args, **kwargs):
    greeting = kwargs.get('greeting', "Hello")
    for name in args:
        personalized_greeting = f"{greeting}, {name}"
        print(personalized_greeting)
dynamic_greeting("Alice", "Bob", "Sergiusz", greeting = "Hello")

# 6. Keyword Arguments Filter:
# Create a function that filters keyword arguments to only include those with string values.

def filtering(**kwargs):
    string_values = {}
    for key, value in kwargs.items():
        if isinstance(value, str):
            string_values[key] = value

    return string_values

result = filtering(name="Alice", age=30, city="New York", is_active=True)
print(result)


# 7. Argument Type Summary:
# Write a function that accepts any args and kwargs, then prints the types of each argument.

def argument_type_summary(*args, **kwargs):
    for arg in args:
        print(f"type: {type(arg)}")
    for key, value in kwargs.items():
        print(f"type: {type(value)}")
argument_type_summary(1, 2, "sergiusz", name="Alice", age=30, city="New York", is_active=True)


# 8. Repeated Arguments:
# Create a function that takes multiple args and repeats each argument n times, where n is passed as a kwarg.

def repeated_arguments(*args, n):
    repeated_list = []
    for arg in args:
        if isinstance(arg, str):
            repeated_list.extend([arg] * n)
        elif isinstance(arg, list):
            repeated_list.extend(arg * n)
        else:
            repeated_list.extend([arg] * n)
    return repeated_list

print(repeated_arguments(1, 2, 3, [1, 2, 3],  n = 3))


# 9. Arguments Reversal:
# Write a function that reverses a list of args and kwargs, and returns them as a tuple.

def arguments_reversal(*args, **kwargs):
    the_list = []
    for arg in args:
        the_list.append(arg)
    for key, value in kwargs.items():
        the_list.append((key, value))
    reversed_list = reversed(the_list)
    tuple_reversed = tuple(reversed_list)
    return tuple_reversed

print(arguments_reversal(1, 2, 3, [1, 2, 3],  n = 3, name = "sergiusz"))


# 10. Keyword Argument Summation:
# Create a function that multiplies all numerical values in kwargs and returns the total.


def keyword_summation(**kwargs):
    multiply = 1
    for key, value in kwargs.items():
        if isinstance(value, (int, float)):
            multiply *= value
    return multiply
print(keyword_summation(age = 30, fruits = 10, bottles_of_vodka = 3, name = "sergiusz"))
