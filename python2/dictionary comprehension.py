numbers = [1, 2, 4, 5, 6, 7, 8]

squares = {}

for num in numbers:
    squares[num] = num ** 2

print(squares)

squares2 = {num: num ** 2 for num in numbers}
valuessq2 = {num ** 2 for num in numbers}
print(type(valuessq2))

print(squares2)
print(valuessq2)

hello = "hello"

symbols = {}

for ch in hello:
    if ch not in symbols:
        symbols[ch] = 1
    else:
        symbols[ch] += 1
print(symbols)

def sum_3() -> int:
    return sum([num for num in range(100) if "3" in str(num)])
print(sum_3())

def make_upper_case(words: str):
    return " ".join([word.upper() for word in words.split() if len(word) > 5])

print(make_upper_case("Sergiusz Kuderski lubi jesc"))

productz = [
    ("Apple", 0.99, 10),
    ("Banana", 0.59, 20),
    ("Orange", 1.29, 15)
]

def products(p: list) -> dict:
    return {product[0]: {"price": product[1], "quantity": product[2]}
    for product in p}

print(products(productz))


cities = [
    ("Paris", "France", 2148327),
    ("Berlin", "Germany", 3644826),
    ("Madrid", "Spain", 3223334)
]

def count_dict(l: list) -> dict:
    return {
        city[0]:
            {"country": city[1], "population": city[2]
             }
        for city in l
    }
print(count_dict(cities))
students = [
    ("Alice", 88, "B+"),
    ("Bob", 92, "A-"),
    ("Charlie", 79, "C+")
]

def grading(ls: list) -> dict:
    return {student[0]: {"score": student[1], "grade": student[2]} for student in ls}
print(grading(students))

cities = {
    "London": 15,
    "Paris": 20,
    "Tokyo": 25,
    "New York": 18
}

def above(l: dict, temp) -> dict:
    return {k: v for k, v in l.items() if v > temp}

print(above(cities, 18))

products = {
    "Book": 12.99,
    "Pen": 1.99,
    "Notebook": 5.49,
    "Headphones": 49.99
}

def below_p(l: dict, amount: int) -> dict:
    return {key: value for key, value in l.items() if value < amount}

print(below_p(products, 10))

# Given a dictionary of students with their total points,
# create a new dictionary that includes only the students who scored above the average score.

students_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 88,
    "Eve": 76
}

def above_average(scores: dict):
    average = sum(scores.values()) / len(scores)
    return {student: score for student, score in scores.items() if score > average}

print(above_average(students_scores))

# Given a list of lists where each inner list contains daily temperatures for different cities over a week,
# create a function that groups together the temperatures for each particular day across all cities.
city_temps = [
    [70, 72, 68, 71, 69, 70, 72],  # City 1
    [65, 67, 66, 64, 66, 65, 67],  # City 2
    [80, 81, 79, 78, 80, 82, 81]   # City 3
]

def temps(t: list) -> list:
   return [[day[i] for day in t] for i in range(len(t[0]))]

print(temps(city_temps))

# Given a list of lists where each inner list represents the scores of a student across different subjects,
# create a function that groups all scores for each subject into separate lists.
student_scores = [
    [80, 90, 70],  # Student 1
    [85, 88, 76],  # Student 2
    [78, 92, 68]   # Student 3
]

def lol(ls: list) -> list:
    return [[score[i] for score in ls] for i in range(len(ls[0]))]

print(lol(student_scores))


# Create a dictionary where keys are numbers from 1 to 5, and values are their factorials.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
dicasa = {n: factorial(n) for n in range(1, 6)}
print(dicasa)

# Create a dictionary where the keys are the numbers from 1 to 10,
# and the values are the squares of those numbers, using a dictionary comprehension.

asdasasda = {k: k ** 2 for k in range(1, 11)}
print(asdasasda)


# Given a list of fruits, create a dictionary mapping each fruit to its length.

fruits = ["apple", "banana", "orange", "grape", "kiwi",
          "mango", "pineapple", "strawberry", "blueberry", "watermelon"]

fruitsd = {fruit: len(fruit) for fruit in fruits}
print(fruitsd)

# Given a list of fruits, create a dictionary where:
#
# The key is the fruit name.
# The value is a tuple containing: The fruit's length.
# The fruit's name in uppercase. A boolean indicating if the fruit's length is greater than 5.


asagqw = {fruit: (len(fruit), fruit.upper(), len(fruit) > 5) for fruit in fruits}
print(asagqw)

# Create a dictionary mapping each letter in the string "hello" to the number of times it appears.

hell = "hello"

hello_dict = {c: hell.count(c) for c in hell}
print(hello_dict)

# Given a string, create a dictionary that maps each unique character to the number of times it appears,
# but only include characters that appear more than once.

name = "Sergiuszek"
named = {c.lower(): name.lower().count(c.lower())  for c in set(name) if name.lower().count(c.lower()) > 1}
print(named)



# From a list of person tuples (name, age), create a dictionary mapping names to ages.

persons = [
    ("Alice", 30),
    ("Bob", 25),
    ("Charlie", 35),
    ("Diana", 28),
    ("Edward", 40),
    ("Fiona", 22),
    ("George", 33),
    ("Hannah", 27),
    ("Ian", 31),
    ("Jane", 29)
]
dicpersons = {person[0]:person[1] for person in persons}
print(dicpersons)


# Create a dictionary from 0 to 9 where each key is the number,
# and the value is whether the number is a prime (True/False).

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primedict = {n: is_prime(n) for n in range(10)}
print(primedict)


# Construct a dictionary where keys are numbers from 1 to 10, and values are the number multiplied by 2,
# but only include even numbers.

qwgqg = {key: key * 2 for key in range(1, 11) if key % 2 == 0}
print(qwgqg)

# Create a dictionary where the keys are numbers from 1 to 20, and the values are the square of each number.
# But only include keys where the number is divisible by 3 or 5.


asgqwgq = {key: key ** 2 for key in range(1, 21) if key % 3 == 0 or key % 5 == 0}
print(asgqwgq)

# Given a string of text, create a dictionary mapping each character to its ASCII value.

text = "Sergiuszek"
diasc = {key: ord(key) for key in text}
print(diasc)

# Given a list of words,
# create a dictionary that maps each word to the sum of the ASCII values of all its characters.

words = [
    "lion", "tiger", "elephant", "giraffe", "zebra",
    "monkey", "panda", "kangaroo", "gorilla", "fox",
    "wolf", "bear", "deer", "coyote", "rabbit"
]

gqwgqwg = {word: sum(ord(c) for c in word) for word in words}
print(gqwgqwg)





# Create a dictionary where keys are numbers from 1 to 7, and values are the day of the week (Monday to Sunday).

numberss = [1, 2, 3, 4, 5, 6, 7]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

agqqg = {number: day for number, day in  zip(numbers, days)}
print(agqqg)

# Create a dictionary where the keys are the numbers from 10 to 15, and the values are their squares.

sq = {num: num ** 2 for num in range(10, 16)}
print(sq)

# Create a dictionary where the keys are numbers from 1 to 12,
# and the values are the corresponding months of the year ("January" to "December").

ns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

combinator = {n: month for n, month in zip(ns, months)}
print(combinator)

# Create a dictionary where the keys are the days of the week ("Monday" to "Sunday"),
# and the values are the number of letters in each day’s name.

qwerty = {day: len(day) for day in days}
print(qwerty)


# From a list of cities, create a dictionary where the city name is the key,
# and the value is the city name in uppercase.

cities1 = ["New York", "London", "Tokyo", "Paris", "Berlin",
          "Sydney", "Madrid", "Rome", "Toronto", "Dubai"]

citiesdic = {city: city.upper() for city in cities1}
print(citiesdic)

# Given the list of cities, create a dictionary where:
#
# The key is the city name.
# The value is the length of the city name.
# Only include cities where the length of the city name is greater than 5.

citiesd = {city: len(city) for city in cities1 if len(city) > 5}
print(citiesd)


# Create a dictionary where keys are the first 5 positive integers,
# and values are their squares, but only for odd numbers.

qqwqr = {key: key ** 2 for key in range(1, 6) if key % 2 != 0}
print(qqwqr)

# Create a dictionary where the keys are the numbers from 1 to 20,
# and the values are the factorials of those numbers,
# but only include the keys where the number is divisible by either 3 or 4.

factd = {n: factorial(n) for n in range(1, 21) if n % 3 == 0 or n % 4 == 0}
print(factd)

# Practice Task:
# Suppose you have raw data for multiple products in a store,
# in a dictionary where each key is a product name,
# and each value is a list of error messages related to that product.
#
# Write a series of functions to produce a structured report:
#
# Create a function format_product_error(error: str) -> dict
# that converts each raw error message into a dictionary with keys:
#
# "message": the original error message.
# "severity": assign "high" if the message contains the word "critical" (case-insensitive), otherwise "low".

# Create a function format_product(product_name: str, errors: list) -> dict
# that formats each product's data into a dictionary:
#
# "name": the product name.
# "errors": a list of formatted error dicts from format_product_error().
# "status": "problematic" if there are any errors, otherwise "OK".
# Create a function generate_report(products_data: dict) -> list
# that produces a list of formatted product reports, using the previous functions.


# def format_product_error(error: str) -> dict:
#     severity = "high" if "critical" in error.lower() else "low"
#     return {
#         "message": error,
#         "severity": severity
#     }
#
# def format_product(product_name: str, errors: list) -> dict:
#     status = "problematic" if errors else "OK"
#     return {
#         "name": product_name,
#         "errors": [format_product_error(error) for error in errors],
#         "status": status
#     }
#
# def generate_report(products_data: dict) -> list:
#     return [
#         format_product(product_name, errors) for product_name, errors in products_data.items()
#     ]
#
# print(generate_report(products_data = {
#     "Smartphone": ["Critical battery drain", "Screen flickering"],
#     "Laptop": ["Overheating issue", "Keyboard not working"],
#     "Tablet": ["Critical Bluetooth connectivity problem"],
#     "Printer": ["Paper jam", "Low ink warning"],
#     "Monitor": []
# }))
#
# # Suppose you have raw data about students and the courses they are enrolled in,
# # stored as a dictionary where each key is a student name, and each value is a list of grades for their courses.
# #
# # Write a series of functions to produce a structured report:
# #
# # Create a function format_grade(grade: float) -> dict that converts each grade into a dictionary with keys:
# #
# # "grade": the original grade.
# # "status": "pass" if the grade is 60 or above, otherwise "fail".
# # Create a function format_student(name: str, grades: list) -> dict
# # that formats each student's data into a dictionary:
# #
# # "name": the student's name.
# # "grades": a list of formatted grade dicts from format_grade().
# # "status": "good standing" if the student has no failing grades, otherwise "probation".
# # Create a function generate_student_report(students_data: dict) -> list
# # that produces a list of formatted student reports using the previous functions.
#
# # def format_grade(grade: float) -> dict:
# #     status = "pass" if grade >= 60 else "fail"
# #     return {
# #         "grade" : grade,
# #         "status" : status
# #     }
# #
# # def format_student(name: str, grades: list) -> dict:
# #     if all(g['status'] == 'pass' for g in [format_grade(g) for g in grades]):
# #         status = "good standing"
# #     else:
# #         status = "probation"
# #     return {
# #         "name": name,
# #         "grades": [format_grade(g) for g in grades],
# #         "status": status
# #     }
# #
# # def generate_student_report(students_data: dict) -> list:
# #     return [
# #         format_student(name, grades) for name, grades in students_data.items()
# #     ]
# #
# # print(generate_student_report(students_data = {
# #     "Alice": [75, 80, 90],
# #     "Bob": [55, 65, 70],
# #     "Charlie": [60, 45, 80],
# #     "Diana": [85, 92, 88],
# #     "Evan": [50, 55, 58]
# # }
# # ))
#
# # New Practice Task:
# # Suppose you have a dictionary where keys are employee names, and values are lists of their sales figures.
# # Write functions to produce a structured report:
# #
# # Create a function format_sale(sale: float) -> dict:
# #
# # "amount": the sale amount.
# # "performance": "above target" if the sale is above 1000, otherwise "below target".
# # Create a function format_employee(name: str, sales: list) -> dict:
# #
# # "name": employee name.
# # "sales": list of formatted sale dicts.
# # "status": "performance", if the average sale is above 1000; otherwise, "needs improvement".
# # Create a function generate_employee_report(employees_data: dict) -> list:
# #
# # Produces a list of employee reports in the desired format.
#
# # def format_sale(sale: float) -> dict:
# #     performance = "above target" if sale > 1000 else "below target"
# #     return {
# #         "amount": sale,
# #         "performance": performance
# #     }
# #
# # def format_employee(name: str, sales: list) -> dict:
# #     average_sale = sum(sales) / len(sales)
# #     status = "performance" if average_sale > 1000 else "needs improvement"
# #     return {
# #         "name": name,
# #         "sales": [format_sale(sale) for sale in sales],
# #         "status": status
# #     }
# #
# # def generate_employee_report(employees_data: dict) -> list:
# #     return [
# #         format_employee(name, sales) for name, sales in employees_data.items()
# #     ]
# #
# # print(generate_employee_report(employees_data = {
# #     "Alice": [1200, 950, 1300],
# #     "Bob": [800, 900, 850],
# #     "Charlie": [1500, 1600, 1550],
# #     "Diana": [700, 720, 680]
# # }))
#
# # Suppose you have a dictionary where the keys are student names, and the values are lists of exam scores.
# #
# # Write functions to produce a structured report:
# #
# # Create a function format_score(score: float) -> dict:
# #
# # "score": the exam score.
# # "grade": "pass" if the score is 60 or higher, otherwise "fail".
# # Create a function format_student(name: str, scores: list) -> dict:
# #
# # "name": student name.
# # "scores": list of formatted score dicts.
# # "status": "passing" if the average score is 60 or higher; otherwise, "failing".
# # Create a function generate_student_report(students_data: dict) -> list:
# #
# # Produces a list of student reports in the specified format.
#
# def format_score(score: float) -> dict:
#     grade = "pass" if score >= 60 else "fail"
#     return {
#         "score": score,
#         "grade": grade,
#     }
#
# def format_student(name: str, scores: list) -> dict:
#     avg = sum(scores) / len(scores)
#     status = "passing" if avg >= 60 else "failing"
#     return {
#         "name": name,
#         "scores": [format_score(score) for score in scores],
#         "status": status
#     }
#
# def generate_student_report(students_data: dict) -> list:
#     return [
#         format_student(name, scores) for name, scores in students_data.items()
#     ]
#
# # New task:
# # Given a dictionary where keys are employee names and values are lists of their monthly sales figures,
# #
# # Create a function format_sale(sale: float) -> dict that returns a dictionary with:
# #
# # "amount": the sale amount
# # "status": "above target" if the sale is greater than or equal to 1000, otherwise "below target".
# # Create a function format_employee(name: str, sales: list) -> dict that returns a dictionary with:
# #
# # "name": employee name
# # "sales": list of formatted sale dictionaries
# # "average": the average sale amount
# # "performance": "good" if the average sale is at least 1000, otherwise "needs improvement"
# # Create a function generate_employee_report(employees_data: dict) -> list
# # that produces a list of all employee reports.
#
# def format_sale(sale: float) -> dict:
#     status = "above target" if sale >= 1000 else "below target"
#     return {
#         "amount": sale,
#         "status": status
#     }
#
# def format_emp(name: str, sales: list) -> dict:
#     avg = sum(sales) / len(sales)
#     return {
#         "name": name,
#         "sales": [format_sale(sale) for sale in sales],
#         "average": avg,
#         "performance": "good" if avg >= 1000 else "needs improvement"
#     }
#
# def generate_emp_rep(employees_data: dict) -> list:
#     return [
#         format_emp(name, sales) for name, sales in employees_data.items()
#     ]
#
# print(generate_emp_rep({
#     "Alice": [1200, 950, 1050],
#     "Bob": [950, 860, 920],
#     "Charlie": [1300, 1350, 1280]
# }))

# Given a dictionary where keys are employee names and values are lists of their monthly sales figures,
# create a function `format_sale(sale: float) -> dict` that returns a dictionary with:
#   - "amount": the sale amount
#   - "status": "above target" if the sale is >= 1000, otherwise "below target".
#
# Then, create a function `format_employee_summary(name: str, sales: list) -> dict` that:
#   - "name": employee name
#   - "total_sales": sum of all sales
#   - "average": average sales
#   - "status": "top performer" if total_sales >= 10,000,
#               "average" if total_sales between 5,000 and 9,999,
#               "needs improvement" if below 5,000.
#
# Finally, use a list comprehension to generate a list of employee reports based on the dictionary,
# utilizing the above functions.

def format_sale(sale: float) -> dict:
    status = "above target" if sale >= 1000 else "below target"
    return {
        "amount": sale,
        "status": status
    }

def format_employee_summary(name: str, sales: list) -> dict:
    total_sales = sum(sales)
    avg = sum(sales) / len(sales)
    if total_sales >= 10000:
        status = "top performer"
    elif total_sales >= 5000:
        status = "average"
    else:
        status = "needs improvement"

    return {
        "name": name,
        "total_sales": total_sales,
        "average": avg,
        "status": status
    }

def report(data: dict) -> list:
    return [
        format_employee_summary(name, sales) for name, sales in data.items()
    ]

print(report({
    "Alice": [1200, 950, 1300],
    "Bob": [950, 860, 920],
    "Charlie": [13000, 13500, 12800],
    "Diana": [3000, 3500, 3100]
}
))

# Create a dictionary where the keys are numbers from 1 to 10 and the values are their squares.

squaresdict = {n: n ** 2 for n in range(1, 11)}
print(squaresdict)

# Make a dictionary that maps each lowercase letter ('a' to 'z') to its uppercase equivalent.

chr = {chr(n):chr(n).upper() for n in range(97, 123)}
print(chr)


# Construct a dictionary of the first 10 positive integers and their factorials.
import math
factorial_dict = {n: math.factorial(n) for n in range(1, 11)}
print(factorial_dict)

# Create a dictionary where the keys are numbers from 1 to 15 and the values are their cubes,
# but only include numbers that are divisible by 3.

cubes_dict = {n: n ** 3 for n in range(1, 16) if n % 3 == 0}
print(cubes_dict)


# Build a dictionary where the keys are students' names and values are their grades, given two separate lists of names and grades.

names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
grades = [85, 92, 78, 90, 88]

zipped = {name: grade for name, grade in zip(names, grades)}
print(zipped)


# Generate a dictionary where the keys are numbers from 0 to 20, and the values are True if the number is even, False otherwise.

true_dict = {n: True if n % 2 == 0 else False for n in range(21)}
print(true_dict)


# Create a dictionary where the keys are strings "Number X" for X from 1 to 5, and values are X squared.

stringed_dict = {f"Number {n}": n ** 2 for n in range(1, 6)}
print(stringed_dict)

# Construct a dictionary from a list of tuples (name, age) to map names to ages.

people = [
    ('Alice', 25),
    ('Bob', 30),
    ('Charlie', 22),
    ('David', 28),
    ('Eve', 35)
]

people_dict = {tup[0]: tup[1] for tup in people}
print(people_dict)

# Create a dictionary mapping each word in a sentence to its length.

sentence = "Python programming is fun and versatile."

len_s = {word.strip("."): len(word.strip(".")) for word in sentence.split(" ")}
print(len_s)

# Create a dictionary where the keys are numbers from 1 to 10, and the values are dictionaries containing their 'double' and 'triple' values.

cool_dict = {n: {"double": n * 2, "triple": n * 3} for n in range(1, 11)}
print(cool_dict)