name = "Sergiusz"
last_name = "Kuderski"
height = 179
age = 30
is_married = False

print(name, last_name)
print(type(age), type(is_married))

print(height + age)
print(age - height)

apples = 1.5
friends = 3
result = apples / friends
print(result) # 0.5

print(type(friends))

budget = 50
milk_price = 3
bread_price = 2

rest = budget - (milk_price + bread_price)
print(rest)

first_name = "Sergiusz"
name_lower = first_name.lower()

print(name_lower)

last_name = "KuDeRsKi"
name_upper = last_name.upper()

print(name_upper)

name = "Sergiusz"
surname = "Kuderski"
age = "30"
height = "179"

details = f"My name is {name} {surname}. I am {age} years old. I am {height} cm tall."
print(details)

different_details = "Nazywam sie " + name + " " + surname + ". " + "Mam " + age + " lat"+". " + "Moj wzrost to " + height + " cm."
print(different_details)

print(len(different_details))

list_of_books = ["The Lord of the Rings", "1984", "The Great Gatsby"]
list_of_books[1] = "The Hobbit"
print(list_of_books)

book_pages = range(0, 51, 5)
list_of_book_pages = list(book_pages)
print(list_of_book_pages)

# sum_of_number = 0
#
# for number in range(5, 16):
#     sum_of_number += number
# print(sum_of_number)

sum_of_numbers = 0

for number in range(5, 16, 2):
    sum_of_numbers += number

print(sum_of_numbers)

initial_distance = 5
increment = 2
total_weeks = 10

for week in range(total_weeks):
    weekly_distance = initial_distance + (week * increment)
    print(f"week {week}: {weekly_distance}")

# count = 0
# max_count = 10
# while count < max_count:
#     count += 1
#     print(count)

count = 1

while count <= 10:
    print(count)
    count += 1

fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

for fruit in fruits:
    if len(fruit) > 5:
        print(fruit)

def hello(you:str):
    print(f"Hello, {you}")
hello("Sergiusz")

def area(a, h):
    print(int(a*h/2))
area(5,2)


def add_interest(balance, interest_rate):
    increment = balance * (interest_rate / 100)
    return balance + increment


initial_balance = 1000
new_balance = add_interest(initial_balance, 5)
result_balance = add_interest(new_balance, 5)
print(new_balance)
print(result_balance)
