# # Sum of numbers: Write a program to calculate the sum of all numbers from 1 to 100.
#
# def calculate():
#     sum_of_all = 0
#     for i in range(1, 101):
#         sum_of_all += i
#     return sum_of_all
#
# print(calculate())
#
# # Calculate factorial: Compute the factorial of a given number.
#
# def factorial(n: int):
#     fact = 1
#     for v in range(1, n + 1):
#         fact *= v
#     return fact
#
# print(factorial(5))
#
#
#
#
# # Check prime number: Write a function to determine if a number is prime.
#
# def prime(n: int):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# print(prime(4))
#
#
# # Find the maximum: Given a list of numbers, find the largest one.
#
# numbers = [3, 7, 12, 25, 42, 58, 73, 89, 101, 150]
#
# print(max(numbers))
#
# # Convert Celsius to Fahrenheit: Write a program that converts Celsius temperature to Fahrenheit.
#
# def conversion(temperature: int):
#     fahrenheit = temperature * (9/5) + 32
#     return fahrenheit
#
# print(conversion(20))
# # Calculate the average: Given a list of numbers, find their average.
#
# def avee(numbers: list):
#     return sum(numbers) / len(numbers)
#
# print(avee([5, 12, 7, 22, 3, 15, 9, 30, 8, 19]))
#

# Generate random numbers: Use Python’s random module to generate 10 random integers between 1 and 100.
import random
def some_random():
    numbers = []
    for _ in range(10):
        n = random.randint(1, 100)
        numbers.append(n)
    return numbers
print(some_random())



# Round numbers: Practice rounding a number to 2 decimal places.
number = 100.2543

print(round(number, 2))

# Calculate the area of a circle: Given the radius, compute the area of a circle.
import math
def area_of_a_circles(radius: int):
    return math.pi * radius ** 2

print(area_of_a_circles(5))

# Find the GCD: Write a function to find the greatest common divisor (GCD) of two numbers.

def greatest_common_divisor(one: int, two: int):
    min_num = min(one, two)
    for i in range(min_num, 0, -1):
        if one % i == 0 and two % i == 0:
            return i

print(greatest_common_divisor(16, 3))
