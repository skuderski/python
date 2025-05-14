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

twentytwo_thirtythree = (22, 33)

num1, num2 = twentytwo_thirtythree

print(num1)
print(num2)



# Pack three strings into a list, then unpack them into individual variables.

three_strings = ["Sergiusz", "super", "boy"]

one, two, three = three_strings

print(one)
print(two)
print(three)


# Write a function that takes three arguments, pack them into a tuple inside the function, and unpack them.

def three_ar(one, two, three):
    the_tuple = (one, two, three)
    a, b, c = the_tuple
    print(a)
    print(b)
    print(c)
three_ar(1, 2, 3)

# Pack a list of fruits into a tuple, then unpack and print each fruit separately.

list_of_fruits = ("apple", "banana", "strawberry", "kiwi", "papaya")

a, b, s, k, p = list_of_fruits

print(a)
print(b)
print(s)
print(k)
print(p)


# Use * to pass a list of numbers as individual arguments to a function that computes their sum.

def add(*args):
    return sum(args)
numbers_list = [1, 2, 5, 6, 7]
print(add(*numbers_list))

# Unpack a tuple of four elements directly into separate variables.

tuple_of_four = ("whiskey", "vodka", "i", "tequila")

w, v, i, t = tuple_of_four

print(w)
print(v)
print(i)
print(t)


# Pack key-value pairs into a dictionary, then unpack them into two variables for key and value in a loop.

sample_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

for key, value in sample_dict.items():
    print(f"The key: {key}, The fkn value: {value}")
# Create a list of tuples representing points (x, y), then loop through and unpack each point to print x and y.

points = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

for x, y in points:
    print (f"zee x: {x} and zee y: {y}")



# Pack multiple values into a single list, then unpack a subset for processing.

some_list = [333, 444, 555, 666]

first, second, *_ = some_list
print(first)
print(second)

# Write a loop that unpacks multiple lists: one containing names, another containing ages, and print each name with corresponding age.

names = ["Alice", "Bob", "Charlie", "Diana"]
ages = [25, 30, 22, 28]

dictyy = {name: age for name, age in zip(names, ages)}

print(dictyy)