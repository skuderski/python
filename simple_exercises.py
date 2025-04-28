import random

# task 1

def hello(word: str) -> str:
    return word

print(hello("Hello, World!"))

# task 2

"""def calculator() -> float:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /): ")

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            print("Error: Division by zero")
            return None
    else:
        print("Invalid operator")
        return None

result = calculator()
if result is not None:
    print(f"The result is {result}")
"""
# task 3

#"""Calculate the Area of a Circle Write a program that takes the radius of a circle from the user and
#calculates its area using the formula ( \text{Area} = \pi \times \text{radius}^2 )."""

def area() -> float:
    radius = float(input("Enter the radius:"))
    pi = 3.14
    the_area = pi * radius**2
    return the_area
area_of_circle = area()

print(f"The area is {area_of_circle}")

# task 4
"""List of Even Numbers:
Write a program that generates a list of all even numbers from 1 to 100 and prints the list."""

def some_list() -> int:
    the_list = []
    for number in range(2, 101, 2):
        the_list.append(number)
    return the_list

print(some_list())


# task 5

"""Create a function that takes a string as input and counts the number of vowels (a, e, i, o, u) in it. Print the count.
"""

def count_vowels(word: str) -> int:
    count = 0
    for letter in word.lower():
        if letter in "aeiou":
            count += 1
    return count

print (count_vowels("Sergiusz"))

# task 6

"""Write a program where the computer randomly selects a number between 1 and 10, and the user has to guess it. 
Inform the user if their guess is too high, too low, or correct."""

def random_number():
    target_number = random.randint(1, 10)
    while True:
        guess = int(input("Select a number from 1 to 10: "))
        if guess < 1 or guess > 10:
            print("Please choose a number within a range of 1 to 10.")
            continue

        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        elif guess == target_number:
            print("Bingo!")
            break
random_number()

# task 7

"""Create a function that accepts a string and returns the string in reverse order."""

def reverse_string(word: str) -> str:
    return word[::-1]

print(reverse_string("Sergiusz"))

# task 8

