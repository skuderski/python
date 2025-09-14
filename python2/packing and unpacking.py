# a, b, c = "123"
# a, b, c = [1, 2, 3]
# d, e, f = range(3)
#
# my = {"one": 1, "two": 2, "three": 3}
# x, y, z = my
# j, k, l = my.values()
# m, n, o = my.items()
#
# one, two, three = {"one", "two", "three"}
#
# a, b = b, a
#
# *a, b = 1, 2, 3
#
# *a, b, c, d = 1, 2, 3
#
# *a, = range(10)

# Create a tuple with three elements and unpack it into three separate variables.

a, b, c = (1, 2, 3)

# Create a tuple containing the names of three fruits (e.g., "apple", "banana", "cherry").
# Unpack this tuple into three separate variables and print each variable.

x, y, z = ("apple", "banana", "cherry")
print(x)
print(y)
print(z)

# Pack four variables into a tuple and then unpack them into four different variables.
e = 10
f = 20
g = 30
h = 40
packed_tuple = e, f, g, h
(x, y, z, k) = packed_tuple
print(x, y, z, k)

# Create four variables with any values you like. Pack them into a tuple.
# Then, unpack that tuple into four different variables and print each one to verify.

one = 100
two = 200
three = 300
four = 400
packed = (one, two, three, four)
q, w, e, r = packed
print(q)
print(w)
print(e)
print(r)

# Given a list [10, 20, 30, 40], unpack its elements into individual variables.

the_list = [10, 20, 30, 40]
aa, bb, cc, dd = the_list
print(aa, bb, cc, dd)

# Given a list ['red', 'green', 'blue'], unpack its elements into three separate variables and print each one.

colours = ["red", "green", "blue"]
r, g, b = colours
print(r, g, b)


# Create a function that takes three parameters, packs them into a tuple, and returns the tuple. Then unpack the returned tuple.

def packing(one, two, three) -> tuple:
    packed = one, two, three
    return packed

result = packing(10, 20, 30)
a, b, c = result
print(a, b, c)

# Create a function that takes four parameters, packs them into a tuple, and returns that tuple.
# Then, call the function with four values and unpack the returned tuple into four separate variables, printing each one.

def packing_one(one, two, three, four):
    packed = one, two, three, four
    return packed
the_result = packing_one(100, 2, 3, 4)
a, b, c, d = the_result
print(a, b, c, d)

# Swap two variables using tuple unpacking.
dd = 100
ee = 200
dd, ee = ee, dd
print(dd)
print(ee)

# Create three variables with different values. Swap the values of the first and third variables using tuple unpacking,
# and then swap the second and third variables. Afterward, print all three variables to see their final values.

aaa = 100
bbb = 200
ccc = 300

aaa, bbb, ccc = ccc, bbb, aaa
print(aaa, bbb, ccc)
aaa, bbb, ccc = aaa, ccc, bbb
print(aaa, bbb, ccc)

# Unpack a tuple (3, 5, 7, 9) into two variables, assuming one gets the first two elements and the other gets the last two.


t = (3, 5, 7, 9)
first_two, last_two = t[:2], t[2:]
print(first_two, last_two)

# Given a tuple with six elements (10, 20, 30, 40, 50, 60),
# unpack it into two variables where the first variable contains the first three elements, and the second variable contains the last three elements.


s = (10, 20, 30, 40, 50, 60)
first_three, second_three = s[:3], s[3:]
print(first_three, second_three)

# Given two tuples (1, 2) and (3, 4), pack them into a single tuple and then unpack all four numbers into individual variables.

one1 = (1, 2)
two2 = (3, 4)
three1 = (one1 + two2)
print(three1)
a, b, c, d = three1
print(a, b, c, d)

# Given two tuples (5, 6, 7) and (8, 9, 10),
# pack them into a single tuple and then unpack all six numbers into six separate variables. Then, print each variable.

lolo = (5, 6, 7)
lol = (8, 9, 10)
xd = (lolo + lol)
a, b, c, d, e, f = xd
print(a, b, c, d, e, f)


# Create a nested tuple, and unpack it into separate variables, including unpacking the nested tuple.

nest = (1, 2, (3, 4))
a, b, (e, f) = nest
print(a, b, e, f)

# Create a nested tuple like (10, (20, 30), 40), and unpack it into three variables,
# where the middle variable unpacks the inner tuple into two separate variables. Then, print all three variables.

nested_t = (10, (20, 30), 40)
a, b, c = nested_t
print(a, b, c)

# Use tuple unpacking to swap the values of two variables, and print the result before and after.

x = 99
y = 88
print(x, y)
x, y = y, x
print(x, y)


# Create three variables with different values. Use tuple unpacking to rotate the values so that each variable takes on the value of the next,
# with the last wrapping around to the first. Print the variables before and after the rotation.


a = 2
b = 3
c = 4
print(a, b, c)
a, b, c = b, c, a
print(a, b, c)

# *Unpack a tuple with a special kwargs style, where the last element is a list, into a fixed part and the list. (Hint: use extended unpacking with *)

matrix = (1, 2, 3, [1, 2])

a, b, c, *d = matrix
print(a, b, c, d)

# Given a tuple like (10, 20, 30, ['a', 'b', 'c']),
# use extended unpacking to assign the first three values to individual variables and the list to another variable, then print all of them.

xxxx = (10, 20, 30, ["a", "b", "c"])
a, b, c, d = xxxx
print(a, b, c, d)

my_tuple = (1, 2, 3)
print((0, *my_tuple, 4))

numbers = {"one": 1, "two": 2}
print({**numbers, "three": 3})

def unlimited_args(*args):
    print(type(args))
    print(args)
    return args
print(unlimited_args(1, 2, 3, "s", [1, 2, 3]))

def unlimited_kwargs(**kwargs):
    print(type(kwargs))
    print(kwargs)
    return kwargs

print(unlimited_kwargs(first=1, second=2, third=3))

def add(required: int, optional: int = 0, *args, **kwargs):
    print(required)
    print(optional)
    print(args)
    print(kwargs)
    return required + optional + sum(args) + sum(kwargs.values())

print(add(1, 2, 3, 3, 4, first = 1))
print(add(1))

list_to_add = [1, 2, 3, 4, 5]
add(*list_to_add)

# Pack three strings into a tuple and print the tuple.

strings_t = ("Sergiusz", "Kuderski", "kocha")
print(strings_t)

# Create a function that takes three string arguments (such as first name, last name, and city),
# pack them into a tuple, and then return that tuple. Call the function with your own data and print the resulting tuple.

def tupling(name, last_name, city):
    the_tuple = (name, last_name, city)
    return the_tuple

print(tupling("Sergiusz", "Kuderski", "Athens"))

# Create a function that takes four arguments: a persons first name, last name, birth year, and city of residence.
# Pack all four into a tuple, then return and print the tuple when calling the function with your own data.)


def tuppling2(name, last_name, birth_year, city):
    the_tuple = (name, last_name, birth_year, city)
    return the_tuple

print(tuppling2("Sergiusz", "Kuderski", 1994, "Athens"))

# Create a function that takes any number of string arguments (representing, for example, a person details like name, occupation, city, etc.),
# packs all of them into a single tuple using *args, and then returns that tuple. Call the function with five or more arguments and print the result.


def something(*args):
    return args

print(something("Sergiusz", "Kuderski", 31, "Athens"))

# Create a function that accepts a variable number of numerical arguments using *args. Inside the function,
# calculate the sum and average of all the arguments, and return both as a tuple.
# Call the function with five or more numbers and print the results.

def som(*args):
    the_sum = sum(args)
    the_average = the_sum / len(args)
    the_t = (f"The sum is: {the_sum}, The average: {the_average}")
    return the_t

print(som(1, 5, 6, 7, 8, 111))

# Create a list of the first ten even numbers and pack it into a single variable.

even_nums = [i for i in range(2, 21, 2)]
print(even_nums)

# Create a list of the first ten odd numbers, then pack this list into a variable.
# Next, generate a new list that contains the squares of these odd numbers, and pack that into another variable. Finally, print both packed lists.

odd_nums = [i for i in range(1, 20, 2)]
squares = [i ** 2 for i in odd_nums]
print(odd_nums, squares)



# Pack different data types (int, float, string, list) into a tuple and print it.

variety_in_tuple = (12, 12.5, "Sergiusz", [1, 2, 3, 4, 5])
print(variety_in_tuple)

# Create a tuple that contains a mix of data types: an integer, a float, a string, a list, and a dictionary.
# Pack them into a single tuple, then unpack the tuple into separate variables and print each variable separately.

another_tuple = (11, 12.10, "Sergiusz", [1, 2, 3], {"one": 1, "two": 2})
a, b, c, d, e = another_tuple
print(a)
print(b)
print(c)
print(d)
print(e)

# Create a tuple containing various data types: an integer, a float, a string, a list, and a nested tuple (which itself contains multiple elements).
# Pack all of these into a single tuple. Then, unpack the outer tuple into separate variables,
# and further unpack the nested tuple into individual variables. Finally, print all the unpacked variables separately.

some_t = (1, 100.25, "Kuderski", [1, 2, 3, 4, 5], (1, 2, 3, 4))
x, y, q, w, (l, o, ll, ii) = some_t
print(x)
print(y)
print(q)
print(w)
print(l)
print(o)
print(ll)
print(ii)


# Create multiple variables (e.g., name, age, height) and pack them into a tuple. Then unpack and print each.

multi = ("Sergiusz", "Kuderski", 179)
name, surname, height = multi
print(name)
print(surname)
print(height)

# Create a tuple that contains five different variables:
# a name (string), age (integer), height (float), hobbies (list), and score (float). Pack all these variables into a tuple.
# Then, unpack the tuple into individual variables, including unpacking the hobbies list into separate variables
# (for example, first hobby, second hobby). Finally, print all variables separately.


somq = ("Sergiusz", 31, 179.2, ["programming", "anti-aging", "sport", "psychology"], 32.15)
a, b, c, (first, second, third, fourth), d = somq
print(a)
print(b)
print(c)
print(first)
print(second)
print(third)
print(fourth)
print(d)



# Pack five numbers into a list, then convert the list into a tuple.
#
# Create a tuple containing a person's info: name, age, and list of hobbies. Pack all these elements into a single tuple.
#
# Pack key-value pairs into a dictionary using the dict() constructor with tuples.
#
# Create a nested list/tuple structure and pack it into a single variable, then access nested elements.
#
# Pack two tuples (a, b) and (c, d) into a list, then access each tuple separately after unpacking.
#
# Create a function that takes three parameters, packs them into a tuple, and returns the tuple.
# Call the function with different arguments and print the returned tuple.