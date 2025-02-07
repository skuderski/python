import random

#task 1

"""
Create two numeric variables, a and b.
Perform and print the results of the following operations:
addition, subtraction, multiplication, division, and modulus.
"""

a = 2
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

# task 2

"""Write a function named calculate_area that takes a radius as a parameter and returns the area of a circle. 
Use the formula: area = π * radius^2. Print the area for a radius of 5."""

def calculate_area(radius: float):
    pi = 3.14
    area = pi * radius ** 2
    return area

radius_value = 5
print(calculate_area(radius_value))

#task 3
"""Create a function named celsius_to_fahrenheit 
that takes a temperature in Celsius as input
and converts it to Fahrenheit using the formula: F = (C * 9/5) + 32. 
Test the function with a temperature of 25°C and print the result."""

def celsius_to_fahrenheit(c: int):
    f = (c * 9/5) + 32
    return f
c = 25
temperature_in_f = celsius_to_fahrenheit(c)
print(temperature_in_f)

#task 4
"""Write a function called is_even that takes an integer as input 
and returns True if the number is even and False if it is odd. 
Test the function with several integer values."""

def is_even(number:int) -> bool:
    return number % 2 == 0
print(is_even(3))
print(is_even(-5))

#task 5
"""Implement a function named factorial that takes a non-negative integer and returns its factorial. 
The factorial of a number n is the product of all positive integers up to n. 
Test the function with the input 5."""

def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))

# task 6
"""Write a function named find_max that takes three numeric arguments and returns the largest one. 
Test the function with a set of three different numbers."""

def find_max(a, b, c) -> int:
    return max(a, b, c)
print(find_max(22,7,6))

# task 7
"""
Use the random module to generate a random integer between 1 and 100. 
Print the generated number. 
Then, create a simple guessing game where the user has to guess the number."""

random_number = random.randint(1, 10)
print(f"The random number is: {random_number}")
guesses = 0
while True:
    guess = (int(input("Guess the number between 1 and 10:")))
    guesses += 1

    if guess < random_number:
        print("Too bad you are shit at this game")
    elif guess > random_number:
        print("Too high, motherfucker")
    elif guess == random_number:
        print(f"You won, it's JOEVER, it took you only {guesses} tries, sonny.")
        break
# task 8
"""Create a function called is_prime that takes an integer 
and returns True if the number is prime and False if it is not. 
Test the function with several numbers, including prime and non-prime numbers."""

def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            return True
print(is_prime(4))

# task 9
"""
Write a function named sum_of_digits that takes a positive integer and returns the sum of its digits. 
For example, if the input is 123, the output should be 6. Test the function with a few values."""

def sum_of_digits(n:int):
    stringged = str(n)
    total = 0
    for digit in stringged:
        total += int(digit)
    return total

print(sum_of_digits(255))

# task 10
"""
Implement a function called fibonacci that takes a non-negative integer n 
and returns a list containing the first n numbers in the Fibonacci sequence. 
The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones. 
est the function with n = 10."""

def fibonacci(n: int) -> list:
    the_fibonacci_list = []
    the_fibonacci_list.append(0)
    the_fibonacci_list.append(1)
    for i in range(2, n):
        the_fibonacci_list.append(the_fibonacci_list[-1]+the_fibonacci_list[-2])
    return the_fibonacci_list
print(fibonacci(5))

#task 11
"""
Count Vowels: 
Write a function that takes a string and returns the number of vowels (a, e, i, o, u) in the string."""

def count_vowels(word: str) -> int:
    count = 0
    for letter in word:
        if letter in "aeiou":
            count += 1
    return count

print(count_vowels(word="konstantynakowiczka"))

#task 12
"""
Reverse a String: 
Create a function that takes a string as an argument and returns the string in reverse order."""

def reverse_string(word: str) -> str:
    return word[::-1]

print(reverse_string(word = "chlopaczek"))

#task 13

"""Implement a function that computes the factorial of a given non-negative integer
 using both iterative and recursive approaches."""

def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(factorial(5))

# task 14

"""
Check Palindrome: 
Write a function that checks if a given string is a palindrome (reads the same forward and backward)."""

def palindrome(word: str) -> bool:
    return word == word[::-1]

print(palindrome(word = "wiataiw"))
print(palindrome(word = "civic"))