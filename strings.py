# # task 1
#
# """Count Vowels: Write a function that takes a string and
# returns the count of vowels (a, e, i, o, u) in the string."""
#
# def count_vowels(word: str) -> int:
#     count = 0
#     for letter in word:
#         if letter in "aeiou":
#             count += 1
#     return count
#
# print(count_vowels(word="Sergiusz"))
#
# # task 2
#
# """Reverse a String: Create a function that takes a string as input and
# returns the string in reverse order."""
#
# def reverse_order(word: str) -> str:
#     reversed_word = "".join(reversed(word))
#     return reversed_word
#
# print(reverse_order(word = "Sergiusz"))
#
# # task 3
#
# """Check for Palindrome: Implement a function that checks if a given string is a palindrome
# (reads the same backward as forward)."""
#
# def palindromme(word: str) -> bool:
#     return word == word[::-1]
#
# print(palindromme(word = "ann"))
#
# # task 4
#
# """Change Case: Write a function that takes a string and
# returns it with all uppercase letters converted to lowercase and vice versa."""
#
# def case(word: str) -> str:
#     some_fancy_list = []
#     for letter in word:
#         if letter.isupper():
#             some_fancy_list.append(letter.lower())
#         elif letter.islower():
#             some_fancy_list.append(letter.upper())
#     return "".join(some_fancy_list)
# print(case(word = "SergiuSz"))
#
#
# # task 5
#
# """Remove Whitespace: Create a function that removes all leading and trailing whitespace from a string."""
#
# def whitespace (word: str) -> str:
#     word.replace( " ", "")
#     return word.strip()
#
# print(whitespace(word = "  Sergiusz  "))
#
# # task 6
#
# """Find Substring: Write a function that checks if a specific substring exists within a given string
# and returns its position.
# If not found, return -1."""
#
# def the_substring(word: str, specific_word: str) -> int:
#     return word.find(specific_word)
#
# print(the_substring(word = "Sergiusz", specific_word="abc"))
#
# # task 7
#
# """Replace Substring: Implement a function that takes a string and
# replaces all occurrences of a specified substring with another substring."""
#
# def substrinnggo(word: str, sub: str, sub2: str) -> str:
#     return word.replace(sub, sub2)
#
# print(substrinnggo(word = "Hello, sweetheart", sub = "sweetheart", sub2 = "cutiepie"))
#
# # task 8
#
# """Count Words: Write a function that takes a sentence and counts the number of words in it.
# Consider words as sequences of characters separated by spaces."""
# def counting(sentence: str, word: str) -> int:
#     count = 0
#     words = sentence.split()
#     for w in words:
#         if w.strip(",") == word:
#             count += 1
#     return count
#
# print(counting("Hello babygirl, it's a baby world. Life in plastic, it's fantastic", word="it's"))
#
# # task 9
#
# """Extract Digits: Create a function that extracts all the digits from a given string and
# returns them as a new string."""
#
# def extract_digits(word: str) -> str:
#     digits = []
#     for letter in word:
#         if letter.isdigit():
#             digits.append(letter)
#     string_of_digits = "".join(digits)
#     return string_of_digits
#
# print(extract_digits(word="123Sergiusz8S223"))
#
# # task 10
#
# """Format String: Write a function that takes a name and an age as arguments and
# returns a formatted string like
# "My name is {name} and I am {age} years old."""
#
# def formatting(name: str, age: int) -> str:
#     return f"My name is {name} and I am {age} years old"
#
# print(formatting(name="Sergiusz", age = 30))
#
#
# # task 11
#
# """Count Consonants: Write a function that takes a string and
# returns the count of consonants (non-vowel letters)."""
#
# def count_consonants(word: str) -> int:
#     count = 0
#     for letter in word:
#         if letter.isalpha() and letter not in "aouieAOUIE":
#             count += 1
#     return count
#
# print(count_consonants(word="Sergiusz to piekny GOSC kurwa"))
#
# # task 12
#
# """String Rotation: Create a function that rotates a string by a given number of positions.
# For example, rotating "hello" by 2 would yield "lohel"."""
#
# def rotating(word: str) -> str:
#     return  word[-2:] + word[:-2]
#
# print(rotating(word="Sergiusz"))
#
# # task 13
#
# """Remove Punctuation: Write a function that removes all punctuation marks from a given string."""
#
# def rm_punctuation(word: str) -> str:
#     no_punctuation = []
#     for letter in word:
#         if letter not in ",.!?:'-":
#             no_punctuation.append(letter)
#     nein_punctuation = "".join(no_punctuation)
#     return nein_punctuation
#
# print(rm_punctuation("Ser,gius?z"))
#
# # task 14
#
# """Check Anagram: Implement a function that checks
# if two strings are anagrams (contain the same letters in a different order)."""
#
# def checking_anagram(word: str, second_word: str) -> bool:
#     first = sorted(word)
#     second = sorted(second_word)
#     return first == second
#
# print(checking_anagram("listen", "silent"))
#
# # task 15
#
# """Longest Word: Create a function that finds and returns the longest word in a given sentence."""
#
# def the_longest(sentence: str) -> str:
#     longest_word = ""
#     words = sentence.split()
#     for word in words:
#         if len(word.strip(",.!?")) > len(longest_word.strip(",.!?")):
#             longest_word = word
#     return longest_word
#
# print(the_longest("Sergiusz,.!? is a very handsome boy, onomatopeia"))
#
# # task 16
#
# """Substring Count: Write a function that counts how many times a specific substring appears in a string."""
#
# def the_counting_insanity(word:str, substring: str) -> int:
#     return word.count(substring)
#
# print(the_counting_insanity("banana", "na"))
#
# # task 17
#
# """Capitalize Each Word: Implement a function that capitalizes the first letter of each word in a sentence."""
#
# def capitalizing(sentence: str) -> str:
#     the_list = []
#     words = sentence.split()
#     for word in words:
#         the_list.append(word[0].upper() + word[1:])
#     capitalized_words = " ".join(the_list)
#     return capitalized_words
#
# print(capitalizing("sergiusz to fajny mis"))
#
# # task 18
#
# """Common Prefix: Write a function that finds the longest common prefix among a list of strings."""
#
#
# def prefixx(strings: list) -> str:
#     if not strings:
#         return ""
#
#     prefix = strings[0]  # Start with the first string
#
#     for string in strings[1:]:
#         while string[:len(prefix)] != prefix:  # Keep checking for prefix
#             prefix = prefix[:-1]  # Shorten the prefix
#             if not prefix:  # If it becomes empty, return
#                 return ""
#
#     return prefix  # Return the common prefix
#
#
# # Example Usage
# print(prefixx(["flower", "flow", "flight"]))
#
# # task 19
#
# """String Compression: Create a function that compresses a string by
# replacing consecutive duplicate characters with their count (e.g., "aaabb" becomes "a3b2")."""
#
# def compress(word: str) -> str:
#     the_list = []
#     current_char = word[0]
#     count = 1
#     for letter in word[1:]:
#         if letter == current_char:
#             count += 1
#         else:
#             the_list.append(current_char)
#             the_list.append(str(count))
#             current_char = letter
#             count = 1
#
#     the_list.append(current_char)
#     the_list.append(str(count))
#
#     return "".join(the_list)
#
# print(compress("SSergggiuuussszz"))
#
# # task 20
#
# """Swap Case: Write a function that
# swaps the case of each letter in a string (lowercase letters become uppercase and vice versa)."""
#
# def swapping(word: str) -> str:
#     list_of_letter = []
#     for letter in word:
#         if letter.islower():
#             list_of_letter.append(letter.upper())
#         elif letter.isupper():
#             list_of_letter.append(letter.lower())
#         else:
#             list_of_letter.append(letter)
#     swapped_letters = "".join(list_of_letter)
#     return swapped_letters
#
# print(swapping("SerGiuSz KuDeEErSSki"))

"""Count vowels: Write a program to count the number of vowels in a given string."""

def count(word: str):
    count = 0
    for c in word:
        if c.lower() in "aeiou":
            count += 1
    return count

print(count("Sergiusz"))


"""Reverse a string: Create a function that takes a string and returns it reversed."""
def reverse(word:str):
    return word[::-1]

print(reverse("Sergiusz"))

"""Check for palindromes: Write a program to check if a string reads the same backward and forward."""

def pali(word: str):
    return word == word[::-1]

print(pali("mama"))

"""Remove punctuation: Remove all punctuation marks from a string."""
def remove_punctuation(word:str):
    no_punctuations = ",.!:?"
    wpunct = ""
    for c in word:
        if c not in no_punctuations:
            wpunct += c
    return wpunct

print(remove_punctuation("Sergiusz, jest fajnym czlowiekiem!"))



"""Find the longest word: Given a string, identify the longest word in it."""

def longest_word(word: str):
    longest = 0
    longest_w = ""
    words = word.split(" ")
    for w in words:
        if len(w) > longest:
            longest = len(w)
            longest_w = w
    return longest

print(longest_word("Apple orange banana grape strawberry pineapple lemon"))




"""Count words: Count how many words are in a sentence."""

def count_words(word: str):
    list_of_words = word.split(" ")
    return len(list_of_words)

print(count_words("Apple orange banana grape strawberry pineapple lemon"))

"""Capitalize: Convert a string to title case (capitalize the first letter of each word)."""

def capitalizing(word: str):
    capitalized_word = []
    split_word = word.split(" ")
    for w in split_word:
        if w:
            new_word = w[0].upper() + w[1:].lower()
            capitalized_word.append(new_word)
    return " ".join(capitalized_word) + "."

print(capitalizing("sergiusz michal wojcik waclaw"))


"""Write a function that takes a string and returns a list of all words in it that contain the character '@'.  """

def extract_emails(email: str):
    words = email.split(" ")
    emails = []
    for word in words:
        if "@" in word:
            cleaned = word.strip(",.")
            emails.append(cleaned)
    return emails

print(extract_emails("john.doe@example.com, jane.smith@domain.com, info@company.org, support@service.net"))

"""Replace substrings: Replace all occurrences of a certain substring with another substring."""

def replacement(text: str, word: str, sub: str):
    replace = text.replace(word, sub)
    return replace

print(replacement("I like orange.", ".", "!"))

"""Check if string contains only digits: Verify if a string consists solely of numbers."""

def only_digits(word: str):
    return word.isdigit()

print(only_digits("1111w"))