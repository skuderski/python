#
# Even or Odd: Write a function that takes an integer as input and returns True if the number is even
# and False if the number is odd.

def even_or_odd(input: int):
    return input % 2 == 0

print(even_or_odd(5))


# Within Range: Write a function that takes a number as input and returns True if the number is within the range of 10 to 20 (inclusive)
# and False otherwise.

def within_range(input:int):
    if input in range(10,21):
        return True
    else:
        return False

print(within_range(11))

# String Starts With: Write a function that takes two strings as input: text and prefix.
# The function should return True if the text string starts with the prefix string, and False otherwise.  (Hint: use the startswith() method).

def string_starts(first: str, second: str):
    return first.startswith(second)

print(string_starts("sergiusz", "se"))


# Is Leap Year: Write a function that takes a year as input and returns True if it's a leap year and False otherwise.
# (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

def is_leap_year(year: int):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(is_leap_year(1996))

# Both Positive: Write a function that takes two numbers as input and returns True if both numbers are positive and False otherwise.

def both_positive(one: int, two: int):
    return one > 0 and two > 0

print(both_positive(2, 4))

# One is Positive, One is Negative: Write a function that takes two numbers as input and returns True if one number is positive
# and the other is negative, and False otherwise.

def one_positive_one_negative(one: int, two: int):
    return (one > 0 and two < 0) or (one < 0 and two > 0)

print(one_positive_one_negative(2, -5))

# Is Vowel: Write a function that takes a single character as input and returns True if it's a vowel (a, e, i, o, u) and
# False otherwise (case-insensitive).

def is_vowel(character: str):
    if character.lower() in "aeiou":
        return True
    else:
        return False

print(is_vowel("A"))
# Check Password Strength: Write a function that takes a password as input and returns True if it meets the following criteria:
#
# At least 8 characters long.
# Contains at least one uppercase letter.
# Contains at least one lowercase letter.
# Contains at least one digit. Otherwise, return False.

def password_strength(password: str):
    has_upper = False
    has_lower = False
    has_digit = False
    if len(password) < 8:
        return False

    for c in password:
        if c.isupper():
            has_upper = True
        elif c.islower():
            has_lower = True
        elif c.isdigit():
            has_digit = True
    return has_upper and has_lower and has_digit

print(password_strength("Sergiusz1"))


# Logical Expression Evaluation: Write a function that takes three boolean values (a, b, c) as input
# and returns the result of the following logical expression: (a and b) or (not c).

def logical_expression(a: bool, b: bool, c: bool):
    return (a and b) or (not c)

print(logical_expression( True,True, True))
# Divisible by Both: Write a function that takes an integer and two divisors as input.
# The function should return True if the integer is divisible by both divisors, and False otherwise.

def divisible_by_both(number: int, one: int, two: int):
    return number % one == 0 and number % two == 0

print(divisible_by_both(5, 5, 2))