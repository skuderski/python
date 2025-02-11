# task 1
"""FizzBuzz: Write a function that takes a number as an input and prints "Fizz" if the number is divisible by 3,
"Buzz" if it is divisible by 5, and "FizzBuzz" if it is divisible by both.
Otherwise, return the number."""

def fizzbuzz(number: int) -> str or int:
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return number
print(fizzbuzz(30))

# task 2

"""Factorial: Create a function to calculate the factorial of a given positive integer using recursion."""

def factorial(number: int) -> int:
    x = 1
    for i in range(2, number + 1):
        x *= i
    return x

print(factorial(5))

# task 3

"""Palindrome Check: Write a function that checks whether a given string is a palindrome 
(reads the same forwards and backwards)."""

def palindrome(word: str) -> str:
    return word.lower() == word.lower()[::-1]

print(palindrome("syntax"))

# task 4

"""Count Vowels: Develop a function that counts the number of vowels in a given string and returns the count."""

def counting_vowels(word: str) -> int:
    count = 0
    for l in word:
        if l in "aouie":
            count += 1
    return count

print(counting_vowels("aouie"))

# task 5

"""Remove Duplicates: Write a function that takes a list as input and 
returns a new list with all duplicates removed, maintaining the original order."""

def remove_duplicates(some_list: list) -> list:
    seen = set()
    the_list = []
    for i in some_list:
        if i not in seen:
            seen.add(i)
            the_list.append(i)
    return the_list

print(remove_duplicates([1, 1, 2, 3, 4, 5,]))

# task 6

"""Sum of Digits: Implement a function that calculates the sum of the digits of a given non-negative integer."""

def summing(n: int) -> int:
    total = 0
    for i in str(n):
        total += int(i)
    return total

print(summing(123))

# task 7

"""Prime Number Check: Create a function that checks whether a given integer is a prime number."""

def prime(n: int) -> bool:
    for i in range(2, int(n**0.5) + 1): # n**0.5 - square root
        if n % i == 0:
            return False
    return True
print(prime(16))

# task 8

"""Temperature Converter: Write a function that converts temperatures between Celsius and Fahrenheit. 
It should take a temperature and a unit ('C' or 'F') as inputs and return the converted temperature."""

def converter(value: float, unit: str) -> float:
    if unit.upper() == 'C':
        fahrenheint = value * 1.8 + 32
        return fahrenheint
    elif unit.upper() == 'F':
        celcius = (value - 32) / 1.8
        return celcius
print(converter(2, "F"))

# task 9

"""Count Unique Words: Implement a function that counts the number of unique words 
in a given sentence by splitting the sentence and using a set to store the words."""

def just_count_it()