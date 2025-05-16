# Basic Arithmetic
# Create a lambda that adds 10 to a number and apply it to the number 5.

print((lambda x: x + 10)(5))

# Multiply List Elements
# Write a lambda to multiply each element in a list [1, 2, 3, 4] by 3 using map().

print(list(map(lambda i: i * 3, [1, 2, 3, 4])))

# Filter Odd Numbers
# Use a lambda with filter() to get all odd numbers from [10, 15, 20, 25, 30].

print(list(filter(lambda i: i % 2 != 0, [10, 15, 20, 25, 30])))

# Sort List of Tuples
# Sort a list of tuples [(2, 1), (1, 9), (3, 4)] based on the second element, using a lambda as the key.

sorted_list = sorted([(2, 1), (1, 9), (3, 4)], key = lambda x: x[1])
print(sorted_list)

# Sum of Two Numbers
# Create a lambda that takes two parameters and returns their sum, then call it with 7 and 8.

print((lambda x, y: x + y)(7, 8))

# Check String Length
# Use a lambda to check whether a string's length is greater than 5, for the string "Hello, World".


print((lambda x: len(x) > 5) ("Hell"))



# 7. Find Maximum in List
# Find the maximum value in [3, 5, 1, 8, 4] using a lambda with max().

print((lambda x: max(x)) ([3, 5, 1, 8, 4]))



# 8. Create a Complex Expression
# Write a lambda that computes (x^2 + y^2) for given x and y, and evaluate it for x=3 and y=4.

print((lambda x, y: (x ** 2 + y ** 2))(3, 4))




# 9. Conditional Expression
# Use a lambda to return 'Even' if a number is even or 'Odd' if odd, for the number 7.

print((lambda n: "Even" if n % 2 == 0 else "Odd")(8))


# 10. Sorting with Custom Key
# Sort a list of strings ["apple", "banana", "cherry"] based on their length using a lambda as the key.

sorted_strings = sorted(["pear", "papaya", "apple", "banana", "apricot", "cherries", "passion fruit"], key = lambda l: len(l))
print(sorted_strings)

# Square a number:
# Create and apply a lambda to square the number 4.

print((lambda x: x ** 2)(4))


# Convert string to uppercase:
# Use a lambda to convert "hello" to uppercase.

print((lambda string: string.upper())("hello"))




# Check if number is positive:
# Create a lambda that returns True if a number is positive, otherwise False. Test it with -3.

print((lambda n: True if n > 0 else False)(-3))



# Concatenate two strings:
# Write a lambda that takes two strings and joins them with a space, then use it with "Hello" and "World".

print((lambda one, two: one + " " + two)("Hello", "World"))


# Calculate double of a number:
# Create a lambda to double the number 7 and print the result.

print((lambda x: x * 2)(7))

# Conditional String Length:
# Create a lambda that takes a string and returns 'Long' if its length is greater than 8, otherwise 'Short'.
# Test it with "Hello" and "Hello, World".

print((lambda s: "Long" if len(s) > 8 else "Short")("Hello, World"))



# Multiple Operations:
# Write a lambda that takes a number and returns its square plus twice the number. For example, for 3, output should be 3*3 + 2*3 = 15.

print((lambda x: (x ** 2) + x * 2)(5))



# Filter and Map Combined:
# Use a lambda with filter() to keep only numbers greater than 10 from [5, 15, 8, 20, 3],
# then use map() with another lambda to double those filtered numbers.

filtered = list(filter(lambda x: x > 10, [5, 15, 8, 20, 3]))
print(filtered)
print(list(map(lambda x: x * 2, filtered)))

# String Manipulation:
# Create a lambda that takes a string and returns the same string with all vowels removed.

print((lambda string: "".join (c for c in string if c.lower() not in "aeiou,")) ("Hello, world"))

# Sorting by Last Character:
# Sort the list ["apple", "banana", "cherry", "date"] based on the last character of each string using a lambda as the key.

sorted_fk_list = sorted(["apple", "banana", "cherry", "date"], key = lambda c: c[-1], reverse= True)
print(sorted_fk_list)