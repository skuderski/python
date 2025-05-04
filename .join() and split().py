"""1. Split a sentence into words
Given a sentence string, use .split() to turn it into a list of words."""

# sentence = "Sergiusz jest wspanialym mezczyzna, lubi jesc jedzenie i sie smiac"
# splitted = sentence.split()
# print(splitted)

"""2. Join a list of words into a sentence
Take a list of words and combine them into a single sentence string with spaces using .join()."""

# list_of_words = ["vodka", "balalaika", "bear", "suka", "Sergiusz"]
# joined = ", ".join(list_of_words)
# print(joined)

"""3. Split a paragraph into sentences
Use .split() to divide a paragraph string into individual sentences based on the period (.) character."""

# paragraph = ("The sun dipped below the horizon, casting a golden glow over the tranquil lake. "
#              "Birds chirped softly as the gentle breeze rustled the leaves. "
#              "In the distance, a small boat glided silently across the water, disappearing into the fading light. "
#              "Nature’s beauty was at its peak, offering a moment of peace and reflection to all who observed it.")
#
# sentences = paragraph.split(".")
# print(sentences)

"""4. Join list of numbers into a comma-separated string
Given a list of numbers, convert each to string and join them with commas using .join()."""

# list_of_numbers = [1, 2, 5, 3, 10, 22, 33, 44, 15]
# string_of_numbers = []
#
# for number in list_of_numbers:
#     string_of_numbers.append(str(number))
# print(string_of_numbers)
#
# joininho = ",".join(string_of_numbers)
# print(joininho)

"""5. Split a string by a delimiter
Use .split(',') to split a string of comma-separated values into a list."""

# animals = " lion, cow, dog, cat"
# print(animals.split(", "))

"""6. Join a list of words with hyphens
Take a list of words and join them into a hyphen-separated string with .join('-')."""

words = ["apple", "banana", "cherry", "date", "elderberry"]
joinZ = "-".join(words)
print(joinZ)

"""7. Split a date string into parts
Use .split('-') to split a date like "2024-04-27" into day, month, and year."""

date = "2024-04-27"
d_m_y = date.split("-")
print(d_m_y)

"""8. Join a list of characters into a string
Given a list of single characters, join them into a single string with no spaces."""

list_of_characters = ["a", "s", "b", "d", "e", "o", "v", "w", "l", "r"]
joined_characters = "".join(list_of_characters)
print(joined_characters)

"""9. Split a string into characters
Use .split() with an empty string to turn a string into a list of individual characters 
(Note: in Python, .split() without arguments splits on whitespace, but splitting into individual characters needs a trick)."""

"""Hint: Use list() to split into characters."""

stringarooni = "Sergiusz Kuderski"
characters = list(stringarooni)
print(characters)


"""10. Compare .split() and .join()
Write an example showing:

How .split() turns a string into a list.
How .join() turns the list back into a string.
Show that .split() usually relies on a delimiter, and .join() takes a list of strings and concatenates with a separator.
Would you like me to help you start solving any of these? Or just more detailed explanations on how .split() and .join() differ?"""

name = "Sergiusz Kuderski wiek 30"
split_name = name.split(" ")
print(split_name)
joining_into_string = " ".join(split_name)
print(joining_into_string)