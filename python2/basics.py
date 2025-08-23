from multiprocessing.process import AuthenticationString

name = "Sergiusz"
surname = "Kuderski"
age = 31
height = 179.5
is_married = False

print(name, surname)
print(type(age), type(is_married))

milk_price = 50

bread_price = 20

total = milk_price + bread_price

print(total)

apple = 5
banana = 10

the_sum = apple + banana
difference = apple - banana
product = apple * banana
quotient = apple / banana

print(the_sum, difference, product, quotient)

length = 10
width = 20

area = length * width
perimeter = 2 * length + 2 * width

print(area, perimeter)

numbers = [1, 2, 3, 4, 5, 6, 7]

for n in numbers:
    print(n * 2 - 5)

the_bill = 200
tip_percentage = 0.05
tip = the_bill * tip_percentage
total_bill = the_bill + tip
split_bill = total_bill / 4
print(split_bill)

temperature = 50

temperature_fahrenheit = (temperature * 9/5) + 32
print(temperature_fahrenheit)

name = "SerggGiusZ"
name_lower = name.lower()
print(name_lower)

surname = "KKuDDerski"
surname_upper = surname.upper()
print(surname_upper)

city = "Athens"

user_data = name + " " + surname + ", " + city
print(user_data)

user_data_f = f"{name} {surname}, {city}"
print(user_data_f)

user_data_length = len(user_data)
print(user_data_length)
print(user_data_f[5].lower())

candy_price = 20
chocolate_price = 100

print(candy_price == chocolate_price)
print(candy_price > chocolate_price)
print(chocolate_price > candy_price)

is_gay = False
likes_women = True

print(not is_gay)
print(is_gay and likes_women)
print(is_gay or likes_women)

number = 11

print(number % 2 == 0)

first_num = 10
second_num = 20

print(first_num > second_num)

the_age = 20

print(the_age >= 18)

password = "the_password"

print(password == "the_password")

the_temp = 31
the_humidity = 30

print(the_temp > 30 and the_humidity < 50)


python_group = ["Alina", "Kacper", "Rozalia", "Anna"]
print(python_group)

students_grades = [78, 80, 90, 2]
print(students_grades)

python_group.append("Wojtek")
python_group.append("Julian")
print(python_group)
print(len(python_group))

first_student = python_group[0]
first_student_grades = students_grades[0]
print(first_student)
print(first_student_grades)

last_student = python_group[-1]
print(last_student)

students_grades[1] = 33
print(students_grades[1])
print(students_grades)

invitations = list(range(1, 21))
print(invitations)

invitations = list(range(1, 21, 3))
print(invitations)

numbers = []
for n in range(1, 11):
    numbers.append(n)
print(numbers)

my_favorite_fruits = ["banana", "apple", "strawberry", "fig"]
print(len(my_favorite_fruits))

the_colors = ["orange", "blue", "yellow", "green", "brown"]
print(the_colors[0], the_colors[-1])

some_list = []
some_list.append("dog")
some_list.append("cat")
some_list.append("capybara")
print(some_list)

empty_list = []
for n in range(0, 19, 2):
    empty_list.append(n)

print(empty_list)

another_empty_list = []
for n in range(10):
    another_empty_list.append(n*n)

print(another_empty_list)

cities = ["Warsaw", "Athens", "Buenos Aires", "Gdansk", "Wroclaw"]
print(cities[-1])

car_brands = ["Toyota", "Ford", "Honda", "BMW", "Mercedes-Benz"]
print(len(car_brands))

odd_numbers = []
for n in range(1, 20, 2):
    odd_numbers.append(n)

print(odd_numbers)

numbers = [11, 12, 13, 14, 15]
numbers[2] = 12
print(numbers)

temp = 20

if temp < 20:
    print("Wear a jacket")
else:
    print("You don't have to wear a jacket")


book_price = 100
money = 500

if book_price <= money:
    print("I can buy a book")

age = 20

if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")

n = 50

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
elif n == 0:
    print("Zero")
else:
    print("Incorrect number")

score = 95

if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Good")
elif score >= 60:
    print("Pass")
elif score < 60:
    print("Fail")
else:
    print("Incorrect score")

t = 35

if t > 30:
    print("Hot")
elif 15 <= temperature <= 30:
    print("Warm")
elif t < 15:
    print("Cold")

some_number = 10

if some_number % 2 == 0:
    print("Even")
else:
    print("Odd")

hour = 22

if 0 <= hour <= 11:
    print("Good morning")
elif 12 <= hour <= 17:
    print("Good afternoon")
elif 18 <= hour <= 23:
    print("Good evening")
else:
    print("Incorrect value")

password = "le password"

if password == "le password":
    print("Access granted.")
else:
    print("Access denied.")

first = 10
second = 20

if first > second:
    print("First # is greater than the second")
elif first < second:
    print("Second # is greater than the first")
else:
    print("Both numbers are equal.")

day = 10

if day == 1:
    print("It is Monday")
elif day == 2:
    print("It is Tuesday")
elif day == 3:
    print("It is Wednesday")
elif day == 4:
    print("It is Thursday")
elif day == 5:
    print("It is Friday")
elif day == 6:
    print("It is Saturday")
elif day == 7:
    print("It is Sunday")
else:
    print("Invalid day.")

num1 = 10
num2 = 20
operation = "-"

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("Invalid operation")

total_savings = 0
monthly_increase = 100

for n in range(1, 13):
    total_savings += monthly_increase
    print(f"Month {n} : {total_savings} saved")

for n in range(1, 11):
    print(n)

the_summary = 0

for n in range(1, 51):
    the_summary += n

print(the_summary)

fruits = ["Apple", "Banana", "Orange", "Grapes", "Strawberry"]

for fruit in fruits:
    print(fruit)

for n in range(2, 21, 2):
    print(n)

squares = []

for n in range(1, 11):
    squares.append(n*n)

print(squares)
counter = 0
for f in fruits:
    counter += 1

print(counter)

name = "Sergiusz"

for c in name:
    print(c.lower())

for fruit in range(len(fruits) -1, -1, -1):
    print(fruits[fruit])

# savings = 100
# book_p = 20
# books_to_buy = savings // book_p
#
# for _ in range(books_to_buy):
#     if savings >= book_p:
#         savings -= book_p
#         print(f"I bought a book. I have {savings} left.")
#     else:
#         break

savings = 100
book_pri = 20
books_bought = 0

while savings >= book_pri:
    books_bought += 1
    savings -= book_pri
    print(f"I bought a book. I have {savings} left.")

starting_n = 0

while starting_n < 10:
    starting_n += 1
    print(starting_n)

s_num = 10

while s_num > 0:
    s_num -= 1
    print(s_num)

count = 1
sumary = 0
while sumary < 50:
    sumary += count
    print(sumary)

number = 2

while number <= 20:
    print(number)
    number += 2