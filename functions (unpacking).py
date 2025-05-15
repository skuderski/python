# (a, b, c) = (1, 2, 3)
#
# print(c)
#
# d, e, f = 4, 5, 6
#
# g, h, i = 7, 8, 9
#
# j, k, l = "123"
#
# a, b, c = [1, 2, 3]
#
# m, n, o = range(3)
#
# my_dict = {"one": 1, "two": 2, "three": 3}
#
# x, y, z = my_dict
#
# xx, qq, zz = my_dict.values()
#
# aa, bb, cc = my_dict.items()
#
# aaa, bbb, ccc = {"one", "two", "three"}
#
# mm, nn, ll = "mm", "nn", "ll"

# *a, b = 1, 2, 3
#
# *c, d, e = 1, 2, 3
#
# *f, g, h, i = 1, 2, 3
#
# *x, = range(10)
#
# arr = ["meaningful", "information", "extra", "extra", "extra", "extra"]
#
# important, info, *_ = arr
#
# my_tuple = (1, 2, 3)
#
# (0, *my_tuple, 4)
#
# numbers = {"one": 1, "two": 2, "three": 3}
#
# {**numbers, "four": 4}
#
# def unlimited_args(*args):
#     print(type(args))
#     print(args)
#
# unlimited_args(1, 5, 3, 2)
#
# def unlimited_kwargs(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#
# unlimited_kwargs(first = 1, second = 5, third = 3, fourth = 2)
#
# def add(required: int, optional: int = 0, *args, **kwargs):
#     print(required)
#     print(optional)
#     print(args)
#     print(kwargs)
#     return required + optional + sum(args) + sum(kwargs.values())
# add(1)
#
# add(1, 2)
#
# add(1, 2, 5, 6)
#
# list_to_be_added = [1, 2, 3, 4, 5]
#
# add (*list_to_be_added)

# Pack two numbers into a tuple, then unpack them into separate variables.

# twentytwo_thirtythree = (22, 33)
#
# num1, num2 = twentytwo_thirtythree
#
# print(num1)
# print(num2)
#
#
#
# # Pack three strings into a list, then unpack them into individual variables.
#
# three_strings = ["Sergiusz", "super", "boy"]
#
# one, two, three = three_strings
#
# print(one)
# print(two)
# print(three)
#
#
# # Write a function that takes three arguments, pack them into a tuple inside the function, and unpack them.
#
# def three_ar(one, two, three):
#     the_tuple = (one, two, three)
#     a, b, c = the_tuple
#     print(a)
#     print(b)
#     print(c)
# three_ar(1, 2, 3)
#
# # Pack a list of fruits into a tuple, then unpack and print each fruit separately.
#
# list_of_fruits = ("apple", "banana", "strawberry", "kiwi", "papaya")
#
# a, b, s, k, p = list_of_fruits
#
# print(a)
# print(b)
# print(s)
# print(k)
# print(p)
#
#
# # Use * to pass a list of numbers as individual arguments to a function that computes their sum.
#
# def add(*args):
#     return sum(args)
# numbers_list = [1, 2, 5, 6, 7]
# print(add(*numbers_list))
#
# # Unpack a tuple of four elements directly into separate variables.
#
# tuple_of_four = ("whiskey", "vodka", "i", "tequila")
#
# w, v, i, t = tuple_of_four
#
# print(w)
# print(v)
# print(i)
# print(t)
#
#
# # Pack key-value pairs into a dictionary, then unpack them into two variables for key and value in a loop.
#
# sample_dict = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }
#
# for key, value in sample_dict.items():
#     print(f"The key: {key}, The fkn value: {value}")
# # Create a list of tuples representing points (x, y), then loop through and unpack each point to print x and y.
#
# points = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
#
# for x, y in points:
#     print (f"zee x: {x} and zee y: {y}")
#
#
#
# # Pack multiple values into a single list, then unpack a subset for processing.
#
# some_list = [333, 444, 555, 666]
#
# first, second, *_ = some_list
# print(first)
# print(second)
#
# # Write a loop that unpacks multiple lists: one containing names, another containing ages, and print each name with corresponding age.
#
# names = ["Alice", "Bob", "Charlie", "Diana"]
# ages = [25, 30, 22, 28]
#
# dictyy = {name: age for name, age in zip(names, ages)}
#
# print(dictyy)

# Pack three variables (name, age, city) into a tuple, then unpack and print each separately.

# cool_tuple = ("name", "age", "city")
#
# n, a, c = cool_tuple
#
# print(n)
# print(a)
# print(c)
#
#
# # Create a function that takes two parameters, packs them into a list inside the function, and then unpacks and returns them.
#
# def unpacking(one, two):
#     the_list = [one, two]
#     first, second = one, two
#     return first, second
#
# print(unpacking(2, 5))
#
#
# # Given a list of tuples (name, age), unpack each tuple in a loop and print "Name is Age years old".
#
# people = [
#     ("Alice", 25),
#     ("Bob", 30),
#     ("Charlie", 22),
#     ("Diana", 28),
#     ("Ethan", 35),
#     ("Fiona", 27)
# ]
#
# for name, age in people:
#     print(f"{name} is {age} years old")
#
# # Given a list of tuples (name, age), find and print only the names of people who are 30 years old or older.
# over_30 = []
# peoples = [
#     ("Alice", 25),
#     ("Bob", 31),
#     ("Charlie", 18),
#     ("Diana", 28),
#     ("Ethan", 35),
#     ("Fiona", 27),
#     ("George", 19),
#     ("Hannah", 40)
# ]
#
# for name, age in peoples:
#     if age >= 30:
#         over_30.append(name)
# print(over_30)
#
# # Create a list of formatted strings for those 20 years old or older, including their children count, with proper string formatting.
#
# children_count = {
#     "Alice": 2,
#     "Bob": 3,
#     "Charlie": 0,
#     "Diana": 1,
#     "Ethan": 4,
#     "Fiona": 2,
#     "George": 0,
#     "Hannah": 3
# }
#
# list_of_strings = []
#
# for name, age in peoples:
#     if age >= 20:
#         children = children_count[name]
#         info_string = f"{name} is {age} years old and has {children} children"
#         list_of_strings.append(info_string)
# print(list_of_strings)

# Given a list of (name, age) tuples and a dictionary mapping name to the number of children,
# create a new list of formatted strings for only those individuals who are at least 25 years old and have more than 1 child.

# peoplez = [
#     ("Alice", 30),
#     ("Bob", 24),
#     ("Charlie", 27),
#     ("Diana", 22),
#     ("Ethan", 35),
#     ("Fiona", 29),
#     ("George", 40),
#     ("Hannah", 23)
# ]
#
# children_counter = {
#     "Alice": 2,
#     "Bob": 0,
#     "Charlie": 3,
#     "Diana": 1,
#     "Ethan": 4,
#     "Fiona": 2,
#     "George": 1,
#     "Hannah": 0
# }
# the_list = []
#
# for name, age in peoplez:
#     if age >= 25:
#         child = children_counter[name]
#         info = f"{name}({age}) has {child} children."
#         the_list.append(info)
#
# print(the_list)




# Pack a list of fruits into a tuple, then unpack each fruit one by one and print them.

# list_of_fruits = ("banana", "apple", "strawberry", "papaya")
# b, a, s, p = list_of_fruits
#
# print(b)
# print(a)
# print(s)
# print(p)

# Write a loop that unpacks each tuple and prints a sentence like:
#
# "The [fruit] is [color]."

# fruits = [("banana", "yellow"), ("apple", "red"), ("grape", "purple"), ("orange", "orange")]
#
# for fruit, color in fruits:
#     print(f"The {fruit} is {color}.")

# Write a loop that unpacks each tuple and prints out a sentence:
#
# "The [fruit] has the color [color]."
#
# But, only print this sentence if the fruit's name starts with a consonant (not a vowel).

# fruitz = [("banana", "yellow"), ("apple", "red"), ("grape", "purple"), ("orange", "orange"), ("blueberry", "blue"), ("kiwi", "green")]
#
# for fruit, color in fruitz:
#     if fruit[0].lower() not in "aeiou":
#         print(f"The {fruit} has the color {color}.")


# Given a list of tuples, each containing a fruit and its color, print sentences only for fruits that:
#
# Start with a consonant (not a vowel),
# And have more than 5 letters in their name.
# The sentence should read:
#
# "The [fruit] is [color]."


# fruits = [
#     ("banana", "yellow"),
#     ("apple", "red"),
#     ("grape", "purple"),
#     ("orange", "orange"),
#     ("blueberry", "blue"),
#     ("kiwi", "green"),
#     ("strawberry", "red"),
#     ("kiwifruit", "brown"),
#     ("mango", "yellow"),
#     ("blackberry", "black")
# ]
#
# for name, color in fruits:
#     if name[0].lower() not in "aeiou" and len(name) > 5:
#         print(f"The {name} is {color}")

# From the list of fruit tuples, print sentences only for fruits that:
#
# Start with a consonant,
# Have more than 5 letters,
# And whose color contains the letter 'r' (case-insensitive).
# The sentence should be:
#
# "The [fruit] is [color]."


# exotic_fruits = [
#     ("Dragon Fruit", "Pink"),
#     ("Rambutan", "Red"),
#     ("Durian", "Greenish-brown"),
#     ("Starfruit", "Yellow"),
#     ("Mangosteen", "Purple"),
#     ("Kiwano", "Orange"),
#     ("Lychee", "Pinkish-white"),
#     ("Longan", "Brown"),
#     ("Cherimoya", "Green"),
#     ("Jackfruit", "Green")
# ]
#
# for name, color in exotic_fruits:
#     if name[0].lower() not in "aeiou" and len(name) > 5 and "r" in color.lower():
#         print(f"The {name} is {color}")

# From the list of exotic fruits, print a sentence for each fruit that satisfies all of these conditions:
#
# The fruit does not start with a vowel.
# The name length is more than 6 characters.
# The color contains the letter 'e'.
# The fruit name contains the letter 'n' somewhere inside.
# Your goal:
# Create a loop that unpacks each tuple and prints a sentence like:
#
# "The [fruit] has the color [color], starts with a consonant, is longer than 6 characters, contains 'n', and the color contains 'e'."

# exotic_fruits2 = [
#     ("Passion Fruit", "Purple"),
#     ("Dragon Fruit", "Pink"),
#     ("Ugli Fruit", "Orange"),
#     ("Physalis", "Yellow"),
#     ("Durian", "Green"),
#     ("Kiwano", "Orange"),
#     ("Starfruit", "Yellow"),
#     ("Rambutan", "Red"),
#     ("Mangosteen", "Purple"),
#     ("Longan", "Brown")
# ]
# for name, color in exotic_fruits2:
#     name_lower = name.lower()
#     color_lower = color.lower()
#     if name_lower[0] not in "aeiou" and len(name_lower) > 6 and "e" in color_lower and "n" in name_lower:
#         print(f"The {name_lower} has the color {color_lower}, starts with a consonant, is longer than 6 characters, contains 'n' and the color contains 'e'.")
#
# # From the list of (name, color) tuples, generate a list of sentences for fruits that satisfy all these conditions:
# #
# # Start with a consonant (not a vowel),
# # Have a name length between 10 and 15 characters (inclusive),
# # Color contains the letter 'e' (case-insensitive),
# # Name contains the letter 'r' but not at the beginning** (so 'r' should be somewhere inside, but not at position 0),
# # And the color has more than 4 characters.
#
# interesting_fruits = [
#     ("Passion Fruit", "Purple"),
#     ("Kiwi", "Green"),
#     ("Dragon Fruit", "Pink"),
#     ("Rambutan", "Red"),
#     ("Starfruit", "Yellow"),
#     ("Durian", "Greenish-brown"),
#     ("Mangosteen", "Purple"),
#     ("Pomelo", "Pink"),
#     ("Longan", "Brown"),
#     ("Loquat", "Orange")
# ]
#
# for name, color in interesting_fruits:
#     name_l = name.lower()
#     color_l = color.lower()
#     if (name_l[0] not in "aeiou" and
#             10 <= len(name_l) <= 15 and
#             "e" in color_l and
#             "r" in name_l[1:] and
#             len(color_l) > 4):
#                 print(f"The fruit {name_l} has the color {color_l}, starts with a consonant, has a length between 10 and 15, contains 'r' not at start, and the color has more than 4 characters.")

# For each fruit in your list, generate a sentence only if all of the following complex conditions are met:
#
# The fruit starts with a consonant (not a vowel).
# The name contains more than 8 characters (excluding spaces).
# The color contains more than 3 vowels (a, e, i, o, u, case-insensitive).
# The name has the letter 'r' not at the start.
# The color starts with a different letter than the first letter of the name.
# The color contains at least two different vowels.
# The sentence should be:
#
# "The fruit [name] has the color [color], meets all complex conditions."

# exotic_fruits_hard = [
#     ("Passion Fruit", "Purple"),
#     ("Dragon Fruit", "Pink"),
#     ("Ugli Fruit", "Orange"),
#     ("Physalis", "Yellow"),
#     ("Durian", "Green"),
#     ("Kiwano", "Orange"),
#     ("Starfruit", "Yellow"),
#     ("Rambutan", "Red"),
#     ("Mangosteen", "Purple"),
#     ("Longan", "Brown"),
#     ("Currantbush", "Peridot")
# ]
#
# for name, color in exotic_fruits_hard:
#     name_lower = name.lower()
#     color_lower = color.lower()
#     if (name_lower[0] not in "aeiou" and
#         len(name_lower) > 8 and
#         sum(letter in "aeiou" for letter in color_lower) >= 3 and
#         "r" in name_lower[1:] and
#         color_lower[0] != name_lower[0] and
#         len(set(letter for letter in color_lower if letter in "aeiou")) >= 2):
#         print(f"The fruit {name_lower} has the color {color_lower}, meets all complex conditions.")
#

# Create a function that takes three arguments, packs them into a tuple, and then unpacks into three variables inside the function.

# def some_cool_function(one, two, three):
#     some_cool_tuple = (one, two, three)
#     a, b, c = some_cool_tuple
#     return a, b, c
#
# print(some_cool_function(1, 2, 3))
#
#
# # Pack five numbers into a list, then unpack the list into 5 separate variables and print each.
#
# fun_list = [2, 3, 6, 2, 4]
#
# a, b, c, d, e = fun_list
#
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
#
#
#
# # Given a dictionary of country-capitals, unpack only the country and print the country name.
#
# country_capitals = {
#     "United States": "Washington, D.C.",
#     "Canada": "Ottawa",
#     "France": "Paris",
#     "Germany": "Berlin",
#     "Japan": "Tokyo",
#     "Australia": "Canberra",
#     "Brazil": "Brasília",
#     "India": "New Delhi",
#     "Russia": "Moscow",
#     "South Africa": "Pretoria"
# }
#
# for key in country_capitals:
#     print(key)
#
#
# # Create a nested list structure, pack elements into inner lists, then unpack these inner lists while looping.
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# for a, b, c in matrix:
#     print(f"a: {a}, b: {b}, c: {c}")
#
#
# # Use unpacking to swap the values of two variables without using a temporary variable.
#
# a = 10
# b = 30
#
# a, b = b, a
#
# print(a)
# print(b)
#
#
# # Suppose you have three variables x, y, and z with the values 10, 20, and 30.
# # Swap x and z, but in such a way that x ends up with the original value of z, z with the original value of x, and y remains unchanged.
#
# x = 10
# y = 20
# z = 30
#
# x, y, z = z, y, x
#
# print(x)
# print(y)
# print(z)
#
# # You have four variables: a=5, b=10, c=15, d=20.
# # Swap the values such that:
# #
# # a takes the value of d
# # b takes the value of a (original)
# # c takes the value of b (original)
# # d takes the value of c (original)
# # Basically, rotate the variables' values circularly.
#
# a = 5
# b = 10
# c = 15
# d = 20
#
# a, b, c, d = b, c, d, a
#
# print(a, b, c, d)
#
#
# # Rotate their values counter-clockwise using a single unpacks-and-assigns statement, so that after the operation:
#
# p, q, r, s, t = 1, 2, 3, 4, 5
#
# p, q, r, s, t = q, r, s, t, p
#
# print(p,q,r,s,t)
#
# a, b, c, d, e, f = 1, 2, 3, 4, 5, 6
#
# a, b, c, d, e, f = c, d, e, f, a, b
#
# print(a, b, c, d, e, f)


# a, b, c, d, e, f, g, h = 1, 2, 3, 4, 5, 6, 7, 8
#
# # a takes the value of g, b takes the value of a (original), c takes the value of h, d takes the value of b (original), e takes the value of f,
# # f takes the value of c (original), g takes the value of d, h takes the value of e
#
# a, b, c, d, e, f, g, h = b, d, f, g, h, e, a, c
#
# print(a, b, c, d, e, f, g, h)

# (a, b, c, d, e, f, g, h) = (1, 2, 3, 4, 5, 6, 7, 8)
# original = (a, b, c, d, e, f, g, h)
# a, b, c, d, e, f, g, h = original[2], original[3], original[4], original[5], original[6], original[7], original[0], original[1]
#
# print(a, b, c, d, e, f, g, h)
#
#
# # Pack multiple strings into a tuple, then in a loop, unpack each string and print its length and first character.
#
# strings_tuple = ("sunshine", "butterfly", "rainbow", "whisper", "harmony")
#
# for item in strings_tuple:
#     print(f"length: {len(item)}, first character: {item[0]}")


# Create three lists (names, ages, cities) that store all names, ages, and cities extracted from a list of (name, age, city) tuples.

# people = [
#     ("Alice", 30, "New York"),
#     ("Bob", 25, "San Francisco"),
#     ("Charlie", 35, "Chicago"),
#     ("Dana", 28, "Los Angeles"),
#     ("Evan", 40, "Houston")
# ]
#
# names = []
# ages = []
# cities = []
#
# for name, age, city in people:
#     names.append(name)
#     ages.append(age)
#     cities.append(city)
#
# print(names)
# print(ages)
# print(cities)

# Given a list of (name, age, city) tuples, create three dictionaries:
#
# One mapping names to ages,
# One mapping names to cities,
# One mapping cities to list of names (i.e., grouping all names by city).

# people = [
#     ("Emma", 27, "Boston"),
#     ("Liam", 31, "Miami"),
#     ("Olivia", 24, "Seattle"),
#     ("Noah", 29, "Denver"),
#     ("Ava", 32, "Austin"),
#     ("James", 28, "San Diego"),
#     ("Mia", 26, "Atlanta"),
#     ("Lucas", 30, "Las Vegas"),
#     ("Amelia", 25, "San Francisco"),
#     ("Ethan", 33, "Chicago")
# ]
#
# name_age_dict = {name: age for name, age, city in people}
# names_to_cities = {name: city for name, age, city in people}
# cities_to_names = {city: name for name, age, city in people}
#
# print(name_age_dict)
# print(names_to_cities)
# print(cities_to_names)

# Create a dictionary that groups all the names of people by their city.
# The keys should be the city names.
# The values should be lists of all names of people who live there.
# The dictionary should include all cities, even if only one person is from that city.

# people = [
#     ("Sophia", 28, "Berlin"),
#     ("Olivia", 22, "Paris"),
#     ("Noah", 31, "New York"),
#     ("Lucas", 30, "Rome"),
#     ("Amelia", 25, "Vienna"),
#     ("Ethan", 33, "San Francisco"),
#     ("Liam", 34, "Sydney"),
#     ("James", 29, "London"),
#     ("Mia", 26, "Madrid"),
#     ("Alex", 27, "Madrid"),
#     ("Carlos", 24, "Madrid"),
#     ("Nina", 25, "Vienna"),
# ]
#
# city_groups = {}
#
# for name, age, city in people:
#     if city not in city_groups:
#         city_groups[city] = []
#
#     city_groups[city].append(name)
#
# print(city_groups)
#
# # Unpack a nested list of (name, age) tuples and create a string report:
# # Loop through the list, unpack each tuple, and construct a string like "Name is Age years old" for each person.
#
# people = [
#     ("Alice", 31),
#     ("Bob", 25),
#     ("Charlie", 35),
#     ("Diana", 28),
#     ("Ethan", 40)
# ]
#
# for name, age in people:
#     print(f"{name} is {age} years old.")
#
# # You have a list of (name, age) tuples like before. Create a single string report summarizing all the people over 30 years old, formatted as:
# #
# # "Name: [name], Age: [age]"
# over_30 = []
# for name, age in people:
#     if age > 30:
#         over_30.append(f"Name: {name}, Age: {age}")
#
# single_string = ", ".join(over_30)
# print(single_string)

# You have a list of tuples where some have 2 items, some have 3. Use unpacking to handle the first two items and the rest separately:
# Extract the first two elements, and pack the remaining into a sub-list.

list_of_tuples = [(1, 2), (3, 4, 5), (6, 7), (8, 9, 10, 11)]

for tup in list_of_tuples:
    first, second, *third = tup
    print(f"{first}, {second}, {third}")


# Suppose you have a list of tuples representing students' data, where each tuple contains:
#
# (name, age, city, grade)
# However, some tuples are missing the grade (so only (name, age, city)), while others have all four.
# Your goal:
#
# Loop through the list and unpack each tuple into four variables.
#
# Handle tuples with 3 elements by assigning a default grade of -1.
#
# For those with 4 elements, unpack all normally.
#
# Then, print a message for each student in the format:
#
# "Student [name] from [city], age [age], grade [grade]".

students = [
    ("Alice", 22, "New York", 85),
    ("Bob", 24, "Los Angeles"),
    ("Charlie", 23, "Chicago", 92),
    ("Diana", 25, "Houston"),
    ("Ethan", 21, "Phoenix", 78),
    ("Fiona", 22, "Philadelphia"),
    ("George", 24, "San Diego", 88),
    ("Hannah", 23, "Dallas")
]

for student in students:
    if len(student) == 3:
        name, age, city = student
        grade = -1
    else:
        name, age, city, grade = student
    print(f"Student {name} from {city}, age {age}, grade {grade}")

# You have a list of tuples representing employee data, where each tuple contains:
#
# (name, department, salary, years_of_service)
# However, some entries might be missing years_of_service (they only have (name, department, salary)).
#
# Your goal:
#
# Loop through the list.
#
# Unpack the data, setting years_of_service to 0 if missing.
#
# Then, print a report like:
#
# "Employee [name] works in [department], earns $[salary], and has [years_of_service] years of service."

employees = [
    ("Alice", "HR", 60000, 5),
    ("Bob", "Finance", 70000),
    ("Charlie", "IT", 65000, 3),
    ("Diana", "Marketing", 55000),
    ("Ethan", "Finance", 72000, 7),
    ("Fiona", "HR", 58000),
    ("George", "IT", 67000, 2),
    ("Hannah", "Marketing", 53000),
]

for employee in employees:
    if len(employee) == 3:
        name, department, salary = employee
        years_of_service = 0
    else:
        name, department, salary, years_of_service = employee
    print(f"Employee {name} works in {department}, earns ${salary}, and has {years_of_service} years of service.")

# Unpack a tuple with multiple elements, swap first and last elements:
# Given (a, b, c, d), swap the first and last elements in one line.
a = 1
b = 2
c = 3
d = 4

(a, b, c, d) = d, b, c, a

print(a, b, c, d)

# Unpack a list of (name, grades) tuples and separate students with passing and failing grades:
# Unpack each tuple, and generate two lists: one for students with grades >= 60 and another for the rest.

students = [
    ("Alice", 88),
    ("Bob", 45),
    ("Charlie", 52),
    ("Diana", 85),
    ("Ethan", 59),
    ("Fiona", 78),
    ("George", 83),
    ("Hannah", 91)
]

passing_list = []
failing_list = []

for name, grade in students:
    if grade >= 60:
        passing_list.append((name, grade))
    else:
        failing_list.append((name, grade))

print(passing_list)
print(failing_list)

# Unpack a list of (product, price, quantity) tuples and sum total value:
# Loop through, unpack, and calculate price * quantity for each, summing the total.

products = [
    ("Laptop", 999.99, 10),
    ("Smartphone", 699.99, 25),
    ("Headphones", 199.99, 50),
    ("Monitor", 299.99, 15),
    ("Keyboard", 89.99, 40),
    ("Mouse", 49.99, 60),
    ("Printer", 149.99, 8),
    ("Webcam", 59.99, 20),
    ("External Hard Drive", 119.99, 12),
    ("Router", 89.99, 18)
]
total_price = 0
for product, price, quantity in products:
    total = price * quantity
    total_price += total
    print(f"The total of {product} is {total}.")
print(f"The total price is {total_price}")

#  Unpack a list of (x, y, z) points and compute the centroid:
# Calculate the centroid (average_x, average_y, average_z) by unpacking each point.

points = [
    (2, 4, 6),
    (3, 6, 9),
    (4, 8, 12),
    (5, 10, 15),
    (6, 12, 18)
]


total_x = 0
total_y = 0
total_z = 0

for x, y, z in points:
        total_x += x
        total_y += y
        total_z += z

average_x = total_x / len(points)
average_y = total_y / len(points)
average_z = total_z / len(points)

print(average_x)
print(average_y)
print(average_z)

# Given a list of (name, age, country) tuples, unpack and group these into a dictionary grouped by country:
# Create a dictionary where each key is a country, and each value is a list of names.

people = [
    ("Alice", 30, "USA"),
    ("Bob", 25, "Canada"),
    ("Charlie", 35, "UK"),
    ("Diana", 28, "Australia"),
    ("Ethan", 40, "India"),
    ("Fiona", 27, "Germany"),
    ("George", 33, "France"),
    ("Hannah", 31, "USA")
]

country_names = {}
for name, age, country in people:
    if country not in country_names:
        country_names[country] = []

    country_names[country].append(name)

print(country_names)
# Unpack a list of (date_string, temperature) tuples, convert date strings to datetime objects, and generate a list of (datetime, temperature) pairs.
#
from datetime import datetime
weather_data = [
    ("2023-07-01", 85),
    ("2023-07-02", 88),
    ("2023-07-03", 90),
    ("2023-07-04", 87),
    ("2023-07-05", 86),
    ("2023-07-06", 89),
    ("2023-07-07", 90),
    ("2023-07-08", 88),
    ("2023-07-09", 87),
    ("2023-07-10", 86)
]
some_f_list = []
for date_string, temperature in weather_data:
    date_obj = datetime.strptime(date_string, "%Y-%m-%d")
    some_f_list.append((date_obj, temperature))
print(some_f_list)

# Swap two variables with a tuple unpacking, then re-unpack from a tuple with multiple values:
# Define x, y, z = 1, 2, 3, then swap x and z in one line, and verify the new order.

x, y, z = 1, 2, 3
x, y, z = z, y, x
print((x, y, z))