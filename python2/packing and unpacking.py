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

some_lst =[1, 2, 3, 4, 5]
tuple_list = tuple(some_lst)
print(tuple_list)
print(type(tuple_list))

# Create a list containing the squares of numbers from 1 to 10.
# Then, convert this list into a tuple, and finally, unpack the tuple to print each squared number individually.

sqrs = [n ** 2 for n in range(1, 11)]
sqrs_t = tuple(sqrs)
for i in sqrs_t:
    print(i)

# Create a tuple containing a person's info: name, age, and list of hobbies. Pack all these elements into a single tuple.


person_info = ("Sergiusz", "Kuderski", ["programming", "cooking", "sport"])
print(person_info)

# Create a tuple that contains a products name (string), price (float), and a list of categories (list of strings).
# Pack all these elements into a single tuple. Then, unpack the tuple into individual variables and print each one separately.)

product = ("Pasta", 125.50, ["spaghetti", "penne", "tagliatelle"])
a, b, c = product
print(a)
print(b)
print(c)

# Create a tuple that contains a cars model (string), the manufacturing year (integer), and a list of features (list of strings). Pack all these elements into a single tuple. '
# Then, unpack the tuple into individual variables, including unpacking the list of features into separate variables, and print each one separately.)

cars = ("BMW", 1999, ["fast", "durable", "economic"])
a, b, [c, d, e] = cars
print(a)
print(b)
print(c)
print(d)
print(e)

# Pack key-value pairs into a dictionary using the dict() constructor with tuples.

one = "one"
two = "two"
three = "three"

pairs = [(one, 1), (two, 2), (three, 3)]
dicas = dict(pairs)

print(dicas)

# Create a list of tuples, where each tuple contains a country name (string) and its population (integer).
# Use the dict() constructor to convert this list into a dictionary. Then, print the resulting dictionary.

countries = [("Poland", 20000), ("Greece", 211000), ("Spain", 2121111)]
countries_dic = dict(countries)
print(countries_dic)

# Create a list of tuples, where each tuple contains a student name (string) and their grade (float).
# Use the dict() constructor to convert this list into a dictionary,
# then update the dictionary with a new student name and grade. Finally, print the updated dictionary.

the_ts = [("Sergiusz", 90.50), ("Inga", 22.40), ("Martyna", 50.50)]
converted = dict(the_ts)
converted["Irena"] = 99.50
print(converted)

# Create a list of tuples, where each tuple contains an employee’s name (string) and their salary (float).
# Convert this list into a dictionary, then increase every salary by 10%. Finally, print the updated dictionary with all salaries increased.

salaries = [("Sergiusz", 10000), ("Irena", 20000), ("Wiesiek", 11111)]
updated = [(name, salary * 1.10) for name, salary in salaries]
dict_upd = dict(updated)
print(dict_upd)

# Create a list of tuples, where each tuple contains a product name (string) and its price (float).
# Convert this list into a dictionary, then increase all prices by 15%. Finally, print the updated dictionary with the new prices.

producto = [("car", 100.50), ("water", 1.20)]
product_d = dict(producto)
updated_product = {p: v * 1.15 for p, v in producto}
print(updated_product)


# Create a nested list/tuple structure and pack it into a single variable, then access nested elements.

nested_tuple = (1, 2, 3, (4, 5, 6), 7)
aa, bb, cc, (dd, ee, ff), gg = nested_tuple
print(aa)
print(bb)
print(cc)
print(dd)
print(ee)
print(ff)
print(gg)

# Create a nested list structure that includes various data types, such as an integer, a string, and a nested list of floats.
# Pack all of these into a single variable. Then, unpack the outer list into individual variables,
# including unpacking the nested list into separate variables, and print all of them separately.

nested_list = [12, "Sergiusz", [1.50, 2.22, 3.33]]
aaa, bbb, [ccc, ddd, eee] = nested_list
print(aaa)
print(bbb)
print(ccc)
print(ddd)
print(eee)

# Create a nested list that contains an integer, a string, and a nested list of dictionaries. Pack all of these into a single variable.
# Then, unpack the outer list into individual variables,
# including unpacking the nested list of dictionaries into separate variables. Finally, print all the unpacked variables separately.

mested = [123, "Kuderski", [{"one": 1, "two": 2, "three": 3}, {"city": "Athens", "population": 30000000}]]
xxx, yyy, [a, b] = mested
print(xxx)
print(yyy)
print(a)
print(b)

# Pack two tuples (a, b) and (c, d) into a list, then access each tuple separately after unpacking.
# a = 2
# b = 4
# c = 6
# d = 8
# the_lista = [(a, b), (c, d)]
# a, b = the_lista[0]
# c, d = the_lista[1]
# print(a)
# print(b)
# print(c)
# print(d)

# Create a list containing three tuples, each tuple with two elements: a string and an integer.
# Then, unpack the list into three tuples, and each tuple into separate variables. Finally, print all the variables individually.


list_of_three = [(1, 2), "Sergiusz", 4]
t1, t2, t3 = list_of_three
a, b = t1
c = t2
d = t3
print(a)
print(b)
print(c)
print(d)

# Create a function that takes three parameters, packs them into a tuple, and returns the tuple.

def three(one, two, three):
    the_tuple = (one, two, three)
    return the_tuple

print(three("sergiusz", "kuderski", "jestem"))

# Create a function that takes any number of string arguments using *args. Inside the function, pack all arguments into a tuple,
# then add a greeting message as a new element at the beginning of the tuple.
# Return the new tuple and print it when calling the function with multiple string arguments.

def arguments(*args):
    greeting = ("Hello,",)
    new_t = greeting + args
    return new_t

print(arguments("Sergiusz", "Michalina"))

# Create a function that accepts any number of string arguments (using *args).
# Inside the function, create a new list that starts with a greeting message "Hello," followed by all the input arguments.
# Convert this list into a tuple and return it. Call the function with several names and print the resulting tuple.

def arggg(*args):
    greeting = ["Hello"]
    combined = greeting + list(args)
    the_t = tuple(combined)
    return the_t
print(arggg("Sergiusz", "Martyna"))

# Create a function that accepts any number of integer arguments using *args. Inside the function,
# create a list starting with the string "Numbers" followed by all the input arguments.
# Convert this list into a tuple and return it. Call the function with several numbers and print the resulting tuple.

def any_n(*args):
    nums = ["Numbers"]
    combo = nums + list(args)
    the_t = tuple(combo)
    return the_t

print(any_n(1, 2, 3, 4, 5))

# Create a function that accepts any number of float arguments using *args.
# Inside the function, create a list starting with the string "Values" followed by all the input arguments multiplied by 10.
# Convert this list into a tuple and then into a set (to remove duplicates).
# Return the set. Call the function with multiple floating-point numbers and print the resulting set.

def any_floats(*args):
    values = ["Values"]
    inputargs = [arg * 10 for arg in args]
    combo = values + inputargs
    the_t = tuple(combo)
    the_set = set(the_t)
    return the_set

print(any_floats(1.20, 1.30, 4.50, 100.22))

# Call the function with different arguments and print the returned tuple.

def different(*args):
    t = args
    return t

print(different("sergiusz", 20, "wodka"))

# Create a function that accepts any number of arguments of mixed data types.
# Inside the function, pack all arguments into a tuple, then create a list that contains only the string arguments from the tuple.
# Return the list. Call the function with multiple arguments of different types and print the resulting list.

def anyy(*args):
    t = args
    ls = []
    for i in t:
        if isinstance(i, str):
            ls.append(i)
    return ls
print(anyy("sergiusz", 20, 20.50, "kuderski", {2, 3, 4}))

# Create a function that accepts any number of arguments, which can be of mixed data types. Inside the function:
#
# Pack all the arguments into a tuple.
# Create and return a list containing only the numerical arguments (integers and floats) multiplied by 2.
# If an argument is a number, include its doubled value; ignore other data types.
# Call the function with multiple arguments, including numbers, strings, lists, etc., and print the resulting list.

def anything(one, two, three, four):
    tu = (one, two, three, four)
    ls = [i * 2 for i in tu if isinstance(i, (int, float))]
    return ls

print(anything(1, 2, "sergiusz", 10.10))

# Create a function that takes any number of arguments of mixed data types. The function should:
#
# Pack all arguments into a tuple.
# Create and return a list containing only the non-string arguments, but each value multiplied by 3.
# Skip any arguments that are strings.
# Call the function with various types of arguments (numbers, strings, lists, etc.) and print the resulting list.

def anysink(*args):
    ls = [i * 3 for i in args if isinstance(i, (list, tuple, float, int))]
    return ls

print(anysink(1, 2, 3, [4, 5], "sergiusz", {12, 15, 19}, (1, 2, 3)))

# Pack three integers into a tuple and then unpack them into separate variables. Print each variable.

some_t = (1, 100, 200)
a, b, c = some_t
print(a)
print(b)
print(c)

# Create a function that takes three integers as parameters, packs them into a tuple,
# and then unpacks the tuple into three separate variables within the function.
# Inside the function, modify one of the variables (e.g., increment it),
# and then return all three variables separately. Call the function and print each returned value.

def pax(one, two, three):
    t = (one, two, three)
    a, b, c = t
    a += 1
    return a, b, c
print(pax(10, 20, 30))

# Create a function that accepts four arguments, packs them into a tuple, unpacks the tuple into four separate variables within the function,
# increases each numerical value by 5,
# and then returns the updated values as separate variables. Call the function with four numbers and print each returned value.

def paxx(one, two, three, four):
    tup = (one, two, three, four)
    a, b, c, d = tup
    a += 5
    b += 5
    c += 5
    d += 5
    return a, b, c, d

print(paxx(1, 2, 3, 4))

# Create a function that accepts five parameters. Pack them into a tuple,
# then unpack the tuple into individual variables inside the function.
# For each variable that is a number (int or float), multiply it by 10. For any non-numeric variables, leave them unchanged.
# Return all five variables after processing. Call the function with five arguments of mixed types and print the results.

def paxxx(one, two, three, four, five):
    tz = (one, two, three, four, five)
    a, b, c, d, e = tz
    result = []
    for i in (a, b, c, d, e):
        if isinstance(i, (int, float)):
            result.append(i * 10)
        else:
            result.append(i)
    return tuple(result)

print(paxxx(1, 2, 3, 4, "sergiusz"))

# Create a list with five elements of your choice, then unpack it into individual variables.

some_list = [1, 2, 3, 4, 5]
a, b, c, d, e = some_list
print(c)

# Given a list of 7 elements, unpack the first three elements into individual variables,
# pack the remaining four elements into a separate list or tuple, and then print all the variables separately.

ls = [1, 2, 3, 4, 5, 6, 7]
a, b, c, *d = ls
print(a)
print(b)
print(c)
print(d)

# Given a list with 10 elements, unpack the first four elements into individual variables,
# pack the next three elements into a tuple, and store the remaining three elements in a separate list. Then, print all the variables separately.

ls11 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a, b, c, d, e, f, g, *h = ls11
mid = (e, f, g)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(h)
print(mid)

# Given a list with 12 elements, unpack the first three elements into individual variables,
# the next five elements into a tuple, and collect the remaining four elements into a list. Then, print all these variables separately.

ls2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
a, b, c, d, e, f, g, h, *i = ls2
middle = (d, e, f, g, h)
print(a)
print(b)
print(c)
print(middle)
print(i)


# Given a tuple with three elements, unpack it into variables and swap the first and last variables using tuple unpacking.

the_t = (1, 2, 3)
a, b, c = the_t
a, b, c = c, b, a
print(a)
print(b)
print(c)

# Given a tuple with four elements, unpack it into four variables,
# then rotate the values so that the second becomes the first, the third becomes the second,
# the fourth becomes the third, and the first moves to the last position. Print all four variables after the rotation.

ms = (1, 2, 3, 4)
q, w, e, r = ms
q, w, e, r = w, e, r, q
print(q)
print(w)
print(e)
print(r)

# Given a tuple with five elements, unpack it into five variables, then rotate the values so that the third becomes the first,
# the fourth becomes the second,
# the fifth becomes the third, the first becomes the fourth, and the second becomes the fifth. Print all five variables after the rotation.

maas = (1, 2, 3, 4, 5)
x, y, z, w, l = maas
x, y, z, w, l = z, w, l, x, y
print(x)
print(y)
print(z)
print(w)
print(l)


# Create a nested list with two lists inside, pack it into a variable, and unpack the outer list and the inner lists into separate variables.

nested2 = [[1, 2, 3], [4, 5, 6]]
a, b = nested2
print(a)
print(b)

# Given a list containing three tuples,
# unpack the list into three variables, then unpack each tuple into individual variables, and print all the individual variables.

nested22 = [(1, 2), (3, 4), (5, 6)]
xx, yy, zz = nested22
x, p = xx
y, z = yy
l, o = zz
print(x)
print(p)
print(y)
print(z)
print(l)
print(o)
# Given a list of four tuples, where each tuple contains three elements, unpack the list into four variables.
# Then, unpack each tuple into three individual variables, and finally, combine all these variables into a single list. Print the final list.

sdad1 = [(1, 2, 3), (3, 4, 5), (5, 6, 7), (7, 8, 9)]
aaa, bbb, ccc, ddd = sdad1
a, b, c = aaa
d, e, f = bbb
g, h, i = ccc
j, k, l = ddd
lista2 = [a, b, c, d, e, f, g, h, i, j, k, l]
print(lista2)



# Pack different data types (string, int, list, float) into a tuple, then unpack only the string and list into variables.

different_tuple = ("Sergiusz", 100, [1, 2, 3, 4], 20.50)
for i in different_tuple:
    if isinstance(i, (str, list)):
        print(i)

# Create a tuple containing different data types: a string, an integer, a list of strings, and a float.
# Unpack the tuple into variables, then create a new list that includes only the string and list elements,
# with the string as-is and the list sorted alphabetically. Finally, print the new list.


the_tupla = ("Sergiusz", 122, ["Sergiusz", "Kuderski"], 10.10)
a, b, c, d = the_tupla
new_list = []
for i in (a, b, c, d):
    if isinstance(i, (str)):
        new_list.append(i)
    elif isinstance(i, list):
        new_list.append(sorted(i))
print(new_list)

# Create a tuple containing different data types:
# an integer, a string, a list of numbers, and a boolean. Unpack the tuple into variables.
# Then, construct a new list that includes only the list and boolean elements,
# with the list sorted if it's a list of numbers. Finally, print that new list.

the_ta = (11, "Sergiusz", [100, 5, 10, 15], True)
m, n, o, p = the_ta
new = []
for i in (m, n, o, p):
    if isinstance(i, bool):
        new.append(i)
    elif isinstance(i, list):
        new.append(sorted(i))
print(new)

# Unpack a tuple with four elements into two variables, where the second variable is also a tuple containing two elements.

msg = (1, (5, 10), 222)
a, (b, c), d = msg
print(a)
print(b)
print(c)
print(d)


# Create a function that takes three parameters, packs them into a tuple, and returns it.
# Call the function and unpack the returned tuple into variables.

def three_pams(one, two, three):
    tuple = (one, two, three)
    return tuple

result = three_pams(1, 2, 3)
a, b, c = result
print(a)
print(b)
print(c)

# Create a function that takes four parameters, packs them into a tuple, and returns the tuple. Call the function with four arguments,
# then unpack the returned tuple into four variables, swapping the first and last variables before printing all four variables individually.

def xoxo(one, two, three, four):
    tup = (one, two, three, four)
    return tup

res = xoxo(1, 2, 3, 4)
a, b, c, d = res
a, b, c, d = d, b, c, a
print(a)
print(b)
print(c)
print(d)

# Create a function that takes any number of arguments (using *args), packs them into a tuple, and returns the tuple.
# Then, unpack the tuple into variables,
# and rotate the variables so that the first becomes the last, and all others shift left by one.
# Finally, print all variables individually.

def anything(*args):
    t = args
    return t

resl = anything(1, 2, 3, 4, 5)
a, b, c, d, e = resl
a, b, c, d, e = b, c, d, e, a
print(a)
print(b)
print(c)
print(d)
print(e)


# Given two lists of equal length, pack their elements into tuples and combine all into a list.
# Then unpack each tuple into separate variables in a loop.

first1 = [1, 2, 3, 4, 5]
first2 = [2, 3, 4, 5, 6]
pair_list = [(a, b) for a, b in zip(first1, first2)]

for a, b in pair_list:
    print(f"{a} : {b}")

# Given two lists of unequal length, zip them into tuples and create a list of these tuples. Then, unpack each tuple in a loop,
# and for each unpacked pair, print the sum of the two values. If the lists are of unequal length, ignore the extra elements in the longer list.

one12 = [1, 2, 3, 5]
one13 = [1, 2, 4]
for a, b in zip(one12, one13):
    print(a + b)



# Pack a tuple of 5 elements, then unpack the first three elements into individual variables and the remaining two elements into another tuple.

kc = (1, 2, 3, 4, 5)
a, b, c, d, e = kc
middle = (d, e)
print(a)
print(b)
print(c)
print(middle)
print(d)
print(e)

# Create a tuple with 7 elements. Unpack the first three elements into individual variables,
# then pack the next four elements into a new tuple. Finally, unpack that tuple into individual variables and print all variables separately.

kz = (1, 2, 3, 4, 5, 6, 7)
a, b, c, d, e, f, g = kz
four = (d, e, f, g)
print(a)
print(b)
print(c)
print(four)
print(d)
print(e)
print(f)
print(g)

# Create a tuple with 10 elements. Unpack the first three elements into individual variables.
# Next, pack the next four elements into a tuple, and then unpack that tuple into four separate variables.
# Finally, pack the remaining three elements into another tuple and unpack it into three variables. Print all of these variables individually.

the_ttz = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
a, b, c, d, e, f, g, h, j, k = the_ttz
fourz = (d, e, f, g)
threez = (h, j, k)
print(a)
print(b)
print(c)
print(fourz)
print(threez)



# Create a tuple containing mixed data types, then unpack it, including nested tuples and lists, into separate variables, and print all.

majj = (1, "sergiusz", [1, 2, 3, [4, 5]], (20, 15, (1, 2), 5), 12)
a, b, c, d, e = majj
aa, bb, cc, *dd = c
aaa, bbb, *ccc, ddd = d
print(dd)
print(ccc)
print(ddd)
print(a)
print(b)
print(c)
print(d)
print(e)