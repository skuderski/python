# Access Global Variable
# Create a global variable x = 10. Write a function that prints x without modifying it.

# x = 10
#
# def printing_x():
#     print(x)
#
# printing_x()
#
# # Change Global Variable with global
# # Create a global variable score = 0. Inside a function, increase score by 5 using global.
#
# score = 0
#
# def increasing():
#     global score
#     score += 5
#     print(score)
#
# increasing()
#
#
#
# # Local Variable Shadowing
# # Create a global variable name = "Alice". Inside a function,
# # declare a local name with a different value and print both inside and outside the function.
#
# name = "Alice"
#
# def fiku_miku():
#     name = "Sergiusz"
#     print(name)
# print(name)
# fiku_miku()
#
#
#
#
# # Append to Global List
# # Create a global list numbers = [1, 2, 3]. Inside a function, append 4 to it without reassigning the list.
#
# numbers = [1, 2, 3]
#
# def numbers_fiku_miku():
#     numbers.append(4)
#     print(numbers)
# numbers_fiku_miku()
#
#
# numbers2 = [4, 5, 6]
#
# def numbers_miku():
#     global numbers2
#     numbers2 = [0, 0, 0]
# print(numbers2)
# numbers_miku()
# print(numbers2)
#
# # Reassign Global Variable
# # Create a global string status = "active". Inside a function, assign status = "inactive" without using global,
# # then print outside the function to see if it's changed.
#
# status = "active"
#
# def reassigning():
#     status = "inactive"
#
# print(status)
#
#
# # Increment a Counter with global
# # Create a global variable counter = 0. Inside a function, reassign it to counter + 1 using global.
#
# counter = 0
#
# def increment_a_counter():
#     global counter
#     counter += 1
#
# print(counter)
# increment_a_counter()
# print(counter)


# Local Variable Example
# Create a function that defines a local variable temp = 5. Change temp inside the function and print it. Show it doesn't affect the outside.

# temp = 3
# def temperature():
#     temp = 5
#     temp += 2
#     print(temp)
# print(temp)
# temperature()
# print(temp)

# Nest a Function and Use Local Variable
# Create a function with a local variable amount = 10. Inside it, define a nested function that prints amount. Call the nested function.

# def outside():
#     amount = 10
#     def inside():
#         print(amount)
#     inside()
# outside()


# Using nonlocal to Modify Outer Variable
# Create a function with a variable total = 0. Inside a nested function, declare nonlocal total and add 10 to it.
# Call the inner function twice and show the total.

# def some_cool_function():
#     total = 0
#     def some_cooler_function():
#         nonlocal total
#         total += 10
#     some_cooler_function()
#     some_cooler_function()
#     print(total)
# some_cool_function()


# Error with nonlocal outside Nested Function
# Show that trying to use nonlocal outside a nested function causes a syntax error.
# total = 0
# def very_cool():
#     nonlocal total
#     total += 10
#     def even_cooler():
#         total
# very_cool()




# Multiple Nesting with nonlocal
# Create a function with count = 0. Inside it, define two nested functions that both modify count with nonlocal. Call both and see the result.


def we_be_countin():
    count = 0
    def we_be_countin_first():
        nonlocal count
        count += 2
    def we_be_countin_second():
        nonlocal count
        count += 3
    we_be_countin_first()
    we_be_countin_second()
    print(count)
we_be_countin()



# Global List Modification
# Create a global list nums = [1, 2, 3]. Inside a function, use global and reassign nums, then show the change outside.


nums = [1, 2, 3]

def list_modi():
    global nums
    nums = [4, 5, 6]
list_modi()
print(nums)

# Local Variable in Function
# Create a function that declares a local variable message = "hello". Change message in the function and show it doesn't affect outside.
message = "hehe"
def just_some_funcy():
    message = "hello"
    message = "bye"
    print(message)

print(message)
just_some_funcy()
print(message)


# Modifying Global Variable without global
# Create a global int a = 5. Inside a function, set a = 10 without global. Explain why the outside a is unchanged.

a = 5

def modi():
    a = 10
    print(a)

print(a)
modi()
print(a)
#it's unchanged because a = 10 is local and its scope is only in the function modi()





# Simple Closure with nonlocal
# Create a function that holds a count variable, and returns an inner function that increments and returns the count each time.

def counting():
    count = 0
    def inner_counting():
        nonlocal count
        count += 1
        return count
    return inner_counting

counter = counting()
print(counter())
print(counter())


# Shadowing Global Variable Locally
# Create a global variable color = "red". Inside a function, declare color = "blue" and print inside and outside to see they are separate.

color = "red"

def changing_colors():
    color = "blue"
    print(color)
print(color)
changing_colors()

# Inner Function No nonlocal
# Create a function with a variable number=0. Inside a nested function, just print number. Call nested function multiple times.

def the_funcjone():
    number = 0
    def the_other_funcjone():
        print(number)
    the_other_funcjone()
    the_other_funcjone()
    the_other_funcjone()
the_funcjone()



# Global Variable from Inside Function (No global)
# Create a variable x = 1 outside. Inside a function, try to change x = 2 without global and explain what happens.

x = 1

def some_insajds():
    x = 2
    print(x)
print(x)
some_insajds()
print(x)

#there are two x, one is global and one is local inside a function





# Use globals()
# Create a global variable g_var = 100. Inside a function, print globals()['g_var'].


g_var = 100

def globallo():
    print(globals()['g_var'])

globallo()



# Simple nonlocal in Inner Function
# Create a function that initializes counter=0. Inside, define an inner function that does nonlocal counter and increments it.
# Call inner multiple times and print the counter.


def somethink():
    counter = 0
    def anythink():
        nonlocal counter
        counter += 1
        return counter
    anythink()
    anythink()
    anythink()
    print(counter)
somethink()
