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

list_of_numbers = [0, 1, 2, 3, 4, 5, 6]
print(any(list_of_numbers))

# 2. Verify All Strings Are Uppercase
# Check if all strings in a list are uppercase letters.

the_list = ["SERGIUSZ", "KUDERSKI"]
print(all(s.isupper() for s in the_list))

# 3. Find If Any Element is Empty
# Given a list of strings, determine if any string is empty ("").

list_of_strings = ["", "sergiusz", "kuderski"]
print(any(s == "" for s in list_of_strings))

# 4. Check if All Elements are Even
# Verify if all numbers in a list are even.

list_nums = [2, 4, 6, 8]
print(all(num % 2 == 0 for num in list_nums))


# 5. Check if Any Number is Negative
# Determine if any number in the list is negative.

list_of_nums = [2, 4, 6, 8]
print(any(num < 0 for num in list_of_nums))


# 6. Verify All Characters Are Alphabets
# Given a string, check whether all characters are alphabetic.

text = "sergiusz"
print(all(s.isalpha() for s in text))

# 7. Find if Any Student Passed
# Given a list of test scores, determine if any student scored above 90.

list_of_scores = [100, 90, 40, 30]
print(any(score > 90 for score in list_of_scores))


# 8. Check If All Items Are Unique
# Given a list, determine if all items are different (no duplicates).

items = ["desk", "wardrobe", "leg", "desk"]
items_set = set(items)
if len(items) != len(items_set):
    print("all items are not unique")
else:
    print("all items are unique")



# 9. Verify if Any String Contains a Specific Letter
# Check if any string in a list contains the letter 'z'.

list_of_str = ["sergiusz", "kuderski"]
print(any("z" in ch for ch in list_of_str))

# 10. Check if All Files are Closed
# Given a list of boolean flags indicating file status (True for closed, False for open), verify if all files are closed.

files = [False, False, False, True]
print(all(files))
