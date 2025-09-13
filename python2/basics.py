# from multiprocessing.process import AuthenticationString
#
# name = "Sergiusz"
# surname = "Kuderski"
# age = 31
# height = 179.5
# is_married = False
#
# print(name, surname)
# print(type(age), type(is_married))
#
# milk_price = 50
#
# bread_price = 20
#
# total = milk_price + bread_price
#
# print(total)
#
# apple = 5
# banana = 10
#
# the_sum = apple + banana
# difference = apple - banana
# product = apple * banana
# quotient = apple / banana
#
# print(the_sum, difference, product, quotient)
#
# length = 10
# width = 20
#
# area = length * width
# perimeter = 2 * length + 2 * width
#
# print(area, perimeter)
#
# numbers = [1, 2, 3, 4, 5, 6, 7]
#
# for n in numbers:
#     print(n * 2 - 5)
#
# the_bill = 200
# tip_percentage = 0.05
# tip = the_bill * tip_percentage
# total_bill = the_bill + tip
# split_bill = total_bill / 4
# print(split_bill)
#
# temperature = 50
#
# temperature_fahrenheit = (temperature * 9/5) + 32
# print(temperature_fahrenheit)
#
# name = "SerggGiusZ"
# name_lower = name.lower()
# print(name_lower)
#
# surname = "KKuDDerski"
# surname_upper = surname.upper()
# print(surname_upper)
#
# city = "Athens"
#
# user_data = name + " " + surname + ", " + city
# print(user_data)
#
# user_data_f = f"{name} {surname}, {city}"
# print(user_data_f)
#
# user_data_length = len(user_data)
# print(user_data_length)
# print(user_data_f[5].lower())
#
# candy_price = 20
# chocolate_price = 100
#
# print(candy_price == chocolate_price)
# print(candy_price > chocolate_price)
# print(chocolate_price > candy_price)
#
# is_gay = False
# likes_women = True
#
# print(not is_gay)
# print(is_gay and likes_women)
# print(is_gay or likes_women)
#
# number = 11
#
# print(number % 2 == 0)
#
# first_num = 10
# second_num = 20
#
# print(first_num > second_num)
#
# the_age = 20
#
# print(the_age >= 18)
#
# password = "the_password"
#
# print(password == "the_password")
#
# the_temp = 31
# the_humidity = 30
#
# print(the_temp > 30 and the_humidity < 50)
#
#
# python_group = ["Alina", "Kacper", "Rozalia", "Anna"]
# print(python_group)
#
# students_grades = [78, 80, 90, 2]
# print(students_grades)
#
# python_group.append("Wojtek")
# python_group.append("Julian")
# print(python_group)
# print(len(python_group))
#
# first_student = python_group[0]
# first_student_grades = students_grades[0]
# print(first_student)
# print(first_student_grades)
#
# last_student = python_group[-1]
# print(last_student)
#
# students_grades[1] = 33
# print(students_grades[1])
# print(students_grades)
#
# invitations = list(range(1, 21))
# print(invitations)
#
# invitations = list(range(1, 21, 3))
# print(invitations)
#
# numbers = []
# for n in range(1, 11):
#     numbers.append(n)
# print(numbers)
#
# my_favorite_fruits = ["banana", "apple", "strawberry", "fig"]
# print(len(my_favorite_fruits))
#
# the_colors = ["orange", "blue", "yellow", "green", "brown"]
# print(the_colors[0], the_colors[-1])
#
# some_list = []
# some_list.append("dog")
# some_list.append("cat")
# some_list.append("capybara")
# print(some_list)
#
# empty_list = []
# for n in range(0, 19, 2):
#     empty_list.append(n)
#
# print(empty_list)
#
# another_empty_list = []
# for n in range(10):
#     another_empty_list.append(n*n)
#
# print(another_empty_list)
#
# cities = ["Warsaw", "Athens", "Buenos Aires", "Gdansk", "Wroclaw"]
# print(cities[-1])
#
# car_brands = ["Toyota", "Ford", "Honda", "BMW", "Mercedes-Benz"]
# print(len(car_brands))
#
# odd_numbers = []
# for n in range(1, 20, 2):
#     odd_numbers.append(n)
#
# print(odd_numbers)
#
# numbers = [11, 12, 13, 14, 15]
# numbers[2] = 12
# print(numbers)
#
# temp = 20
#
# if temp < 20:
#     print("Wear a jacket")
# else:
#     print("You don't have to wear a jacket")
#
#
# book_price = 100
# money = 500
#
# if book_price <= money:
#     print("I can buy a book")
#
# age = 20
#
# if age >= 18:
#     print("Eligible to vote.")
# else:
#     print("Not eligible to vote.")
#
# n = 50
#
# if n > 0:
#     print("Positive")
# elif n < 0:
#     print("Negative")
# elif n == 0:
#     print("Zero")
# else:
#     print("Incorrect number")
#
# score = 95
#
# if score >= 90:
#     print("Excellent")
# elif score >= 75:
#     print("Good")
# elif score >= 60:
#     print("Pass")
# elif score < 60:
#     print("Fail")
# else:
#     print("Incorrect score")
#
# t = 35
#
# if t > 30:
#     print("Hot")
# elif 15 <= temperature <= 30:
#     print("Warm")
# elif t < 15:
#     print("Cold")
#
# some_number = 10
#
# if some_number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
#
# hour = 22
#
# if 0 <= hour <= 11:
#     print("Good morning")
# elif 12 <= hour <= 17:
#     print("Good afternoon")
# elif 18 <= hour <= 23:
#     print("Good evening")
# else:
#     print("Incorrect value")
#
# password = "le password"
#
# if password == "le password":
#     print("Access granted.")
# else:
#     print("Access denied.")
#
# first = 10
# second = 20
#
# if first > second:
#     print("First # is greater than the second")
# elif first < second:
#     print("Second # is greater than the first")
# else:
#     print("Both numbers are equal.")
#
# day = 10
#
# if day == 1:
#     print("It is Monday")
# elif day == 2:
#     print("It is Tuesday")
# elif day == 3:
#     print("It is Wednesday")
# elif day == 4:
#     print("It is Thursday")
# elif day == 5:
#     print("It is Friday")
# elif day == 6:
#     print("It is Saturday")
# elif day == 7:
#     print("It is Sunday")
# else:
#     print("Invalid day.")
#
# num1 = 10
# num2 = 20
# operation = "-"
#
# if operation == "+":
#     print(num1 + num2)
# elif operation == "-":
#     print(num1 - num2)
# elif operation == "*":
#     print(num1 * num2)
# elif operation == "/":
#     print(num1 / num2)
# else:
#     print("Invalid operation")
#
# total_savings = 0
# monthly_increase = 100
#
# for n in range(1, 13):
#     total_savings += monthly_increase
#     print(f"Month {n} : {total_savings} saved")
#
# for n in range(1, 11):
#     print(n)
#
# the_summary = 0
#
# for n in range(1, 51):
#     the_summary += n
#
# print(the_summary)
#
# fruits = ["Apple", "Banana", "Orange", "Grapes", "Strawberry"]
#
# for fruit in fruits:
#     print(fruit)
#
# for n in range(2, 21, 2):
#     print(n)
#
# squares = []
#
# for n in range(1, 11):
#     squares.append(n*n)
#
# print(squares)
# counter = 0
# for f in fruits:
#     counter += 1
#
# print(counter)
#
# name = "Sergiusz"
#
# for c in name:
#     print(c.lower())
#
# for fruit in range(len(fruits) -1, -1, -1):
#     print(fruits[fruit])
#
# # savings = 100
# # book_p = 20
# # books_to_buy = savings // book_p
# #
# # for _ in range(books_to_buy):
# #     if savings >= book_p:
# #         savings -= book_p
# #         print(f"I bought a book. I have {savings} left.")
# #     else:
# #         break
#
# savings = 100
# book_pri = 20
# books_bought = 0
#
# while savings >= book_pri:
#     books_bought += 1
#     savings -= book_pri
#     print(f"I bought a book. I have {savings} left.")
#
# starting_n = 0
#
# while starting_n < 10:
#     starting_n += 1
#     print(starting_n)
#
# s_num = 10
#
# while s_num > 0:
#     s_num -= 1
#     print(s_num)
#
# count = 1
# sumary = 0
# while sumary < 50:
#     sumary += count
#     print(sumary)
#
# number = 2
#
# while number <= 20:
#     print(number)
#     number += 2
#
# def greeting(name):
#     print(f"Hey {name}, welcome to our website.")
#
# greeting("Sergiusz")
#
# def add(number1, number2):
#     return number1 + number2
#
# print(add(10, 15))
#
#
# def greeting2(name):
#     print(f"Hey {name}, welcome to hell.")
#
# greeting2("Sergiusz")
#
# def add(num1, num2):
#     return num1 + num2
#
# print(add(1, 2))
#
# def calculate_area(length, width):
#     return length * width
#
# print(calculate_area(10, 2))
#
# # Make a function that takes a number and returns True if it's even, False if odd.
#
# def even_odd(num):
#     return num % 2 == 0
#
# print(even_odd(3))
#
# # Write a function that takes Celsius temperature and returns Fahrenheit.
#
# def conversion(temperature_c):
#     temperature_f = (temperature_c * 9/5) + 32
#     return temperature_f
#
# print(conversion(9))
#
# # Create a function that takes two numbers and returns the greater one.
#
# def greater_num(num1, num2):
#     return max(num1, num2)
#
# print(greater_num(30, 20))
#
# # Write a function that takes a string and returns the number of vowels in it.
#
#
# def counting_vowels(word):
#     count = 0
#     for c in word:
#         if c in "aeiou":
#             count += 1
#     return count
#
# print(counting_vowels("Sergiusz"))
#
# def is_sorted(box_numbers):
#     for i in range(len(box_numbers) - 1):
#         if box_numbers[i] > box_numbers[i + 1]:
#             return False
#     return True
#
# is_sorted([1, 2, 3, 4])
#
# def is_sorted(box_numbers):
#     for i in range(len(box_numbers) - 1):
#         print(f"Comparing {box_numbers[i]} and {box_numbers[i+1]}")
#         if box_numbers[i] > box_numbers[i + 1]:
#             print("Found out of order")
#             return False
#     return True
#
# is_sorted([1, 2, 3, 4])
#
# from math import floor
#
#
# def get_speed_statistic(test_results):
#     the_list = []
#     if not test_results:
#         return [0, 0, 0]
#
#     the_list.append(min(test_results))
#     the_list.append(max(test_results))
#     average = floor(sum(test_results) / len(test_results))
#     the_list.append(average)
#     return the_list
#
# print(get_speed_statistic([10, 20, 30, 50]))
#
# def add_numbers(number1: int, number2: int) -> int:
#     print(number1, number2)
#     print(type(number1), type(number2))
#     return number1 + number2
#
# result = add_numbers(10, 20)
# print(f"Wynik dodawania wynosi {result}.")
# import pdb
# numbers1 = [1, "2", 3]
#
# my_sum = 0
#
# # for number in numbers:
# #     pdb.set_trace()
# #     my_sum += number
# #     print(my_sum)
#
# for number in numbers1:
#     my_sum += number
#     print(my_sum)
from math import remainder

# def find_max(numbers):
#     if not numbers:
#         return None
#     max_num = 0
#     for num in numbers:
#         if max_num < num:
#             max_num = num
#     return max_num
#
# print(find_max([1, 2, 3]))


# def calculate_average(numbers):
#     total = 0
#     count = len(numbers)
#     for number in numbers:
#         total += number
#
#     if count > 0:
#         return total / count
#
#     return 0
#
# print(calculate_average([1, 2, 3, 4, 5]))


# Write a program to print "Hello" 5 times. Use the debugger to pause after each print and check the loop variable.

# def greeting(word):
#     for n in range(5):
#         print(word)
#
# greeting("Hello")

# Sum all numbers in a list. Use breakpoints to stop at each step and inspect your running totals.

# def summ(numbers):
#     total = 0
#     for n in numbers:
#         total += n
#     return total
#
#
# print(summ([1, 2, 3, 4, 5]))

# Find the maximum number in a list. Set breakpoints inside the loop to see how the max value updates.

# def maximum(numbers):
#     maxx = 0
#     for n in numbers:
#         if n > maxx:
#             maxx = n
#     return maxx
#
# print(maximum([1, 5, 10, 2, 3, 11, 99, 2, 140]))

# Count vowels in a string. Use the debugger to watch how the count variable changes with each character.

# def vowels(word):
#     count = 0
#     for c in word:
#         if c in "aeiou":
#             count += 1
#     return count
#
# print(vowels("Sergiusz"))

# Reverse a list with a loop. Use breakpoints to observe the swapping or appending process.

# def reversing(nums):
#     for n in range(len(nums) // 2):
#         print(f"Before swap {n=}: {nums}")
#         nums[n], nums[len(nums) - 1 - n] = nums[len(nums) - 1 - n], nums[n]
#         print(f"After swap {n=}: {nums}\n")
#
#
# print(reversing([1, 2, 4, 2, 10]))

# def create_list(n):
#     the_list = []
#     if n == 0:
#         return the_list
#
#     for i in range(1, n + 1):
#         if i % 2 == 0:
#             the_list.append(i)
#     return the_list
#
# print(create_list(10))

# def check_number(number: int) -> list[bool]:
#     the_list = []
#     if number > 0:
#         the_list.append(True)
#     if number % 2 == 0:
#         the_list.append(True)
#     if number % 10 == 0:
#         the_list.append(True)
#     return the_list
#
# print(check_number(44))

# def get_century(year: int) -> int:
#     if year == 0:
#         return 1
#     return (year + 99) // 100
#
# print(get_century(100))

# distance_light_years = 2.537 * 1_000_000
# distance_km = distance_light_years * 9_461_000_000_000
# speed_of_light_km_per_s = 300_000
#
# time_in_seconds = distance_km / speed_of_light_km_per_s
# time_in_years = time_in_seconds / (60 * 60 * 24 * 365)
#
# print(time_in_seconds)
# print(time_in_years)

# def make_lemonade(sugar_grams: int, water_liters: int) -> int:
#     if not water_liters:
#         return float("nan")
#
#     water_ml = water_liters * 1000
#     water_portion = water_ml // 500
#     sugar_portion = sugar_grams // 100
#     return min(water_portion, sugar_portion)
#
# print(make_lemonade(550, 10))

# import random
#
#
# def generate_random_list(min_value, max_value, length: int) -> list:
#     the_list = []
#     for _ in range(length):
#         the_list.append(random.randint(min_value, max_value))
#     return the_list
#
# print(generate_random_list(1, 2, 5))

# Divide Two Numbers
# Take two numbers and print their division result using /.

# a = 10
# b = 20
# print(10 / 20)

# Integer Division
#
# Divide two numbers using // and print the quotient as an integer.

# num1 = 20
# num2 = 30
#
# print(20 // 30)

# Calculate Remainder
#
# Find the remainder when dividing a number by 3 using %.

# x = 20
#
# print(x % 3)

# Count How Many Times a Number Fits
# Given two numbers, divide one by the other using // and print how many times it fits completely.

# a = 10
# b = 3
#
# c = a // b
#
# print(c)

# Find Remainder for Even/Odd check
#
# Use % to check if a number is even or odd.

# def even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
#
# print(even_odd(5))



# Share equally

# Divide a total number of candies among a certain number of friends using // for how many each gets, and % for how many are leftover.

# candies = 85
# people = 6
#
# each_gets = candies // people
# remainder = candies % people
#
# print(each_gets)
# print(remainder)



# Find the last digit
# Use % to get the last digit of a number (e.g., 1234 % 10).

# number = 2056
#
# print(number % 10)


# Calculate days and leftover hours
# Given total hours, find how many full days (//) and leftover hours (%) there are.


# hours = 100
#
# days = hours // 24
# leftover_hours = hours % 24
# print(days)
# print(leftover_hours)


# Break down a total amount into bills
# Divide an amount of money into bills of specific denominations using // and get the remaining cents with %.

# amount = 944
# amount_of_fives = amount // 20
# remaining_dollars = 944 % 20
# remaining_cents = remaining_dollars * 100
# print(amount_of_fives)
# print(remaining_dollars)
# print(remaining_cents)




# Check divisibility
# Write a program that checks if a number is divisible by 4 or 5 using %, and print appropriate messages.


# def divided_by_four_and_five(number):
#     if number % 4 == 0 and number % 5 == 0:
#         print(f"{number} is divisible by both 4 and 5.")
#     else:
#         print(f"{number} is not divisible by either 4 or 5.")
#
# divided_by_four_and_five(21)

# Calculate Average
# Given total points and number of exams, compute the average score using /.

# total_points = 450
# number_of_exams = 3
# average_score = total_points / number_of_exams
# print(average_score)


# Determine Full Hours in Seconds
#
# Convert total seconds to full hours using //.

# seconds = 15234
# full_hours = seconds // (60 * 60)
# print(full_hours)
#
#
# # Find Remaining Seconds After Full Hours
# # Use % to find leftover seconds after extracting full hours.
#
# left_over_seconds = seconds % 3600
# print(left_over_seconds)

# Calculate How Many Times a Number Fits into Another
# Divide a total number of items by a batch size with // to find how many full batches fit.

# a = 2
# b = 15
#
# c = b // a
# print(c)

# # Determine if a Number is Divisible by 8
# # Use % to check if a number leaves no remainder when divided by 8.
#
# def check_8(numbers):
#     the_list = []
#     for n in numbers:
#         if n % 8 == 0:
#             the_list.append("yes")
#         else:
#             the_list.append("no")
#     return the_list
#
# print(check_8([1, 2, 8, 16, 24, 3, 2]))




# Find How Many Full Minutes in Total Seconds
# Convert seconds to minutes with //, and find leftover seconds with %.

# total_seconds = 124912
# full_minutes = 124912 // 60
# left_over_seconds = total_seconds % 60
# print(full_minutes)
# print(left_over_seconds)


# Divide a Pizza into Slices
# Given total slices, find how many slices each person gets using //, with remaining slices from %.

# total_slices = 27
# people = 5
# each_person_slices = total_slices // people
# remaining_slices = total_slices % people
# print(each_person_slices)
# print(remaining_slices)



# Find Last Digit of a Number
# Use % to extract the last digit of any integer.

# def last_intiger(num):
#     return num % 10
#
# print(last_intiger(241))

# Count How Many Full Weeks in Days
# Convert total days into full weeks using //, and leftover days with %.

# days = 1249
# full_weeks = days // 7
# leftover_days = days % 7
# print(full_weeks)
# print(leftover_days)


# Determine if a Number is a Multiple of 10
# Use % to check if the number ends with 0.

# def check_10(num):
#     if num % 10 == 0:
#         print("yes")
#     else:
#         print("no")
#
# check_10(10)
# check_10(8)

# Calculate the number of seconds in a given number of days
# Given days, convert to seconds using / and *.

# days = 244
# seconds_in_day = 24 * 60 * 60
# seconds = days * seconds_in_day
# print(seconds)



# Break down a total number of seconds into days, hours, and minutes
# Use // and % to find each component.

# seconds = 21412412
# full_days = seconds // (24 * 3600)
# remainder_seconds = seconds % (24 * 3600)
# hours = remainder_seconds // 3600
# remaining_seconds_after_hours = remainder_seconds % 3600
# minutes = remaining_seconds_after_hours // 60
#
# print(full_days)
# print(remainder_seconds)
# print(hours)
# print(remaining_seconds_after_hours)
# print(minutes)

# Determine if a number is a multiple of 3, 4, or both
# Use % with 3 and 4, and print different messages for each case.

# num = 12
#
# if num % 3 == 0 and num % 4 == 0:
#     print("It is both a multiple of 3 and 4.")
# elif num % 3 == 0:
#     print("It is a multiple of 3.")
# elif num % 4 == 0:
#     print("It is a multiple of 4.")

# Find the number of full hundreds in an amount and the leftover amount
# Given an amount, find out how many hundreds it includes and the remaining amount.

# amount = 21512512
# full_hundreds = amount // 100
# remaining_from_full_hundreds = amount % 100
#
# print(full_hundreds)
# print(remaining_from_full_hundreds)



# Calculate the number of full baskets needed for a set of items
# Given total items and basket capacity, determine how many full baskets are needed using // and the leftover items with %.

# total_items = 21412
# basket = 6
# full_baskets = total_items // basket
# leftover_items = total_items % basket
# print(full_baskets)
# print(leftover_items)


# Convert minutes into hours and remaining minutes
# Use // and % to break total minutes into hours and remaining minutes.

# minutes = 141241
# hours = minutes // 60
# remaining_minutes = minutes % 60
# print(hours)
# print(remaining_minutes)



# Determine if a year is a leap year using division operators
# Use % to check divisibility by 4, 100, and 400 to decide leap year.

# def leap_year(years):
#     for year in years:
#         if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#             print(f"{year} is a leap year.")
#         else:
#             print(f"{year} is not a leap year")
#
# leap_year([100, 244, 2, 1994, 1923, 1996, 1998, 1994, 1992, 1990])


# Calculate the number of full thousands in an amount
# Given an amount of money, find how many thousands it contains and the leftover.

# amount = 1312512512
# thousands = amount // 1000
# remainder = amount % 1000
# print(thousands)
# print(remainder)


# Find how many complete sets of items can be made from a total
# For example, if you have 53 candies and each pack contains 8, find out how many complete packs and leftovers.

# items = 21421
# pack = 14
# complete_packs = items // pack
# leftover = items % pack
# print(complete_packs)
# print(leftover)


# Calculate the number of complete trips needed for a delivery
# If each trip can carry a certain weight, and you have a total weight, determine how many full trips are required and the remaining weight.


# delivery = 1241
# trip = 13
# full_trips = delivery // trip
# remaining_weight = delivery % trip
# print(full_trips)
# print(remaining_weight)
import random
# # Generate a Random Floating-Point Number
# # Use random.random() to produce a random number between 0 and 1 and print it.
#
# random_number = random.random()
# print(random_number)


# # Simulate a Dice Roll
# # Use random.randint() to simulate rolling a six-sided die, printing a number from 1 to 6.
#
# dice_roll = random.randint(1, 6)
# print(dice_roll)


# Select a Random Element from a List
# Create a list of colors and use random.choice() to pick and print a random color.

# colors = ["red", "blue", "green", "yellow"]
# random_color = random.choice(colors)
# print(random_color)



# Generate a Random Number in a Range
# Use random.randint() to generate a random number between 50 and 100.

# random_num = random.randint(50, 100)
# print(random_num)

# Simulate a Coin Flip
# Use random.choice() with ["Heads", "Tails"] to simulate flipping a coin.

# coin_flip = ["Heads", "Tails"]
# print(random.choice(coin_flip))


# Generate a Random Float in a Range
# Use random.uniform() (if available, or random.random()) to generate a float between 10.0 and 20.0.

# random_num = random.random() * (10) + 10
# print(random_num)


# Create a Simple Password Generator
# Use random.choice() to randomly select characters from a list of letters for a password.

# letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
# random_letter = random.choice(letters)
# print(random_letter)
#
# password = ""
#
# for _ in range(6):
#     password += random.choice(letters)
#
# print(password)

# Random Number of Items
# Use random.randint() to decide how many items to pick from a list (e.g., pick 3 random fruits from a list).
# fruits = ["apple", "banana", "cherry", "kiwi", "strawberry", "papaya", "fig"]
# quantity_of_fruits = random.randint(1, len(fruits))
# picked_fruits = random.sample(fruits, quantity_of_fruits)
# print(quantity_of_fruits)
# print(picked_fruits)

# Simulate a Random Walk
# Use random.choice() to randomly decide whether to move +1 or -1 at each step, simulating a simple random walk.
# steps = 19
# position = 0
# for _ in range(steps):
#     move = random.choice(["+3", "-1"])
#     if move == "+3":
#         position += 3
#     elif move == "-1":
#         position -= 1
#     print(f"Step {_+1}, move {move}, current position {position}")


# Generate Multiple Random Numbers
# Use a loop with random.uniform() or random.random() to generate and print 5 random floating-point numbers between 0 and 1.

# for _ in range(5):
#     print(random.random())


# Simulate a Random Temperature Range
# Generate and print a list of 10 random floating-point temperatures between -10.0 and 40.0 degrees Celsius.
# list_of_floats = []
# for _ in range(10):
#     list_of_floats.append(random.random() * 50 - 10)
#
# print(list_of_floats)

# Create a Random Password
# Generate an 8-character password by randomly selecting characters from a combination of uppercase letters, lowercase letters, and digits.
import string
# the_list = string.ascii_letters + string.digits
# password = ""
#
# for _ in range(8):
#     password += random.choice(the_list)
#
# print(password)

# Simulate a Lotto Drawing
# Pick 5 unique random numbers from 1 to 50 using random.sample(), then sort and display them.

# lotto_drawing = random.sample(range(1, 50), 5)
# lotto_drawing.sort()
# print(lotto_drawing)



# Generate a Random Sentence
# Pick 10 words randomly from a predefined list and combine them into a sentence.

# words = ["apple", "river", "mountain", "sky", "flower", "music", "book", "computer", "ocean", "garden",
#          "sun", "cloud", "tree", "bird", "star", "forest", "desert", "rain", "snow", "rock"]
#
# sentence = ""
#
# for _ in range(10):
#     sentence += random.choice(words)
#     sentence += " "
# capitalized_sentence = sentence.capitalize()
# print(capitalized_sentence + ".")


# Simulate a Card Draw
# Randomly select a card (like "Ace of Spades", "10 of Clubs", etc.) from a deck of 52 cards.


# deck_of_cards = [
#     "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts",
#     "7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts", "Jack of Hearts",
#     "Queen of Hearts", "King of Hearts", "Ace of Hearts",
#     "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds", "6 of Diamonds",
#     "7 of Diamonds", "8 of Diamonds", "9 of Diamonds", "10 of Diamonds",
#     "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds", "Ace of Diamonds",
#     "2 of Clubs", "3 of Clubs", "4 of Clubs", "5 of Clubs", "6 of Clubs",
#     "7 of Clubs", "8 of Clubs", "9 of Clubs", "10 of Clubs",
#     "Jack of Clubs", "Queen of Clubs", "King of Clubs", "Ace of Clubs",
#     "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades",
#     "7 of Spades", "8 of Spades", "9 of Spades", "10 of Spades",
#     "Jack of Spades", "Queen of Spades", "King of Spades", "Ace of Spades"
# ]
#
# draw_a_card = random.choice(deck_of_cards)
# print(draw_a_card)


# Create a Random Color Gradient
# Generate a list of 5 random colors, each chosen randomly from a list of 20 predefined colors.

# colors = [
#     "Red", "Blue", "Green", "Yellow", "Orange",
#     "Purple", "Pink", "Brown", "Black", "White",
#     "Gray", "Violet", "Indigo", "Turquoise", "Magenta",
#     "Lime", "Cyan", "Maroon", "Beige", "Lavender"
# ]
#
# random_colors = []
# for _ in range(5):
#     random_colors.append(random.choice(colors))
#
# print(random_colors)



# Generate a Random Walk in 2D
# Starting at position (0,0), randomly move up, down, left, or right by 1 unit for 50 steps, tracking the final position.
# steps = 50
# position = [0, 0]
#
# for _ in range(steps):
#     move = random.choice(["x - 1", "y - 1", "x + 1", "y + 1"])
#     if move == "x - 1":
#         position[0] -= 1
#     elif move == "y - 1":
#         position[1] -= 1
#     elif move == "x + 1":
#         position[0] += 1
#     elif move == "y + 1":
#         position[1] += 1
#     else:
#         print("Incorrect move")
# print(position)




# Simulate Multiple Coin Flips
# Flip a coin 100 times and calculate the percentage of heads versus tails.

# coin = ["Heads", "Tails"]
#
# heads = 0
# tails = 0
#
# for _ in range(100):
#     flip = random.choice(coin)
#     if flip == "Heads":
#         heads += 1
#     else:
#         tails += 1
#
# heads_percentage = (heads / 100) * 100
# tails_percentage = (tails / 100) * 100
# print(f"{heads_percentage:.2f}%")
# print(f"{tails_percentage:.2f}%")



# # Generate a Random RGB Color
# # Generate and display three random integers between 0 and 255 to represent an RGB color.
#
# for _ in range(3):
#     random_color = random.randint(0, 255)
#     print(random_color)

# Create a Multiline String
# Use \n to write a message with multiple lines when printing.

# message = "Hello world, \nthis is captain speaking, \nwelcome to your first day of the rest of your life"
#
# print(message)

# Add Tabs Between Words
# Print a list of words separated by tab characters (\t).

# message = "Hello \tworld, \nthis is \tCAPTAIN \tspeaking, \nwelcome to your \tfirst \tday of the rest of your life"
#
# print(message)


# Format a Table
# Print a small table with columns aligned using \t.

# table = "Anna \tage \t30 \nTommy \tage \t36 \nSergiusz age \t31"
# print(table)

# Escape Quotes Inside a String
# Write a string that contains quotes, for example, He said, "Hello".

# the_message = "He said \"Hello\""
# print(the_message)


# Create a String with Newlines and Tabs
# Make a string that has a paragraph with indentation, using \n for new lines and \t for indenting lines.

# hymn = "\tJeszcze Polska nie zginela, kiedy my zyjemy. \n\tCo nam obca przemoc wziela, szabla odbierzemy. \n\tMarsz, marsz Dabrowski..."
# print(hymn)


# Print a Path
# Display a Windows-style file path, such as C:\Users\Name (use \\ to escape backslashes).

# path = "C:\\Users\\Sergiusz\\python\\love"
# print(path)

# Create a List with Quotes
# Make a string that lists items with quotes around each item, like "apple", "banana".

# fruits = "\"apple\", \"banana\", \"cherry\""
# print(fruits)
#
#
# # Design a Receipt
# # Use \n and \t to make a receipt with multiple lines and aligned prices.
#
# receipt = "apple \t\t10 dollars \nvodka \t\t25 dollars \nbananas \t3 dollars \nshoes \t\t70 dollars"
# print(receipt)


# Write a Poem
# Format a short poem using newlines and tabs for indentation.

# poem = """\tTwinkle, twinkle, little star,
# \nHow I wonder what you are!
# \n\tUp above the world so high,
# \nLike a diamond in the sky.
# \n\tTwinkle, twinkle, little star,
# \nHow I wonder what you are!"""
#
# print(poem)

# Remove Spaces
# Given a string with extra spaces at the beginning and end, use strip() to clean it up and then print the cleaned string.

# name = "   Sergiusz    "
# print(name.strip())


# Count Occurrences of a Letter
# Count how many times the letter 'a' appears in a given string.

# name = "Alicja lubi jesc banany i pic wode"
#
# print(name.lower().count("a"))


# Remove Specific Characters
# Remove leading and trailing punctuation (like !, ?, or .) from a string using strip().

# sentence = ".Wodka nie jest dobra! Nie pijcie wodki! Czy dzieci powinny pic wodke? Wodka zdrowia Ci doda."
# clean_sentence = sentence.strip("!?.")
# print(clean_sentence)

# Count Words
# Count how many times a specific word (e.g., "the") appears in a long text.

# text = """Once upon a time, in a land far, far away, there was a small village nestled between lush green hills.
# The villagers lived peacefully, tending to their farms and animals. Every morning, they greeted the sunrise with joy.
# One day, a mysterious traveler arrived, bringing tales of distant lands and shining treasures.
# The villagers listened intently, dreaming of adventures beyond their humble fields."""
#
#
# print(text.lower().count("the"))


# Strip Multiple Characters
# Remove leading and trailing whitespace and punctuation from a string with strip().

# sentence = " Sergiusz to fajny gosc.  "
# print(sentence.strip(" ."))


# Count Substring in String
# Count how many times a particular substring (e.g., "ab") appears in a longer string.

# text = "Dzien dobry Panstwu, kochani moi, nadszedl dzien dzisiejszy."
# stringz = "d"
# print(text.lower().count(stringz))


# Remove Extra Spaces
# Use strip() to remove spaces, then replace() to replace multiple spaces with a single space.

# text = "   This   is    a    string      with     unnecessary   spaces.   "
#
# stripped_text = text.strip(" ")
# text1 = stripped_text.replace("  ", " ")
# text2 = text1.replace("   ", " ")
# text3 = text2.replace("    ", " ")
# text4 = text3.replace("  ", " ")
# print(text4)
#

# Count Vowels
# Count the total number of vowels (a, e, i, o, u) in a string.

# text = "Sergiusz to kochany czlowiek. Bardzo go lubie."
# total_vowels = (
#     text.lower().count("a") +
#     text.lower().count("e") +
#     text.lower().count("i") +
#     text.lower().count("o") +
#     text.lower().count("u")
# )
#
# print(total_vowels)



# Trim a URL
# Remove "http://" or "https://" prefix and trailing slashes from a URL string with strip() or slicing.

# url = "https://www.youtube.com/watch?v=QIhRFbmiGAY"
# print(url.lstrip("https://"))

# Compare Counts
# Count the number of x and o characters in a string and determine which occurs more often.

# sentence = "Sergiusz to x man. On kocha x menow"
# o = sentence.lower().count("o")
# x = sentence.lower().count("x")
#
# if o > x:
#     print("\"o\" occurs more often")
# else:
#     print("\"x\" occurs more often")

# Convert a sentence to a list of words
#
# Use split() on a sentence string to create a list.


# sentence = "Sergiusz to kochany mis"
# the_list = sentence.split()
# print(the_list)


# Join a list of words into a sentence
# Use ' '.join() to combine a list of words into a single string with spaces.

# words = ["wodka", "balalaika", "matreshka", "mishka"]
# print(", ".join(words))


# Split a comma-separated string
# Take a string like "apple,banana,cherry" and split it into a list using split(",").


# some_string = "apple, banana, cherry, kiwi, watermelon"
# fruits = some_string.split(",")
# print(fruits)


# Create a CSV line
# Given a list of values (name, age, city), join them into a CSV-formatted string with commas.

# values = ["name", "age", "city"]
# print(",".join(values))

# Convert a list into a paragraph
# Use join() to create a paragraph where each sentence ends with a period and a space.

# fruits = ["apples are good", "bananas are cool", "cherry is red", "date is very sweet", "elderberry is mysterious",
#           "fig is my favourite", "grapefruit can be sour", "honeydew I have never tried", "kiwi is also one of my favourites", "lemon is healthy and sour"]
#
# paragraph = ". ".join(fruits)
# print(paragraph.capitalize())


# Split a path into components
#
# Split a file path like "C:/Users/Public/Documents" into parts using '/' as the separator.

# path = "C:/Users/Sergiusz/Python/the_project"
# print(path.split("/"))

# Trim and split user input
# Take a user input string, strip whitespace, and split into words.

# user_input = "    Hello,    how are you today?    "
#
# stripped_input = user_input.strip()
#
# print(stripped_input.split())


# Join list with custom separator
# Join words with a hyphen '-' instead of space.

# fruits = ["banana", "apple", "cherry", "kiwi"]
# print("-".join(fruits))


# Reversing a sentence
# Split a sentence into words, reverse the list, then join it back into a sentence.

# sentence = "Sergiusz to mily misiek, bardzo go kocham"
# split_sentence = sentence.split()
# print(split_sentence)
# reversed_sentence = split_sentence[::-1]
# print(reversed_sentence)
# joined_reversed_sentence = " ".join(reversed_sentence)
# print(joined_reversed_sentence)


# Extract the first 5 characters of a string.

# word = "Sergiuszek kocha"
# print(word[:5])
#
#
# # Get the last 4 characters of a string.
#
# print(word[-4:])
#
# # Extract a substring from the middle of the string (e.g., characters 3 to 8).
#
# print(word[2:9])
#
# # Reverse a string using slicing.
# print(word[::-1])
#
# # Get every second character of a string (e.g., characters at even indices).
#
# print(word[::2])
#
# # Extract a substring with a step of 3, starting from index 0.
#
# print(word[0::3])
#
# # Remove the first 3 characters from a string.
#
# new_word = word[3:]
# print(new_word)
#
# # Remove the last 2 characters from a string.
#
# new = word[:-2]
# print(new)

# Get a string's middle half (split the string into halves, take the middle part).

# length = len(word)
# start = length // 4
# end = start + length // 2
# middle_half = word[start:end]
# print(middle_half)

# 1. Reverse a List
# Take a list of numbers and reverse it in place using reverse().

# numbers = [1, 2, 3, 4, 5]
# numbers.reverse()
# print(numbers)

# 2. Sort a List Alphabetically
# Sort a list of strings alphabetically using sort().

# fruits = ["banana", "apple", "cherry"]
# fruits.sort()
# print(fruits)

# 3. Get a Sorted Copy
# Use sorted() to get a sorted version of a list without changing the original.

# sorted_fruits = sorted(fruits, reverse=True)
# print(sorted_fruits)
# print(fruits)

# 4. Make a Copy of a List
# Make a copy of a list with copy() and then modify the copy to show the original remains unchanged.

# copied_list = fruits.copy()
# print(copied_list)
# copied_list.append("kiwi")
# print(fruits)
# print(copied_list)


# 5. Remove the Last Element
# Use pop() to remove the last element from a list and print both the element and the updated list.

# last = fruits.pop()
# print(fruits)
# print(last)

# 6. Pop a Specific Element
# Use pop(index) to remove and display an element at a specific position (e.g., index 2).

# second_element = fruits.pop(1)
# print(second_element)


# 7. Sort a List of Tuples by Second Element
# Have a list of tuples and sort it based on the second element using sort() with a key.

# people = [
#     ("Alice", 30),
#     ("Bob", 25),
#     ("Charlie", 35),
#     ("Diana", 28),
#     ("Ethan", 40)
# ]
#
# people.sort(key=lambda person: person[1])
# print(people)
# 8. Reverse a String
# Convert a string to a list of characters, reverse it in place with reverse(), and turn it back into a string.

# text = "Sergiusz ma bardzo duze serce"
# reversed_text = text[::-1]
# print(reversed_text)

# 9. Sort in Descending Order
# Sort a list of numbers in descending order with sort() or sorted().

# numbers1 = [2, 4, 5, 6, 7]
#
# numbers1.sort(reverse=True)
# print(numbers1)

# 10. Clear a List
# Use pop() repeatedly or clear() (not in your list but good to practice) to remove all items.


# print(fruits)
# fruits.pop()
# fruits.pop()
# print(fruits)
# fruits.pop()
# print(fruits)

# Sort a list of words alphabetically by default, then sort by length using key=len.

# fruits = ["apple", "cherry", "banana", "kiwi", "papaya", "fig"]
# fruits.sort()
# print(fruits)
# fruits.sort(key=len)
# print(fruits)

# Sort a list of tuples representing people, by their age (second element) using key=lambda or another function.

# people = [
#     ("Alice", 30),
#     ("Bob", 25),
#     ("Charlie", 35),
#     ("Diana", 28),
#     ("Ethan", 40)
# ]
#
# people.sort(key = lambda people : people[1] )
# print(people)

# Sort a list of strings case-insensitively (so "apple" and "Apple" are considered equal), by converting to lowercase in the key.


# words = ["Apple", "Banana", "Grape", "Cherry", "date", "Elderberry", "fig", "honeydew"]
#
# words.sort(key=lambda x: x.lower())
# print(words)

# Task 1: Sort a List of Strings by the Number of Vowels
# Given a list of words, sort them based on the number of vowels they contain, from fewest to most vowels.

# words = ["Sergiusz", "nogaa", "miska", "wodka", "Inga"]
# words.sort(key=lambda word: sum(1 for ch in word.lower() if ch in "aeiou"))
# print(words)

# Task 2: Sort a List of Tuples by the First Name Length
# Given a list of tuples where each tuple contains a first name and last name, sort the list by the length of the first name.

# Given a list of words or phrases, sort them alphabetically by their last letter using sorted() and a key function.
# For example, "apple" and "banana" should be sorted based on "e" and "a" (their last characters).

# fruits = ["apple", "banana", "cherry", "kiwi"]
# fruits.sort(key=lambda ch:ch[-1])
# print(fruits)

# 1. Merge Two Lists
# Combine two lists of numbers into one list using +.

# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# merged_list = list1 + list2
# print(merged_list)

# 2. Extend a List with Another List
# Use .extend() to add all elements from one list to another.

# list2.extend(list1)
# print(list2)


# 3. Concatenate Multiple Lists
# Use + to combine three or more lists into a single list.

# list3 = [2, 3, 4]
# another_merged_list = list1 + list2 + list3
# print(another_merged_list)


# 4. Add Elements of a List into Another List
# Use extend() to append multiple elements from a list to another list.

# one = [1, 2, 3, 4]
# two = [2, 3, 4, 5]
# one.extend(two)
# print(one)

# 5. Create a List of Lists
# Combine several small lists into a larger nested list using +.

# three = [1, 2]
# four = [1, 3]
# five = [1, 4]
#
# combined = three + four + five
# print(combined)


# 6. Insert Multiple Items at Once
# Use extend() to add a list of items into a specific list at a certain position (by concatenation).

# five.extend(three + four)
# print(five)

# 7. Expand a List with Repeated Elements
# Use + to add multiple copies of a list to itself (e.g., [1, 2] + [1, 2]*3).

# repeated = [1, 2] + (five * 3)
# print(repeated)

# 8. Convert a String to a List and Extend
# Convert a string into a list of characters, then extend another list with these characters.

# text = "Sergiusz jest kochany"
# some_list = list(text)
# repeated.extend(some_list)
# print(repeated)

# 9. Compare + and extend() Effects
# Show that list1 + list2 creates a new list, while list1.extend(list2) modifies the original.
# o_ne = [1, 2, 3, 4, 5]
# t_wo = [2, 3, 4, 5, 6]
# three = o_ne + t_wo
# print(three)
# o_ne.extend(t_wo)
# print(o_ne)


# 10. Build a Shopping List
# Start with an empty list, then extend it with multiple small lists of items, simulating adding items from different categories.

# shopping_list = []
#
# fruits = ["apple", "banana"]
# dairy = ["milk", "cheese"]
# alcohol = ["Jack Daniels", "vodka"]
# shopping_list.extend([fruits, dairy, alcohol])
# print(shopping_list)

# 1. Check if Any Number is Zero
# Given a list of numbers, determine if any of them is zero.

# list_of_numbers = [0, 1, 2, 3, 4, 5, 6]
# print(any(list_of_numbers))
#
# # 2. Verify All Strings Are Uppercase
# # Check if all strings in a list are uppercase letters.
#
# the_list = ["SERGIUSZ", "KUDERSKI"]
# print(all(s.isupper() for s in the_list))

# 3. Find If Any Element is Empty
# Given a list of strings, determine if any string is empty ("").

# list_of_strings = ["", "sergiusz", "kuderski"]
# print(any(s == "" for s in list_of_strings))

# 4. Check if All Elements are Even
# Verify if all numbers in a list are even.

# list_nums = [2, 4, 6, 8]
# print(all(num % 2 == 0 for num in list_nums))


# 5. Check if Any Number is Negative
# Determine if any number in the list is negative.

# list_of_nums = [2, 4, 6, 8]
# print(any(num < 0 for num in list_of_nums))


# 6. Verify All Characters Are Alphabets
# Given a string, check whether all characters are alphabetic.

# text = "sergiusz"
# print(all(s.isalpha() for s in text))

# 7. Find if Any Student Passed
# Given a list of test scores, determine if any student scored above 90.

# list_of_scores = [100, 90, 40, 30]
# print(any(score > 90 for score in list_of_scores))


# 8. Check If All Items Are Unique
# Given a list, determine if all items are different (no duplicates).

# items = ["desk", "wardrobe", "leg", "desk"]
# items_set = set(items)
# if len(items) != len(items_set):
#     print("all items are not unique")
# else:
#     print("all items are unique")



# 9. Verify if Any String Contains a Specific Letter
# Check if any string in a list contains the letter 'z'.

# list_of_str = ["sergiusz", "kuderski"]
# print(any("z" in ch for ch in list_of_str))

# 10. Check if All Files are Closed
# Given a list of boolean flags indicating file status (True for closed, False for open), verify if all files are closed.

# files = [False, False, False, True]
# print(all(files))

# Create a Tuple of Your Favorite Colors
# Define a tuple with at least five colors.
colors = ("orange", "blue", "green", "red")


# Access Elements in a Tuple
# Retrieve and print the first and last item from a tuple of city names.

# cities = ("Warsaw", "Athens", "New York", "Barcelona")
# print(cities[0])
# print(cities[-1])


# Unpack a Tuple into Variables
# Given a tuple (name, age, city), unpack into separate variables and print them.

# the_tuple = ("Sergiusz", 31, "Athens")
# name, age, city = the_tuple
# print(name)
# print(age)
# print(city)



# Create a Tuple with Different Data Types
# Make a tuple that includes a string, an integer, and a float.

# different_data_tuple = ("Sergiusz", 30, 179.5)
# name, age, height = different_data_tuple
# print(height)
#
# # Convert a List to a Tuple
# # Take a list of numbers and convert it into a tuple.
#
# numbers = [1, 2, 3, 4, 5, 6, 7]
# tuple_of_numbers = tuple(numbers)
# print(tuple_of_numbers)
#
#
# # Find the Length of a Tuple
# # Use len() to find how many elements are in a tuple.
#
# the_length = len(tuple_of_numbers,)
# print(the_length)
# # Tuple Slicing
# # Slice a tuple to get a subset of its elements (e.g., elements from index 2 to 4).
#
# print(tuple_of_numbers[2:4])
#
#
# # Concatenate Two Tuples
# # Join two tuples to make a larger tuple.
#
# tuple1 = (1, 2, 3, 4, 5)
# tuples2 = ("Sergiusz", "Kuderski")
# tuples3 = tuple1 + tuples2
# print(tuples3)
#
#
# # Count Occurrences in a Tuple
# # Count how many times a specific element appears.
#
# tup_le = (1, 2, 3, 3, 2, 3, 5, 10)
# print(tup_le.count(3))
#
#
# # Find an Element by Index
# # Find which element is at a given index in a tuple.
#
# print(tup_le[0])
# print(tup_le[-2])
#
# # Create a Tuple of Even Numbers
# # Make a tuple containing only even numbers between 2 and 20.
#
# even_tuple = ()
# for n in range(2, 21, 2):
#     even_tuple += (n,)
# print(even_tuple)
#
# # Unpack a Tuple with Multiple Variables
# # Given a tuple (10, "Python", 3.14), unpack into variables and print each.
#
# nice_tuple = (10, "Python", 3.14)
# number, language, pi = nice_tuple
# print(number)
# print(language)
# print(pi)
#
# # Convert Tuple to List
# # Change a tuple (1, 2, 3, 4) into a list, then add a new element to the list.
#
# tu_ple = (1, 2, 3, 4)
# l_ist = list(tu_ple)
# l_ist.append(5)
# print(l_ist)
# print(l_ist.index(1))
#
# # Find the Index of an Element
# # In a tuple of city names, find the position of "Berlin".
#
# cities = ("New York", "Paris", "Tokyo", "London", "Sydney", "Berlin", "Rome", "Madrid", "Cairo", "Rio de Janeiro")
# print(cities.index("Berlin"))
#
# # Count Items in a Tuple
# # Count how many times a specific number, say 2, appears in a tuple.
#
# tuple_of_nums = (1, 2, 3, 4, 5, 6, 6, 5, 6, 6, 6, 5, 6,)
# print(tuple_of_nums.count(2))
#
#
# # Create a Tuple with Repeated Elements
# # Generate a tuple with five repeated "hello" strings.
#
# hello_tuple = ("hello", "hello", "hello", "hello", "hello")
#
# # Check if an Element Exists in a Tuple
# # Verify whether "Madrid" is in a tuple of cities.
#
# print("Madrid" in cities)
#
# # Tuple Slicing with Step
# # Extract every second element from a tuple of numbers.
#
# print(numbers[::2])
#
# # Sort a Tuple (Convert to List first)
# # Since tuples are immutable, convert a tuple of numbers into a list, sort it, then convert back to a tuple.
#
# sorting = list(tuple_of_nums)
# print(sorting)
# sorting.sort()
# print(tuple(sorting))
# # Tuple Concatenation
# # Combine two tuples into a new tuple.
#
# uno = ("Sergiusz")
# dos = ("Kuderski")
# tres = uno + " " + dos
# print(tres)
#
# # Create a Dictionary of Countries and Capitals
# # Make a dictionary with at least five country-capital pairs.
#
# countries_capitals = {"Poland" : "Warsaw", "Greece" : "Athens", "Spain" : "Madrid", "Portugal" : "Lisbon", "Russia" : "Moscow"}
# print(countries_capitals)
#
# # Access a Value by Key
# # Given a dictionary, retrieve the capital of a specific country.
#
# print(countries_capitals["Poland"])
# print(countries_capitals.get("Poland"))
#
# # Add a New Key-Value Pair
# # Add a new country and its capital to the dictionary.
#
# countries_capitals["Ukraine"] = "Kiev"
# print(countries_capitals)
#
# # Update a Value
# # Change the capital of an existing country.
#
# countries_capitals["Poland"] = "Krakow"
# print(countries_capitals)
#
# # Remove a Key-Value Pair
# # Remove a country and its capital from the dictionary.
#
# del countries_capitals["Russia"]
# print(countries_capitals)
# # Check if a Key Exists
# # Verify if a certain country is in the dictionary.
#
#
# if "Belarus" in countries_capitals:
#     print("Belarus is in the dictionary")
# else:
#     print("Belarus is not in the dictionary")
# # Loop Through Keys and Values
# # Print all country-capital pairs in a formatted way.
#
# for key, value in countries_capitals.items():
#     print(f"{key} : {value}")
#
# # Get a List of All Keys
# # Use .keys() to list all countries.
#
# for key in countries_capitals.keys():
#     print(f"{key}")
#
# # Get a List of All Values
# # Use .values() to list all capitals.
#
# for value in countries_capitals.values():
#     print(f"{value}")
#
#
# # Count How Many Items in the Dictionary
# # Use len() to find out how many country-capital pairs are stored.
#
# length_of_pairs = len(countries_capitals)
# print(length_of_pairs)
#
# # Number and Print List Items
# #
# # Loop through a list of fruits, printing each with its index starting at 0.
#
# fruits = ["apple", "banana", "cherry", "kiwi"]
# for index, fruit in enumerate(fruits):
#     print(f"{fruit} : {index}")
#
# # Find the Index of a Specific Item
# # Use enumerate() to locate the index of "banana" in a list of fruits.
#
# for index, fruit in enumerate(fruits):
#     if fruit == "banana":
#         print(f"the index of banana is {index}")
#
# # Print Items with a Custom Start Index
# # Loop through a list and number items starting from 1 instead of 0.
#
# nums = [5, 6, 7, 8, 9, 10]
# for index, num in enumerate(nums,start=1):
#     print(f"{index}: {num}")
#
# # Identify and Print Odd Index Items
# # Print only the items from odd positions in a list.
#
# the_list = [2, 5, 110, 2, 1, 9, 15, 3]
#
# for index, n in enumerate(the_list):
#     if index % 2 != 0:
#         print(f"{index} : {n}")
#
# # Create a List of (Index, Item) Tuples
# # Use enumerate() to create a list of tuples (index, item) from a list.
#
# some_cool_list = ["Sergiusz", "Kuderski", "noga", "reka"]
# list_of_t = []
# for index, word in enumerate(some_cool_list):
#     list_of_t.append((index, word))
#
# print(list_of_t)
#
#
#
# # Find All Occurrences of a Value
# # Find all indices where a certain value (e.g., 3) appears in a list using enumerate().
#
# ns = [1, 3, 4, 3, 5, 3]
# for i, n in enumerate(ns):
#     if n == 3:
#         print(f"{i}")
#
#
# # Print List Items with Line Numbers
# # Print each item prefixed with its line number, starting from 1.
#
# color = ["green", "blue", "yellow", "black", "white", "purple"]
#
# for i, c in enumerate(color, start=1):
#     print(f"{i} : {c}")
#
#
# # Use enumerate() with String Characters
# # Loop over a string, printing character and its position.
#
# the_word = "God bless the USA"
#
# for index, ch in enumerate(the_word):
#     print(f"{ch} : {index}")
#
# # Edit Items Based on Index
# # Use enumerate() to replace certain items in a list based on their index (> 2).
#
# for index, n in enumerate(ns):
#     if index > 2:
#         ns[index] = "x"
#
# print(ns)

# Create a Dictionary of Student Grades
# Initialize a dictionary with student names as keys and grades as values.

# student_grades = {"Sergiusz" : "A", "Jane": "B", "John" : "A", "Jenny" : "C"}
#
#
# # 2. Update a Grade
# # Change a specific student’s grade using update().
#
# student_grades.update({"Jenny" : "A"})
# print(student_grades)
#
# # 3. Add Multiple Entries
# # Use update() to add several new students and their grades at once.
#
#
# student_grades.update({"John": "D", "Wiesiek" : "A", "Irena" : "F"})
# print(student_grades)
#
#
# # 4. Retrieve a Grade Safely
# # Use get() to retrieve a student's grade, providing a default message if the student isn’t in the dictionary.
#
# print(student_grades.get("Serg", "not on the list"))
#
# # 5. Update with Default if Key Doesn't Exist
# # Use update() with a new key-value pair, where the key might or might not exist.
#
# student_grades.update({"Inga" : "E"})
# print(student_grades)
#
# # 6. Count the Number of Students
# # Use len() to find out how many students are in the dictionary.
#
# count_students = len(student_grades)
# print(count_students)
#
#
# # 7. Check if a Key Exists
# # Use get() to check if a particular student is in the dictionary (by seeing if the return is None).
#
# print(student_grades.get("Martyna"))
#
#
#
# # 8. Merge Two Dictionaries
# # Use update() to merge two dictionaries of student grades.
#
# more_student_grades = {"Tommy" : "A", "Edgaras" : "B", "Jakub" : "A"}
# student_grades.update(more_student_grades)
# print(student_grades)
#
# # 9. Update a Student’s Grade or Add if Not Present
# # Use get() with a default and update() to modify or insert a student with a new grade.
#
# print(student_grades.get("Sergiusz"))
# student_grades.update({"Sergiusz" : "A+"})
# print(student_grades)
#
# # 10. Use get() with a Complex Default Message
# # Retrieve a value with a default message that includes information like "Student not found."
#
#
#
# print(student_grades.get("Wojciech", "Student not found"))
#
# # List All Keys
# # Given a dictionary, print all the keys using .keys().
#
# print(list(student_grades.keys()))
#
#
# # 2. List All Values
# # Given a dictionary, print all the values using .values().
#
# print(list(student_grades.values()))
#
#
# # 3. Print Key-Value Pairs
# # Use .items() to print each key and value in the format key: value.
#
# for key, value in student_grades.items():
#     print(f"{key}: {value}")
#
#
#
# # 4. Check for a Specific Key
# # Check if a certain key exists in the dictionary using .keys().
#
# if "Sergiusz" in student_grades.keys():
#     print("Sergiusz is on the list.")
#
#
# # 5. Sum All Values
# # If the dictionary contains numbers as values, sum all of them using .values().
#
#
# number_dict = {
#     "one": 1,
#     "two": 2,
#     "three": 3,
#     "four": 4,
#     "five": 5
# }
#
# print(sum(number_dict.values()))
#
#
#
#
# # 6. Find Max Value Key
# # Find the key that has the highest value.
#
# max_key = max(number_dict, key=number_dict.get)
# print(max_key)
#
#
# # 7. Create a List of Keys with Certain Values
# # Get all keys whose values are greater than a certain number.
#
# the_list = []
# for key, value in number_dict.items():
#     if value > 2:
#         the_list.append(key)
# print(the_list)
#
#
# # 8. Count Unique Values
# # Count how many unique values are present in the dictionary.
#
# unique = set()
# for key, value in number_dict.items():
#     unique.add(value)
#
# count = len(unique)
# print(count)
#
#
#
# # 9. Create a Dictionary from Two Lists
# # Use two lists—one of keys and one of values—and create a dictionary with dict(zip(keys, values)).
#
#
# list_one = [1, 2, 3, 4, 5, 1, 2]
# list_two = [5, 4, 3, 2, 1, 1, 2]
# zapped = dict(zip(list_one, list_two))
# print(zapped)
#
# dictionary = {"Sergiusz" : 1, "Monica" : 1, "Michal": 2, "Wojtek": 2, "Ja" : 3}
# # 10. Find Keys with Duplicate Values
# # Find all keys that share the same value with another key (i.e., find duplicates in value).
# reverse = {}
# for key, value in dictionary.items():
#     if value not in reverse:
#         reverse[value] = []
#     reverse[value].append(key)
# print(reverse)
#
# dupli = []
#
# for value, key in reverse.items():
#     if len(key) > 1:
#         dupli.extend(key)
# print(dupli)

# Create a Set of Unique Words
# Convert a list of words with duplicates into a set to get only unique words.

# some_fun_list = ["Sergiusz", "Sergiusz", "Kuderski", "misiek"]
# print(set(some_fun_list))
#
#
# # Add Items to a Set
# # Add a new element to an existing set.
#
# some_fun_set = {"Sergiusz", "Kuderski", "zolw"}
# some_fun_set.add("noga")
# print(some_fun_set)
#
#
# # Remove Items from a Set
# # Remove an element from a set using .remove() or .discard().
#
# some_fun_set.remove("Kuderski")
# print(some_fun_set)
#
#
# # Check Membership
# # Verify if a particular element exists in a set.
#
# if "Sergiusz" in some_fun_set:
#     print("Sergiusz is in the set")
#
#
# # Find the Intersection of Two Sets
# # Find common elements between two sets.
#
# first_set = {1, 2, 3, 4, 5}
# second_set = {3, 4, 5, 6, 7, 1, 2}
# print(first_set.intersection(second_set))
#
# # Find the Union of Two Sets
# # Combine two sets to get all unique elements.
#
# print(first_set.union(second_set))
#
# # Find the Difference of Two Sets
# # Find elements that are in one set but not in another.
#
# print(second_set.difference(first_set))
#
#
# # Check if One Set is a Subset of Another
# # Verify whether all elements of one set are contained in another.
#
# print(first_set.issubset(second_set))
#
# # Find Symmetric Difference
# # Find elements that are in either set but not in both.
#
# print(first_set.symmetric_difference(second_set))
#
# # Convert a List to a Set and back
# # Remove duplicates by converting a list to a set, then back to a list.
#
#
# the_list = [1, 2, 3, 4, 5, 2, 1, 5, 6, 10, 22, 22, 3, 4, 5, 1, 9, 30]
# the_set = set(the_list)
# unique_list = list(the_set)
# print(unique_list)
#
# # Create a Dictionary of Countries and Capitals
#
# countries_capitals = {"Poland" : "Warsaw", "Russia" : "Moscow", "Spain" : "Madrid", "Greece" : "Athens"}
# print(countries_capitals)
#
# # Add a new country-capital pair to the dictionary.
#
# countries_capitals["Turkey"] = "Istanbul"
# print(countries_capitals)
#
# # Update an existing country’s capital.
#
# countries_capitals.update({"Russia" : "St Petersburg"})
# print(countries_capitals)
#
# # Remove a country from the dictionary using del.
#
# del countries_capitals["Poland"]
# print(countries_capitals)
#
# # Safely remove a country with .pop(), handling if it's not present.
#
# print(countries_capitals.pop("Argentina", "not in the dictionary"))
#
# # Check if a specific country exists using in with the dictionary.
#
# if "Russia" in countries_capitals:
#     print("Russia is in the dictionary.")
#
# # Get a list of all countries using .keys().
#
# print(list(countries_capitals.keys()))
#
# # Get a list of all capitals using .values().
#
# print(list(countries_capitals.values()))
#
# # Iterate through the dictionary to print country and capital pairs.
#
# for key, value in countries_capitals.items():
#     print(f"{key} and its capital")
#
# # Count the total number of country-capital pairs.
# length = len(countries_capitals)
# print(length)
# print(countries_capitals)
#
# # Merge two dictionaries into one.
#
# first_dictionary = {"Sergiusz" : 8, "Viktoria" : 10, "Tomek" : 5, "Edgaras" : 8}
# second_dictionary = {"Irena" : 5, "Waclaw" : 10, "John" : 8}
# merged_dictionary = {**first_dictionary, **second_dictionary}
# print(merged_dictionary)
#
# # Create a new dictionary from two separate lists: one of countries, one of capitals, using zip().
#
#
# countries = ["Poland", "Ukraine", "England", "Scotland", "Russia", "Germany", "France", "Spain"]
# capitals = ["Warsaw", "Kiev", "London", "Edinburgh", "Moscow", "Berlin", "Paris", "Madrid"]
# countries_and_capitals = dict(zip(countries, capitals))
# print(countries_and_capitals)
#
#
# # Find the country with the longest name.
# longest = 0
# longest_country = ""
# for key in countries_and_capitals.keys():
#     if len(key) > longest:
#         longest = len(key)
#         longest_country = key
# print(longest)
# print(longest_country)
#
# # Find the country with the shortest name.
#
# shortest = 10
# shortest_country = ""
#
# for key in countries_and_capitals.keys():
#     if len(key) < shortest:
#         shortest = len(key)
#         shortest_country = key
#
# print(shortest)
# print(shortest_country)
#
#
# # Create a dictionary of countries and their populations (random large numbers).
#
# populations = {"Poland" : 40000000, "Russia" : 140000000, "Greece" : 8000000, "Portugal" : 20200000, "Paraguay" : 2000000}
# print(populations)
#
#
# # Calculate the total population using .values().
#
# print(sum(populations.values()))
#
#
# # Identify countries with capitals starting with a specific letter.
#
# for key, value in countries_and_capitals.items():
#     if value.startswith("P"):
#         print(f"{key}'s capital starts with the letter \"P\"")
#
# # Find all countries with a specific ending in their name.
#
# for key, value in countries_and_capitals.items():
#     if value.lower().endswith("s"):
#         print(f"{key}'s capital ends with a letter \"S\"")
#
# # Create a dictionary of country lengths (name length as value).
#
# dictionary_of_name_lengths = {"Poland": len("Poland"), "Russia" : len("Russia"), "Greece" : len("Greece"), "Portugal" : len("Portugal")}
# print(dictionary_of_name_lengths)
#
#
# # Invert the dictionary: swap keys and values, assuming all values are unique.
#
# inverted = {value : key for key, value in countries_and_capitals.items()}
# print(inverted)
#
# # String to Integer
# # Convert a string "123" into an integer and print the result.
#
# text = "123"
# print(int(text))
#
# # Integer to String
# # Convert an integer 456 into a string and print it.
#
# num = 456
# number = str(num)
# print(number)
# print(type(number))
#
# # String to Float
# # Convert a string "3.14159" into a float and print it.
#
# the_number = "3.14159"
# the_num = float(the_number)
# print(the_num)
# print(type(the_num))
#
# # Float to Integer
# # Convert a float 9.8 into an integer (truncate or round) and print it.
#
# fl = 9.8
# integ = int(fl)
# print(integ)
#
#
# # List of Strings to List of Integers
# # Given ["1", "2", "3"], convert each element to int.
#
# strings = ["1", "2", "3"]
# strings_of_int = []
# for n in strings:
#     strings_of_int.append(int(n))
# print(strings_of_int)
# print(type(strings_of_int))
#
# # List of Numbers to a String
# # Convert [1, 2, 3, 4] into a single string "1, 2, 3, 4".
#
# list_of_nums = [1, 2, 3, 4]
# num_str = ""
# for n in list_of_nums:
#     str_num = str(n)
#     if num_str:
#         num_str += ", " + str_num
#     else:
#         num_str = str_num
# print(num_str)
#
# # String to Boolean
# # Convert "True" and "False" strings to boolean values.
#
# t = "True"
# f = "False"
# t_bool = (t == "True")
# f_bool = (f == "True")
# print(t_bool)
# print(f_bool)
#
#
# # Integer to List of Characters
# # Convert an integer 12345 to a string, then to a list of individual characters.
#
# the_numberr = 12345
# string_number = str(the_numberr)
# lista = []
# for n in string_number:
#     lista.append(n)
#
# print(lista)
#
#
# # Handling Conversion Errors
# # When converting a string "abc" to int, catch the exception and print a friendly message.
#
# the_ej_bi_sea = "abc"
# try:
#     print(float(the_ej_bi_sea))
# except ValueError:
#     print("can't do it, doc")
#
#
# # Convert List of Floats to List of Strings
# # Convert [3.14, 2.71, 1.41] into a list of strings.
#
# the_floaties = [3.14, 2.71, 1.41]
# the_stringies = []
# for n in the_floaties:
#     the_stringies.append(str(n))
#
# print(the_stringies)
#
# # Check if Two Numbers Are Equal
# # Given two numbers, determine if they are equal.
#
# a = 1
# b = 2
# print(a == b)
#
# # 2. Compare if One Number is Greater Than Another
# # Check if a variable a is greater than b.
#
# print(a > b)
#
# # 3. Determine if a String is Empty
# # Check if a string variable has length 0.
#
# message = ""
# print(len(message) == 0)
#
# # 4. Compare Two Strings (Case-Insensitive)
# # Check if two strings are equal ignoring case differences.
#
# message1 = "Sergiusz"
# message2 = "Kuderski"
#
# print(message1.lower() != message2.lower())
#
# # 5. Check if a Number Is Less Than or Equal to a Threshold
# # Verify if a score is below or equal to 100.
#
# score = 90
# print(score <= 100)
#
# # 6. Compare List Lengths
# # Given two lists, check if the first is longer than the second.
#
# some_list = [1, 2, 3, 4, 5]
# some_other_list = [2, 3, 4, 5, 6, 1]
# print(some_list > some_other_list)
#
# # 7. Check if a Number Is Outside a Range
# # Determine if a value x is less than 0 or greater than 100.
#
# x = 200
# print(x < 0 or x > 100)
#
# # 8. Verify if Two Variables Are Not Equal
# # Check if two variables are different.
#
# c = 123
# d = 124
# print(c != d)
#
#
# # 9. Compare Elements in a List at Different Indices
# # Check if the element at index 0 is greater than the element at index 1.
#
# indeces = [1, 2, 3, 4 ,5]
# print(indeces[0] > indeces[1])
#
# # 10. Determine if a Character Is a Vowel
#
# vowels = "aeiou"
# print("b" in vowels)

# Check if a Number is Even or Odd
# Given a number, determine whether it's even or odd.

# def even_odd(num: int):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
#
# print(even_odd(4))
#
# # Find the Absolute Value
# # Given a negative number, find its absolute (positive) value.
#
# def absolute_val(num: int):
#     return abs(num)
#
# print(absolute_val(-5))
#
# # Calculate the Square of a Number
# # Square a given number.
#
# def square_a_number(num: int):
#     return num * num
#
# print(square_a_number(5))
#
# # Calculate the Cube of a Number
# # Cube a given number.
#
# def cube_a_numbers(num: int):
#     return num * num * num
#
# print(cube_a_numbers(3))
#
#
# # Find the Remainder of a Division
# # Given two numbers, find the remainder when the first is divided by the second.
#
# a = 10
# b = 3
#
# rem = a % b
# print(rem)
#
# # Find the Average of Three Numbers
# # Calculate the average of three user-inputted numbers.
#
#
# def calculate_average(nums: list):
#     return sum(nums) / len(nums)
#
# print(calculate_average([1, 2, 3, 4, 5]))
#
# # Convert Minutes to Hours and Minutes
# # Convert a total number of minutes into hours and remaining minutes.
#
# minutes = 100000
# hours = minutes // 60
# minutes_left = minutes % hours
# print(hours)
# print(minutes_left)
#
# # Determine if a Year is a Leap Year
# # Given a year, check if it's a leap year.
# def check_leap(year: int):
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#
# print(check_leap(1996))
#
#
# # Calculate the Distance Between Two Points
# # Given two points (x1, y1) and (x2, y2), calculate the Euclidean distance.
#
# import math
#
# def distance(a, b):
#     return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
#
#
# print(distance(a = [10, 2], b = [2, 3]))
#
# # Generate a Random Number Between 1 and 50
# # Use random.randint() to generate and print it.
#
# import random
#
# print(random.randint(1, 50))
#
#
# # Count the Number of Words
# # Given a sentence, count how many words it contains.
#
# sentence = "Sergiusz bardzo kocha zycie"
# list_of_words = sentence.split()
# print(len(list_of_words))
#
#
# # Reverse a String
# # Reverse the order of characters in a string.
#
# some_string = "Sergiusz"
# print(some_string[::-1])
#
#
# # Extract a Substring
# # Extract characters from index 3 to 8 from a string.
#
# imie = "Sergiuszek"
# print(imie[3:8])
#
# # Convert a String to Lowercase and Uppercase
# # Change all characters in a string to lowercase or uppercase.
#
# name = "Sergiusz"
# name_lower = name.lower()
# name_upper = name.upper()
# print(name_lower, name_upper)
#
#
# # Check if a String Contains a Substring
# # Verify whether one string is present inside another.
#
#
# def substring(one, two):
#     return two in one
#
# print(substring("Sergiusz", "giu"))
#
# # Replace Parts of a String
# # Replace all occurrences of a word or phrase with another.
#
# def replacing(one):
#     return one.replace("S", "gowno")
#
# print(replacing("Sergiusz"))
#
# # Remove Leading and Trailing Spaces
# # Use strip() to trim spaces from the start and end.
#
# message = "  Sergiusz Kuderski jest kochany.   "
# stripped_message = message.strip()
# print(stripped_message)
#
# # Check if a String is a Palindrome
# # Determine if a string reads the same backward and forward.
#
# def palindrome(word):
#     return word == word[::-1]
#
# print(palindrome("wow"))
#
#
# # Count Specific Characters in a String
# # Count how many times a specific character appears.
#
# print(name.lower().count("s"))
#
#
#
# # Format a String with Variables
# # Use f-strings or .format() to insert variables into a string for personalized messages.
#
#
# some_message = "Sergiusz Kuderski"
# iss = "jest"
# loving = "kochany"
# dot = "."
#
# print(f"{some_message} {iss} {loving}{dot}")
#
# # Create a List of Prime Numbers
# # Generate a list containing all prime numbers between 1 and 50.
#
# import math
#
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True
# primes = []
# for num in range(1, 51):
#     if is_prime(num):
#         primes.append(num)
# print(primes)
#
#
# # Add Items to a List
# # Create an empty list and then add five different colors to it using .append().
#
# colors = []
# colors.append("blue")
# colors.append("yellow")
# colors.append("green")
# colors.append("white")
# colors.append("black")
#
# print(colors)
#
# # Remove an Item from a List
# # Remove a specific item from a list by value using .remove().
#
# colors.remove("green")
# print(colors)
#
#
# # Insert an Item at a Specific Position
# # Insert an element at index 2 in a list.
#
# colors.insert(2, "gray")
# print(colors)
#
# # Sort a List in Reverse Order
# # Sort a list of numbers from highest to lowest.
#
# the_nums = [2, 5, 10, 1, 2, 3, 4]
# sorted_nums = sorted(the_nums, reverse=True)
# print(sorted_nums)
#
# # Reverse the List
# # Reverse the list order using .reverse().
#
# some_numbers = [2, 10, 11, 3, 5, 7, 5, 111]
# some_numbers.reverse()
# print(some_numbers)
#
# # Find the Length of a List
# # Use len() to determine how many elements are in the list.
#
# print(len(some_numbers))
#
# # Access a Range of Elements
# # Extract a sublist from index 3 to 7.
#
# range_of_elements = some_numbers[3:7]
# print(range_of_elements)
#
# # Create a List of Squares
# # Use a loop to fill a list with the squares of numbers from 1 to 10.
#
# squares = []
#
# for i in range(1, 11):
#     squares.append(i*i)
#
# print(squares)
#
#
# # Duplicate a List
# #
# # Copy a list by creating a duplicate (using slicing or .copy()) and append an element to the copy without changing the original.
#
#
# copied_list = some_numbers.copy()
# print(some_numbers)
# print(copied_list)
# copied_list.append(2)
# print(copied_list)
#
# # 1. Create a Dictionary of Countries and Capitals
# # Initialize a dictionary with at least five country-capital pairs.
#
# countries_and_capitals = {"Poland" : "Warsaw", "Greece" : "Athens", "Russia": "Moscow", "Germany" : "Berlin", "Spain" : "Madrid"}
# print(countries_and_capitals)
#
# # Create a Dictionary of Countries and Capitals, then Update and Verify
# # Steps:
# #
# # Start with a dictionary containing at least five country-capital pairs.
# # Update the capital of one specific country.
# # Check if another country (e.g., "France") is in the dictionary.
# # Print a message indicating whether it exists.
# # Print the final dictionary.
#
# countries_and_capitals.update({"Poland" : "Krakow"})
# if "France" not in countries_and_capitals:
#     print("France is not in the dictionary")
# else:
#     print("France is in the dictionary")
# print(countries_and_capitals)
#
# # Start with a dictionary of at least 5 country-capital pairs.
# # Update the capital of a specific country (choose one in your dictionary).
# # Add a new country with its capital.
# # Check if another country (e.g., "Italy") exists:
# # If it exists, print its capital.
# # If it doesn't, add "Italy" with its capital and inform that it was added.
# # Remove a country (e.g., "Spain"), if it exists.
# # Print the final dictionary with all changes.
#
# countries_and_capitals.update({"Russia" : "St Petersburg"})
# countries_and_capitals["Japan"] = "Tokyo"
#
# if "Italy" in countries_and_capitals:
#     print("The capital of Italy is Rome.")
# else:
#     countries_and_capitals["Italy"] = "Rome"
#     print("Italy and its capital Rome was added.")
#
# del countries_and_capitals["Poland"]
# print(countries_and_capitals)
#
# # 2. Add a New Country and Capital
# # Add another country with its capital to your existing dictionary.
#
# countries_and_capitals["Ukraine"] = "Kiev"
# print(countries_and_capitals)
#
# new_pairs = [("Italy", "Rome"), ("Portugal", "Lisbon"), ("Hungary", "Budapest")]
# countries_and_capitals.update(new_pairs)
# print(countries_and_capitals)
#
# # 3. Update an Existing Capital
# # Change the capital of a country already in your dictionary.
#
# countries_and_capitals.update({"Italy" : "Milano"})
# print(countries_and_capitals)
#
# new_capitals = [("Poland", "Gdynia"), ("Italy", "Bari"), ("Russia", "Vladivostok")]
# countries_and_capitals.update(new_capitals)
# print(countries_and_capitals)
#
# # 4. Remove a Country from the Dictionary
# # Remove a country (and its capital) using del or .pop().
#
# del countries_and_capitals["Russia"]
# print(countries_and_capitals)
#
# countries = ["Italy", "Poland", "Greece"]
# for i in countries:
#     countries_and_capitals.pop(i, None)
#
# print(countries_and_capitals)
#
# # 5. Safely Remove a Country (using .pop())
# # Remove a country that may or may not be in the dictionary, with a default message if it doesn't exist.
#
# countries_and_capitals.pop("China", "country not in the dictionary")
#
# # 6. Check if a Country is in the Dictionary
# # Use in to check if a specific country exists.
#
# if "Poland" in countries_and_capitals:
#     print("Poland is in the dictionary")
# else:
#     print("Poland was in the dictionary but has been recently removed.")
#
# # 7. Get a List of All Countries
# # Use .keys() to get a list of all country names.
#
# all_countries = countries_and_capitals.keys()
# the_list_of_countries = list(all_countries)
# the_list_of_countries.sort()
# print(the_list_of_countries)
#
# b_capitals = []
# for key, value in countries_and_capitals.items():
#     if value[0] == "B":
#         b_capitals.append(key)
#
# b_capitals.sort()
# print(b_capitals)
#
# # 8. Get a List of All Capitals
# # Use .values() to get all capitals.
#
# the_capitals = list(countries_and_capitals.values())
# print(the_capitals)
# capitals_with_a = []
# for value in countries_and_capitals.values():
#     if "a" in value:
#         capitals_with_a.append(value)
# sorted_capitals = sorted(capitals_with_a)
# print(sorted_capitals)
#
# # 9. Print All Country-Capital Pairs
# # Loop through the dictionary with .items() and print in a formatted way.
#
# # Then, sort the countries alphabetically before printing, so the output is ordered by country name.
#
# for country in sorted(countries_and_capitals.keys()):
#     capital = countries_and_capitals[country]
#     print(f"Country: {country} | Capital: {capital}")
#
# # 10. Count Total Number of Countries
# # Use len() to count how many country-capital pairs are stored.
#
# print(len(countries_and_capitals))
# the_count = 0
# the_names_bigger_than5 = ""
# for key, value in countries_and_capitals.items():
#     if len(value) > 5:
#         the_count += 1
#         the_names_bigger_than5 += " "
#         the_names_bigger_than5 += value
# print(the_count)
# print(the_names_bigger_than5)
#
#
# # Find the First Even Number
# # Loop through numbers from 1 to 20 and print the first even number you encounter using break.
#
# for n in range(1, 21):
#     if n % 2 == 0:
#         print(n)
#         break
#
# # 2. Skip Negative Numbers
# # Loop through a list of integers, printing only positive numbers using continue.
#
# list_of_ints = [-2, 3, 4, 0, -5, - 10, 16]
#
# for n in list_of_ints:
#     if n < 0:
#         continue
#     print(n)
#
# # 3. Stop at a Specific Number
# # Loop from 1 to 50 and stop printing once you reach number 30 using break.
#
# for n in range(1, 51):
#     print(n)
#     if n == 30:
#         break
#
# # 4. Skip Multiple Values
# # Loop through numbers 1 to 20, but skip multiples of 3 using continue.
#
# for n in range(1, 21):
#     if n % 3 == 0:
#         continue
#     print(n)
#
# # 5. Find the First Multiple of 7
# # Loop from 1 to 100, printing and breaking once you find a number divisible by 7.
#
#
# for n in range(1, 101):
#     if n % 7 == 0:
#         print(n)
#         break
#
# # 6. Ignore Zero
# # Loop through a list of integers, skipping zeros and printing all others.
#
#
# the_list = [1, 0, 20, 3, 4, 5, 11]
#
# for n in the_list:
#     if n == 0:
#         continue
#     print(n)
#
# # 7. Break on a Condition
# # Loop through a list of strings, breaking when you find the string "stop".
#
#
# stringz = ["hello", "world", "this", "stop"]
#
# for s in stringz:
#     if s == "stop":
#         print("found the word")
#         break
#     print(s)
#
# # 8. Skip Conversations Over a Certain Length
# # Loop through a list of message lengths, skipping messages longer than 10 characters.
#
#
# messages = ["Sergiusz Kuderski", "kocha wszystkich wokol", "dziekuje", "za", "uwage"]
#
# for m in messages:
#     if len(m) > 10:
#         continue
#     print(m)
#
# # 9. Find the First Prime in a List
# # Loop through a list of numbers, break as soon as you find a prime number.
#
#
#
# import math
#
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# check_them_primez = [1, 2, 3, 4, 5, 6, 7, 8]
#
# for n in check_them_primez:
#     if is_prime(n):
#         print(f"The first prime number is {n}")
#         break
#
# # 10. Remove Duplicates with Continue
# # Loop through a list with duplicates, printing only the
# # first occurrence of each item using continue to skip repeats (use an auxiliary set).
#
#
# the_set = set()
# the_lista = [1, 1, 2, 3, 4, 5, 5, 6, 7]
#
# for n in the_lista:
#     if n in the_set:
#         continue
#     else:
#         the_set.add(n)
# print(the_set)

# 1. Basic Infinite Loop
# Write a loop that runs forever, printing "Hello". (Use while True:)

# while True:
#     print("Hello")


# 2. Count Up Indefinitely
# Use an infinite loop to keep counting upwards starting from 1, printing the current number each time (use while True: and a counter).
# counter = 1
# while True:
#     print(counter)
#     counter += 1

# 3. Break on User Input
# Create an infinite loop that repeatedly asks for user input and breaks when the user types "exit".

# while True:
#     user = input()
#     if user == "exit":
#         break
#     else:
#         print("continuing on")

# 4. Echo Input
# Make a program that echoes whatever the user types until they type "stop".


# while True:
#     user = input()
#     if user == "stop":
#         print("fine")
#         break
#     else:
#         print(user)

# 5. Count Down with Break
# Use an infinite loop that starts at some number and decreases until it reaches 0, then break.

# counter = 100
#
# while True:
#     print(counter)
#     counter -= 1
#     if counter < 0:
#         break


# 6. Print Even Numbers Indefinitely
# Use an infinite loop to print even numbers, starting from 0, increasing by 2 each time.
# counter = 0
# while True:
#     for num in range(0, 10**6, 2):
#         print(num)
#

# 7. Input Validation Loop
# Use an infinite loop to keep asking for a number input, breaking only if the input is valid (e.g., a number between 1 and 10).

# while True:
#     user = input()
#     try:
#         num = int(user)
#         if 1 <= num <= 10:
#             print(f"You entered a valid number: {num}")
#             break
#         else:
#             print("wrong num son")
#     except ValueError:
#         print("please give a numba, sonny.")

# 8. Simulate a Real-time Counter
# Use while True: with time.sleep() to print the current time every second.
# from time import sleep, time
#
# while True:
#     print(time())
#     sleep(1)


# 9. Random Number Generator
# Keep generating random numbers forever until a specific number (e.g., 777) appears, then break.
# import random
#
# while True:
#     n = random.randint(1, 777)
#     print(n)
#     if n == 777:
#         break


# 10. Menu-driven Program
# Create an infinite menu loop that displays options; exit only if a specific choice (e.g., "Quit") is made.

# while True:
#     user = input("Type \"Continue\" to continue, type \"Quit\" to quit\n")
#     if user == "Quit":
#         break
#     elif user == "Continue":
#         print("Continuing on")
#     else:
#         print("WTf dawg, stop playing")


# 1. Print a Multiplication Table (1-10)
# Use nested loops to print multiplication results from 1 to 10 in a formatted grid.

# for n in range(1, 11):
#     for num in range(1, 11):
#         print(n*num, end="\t")
#     print()
#
#
# # 2. Print a Pattern of Stars
# # Use nested loops to create a right-angled triangle of stars, increasing each row.
#
# for n in range(1, 11):
#     for m in range(1, n + 1):
#         print("*", end =" ")
#     print()
#
# # 3. Create a 3x3 Grid of Coordinates
# # Print coordinate pairs (row, column) for a 3x3 grid.
#
# for n in range(1, 4):
#     for m in range(1, 4):
#         print((n, m), end = " ")
#     print()
#
# for n in range(1, 6):
#     print((n, n), end = " ")
# print()
#
#
# for n in range(1, 6):
#     for x in range( 1, 6):
#         print((n, x), end = " ")
#     print()


# n = 4
#
# for x in range(1, n + 1):
#     for y in range(1, n + 1):
#         if x == 1 or x == n or y == 1 or y == n:
#             print(f"({x}, {y})", end = " ")
#     print()
#
# # 4. Generate a List of All Pairs from Two Lists
# # Combine elements from two lists to produce all possible pairs (item1, item2).
#
# list1 = [1, 2, 3, 4, 5, 6, 7, 8]
# list2 = [3, 4, 5, 6, 7, 8, 9, 10]
#
# for n in list1:
#     for m in list2:
#         print((n, m), end = " ")
#     print()
#
#
# # 5. Print a Chessboard Pattern
# # Print an 8x8 grid with alternating 'X' and 'O'.
#
# for n in range(1, 9):
#     for m in range(1, 9):
#         if (n + m) % 2 == 0:
#             print("X", end= " ")
#         else:
#             print("O", end = " ")
#     print()
#
#
# for a in range(1, 11):
#     for b in range(1, 11):
#         if (a + b) % 2 == 0:
#             print("A", end = " ")
#         else:
#             print("B", end = " ")
#     print()
#
# # 6. Print Each Letter in Each Word
# # Given a list of words, print each letter of every word line by line.
#
# words = ["Sergiusz", "Kuderski", "kocha", "zycie"]
#
# for word in words:
#     for c in word:
#         print(c)
#     print()
#
#
# # 7. Create a Number Pattern
# # Print numbers in a pattern like:
#
# counter = 1
# for row in range(1, 5):
#     for _ in range(row):
#         print(counter, end = " ")
#         counter +=1
#     print()
#
# # Print a pattern starting with 10 numbers in the first row, then 9 in the second, down to 1 in the last.
# # Fill each row with sequential numbers, starting from 1.
#
#
# counter = 1
# for n in range(10, 0, -1):
#     for _ in range(n):
#         print(counter, end = " ")
#         counter += 1
#     print()
#
#
# # Add Two Numbers
# # Write a function that takes two integers and returns their sum.
#
# def sum_numbers(a: int, b: int):
#     return a + b
#
# print(sum_numbers(1, 5))
#
# # Find the Maximum of Two Numbers
# # Write a function that accepts two floats and returns the larger one.
#
# def find_max(a: float, b: float):
#     return max(a, b)
#
# print(find_max(2, 5))
#
# # Check if a String is Palindrome
# # Write a function that takes a string and returns a bool.
#
# def palindrome(word: str) -> bool:
#     return word == word[::-1]
#
# print(palindrome("wowo"))
#
#
# # Calculate the Area of a Rectangle
# # Write a function that takes width and height as floats and returns the area as float.
#
# def area_of_rectangle(width: float, height: float) -> float:
#     return width * height
#
# print(area_of_rectangle(2.5, 3.5))
#
#
# # Convert Celsius to Fahrenheit
# # Define a function that accepts a float Celsius temperature and returns a float Fahrenheit temperature.
#
# def celsius_to_fahrenheit(celcius: float) -> float:
#     return (celcius * 9/5) + 32
#
# print(celsius_to_fahrenheit(5.5))
#
# # Return a List of First N Fibonacci Numbers
# # Take an integer n and return a list of integers.
#
# def fibonacci(n: int) -> list[int]:
#     the_list = [0, 1]
#     for x in range(2, n):
#         next_number = the_list[-1] + the_list[-2]
#         the_list.append(next_number)
#
#     return the_list[:n]
#
#
# print(fibonacci(10))
#
#
# # Count vowels in a string
# # Function takes a string and returns an integer count.
#
# def count_vowels(word: str) -> int:
#     counter = 0
#     for c in word:
#         if c in "aeiou":
#             counter +=1
#     return counter
#
# print(count_vowels("sergiusz"))
#
# # Concatenate Two Lists
# # A function that receives two lists of integers and returns a new list containing all elements.
#
# def concatenate_two_lists(one: list, two: list) -> list:
#     return one + two
#
# print(concatenate_two_lists([1, 2], [2, 3]))
#
# # Create a dictionary mapping numbers to their squares
# # Accepts a list of integers and returns a dictionary with int keys and int values.
#
# def dic_mapping(ints: list) -> dict:
#     squares = {}
#     for i in ints:
#         squares[i] = i * i
#     return squares
#
# print(dic_mapping([1, 2, 3, 4, 5]))
#
# # Sum All Numeric Arguments
# # Create a function that accepts any number of numeric arguments (*args) and returns their sum.
#
# def arguments(*args):
#     return sum(args)
#
# print(arguments(1, 2, 3))
#
#
# # 2. Print All Arguments
# # Write a function that prints all positional arguments (*args) and all keyword arguments (**kwargs) separately.
#
# def printing(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")
#
# printing(1, 2, 3, {3 : 4}, name = "Sergiusz", age = 30)
#
#
# # 3. Create a Greeting Function
# # The function takes a greeting phrase (positional argument), optional suffixes (*args), and optional keyword arguments
# # for personalization (like name and title).
#
# def greeting(phrase: str, *args, **kwargs):
#     message = phrase
#
#     if args:
#         message += " " + " ".join(args)
#
#     if 'name' in kwargs:
#         message += f" {kwargs['name']}"
#     if 'title' in kwargs:
#         message += f", {kwargs['title']}"
#     print(message)
#
# greeting("Bonjour", "you.", "are", "you", name="Sergiusz")
# # 4. Merge Dictionaries
# # Create a function that accepts any number of dictionaries via **kwargs and merges all into a single dictionary.
#
#
# def merging(**kwargs):
#     merged = {}
#     for k, v in kwargs.items():
#         merged[k] = v
#     return merged
#
# print(merging(dict1 ={"Polska" : "Warszawa"}, dict2 = {"wodka" : "bols"}, dict3 = {"red" : 100}))
#
#
# # 5. Flexible Formatting
# # Write a function that takes any number of positional strings (*args) and keyword arguments for formatting options,
# # and returns a formatted string.
#
# def flex(*args, **kwargs):
#     return f"{args} - these are positional arguments and {kwargs} - these are keyword arguments"
#
# print(flex(1, 2, 3, name = "Sergiusz", age = 30))
#
#
# # 6. Calculate Total Price
# # Accept multiple prices as *args, and optional discounts via **kwargs, then calculate total price after discounts.
#
# def calculate_total_price(*args, **kwargs):
#     total = sum(args)
#     discount = kwargs.get("discount", 0)
#     final_price = total - (total * discount // 100)
#     return final_price
#
# print(calculate_total_price(200, 300, 400, discount=10))
#
#
# # 7. Build a Profile
# # A function that takes personal info as **kwargs (like name, age, city) and additional info as *args (like hobbies), then displays all data.
#
#
# def building_profile(*args, **kwargs):
#     print(f"my hobbies: {args}")
#     for k, v in kwargs.items():
#         print(f"{k} : {v}")
#
# building_profile("football", "swimming", name = "Sergiusz", age = 31, city = "Athens")
#
#
#
# # 8. Create a List of Squares with Extras
# # Accept numbers in *args, and optional multiplier in **kwargs, return a list of squares multiplied by the multiplier.
#
# def list_of_squares_extra(*args, **kwargs):
#     multiplier = kwargs.get('multiplier', 1)
#     list_of_squares = []
#     for arg in args:
#         list_of_squares.append(arg * arg)
#
#     for i in range(len(list_of_squares)):
#         list_of_squares[i] *= multiplier
#
#     return list_of_squares
#
# print(list_of_squares_extra(2, 3, 4, 5, 6, 7, multiplier=2))
#
#
#
# # 9. Print Arguments with Labels
# # Use *args and **kwargs to print each argument with an associated label, if provided.
#
# def printing_nicely(*args, **kwargs):
#     for n in args:
#         print(f"the positional argument: {n}")
#
#     for k, v in kwargs.items():
#         print(f"key: {k} value: {v}")
#
# printing_nicely(1, 2, 3, 4, 5, name= "Sergiusz", surname = "Kuderski", age = 31)
#
#
#
# # Write a function that:
# #
# # Takes a string as input.
# # Counts how many times each vowel (a, e, i, o, u) appears in the string.
# # Returns a dictionary with vowels as keys and their counts as values.
#
# def counting_vowels(word: str) -> dict:
#     dicti = {}
#     word = word.lower()
#     for ch in word:
#         if ch in "aeiou":
#             if ch in dicti:
#                 dicti[ch] += 1
#             else:
#                 dicti[ch] = 1
#     return dicti
#
# print(counting_vowels("sergiusz"))
#
# # Task: Count Digits in a String
# # Write a function that accepts a string containing various characters.
# # Count how many times each digit (0 through 9) appears in the string.
# # Return a dictionary with digits as keys and their counts as values.
# # Ignore case for alphabetic characters (only focus on digits).
#
# def count_digits(word: str) -> dict:
#     dicti = {}
#     for ch in word:
#         if ch.isdigit():
#             if ch in dicti:
#                 dicti[ch] += 1
#             else:
#                 dicti[ch] = 1
#
#     return dicti
#
# print(count_digits("se213sg392150"))
#
# # Task: Split and Sum Odd and Even Indexed Elements
# # Write a function that takes a list of numbers.
# # Calculate the sum of elements at even indices and odd indices.
# # Return a list containing the sum of even-indexed elements first, then the sum of odd-indexed elements.
#
#
# def sum_elements(numbers: list) -> list:
#     the_list = []
#     even = sum(numbers[::2])
#     odd = sum(numbers[1::2])
#     the_list.append(even)
#     the_list.append(odd)
#     return the_list
#
# print(sum_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
#
# # Write a function that takes a list of numbers.
# # Calculate the sum of the first half of the list.
# # Calculate the sum of the second half.
# # Return a list with these two sums.
#
#
# def summing_halves(numbers: list) -> list:
#     the_list = []
#     n = len(numbers)
#     half_index = n // 2
#     first = numbers[:half_index]
#     second = numbers[half_index:]
#     sum_first = sum(first)
#     sum_second = sum(second)
#     the_list.append(sum_first)
#     the_list.append(sum_second)
#     return the_list
#
# print(summing_halves([1, 2, 3, 4, 5, 6, 7, 8]))
#
# # Given a list of book titles (each title can appear multiple times if multiple copies are available),
# # determine how many complete sets you can form.
# #
# # A set requires one copy of each book title.
# # Count how many full sets are possible with the given list.
# # Return that number.
#
#
# def counting_books(books: list) -> int:
#     books_d = {}
#     for book in books:
#         if book not in books_d:
#             books_d[book] = 1
#         else:
#             books_d[book] += 1
#     return min(books_d.values())
#
# print(counting_books(["1", "2", "1", "3", "4", "2", "3", "4", "5", "1", "5"]))
#
#
# def get_leaders(numbers: list) -> list:
#     Leaders = []
#     to_the_right = 0
#     for n in numbers[::-1]:
#         if n > to_the_right:
#             Leaders.append(n)
#         to_the_right += n
#
#     return Leaders[::-1]
#
# print(get_leaders([1, 5, 10, 2, 14, 9]))
#
# # Task: Find All "Peak" Elements in an Array
# # A "peak" element is an element that is greater than the element immediately to its right.
# # Write a function that takes a list of numbers and returns a list of all such peak elements.
#
# def peaking(numbers: list) -> list:
#     the_list = []
#     for i in range(len(numbers) - 1):
#         if numbers[i] > numbers[i + 1]:
#             the_list.append(numbers[i])
#     return the_list
#
# print(peaking([1, 3, 1, 5, 10, 1, 2, 3]))
#
# # Given a list of numbers, identify all "valleys" — elements that are less than both the previous and next elements.
# # For the first and last elements, ignore them because they don't have two neighbors.
# # Return a list of all valley elements.
#
# def valleys(numbers: list) -> list:
#     the_valleys = []
#     for i in range(1, len(numbers) - 1):
#         if numbers[i] < numbers[i - 1] and numbers[i] < numbers[i + 1]:
#             the_valleys.append(numbers[i])
#
#     return the_valleys
#
# print(valleys([1, 2, 3, 4, 5, 10, 2, 1, 9, 111, 2, 3, 4, 15]))
#
#
# # Given a list of numbers, identify and return all the "peaks" — elements that are greater than both their neighbors.
# # For the first and last elements (which don't have two neighbors), ignore them.
#
# def peaks(numbers: list) -> list:
#     the_peaks = []
#     for i in range(1, len(numbers) - 1):
#         if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
#             the_peaks.append(numbers[i])
#
#     return the_peaks
#
# print(peaks([1, 2, 3, 4 ,5, 10, 22, 33, 10, 1, 9, 5]))
#
# # Task: Count Adjacent Duplicates in a String
# # Write a function that takes a string and counts how many times adjacent characters are the same.
# # Return that number of adjacent duplicates.
#
# def adjacents(word: str) -> int:
#     duplicates = 0
#     for i in range(len(word) - 1):
#         if word[i] == word[i + 1]:
#             duplicates += 1
#     return duplicates
#
# print(adjacents("sseerrgiussz"))
#
# # Exercise: Extract and Print All Pairs of Consecutive Characters
# # Given a string (e.g., "hello"), write code to:
# # Loop through the string.
# # Extract each pair of consecutive characters.
# # Print each pair.
#
# word = "hello"
# pairs = set()
# for i in range(len(word) - 1):
#     pair = word[i:i+2]
#     pairs.add(pair)
#
# print(len(pairs))
#
# my_list = ['a', 'b', 'c']
# for i in range(len(my_list)):
#     print(f"Index {i}: {my_list[i]}")
#
# for index, value in enumerate(['a', 'b', 'c']):
#     print(f"At index {index}, value is {value}")
#
#
# def find_smaller_digits(ls: list) -> list:
#     the_list = []
#     for index in range(len(ls)):
#         digits_to_the_right = 0
#         for digit in range(index + 1, len(ls)):
#             if ls[index] > ls[digit]:
#                 digits_to_the_right += 1
#         the_list.append(digits_to_the_right)
#
#     return the_list
#
# print(find_smaller_digits([9, 8, 7, 6, 5, 1, 2, 3, 9, 8, 7]))
#
# # Task: Count How Many Larger Numbers Are After Each Element
# # Given a list of numbers, for each element, count how many numbers to the right are larger than it.
# # Return a list with these counts.
#
# def larger_numbers(numbers: list) -> list:
#     the_list = []
#     for i in range(len(numbers)):
#         larger_n = 0
#         for j in range(i + 1, len(numbers)):
#             if numbers[j] > numbers[i]:
#                 larger_n += 1
#         the_list.append(larger_n)
#
#     return the_list
#
# print(larger_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
#
# # Task: Count How Many Smaller Numbers Are to the Right
# # # Given a list of integers, for each element, count how many numbers to the right are smaller than it.
# # # Return a list of these counts.
#
# def smaller_numbers(numbers: list) -> list:
#     the_list = []
#     for i in range(len(numbers)):
#         count = 0
#         for j in range(i + 1, len(numbers)):
#             if numbers[j] < numbers[i]:
#                 count += 1
#         the_list.append(count)
#
#     return the_list
#
# print(smaller_numbers([1, 2, 3, 1, 2, 3, 5]))
#
# # Task: Extract the Year from a URL
# # Given a URL string that contains a year in its format (e.g., "https://example.com/product-2023-details"), extract the year as a string.
# # Assume the year is always the second-to-last segment when splitting by hyphens "-".
# # Write a function to do this.
#
# def extract_year(url: str) -> int:
#     splitted = url.split("-")
#     the_year = splitted[-2]
#     return int(the_year)
#
# print(extract_year("https://example.com/product-2023-details"))
#
# # Task: Extract the Filename from a File Path URL
# # Given a URL or file path like "https://example.com/folder/subfolder/file_name.txt", extract only the filename ("file_name.txt").
# # Assume the filename always appears after the last slash ('/').
#
# def extract_filename(filename: str) -> str:
#     splitting = filename.split("/")
#     file = splitting[-1]
#     return file
#
# print(extract_filename("https://example.com/folder/subfolder/file_name.txt"))
#
# # Task: Compute the Total Sum and the Sum of Each Element Divided by the Total
# # Given a list of positive numbers, first find the total sum.
# # Then, create a list where each element is the original element divided by the total sum.
# # Return this list.
#
# def computing_sum(numbers: list) -> list:
#     the_list = []
#     the_sum = sum(numbers)
#     for n in numbers:
#         number = n / the_sum
#         the_list.append(number)
#
#     return the_list
#
# print(computing_sum([1, 2, 3, 4, 5, 6, 7, 8, 9]))
#
# # Task: Combine Multiple Dictionaries with Multiplication
# # Write a function that accepts any number of dictionaries as arguments.
# # For each key, multiply all the values associated with that key across all dictionaries.
# # If a key appears in some dictionaries but not others, treat the missing values as 1 (neutral in multiplication).
# # Return a new dictionary with the keys and the multiplied result.
#
# def combining(*args):
#     multiplied = {}
#     for arg in args:
#         for i in arg:
#             if i in multiplied:
#                 multiplied[i] *= arg[i]
#             else:
#                 multiplied[i] = arg[i]
#     return multiplied

# # Create a Tuple of Your Favorite Fruits
# # Make a tuple containing at least five fruits.
#
# fruits = ("apple", "banana", "kiwi", "fig", "pineapple")
#
# # Access Elements in a Tuple
# # Retrieve and print the first and last items from a tuple of city names.
#
#
# cities = ("New York", "London", "Barcelona", "Warsaw")
# print(f"first city: {cities[0]}, last city: {cities[3]}")
#
# # Unpack a Tuple into Variables
# # Given a tuple like (name, age, city), unpack into separate variables and print them.
#
# a_tuple = ("Sergiusz", 31, "Athens")
# name, age, city = a_tuple
# print(name)
# print(age)
# print(city)
#
# # Create a Tuple with Different Data Types
# # Make a tuple that includes a string, an integer, and a float.
#
# varied_tuple = ("Sergiusz", 31, 1.79)
# print(varied_tuple)
#
# # Convert a List to a Tuple
# # Take a list of numbers and convert it into a tuple.
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# tuple_num = tuple(numbers)
# print(tuple_num)
#
# # Find the Length of a Tuple
# # Use len() to find how many elements are in a tuple.
#
# print(len(tuple_num))
#
# # Tuple Slicing
# # Slice a tuple to get a subset of its elements (e.g., elements from index 2 to 4).
#
# sliced_tuple = tuple_num[2:4]
# print(sliced_tuple)
#
# # Concatenate Two Tuples
# # Join two tuples into a new tuple.
#
# first_tuple = ("Sergiusz", "Kuderski")
# second_tuple = ("kocha", "zycie")
# new_tuple = first_tuple + second_tuple
# print(new_tuple)
#
#
# # Count Occurrences in a Tuple
# # Count how many times a specific element appears.
#
# print(first_tuple.count("Sergiusz"))
#
# # Find an Element by Index
# # Find which element is at a given index in a tuple.
#
# print(new_tuple.index("Sergiusz"))
#
# # 1. Create a Set of Unique Words
# # Convert a list of words with duplicates into a set to keep only unique words.
#
# words = ["Sergiusz", "Kuderski", "Sergiusz", "Kuderski", "wiek", "30"]
# set_of_words = set(words)
# print(set_of_words)
#
#
# # 2. Add Items to a Set
# # Add a new element to an existing set using .add().
#
# set_of_words.add("S")
# print(set_of_words)
#
# # 3. Remove Items from a Set
# # Remove an element from a set using .remove() or .discard().
#
# set_of_words.remove("S")
# print(set_of_words)
# set_of_words.discard("30")
# print(set_of_words)
#
# # 4. Check Membership
# # Check if a specific item exists in a set using the in keyword.
# print("Sergiusz" in set_of_words)
# # 5. Find the Intersection of Two Sets
# # Find common elements between two sets using .intersection() or &.
#
# set1 = {1, 2, 3, 4, 5, 6}
# set2 = {3, 4, 5, 6, 7, 8}
# print(set1.intersection(set2))
#
#
# # 6. Find the Union of Two Sets
# # Combine two sets to get all unique elements using .union() or |.
#
# print(set1.union(set2))
#
# # 7. Find the Difference of Two Sets
# # Get elements in one set not in the other using .difference() or -.
#
# print(set1.difference(set2))
#
# # 8. Check Subset and Superset
# # Verify if one set is a subset or superset of another using .issubset() and .issuperset().
#
# print(set1.issubset(set2))
# print(set1.issuperset(set2))
#
# # 9. Find Symmetric Difference
# # Find elements in either set but not in both using .symmetric_difference() or ^.
#
# print(set1.symmetric_difference(set2))
# # 10. Convert a List to a Set and Back
# # Remove duplicates by converting a list to a set, then back to a list for ordered operations.
#
# one = [1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8]
# the_set = set(one)
# the_list = list(the_set)
# print(the_list)


# count_people: int = "5"
# price: float = 13.25
# is_empty: bool = True
# message: str = "Hello, world"
#
# # Tasks Involving Mutable Types (list, dict, set):
# # Create a List of Names and Append a New Name
#
# names = ["Sergiusz", "Irena", "Inga", "Wojtek"]
# names.append("Martyna")
# print(names)
#
#
# # Modify an Element in a List
#
# names[2] = "W"
# print(names)
#
# # Remove an Element from a List
#
# names.remove("W")
# print(names)
#
# # Add a New Key-Value Pair to a Dictionary
#
# some_dict = {"Sergiusz" : 31, "Inga" : 39, "Michal" : 31}
# some_dict["Martyna"] = 25
# print(some_dict)
#
#
#
# # Update the Value for an Existing Key in a Dictionary
#
# some_dict.update({"Sergiusz" : 30})
# print(some_dict)
#
# # Remove a Key from a Dictionary
#
# del some_dict["Sergiusz"]
# print(some_dict)
# # Add Elements to a Set
#
# nums = {1, 2, 3, 4, 5}
# nums.add(6)
# print(nums)
#
#
# # Remove Elements from a Set
#
# nums.remove(2)
# nums.remove(3)
# print(nums)
#
# # Sort a List of Numbers (in-place sorting)
#
# list_of_numbers = [1, 2, 3, 4, 3, 6, 7, 8, 9]
# list_of_numbers.sort()
# print(list_of_numbers)
#
# # Reverse a List In-Place
#
# list_of_numbers.sort(reverse=True)
# print(list_of_numbers)
#
# # Tasks Involving Immutable Types (tuple, string, frozenset):
# # Create a Tuple of Integers
#
# integers = (1, 2, 3, 4)
# # Attempt to Change an Element in a Tuple (observe the error)
# # integers[0] = 2
# # print(integers)
#
# # Concatenate Two Tuples to Create a New Tuple
#
# one_tuple = (1, 2, 3, 4, 5, 6, 7)
# two_tuple = (8, 9, 10, 11, 12, 13)
# big_tuple = one_tuple + two_tuple
# print(big_tuple)
#
#
# # Create a String and Attempt to Change a Character (observe the error)
#
# # word = "Sergiusz"
# # word[0] = "F"
#
#
#
# # Create a String and Use Slicing to Extract a Substring
#
# text = "Sergiusz Kuderski"
# sliced_text = text[3:8]
# print(sliced_text)
#
# # Create a Frozenset and Try to Add an Element (observe the error)
#
# # froz = frozenset([1, 2, 3, 2])
# #
# # froz.add(1)
# # Convert a String to a List, Modify it, and Convert Back
#
#
# the_text = "Sergiusz Kuderski"
# the_list = the_text.split(" ")
# the_list.append("wiek 30")
# modified_text = " ".join(the_list)
# print(modified_text)
#
# # Extract a Substring from a String Using Slicing
#
# print(modified_text[2:10])
#
# # Convert a Tuple to a List, Change the List, and Convert Back to a Tuple
#
# some_tuple = (1, 2, 5, 1)
# a_list = list(some_tuple)
# a_list.append(10)
# tuple_changed = tuple(a_list)
# print(tuple_changed)
#
#
# # Create an Immutable Set (frozenset) from a List and Try to Add Elements
#
# # numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # frozen = frozenset(numbers_list)
# # frozen.append(1)
#
# # 1. Print Numbers from 0 to N-1
# # Use range() and len() to print numbers from 0 up to one less than the length of a list.
#
# some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for n in range(len(some_list)):
#     print(n)
#
# # 2. Count the Number of Elements in a List
# # Use len() to find and print the total number of elements.
#
# print(len(some_list))
#
#
# # 3. Print Indices of a List
# # Use range(len(list)) to print all the indices of a list.
#
# for n in range(len(some_list)):
#     print(f"index: {n}")
#
#
# # 4. Create a List of Squares
# # Use range() to generate numbers from 0 to N-1 and create a list of their squares.
# squares = []
# x = 11
# for n in range(x):
#     squares.append(n * n)
# print(squares)
#
#
# # 5. Find the Last Index of a List
# # Use len() to determine the last valid index in a list.
#
# print(len(some_list) - 1)
#
#
# # 6. Print List Elements Using Indices
# # Loop through indices with range() and print each list element.
#
# for n in range(len(some_list)):
#     print(some_list[n])
#
# # 7. Print All Even Indices
# # Use range() with a step to print only even indices of a list.
#
# for n in range(0, len(some_list), 2):
#     print(n)
#
# # 8. Create a List of Index-Value Tuples
# # Use range() and len() to create pairs of index and value from a list.
#
# the_l = []
# for n in range(len(some_list)):
#     the_l.append((n, some_list[n]))
#
# print(the_l)
#
#
# # 9. Count and Print the Length of a String
# # Use len() on a string, and then print numbers from 0 up to that length minus 1 using range().
#
# word = "Sergiusz"
# length = len(word)
# print(length)
# for n in range(length):
#     print(n)
#
#
#
# # 10. Generate a Custom Sequence
# # Generate a list of numbers starting from 0 to len(list)-1, but only at odd indices.
#
# odd_list = []
#
# for n in range(1, len(some_list), 2):
#     odd_list.append(some_list[n])

# print(odd_list)
#
# message = "Hello"
# some_cool_list = [1, 2, 3]
# print(id(message))
# print(id(some_cool_list))
# message += " world"
# some_cool_list += [4]
# print(id(message))
# print(id(some_cool_list))
# print(message)
# print(some_cool_list)
#
# a = 10
# b = a
# print(id(a), id(b))
#
# a += 1
# print(id(a), id(b))
#
# arr1 = [1]
# arr2 = arr1
# print(id(arr1), id(arr2))
#
# c = [1, 2, 3]
# d = [1, 2, 3]
# print(id(c), id(d))
#
# print(c == d)
# d = c
# print(id(c), id(d))
#
# x = 0
# y = False
# print(x == y)
# print(x is y)
# print(id(x))
# print(id(y))

# x = 500
# y = 500
# print(id(x))
# print(id(y))
#
#
# a = 999999
# b = 999999
# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)
#
# arr1 = [1, 2, 3]
# arr2 = [1, 2, 3]
# print(id(arr1))
# print(id(arr2))
#
# none1 = None
# none2 = None
#
# print(id(none1))
# print(id(none2))
#
# print(none1 is none2)
#
# f1 = False
# f2 = False
#
# print(f1 is f2)
# print(f1 == f2)
#
# one1 = 123
# one2 = 123
# print(id(one1))
# print(id(one2))
# print(one1 == one2)
# print(one1 is one2)
#
# # 1. Compare IDs of Two Same Literals
# # Assign the same string literal to two variables and compare their id() values.
#
# wordz = "Sergiusz"
# words = "Sergiusz"
# print(id(wordz))
# print(id(words))
#
#
# # 2. Create Two Different Lists with Same Elements
# # Create two separate lists with the same elements and compare their id() values;
# # observe that they are different.
#
# first_list = [1, 2, 3, 4, 5]
# second_list = [1, 2, 3, 4, 5]
# print(id(first_list), id(second_list))
#
#
# # 3. Check ID of Built-in Singleton Objects
# # Use id() on None, True, and False and verify they are the same object.
#
# nonce = None
# agree = True
# disagree = False
# print(id(nonce), id(agree), id(disagree))
#
# # 4. Create Two Variables with Same Small Integer
# # Assign the same small integer (e.g., 100) to two variables and compare their id().
#
# xx = 10
# yy = 10
# print(id(xx), id(yy))
# # Are they the same object?
# # 5. Compare IDs of New List and Tuple with Same Elements
# # Create a list and a tuple with the same data and compare their id();
# # they should be different.
#
# some_cool_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# some_cool_tuple = [1, 2, 3, 4, 5, 6, 7, 8 , 9]
# print(id(some_cool_list), id(some_cool_tuple))
#
#
# # 6. Create Two Large Lists with Same Content
# # Create two large lists with the same content and check their id(). Are they the same?
#
# strings_list = ["Sergiusz", "Kuderski", "kocha", "zycie", "i", "lubi", "jesc"]
# strings_list2 = ["Sergiusz", "Kuderski", "kocha", "zycie", "i", "lubi", "jesc"]
#
# print(id(strings_list), id(strings_list2))
#
# # 7. Assign the Same String Literal to Two Variables
# # Assign "hello" to two variables, compare their id(). Are they the same object?
#
# hillo = "hello"
# hello = "hello"
# print(id(hillo), id(hello))
#
# # 8. Create Two Sets with Same Content
# # Create two sets with the same elements and compare their id(). Are they the same?
#
# first_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# second_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(id(first_set), id(second_set))
#
#
# # 9. Check IDs of Integer Objects in Different Ranges
# # Assign small integers in different ranges (e.g., 10, 200, 500) to different variables
# # and compare IDs. Which are shared and which are unique?
#
# aa = 20
# bb = 20
# cc = 500
# dd = 500
# print(id(aa), id(bb))
# print(id(cc), id(dd))
#
# def change_list(numbers: list):
#     numbers += [10]
#
# some_fun_list = [1, 2]
# print(id(some_fun_list))
# change_list(some_fun_list)
# print(id(some_fun_list))
# print(some_fun_list)
#
# # Task: Create a Dictionary of Elements with Their Lengths
# # Write a function that takes any number of arguments (*args).
# # For each argument:
# # If it's a string, add it to the dictionary as a key, with its length as the value.
# # If it's a list, set, or dict, print a message indicating it can't be added
# # (similar to your example).
# # Return the resulting dictionary.
#
# def dictionary_length(*args):
#     a_dict = {}
#     for index, value in enumerate(args):
#         if isinstance(value, (list, set, dict)):
#             print(f"Cannot add {value} to the dictionary.")
#         elif isinstance(value, str):
#             a_dict[value] = len(value)
#     return a_dict
#
# result = dictionary_length("hello", [1, 2, 3], "world", {1: 'a'}, "Python")
# print(result)
#
# # Task: Create a Dictionary of Argument Types
# # Write a function that accepts any number of arguments (*args).
# # For each argument:
# # If it's a string, add it to the dictionary with the value "string".
# # If it's an integer, add it with the value "integer".
# # If it's a float, add it with the value "float".
# # For any other type, print a message saying it can't be added.
# # Return the dictionary mapping argument values to their types.
#
# def argument_types(*args):
#     dictionary = {}
#     for index, value in enumerate(args):
#         if isinstance(value, str):
#             dictionary[value] = "string"
#         elif isinstance(value, int):
#             dictionary[value] = "integer"
#         elif isinstance(value, float):
#             dictionary[value] = "float"
#         else:
#             print(f"The {value} cannot be added to the dictionary. I am sorry.")
#     return dictionary
#
#
# # Task: Categorize Arguments and Count Their Occurrences
# # Write a function that accepts any number of arguments (*args).
# # For each argument:
# # Determine its type: "string", "integer", "float", or "other".
# # Count how many times each type appears.
# # Return a dictionary with the types as keys and their counts as values.
#
# def counting_occurrences(*args):
#     dictionary = {}
#     for value in args:
#         if isinstance(value, str):
#             key = "string"
#         elif isinstance(value, int):
#             key = "integer"
#         elif isinstance(value, float):
#             key = "float"
#         else:
#             key = "other"
#         if key in dictionary:
#             dictionary[key] += 1
#         else:
#             dictionary[key] = 1
#     return dictionary
#
# result = counting_occurrences("hello", 42, 3.14, None, "world", "sergiusz", False, 22, [1, 2, 3])
# print(result)
#
#
# # 1. Check if All Words Are Capitalized
# # Given a sentence, verify if each word starts with an uppercase letter.
#
# sentence = "Sergiusz Kuderski lubi zycie."
# words = sentence.split(" ")
# verification = []
# for word in words:
#     if word[0].isupper():
#         verification.append(True)
#     else:
#         verification.append(False)
#
# print(verification)
# print(all(verification))
#
# # 2. Remove All Punctuation
# # Remove all punctuation marks from a string, leaving only letters and numbers.
#
# import string
#
# other_sentence = "Sergiusz, Kuderski, kocha zycie.!"
# clean_word = other_sentence.strip(string.punctuation)
# print(clean_word)
#
# # 3. Find the Most Frequent Character
# # Identify the character that appears most frequently in a string (ignore case).
#
#
# sentence2 = "SErgiusz Kuderski"
# dictionary = {}
# for ch in sentence2:
#     ch = ch.lower()
#     if ch in dictionary:
#         dictionary[ch] += 1
#     else:
#         dictionary[ch] = 1
# print(dictionary)
# most_freq_char = max(dictionary, key=dictionary.get)
# print(most_freq_char)
# print(min(dictionary, key=dictionary.get))
#
# # 4. Count Words of a Certain Length
# # Count how many words in a sentence have more than 5 characters.
#
# sentence3 = "Dzien dobry Polsko Witajcie w 2026 roku."
# wordzz = sentence3.split(" ")
# count = 0
# for word in wordzz:
#     if len(word) > 5:
#         count += 1
#         print(word)
# print(count)
#
# # 5. Convert a String Into a Title Case
# # Transform a string so that each word starts with an uppercase letter
# # and the rest are lowercase.
# title_case = sentence3.title()
# print(title_case)
#
# # 6.Task: Generate a String of Unique Words
# # Given an input string, create a string containing all unique words from it.
# # Preserve the order of first appearance.
# # Remove duplicate words, but keep the original order.
#
# the_string2 = "Sergiusz Kuderski kocha zycie kocha Kuderski wodka"
# list_the_string = the_string2.split(" ")
# unq = set()
# ordered_unq = []
# for word in list_the_string:
#     if word not in unq:
#         unq.add(word)
#         ordered_unq.append(word)
# print(ordered_unq)
#
#
#
#
# # 7. Create a String of Unique Characters
# # Generate a string of all unique characters from an input string, preserving order.
#
# unique = set()
# the_string = "Sergiusz Kuderski"
# unique_chars = []
#
# for c in the_string:
#     c_lower = c.lower()
#     if c_lower not in unique:
#         unique.add(c_lower)
#         unique_chars.append(c)
# print(unique_chars)
#
# # 8. Check if a String is a Valid URL
# # Verify whether a string starts with 'http://' or 'https://'
# # and ends with a domain extension like '.com'.
#
# website = "http://www.onet.pl"
# if (website.startswith("http://") or website.startswith("https://")) and website.endswith(".com"):
#     print("Valid url")
# else:
#     print("Invalid url")
#
# # 9. Count Vowels and Consonants
# # Count the number of vowels and consonants in a string.
#
# some_very_cool_string = "Sergiusz Kuderski"
# count_vowels = 0
# count_consonants = 0
#
# for c in some_very_cool_string:
#     c_low = c.lower()
#     if c.isalpha():
#         if c_low in "aeiou":
#             count_vowels += 1
#         else:
#             count_consonants += 1
# print(f"vowels: {count_vowels}, consonants: {count_consonants}")
#
#
# # 10. Insert Spaces Before Capital Letters
# # Convert a camelCase string into a space-separated phrase
# # (e.g., "CamelCaseString" → "Camel Case String").
#
#
# camel_case_string = "CamelCaseString"
# camel_case = ""
# for i, c in enumerate(camel_case_string):
#     if c.isupper() and i is not 0:
#         camel_case += " "
#     camel_case += c
# print(camel_case)
#
# print(list(range(100)))
# result_list = []
#
# for i in range(100):
#     if "3" in str(i):
#         result_list.append(i)
# print(result_list)
#
# result_list_comprehended = [i for i in range(100) if "3" in str(i)]
# print(result_list_comprehended)


numbers = [1, 2, 3, 4, 5, 6]

squared_numbers = [(num * num) for num in numbers]
print(squared_numbers)

student_groups = [["group1", "group2"],
                  ["group3", "group4"]]

# new_group_list = []
# for group in student_groups:
#     new_group = []
#
#     for student in group:
#         new_group.append(student + " - Python")
#
#     new_group_list.append(new_group)
# print(new_group_list)

new_group_list = [
    [student + " - Python" for student in group]
    for group in student_groups
    ]
print(new_group_list)
hundred =[
    [
    [student + " - Python" for student in group]
    for group in student_groups
    ]
    for _ in range(100)

]
print(hundred)

# Create a dictionary with day names as keys and their abbreviations as values (e.g., 'Monday': 'Mon').

week_days = {"Monday": "Mon", "Tuesday": "Tue", "Wednesday": "Wed", "Thursday": "Thu", "Friday": "Fri"
             , "Saturday": "Sat", "Sunday": "Sun"}

print((week_days))


# Write a program to merge two dictionaries into one.

dict1 = {1: 2, 3: 4, 5: 6}
dict2 = {2: 3, 4: 5, 6: 7}
dict3 = {**dict1, **dict2}
print(dict3)


# Create a dictionary that maps integers from 1 to 5 to their squares.
dictio = {}
for i in range(1, 6):
    dictio[i] = i ** 2
print(dictio)



# Write a code to list all the keys in a dictionary.

print(list(dictio.keys()))


# Write a code to list all the values in a dictionary.

print(list(dictio.values()))

# Create a dictionary from two lists: one with names and one with ages.

list1 = ["Sergiusz", "Martyna", "Wiesiek"]
list2 = [31, 25, 69]
dicta = dict(zip(list1, list2))
print(dicta)


# Check if the dictionary is empty, and print a message accordingly.
asd = {}
if not asd:
    print("empty")


# Count the frequency of each word in a sentence and store the counts in a dictionary.

sentece = "Sergiusz Sergiusz Sergiusz"
dicaa = {}
for i in sentece.split():
    dicaa[i] = dicaa.get(i, 0) + 1
print(dicaa)


# Write a code to copy a dictionary (create a new copy of it).

d = dicaa.copy()
print(d)
print(id(dicaa))
print(id(d))

# Create a dictionary with default values using dict.get() when retrieving a key that might not exist.

print(dicaa.get("John", "doesn't exist"))

# 1. Sum all positional arguments using *args.

def summing(*args):
    count = 0
    for arg in args:
        count += arg
    return count
print(summing(1, 2, 3, 4, 5))

# 2. Create a greeting function that accepts a variable number of names and greets each one.

def greeting( *args):
    names  = ", ".join(args)
    return f"Hello, {names}"

print(greeting( "Johnny", "Sergiusz"))
# 3. Write a function that accepts any number of integers and returns their average.

def averages(*args):
    return sum(args) / len(args)

print(averages(1, 2, 3, 4))

# 4. Build a product function that multiplies any number of numbers supplied via *args.

def product(*args):
    num = 1
    for arg in args:
        num *= arg
    return num

print(product(1, 2, 3, 4, 5, 6, 7, 8))


# 5. Write a function that takes a fixed argument prefix, optional *args for suffixes,
#     and **kwargs for optional formatting options, then constructs and returns a string.

def some_function(name: str, *args, **kwargs):
    args_str = ", ".join(str(arg) for arg in args)
    kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())
    return f"{name}: {args_str}, {kwargs_str}"

print(some_function("Sergiusz", "30", country = "Greece", city = "Athens"))

# Write a function build_message(sender: str, *messages, **attributes) that constructs a message string:
#
# sender: the sender's name.
# *messages: any number of message parts.
# **attributes: optional key-value pairs describing the message, like "timestamp": "2023-09-15" or "priority": "high".
# The function should:
#
# Concatenate all message parts separated by spaces.
# Append the attributes at the end, formatted as key=value, separated by commas.
# Return a string that looks like:
# "From {sender}: {messages} [{attributes}]"

def build_message(sender: str, *args, **kwargs):
    message = " ".join(str(arg) for arg in args)
    attrs = ", ".join(f"{k}={v}" for k, v in kwargs.items())
    return (f"From {sender}: {message} [{attrs}]")

print(build_message("Alice", "Hi there!", "How are you?", timestamp="2023-09-15", priority="high"))

# 6. Implement a function that accepts any number of key-value pairs via **kwargs,
# and prints each key and value.

def implementingkwargs(**kwargs):
    return [f"{k} - {v}" for k, v in kwargs.items()]

print(implementingkwargs(name="Alice", age=30, city="New York"))

# 7. Write a function that can accept multiple lists via *args,
# and returns a single list concatenating everything.

def conc(*args):
    result = []
    for ls in args:
        result.extend(ls)
    return result

l = [1, 2, 3]
ll = [2, 3, 4]
lll = [2, 7, 2]
print(conc(l,ll,lll))

# Write a function that accepts any number of lists via *args, and returns a single list containing all elements from all the input lists,
# concatenated together.

def together(*args):
    return sum(args, [])

print(together(l, ll, lll))

# 8. Define a function with positional arguments, *args, and **kwargs,
# and demonstrate how to call it with various combinations.

def calling(*args, **kwargs):
    for arg in args:
        print(f"{arg}")
    print(f"{args}")

    for k, v in kwargs.items():
        print(f"{k} is {v}")
    print(f"all keyword arguments: {kwargs}")

calling(1, 2, 3, 4, x=10, y=20)

# Create a tuple containing the first five prime numbers.
import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
primes = []
num = 2
while len(primes) < 5:
    if is_prime(num):
        primes.append(num)
    num += 1

tuple_prime = tuple(primes)
print(tuple_prime)


# Write a function that takes a tuple of numbers and returns a new tuple with each number squared.

random_numbers = (12, 7, 19, 3, 45, 8)

randoms_sq = tuple((n ** 2 for n in random_numbers))
print(randoms_sq)


# Given two tuples, (a, b, c) and (x, y, z), create a new tuple that contains their element-wise sum.

first = (1, 2, 3)
second = (4, 5, 6)
third = tuple(a + b for a, b in zip(first, second))
print(third)

# Write a tuple containing the days of the week, then access and print the third day.

week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(week[2])


# Create a tuple of 10 random integers between 1 and 100. Find the maximum and minimum values in the tuple.

import random

r = tuple(random.randint(1, 100) for n in range(10))
print(r)

max_val = max(r)
min_val = min(r)
print(f"Maximum value: {max_val}")
print(f"Minimum value: {min_val}")


# Given a tuple with mixed data types, write code to access only the string elements.

mixed_tuple = (42, "Hello", 3.14, True, [1, 2, 3], {'a': 1})

for n in mixed_tuple:
    if isinstance(n, str):
        print(n)


# Convert a list of tuples [(1, 'a'), (2, 'b'), (3, 'c')] into a dictionary.

something = [(1, 'a'), (2, 'b'), (3, 'c')]

something_d = {a[0]: a[1] for a in something}
print(something_d)

# Write a function to swap the first and last elements of a tuple and return the new tuple.

def swapping(new: tuple):
    first = new[0]
    last = new[-1]
    middle = new[1:-1]
    swapped = (last,) + middle + (first,)
    return swapped



print(swapping((1, 2, 3, 4, 5, 6)))

# Create a tuple with 3 elements, and check if a specific value (e.g., 5) exists within the tuple.
aiaaaa = (1, 2, 3)
print(5 in aiaaaa)
# Write a program to concatenate two tuples (1, 2, 3) and (4, 5, 6) into a single tuple.

one1 = (1, 2, 3)
two2 = (4, 5, 6)
three = one1 + two2
print(three)