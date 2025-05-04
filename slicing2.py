"""1. Extract a substring
Given "Hello, world!", extract "Hello" using slicing.
"""

# substring = "Hello, world!"
# print(substring[:5])


"""2. Get the last 5 characters
From the string "Python is fun", get the last 5 characters."""

# python = "Python is fun"
# print(python[-5:])

"""3. Reverse a string
Reverse the string "abcdef" using slicing."""

# word = "abcdef"
# print(word[::-1])

"""4. Extract every second character
From "abcdefghijklmnopqrstuvwxyz", create a string with every second letter."""

# word = "abcdefghijklmnopqrstuvwxyz"
# every_second = word[::2]
# print(every_second)

"""5. Get the middle part of a string
Extract the middle three characters from "abcdefgh"."""

word = "abcdefgh"
middle = word[2:5]
print(middle)

"""6. Slice a list
Given [10, 20, 30, 40, 50, 60], slice the list to retrieve [20, 30, 40]."""

the_list = [10, 20, 30, 40, 50, 60]
slicarinho = the_list[1:4]
print(slicarinho)

"""7. Extract a sublist
From ["a", "b", "c", "d", "e", "f"], get ["c", "d", "e"]."""

some_list = ["a", "b", "c", "d", "e", "f"]

middle_list = some_list[2:5]
print(middle_list)
"""8. Skip first and last elements
From "123456789", get "2345678"."""

numerek = "123456789"
mid = numerek[1:9]
print(mid)

"""9. Slice with steps
From [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], get every third element starting from index 0."""

some_cool_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
every_third = some_cool_list[0::3]
print(every_third)

"""10. Get the first half and second half of a list
Split [1, 2, 3, 4, 5, 6] into two parts: [1, 2, 3] and [4, 5, 6]."""

splitting = [1, 2, 3, 4, 5, 6]
first = splitting[:3]
print(first)
second = splitting[3:6]
print(second)