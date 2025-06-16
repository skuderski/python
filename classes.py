import datetime

# class Pizza:
#    def __init__(self, sauce: str, toppings: str, cheese: str):
#        self.sauce = sauce
#        self.toppings = toppings
#        self.cheese = cheese
#
#
# margherita_pizza = Pizza("tomato sauce", "tomatoes", "mozzarella")
# buffalo_pizza = Pizza("buffalo sauce", "mushrooms", "provolone")
#
# class User:
#    def __init__(self, name: str, surname: str):
#        self.name = name
#        self.surname = surname
#
# first_user = User("Joseph", "Green")
#
# print(first_user.name)
# print(first_user.surname)


class User: #PascalCase
    pass

user1 = User()

user1.name = "John"
user1.age = 25

user2 = User()
user2.name = "Emily"
user2.age = 20

class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

user1 = User("John", 25)
user2 = User("Emily", 20)

print(user1.name)
print(user2.age)

user1 = User(
    name = "John",
    age = 30
)

class Robot:
    def __init__(self, name: str) -> None:
        self.partner = None
        self.name = name


def pair_robots(robots: list) -> tuple:
    robots1 = Robot(robots[0])
    robots2 = Robot(robots[1])
    robots1.partner = robots2
    robots2.partner = robots1
    return (robots1, robots2)

# Create a Dog Class:
#
# Create a class called Dog.
# Give it an __init__ method that takes a name attribute.
# Create an object of the Dog class.

class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def bark(self):
        print("Woof!")
my_dog = Dog("Buddy", 3)
my_dog.bark()
print(my_dog.name)
print(my_dog.age)


# Add a bark() Method:
#
# Add a method called bark() to the Dog class.
# Make the bark() method print "Woof!".
# Call the bark() method on your Dog object.

# Add an age Attribute:
# Add an age attribute to the Dog class's __init__ method.
# When creating a Dog object, set the age.
# Print the age of your Dog object.

# Create a Person Class:
#
# Create a class called Person.
# Give it name and age attributes in the __init__ method.
# Create two Person objects with different names and ages.

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name}")



person_one = Person("Sergiusz", 30)
person_two = Person("Irena", 62)

print(person_two.name)
print(person_one.age)
person_two.greet()
person_one.greet()


# Person Greeting:
#
# Add a method called greet() to the Person class.
# Make the greet() method print "Hello, my name is [name]".
# Call the greet() method on one of your Person objects.

# BankAccount Class:
#
# Create a class called BankAccount.
# Give it an attribute called balance initialized to 0 in the __init__ method.

class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
account = BankAccount()
print(account.balance)
account.deposit(500)
print(account.balance)
account.withdraw(300)
print(account.balance)
# deposit() Method:
#
# Add a method called deposit() to the BankAccount class.
# The deposit() method should take an amount as input and add it to the balance.

# withdraw() Method:
#
# Add a method called withdraw() to the BankAccount class.
# The withdraw() method should take an amount as input and subtract it from the balance.
# Make sure to check if the amount is greater than the balance before withdrawing.


# Create Book Class:
#
# Create a class called Book.
# Give it title, author, and pages attributes in the __init__ method.

class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
    def describe(self):
        print(f"This book is titled {self.title} by {self.author} and has {self.pages} pages.")
book = Book("Harry Potter", "J. K. Rowling", 300)
book.describe()

# Book Description:
#
# Add a method called describe() to the Book class.
# Make the describe() method print a sentence describing the book (e.g., "This book is titled [title] by [author] and has [pages] pages.").
# Call the describe() method on one of your Book objects.


# Car Class with start() and stop():
#
# Create a Car class with attributes: make, model, year, is_running (default False).
# Add methods: start() (sets is_running to True and prints "Engine started") and stop() (sets is_running to False and prints "Engine stopped").

class Car:
    def __init__(self, make, model, year, is_running: bool = False):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = is_running
    def start(self):
        self.is_running = True
        print("Engine started")
    def stop(self):
        self.is_running = False
        print("Engine stopped")

my_car = Car("Toyota", "Corolla", 2025)
print(my_car.is_running)
my_car.start()
print(my_car.is_running)
my_car.stop()
print(my_car.is_running)
# # Rectangle Class with Area and Perimeter:
# Create a Rectangle class with attributes: width, height.
# Add methods: calculate_area() (returns the area) and calculate_perimeter() (returns the perimeter).

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

my_rectangle = Rectangle(2, 5)
print(f"{my_rectangle.calculate_area()}")
print(f"{my_rectangle.calculate_perimeter()}")
# Student Class with Grades:
# Create a Student class with attributes: name, student_id, grades (an empty list initially).
# Add methods: add_grade(grade) (appends a grade to the grades list) and calculate_average() (returns the average of the grades).
# Handle the case where the grades list is empty.


class Student:
    def __init__(self, name, student_id, grades: list = None):
        self.name = name
        self.student_id = student_id
        self.grades = grades or []
    def add_grade(self, grade):
        self.grades.append(grade)
    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

student_one = Student("Sergiusz", 15, [1, 2, 3, 5, 10])
student_one.add_grade(2)
student_one.add_grade(3)
print(student_one.grades)
print(student_one.calculate_average())

# Circle Class with Radius and Area:
# Create a Circle class with attribute: radius.
# Add a method calculate_area() that returns the area of the circle (use math.pi). Remember to import math.
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * self.radius **2
my_circle = Circle(2)
my_circle.calculate_area()



# Employee Class with Salary and Raise:
# Create an Employee class with attributes: name, employee_id, salary.
# Add a method give_raise(amount) that increases the salary by the given amount.

class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    def give_raise(self, amount):
        self.salary += amount

employee_one = Employee("John", 22, 2000)
employee_one.give_raise(1000)
print(employee_one.salary)

# Product Class with Discount:
# Create a Product class with attributes: name, price.
# Add a method apply_discount(discount_percent) that reduces the price by the given discount_percent (e.g., 10 for 10%).
# Make sure to update the price attribute.


class Discount:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def apply_discount(self, discount_percent):
        self.price -= (self.price * discount_percent / 100)
item = Discount("fridge", 1000)
item.apply_discount(10)
print(item.price)

# Playlist Class with Songs:
# Create a Playlist class with attribute: songs (an empty list initially).
# Add methods: add_song(song_name) (adds a song to the songs list) and list_songs() (prints each song in the playlist).

class Playlist:
    def __init__(self, songs = None):
        self.songs = songs or []
    def add_song(self, song):
        self.songs.append(song)
    def list_songs(self):
        for song in self.songs:
            print(f"{song}")
my_playlist = Playlist(["Billie Jean", "Nam s toboy", "Kukushka"])
my_playlist.add_song("Konchitsa Leto")
my_playlist.list_songs()


# Point Class with Distance:
# Create a Point class with attributes: x, y.
# Add a method calculate_distance(other_point) that calculates the distance between the current point and another Point object.
# Use the distance formula: sqrt((x2 - x1)**2 + (y2 - y1)**2). You'll need to import math.

import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def calculate_distance(self, other_point):
        return math.sqrt((other_point.x - self.x)**2 + (other_point.y - self.y)**2)

the_point = Point(5, 10)
other_point = Point(2, 20)
distance = the_point.calculate_distance(other_point)
print(distance)


# Animal Class with a Method and Inheritance (Very Basic):

# Create an Animal class with a method speak() that prints "Generic animal sound".
# (Introduction to inheritance): Create a Dog class that inherits from the Animal class.
# Override the speak() method in the Dog class to print "Woof!". (This is your first taste of inheritance and polymorphism!)

# class Animal:
#     def speak(self):
#         print("Generic animal sound")
#
# class Dog(Animal):
#     def speak(self):
#         print("Woof")
#
# animal = Animal()
# dog = Dog()
#
# animal.speak()
# dog.speak()


# TemperatureConverter Class:
#
# Create a TemperatureConverter class.
# Add methods: celsius_to_fahrenheit(celsius) (returns Fahrenheit) and fahrenheit_to_celsius(fahrenheit) (returns Celsius).
# Use the conversion formulas.

class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        result = (celsius * 9/5) + 32
        return result
    def fahrenheit_to_celsius(self, fahrenheit):
        result = (fahrenheit - 32) * 5/9
        return result
celsius = TemperatureConverter()
print(celsius.celsius_to_fahrenheit(10))
fahrenheit = TemperatureConverter()
print(fahrenheit.fahrenheit_to_celsius(20))

class Book:
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

book = Book("My favourite book", 42)

# Extending the Car Class (Inheritance):
# Start with your existing Car class (with make, model, year, is_running, start(), stop()).
# Create an ElectricCar class that inherits from the Car class.
# Add a new attribute battery_capacity to the ElectricCar class.
# Override the start() method in the ElectricCar class to also print "Electric motor started silently"
# in addition to the base Car's "Engine started".

# class Car:
#     def __init__(self, make, model, year, is_running: bool = False):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.is_running = is_running
#     def start(self):
#         self.is_running = True
#         print("Engine started.")
#     def stop(self):
#         self.is_running = False
#         print("Engine stopped")

# class ElectricCar(Car):
#     def __init__(self, make, model, year, battery_capacity, is_running:bool = False):
#         super().__init__(make, model, year, is_running)
#         self.battery_capacity = battery_capacity
#     def start(self):
#         super().start()
#         print("Electric motor started silently.")
#
# my_car = ElectricCar("Tesla", "Model S", 2023, 100)
# my_car.start()


# BankAccount with Transaction History:
# Start with your existing BankAccount class (with balance, deposit(), withdraw()).
# Add a new attribute transaction_history that is a list.
# Modify the deposit()
# and withdraw() methods to add a record of each transaction to the transaction_history list (e.g., "Deposit: +500", "Withdrawal: -100").

class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance
        self.transaction_history = []
    def deposit(self, amount):
        self.balance += amount
        depo = f"Deposit: +{amount}"
        self.transaction_history.append(depo)
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            withd = f"Withdrawal: -{amount}"
            self.transaction_history.append(withd)

account = BankAccount()
print(account.balance)
account.deposit(500)
print(account.balance)
account.withdraw(300)
print(account.balance)
print(account.transaction_history)

# Library Class with Books:
#
# Create a Library class with an attribute books that is a dictionary.
# The keys of the dictionary should be book titles, and the values should be Book objects (from your earlier task).
# Add methods: add_book(book) (adds a book to the books dictionary) and find_book(title) (returns the Book object with the given title,
# or None if not found).
class Book:
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

class Library:
    def __init__(self, books: dict = None):
        self.books = books or {}
    def add_book(self, book):
        self.books[book.title] = book
    def find_book(self, title):
        if title in self.books:
            return self.books[title]
        else:
            return None


# Shape Hierarchy (Inheritance and Polymorphism):
#
# Create a base class Shape with an abstract method calculate_area().
# (To do this properly, you'd use the abc module, but for simplicity, just define the method and have it raise NotImplementedError if called directly).
# Create subclasses Rectangle (from your earlier task) and Circle (from your earlier task) that inherit from Shape
# and implement the calculate_area() method.
import math
class Shape:
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement calculate_area method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
            self.radius = radius
    def calculate_area(self):
            return math.pi * self.radius ** 2

rectangle = Rectangle(width=5, height=10)
circle = Circle(radius=7)

print(f"Rectangle area: {rectangle.calculate_area()}")
print(f"Circle area: {circle.calculate_area()}")

try:
    shape = Shape()  # This will raise an error
    area = shape.calculate_area()
    print(area)
except NotImplementedError as e:
    print(e)

# Counter Class:
# Create a class called Counter.
# Give it an attribute count initialized to 0 in the __init__ method.
# Add a method increment() that increases the count by 1.
# Add a method reset() that sets the count back to 0.

class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def reset(self):
        self.count = 0
incrementing = Counter()
incrementing.increment()
print(incrementing.count)
incrementing.reset()
print(incrementing.count)

# Bounded Counter Class:
# Create a class called BoundedCounter.
# Give it an attribute count initialized to 0 in the __init__ method.
# The __init__ method should also take a max_value argument, which represents the maximum value the counter can reach.
# Store this in an attribute called self.max_value.
# Add a method increment() that increases the count by 1, but only if the count is less than max_value.
# If the count is already at max_value, the increment() method should do nothing.
# Add a method reset() that sets the count back to 0.
# Add a method is_at_max() that returns True if the counter is at its maximum value (count == max_value), and False otherwise.

class BoundedCounter:
    def __init__(self, max_value):
        self.count = 0
        self.max_value = max_value
    def increment(self):
        if self.count < self.max_value:
            self.count += 1
        elif self.count == self.max_value:
            return
    def reset(self):
        self.count = 0
    def is_at_max(self):
        return self.count == self.max_value

counter = BoundedCounter(4)
counter.increment()
counter.increment()
counter.increment()
counter.increment()
counter.increment()
print(counter.count)



# Dog Class with Multiple Attributes:
# Create a class called Dog.
# Give it name, breed, and age attributes in the __init__ method.
# Create a method description() that returns a string describing the dog (e.g., "This is a [breed] named [name] who is [age] years old.").



class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    def description(self):
        return f"This is a {self.breed} name {self.name} who is {self.age} years old."

dog = Dog("Sergiusz", "kundel", "30")

print(dog.description())

# Movie Class:
# Create a class called Movie.
# Give it title, director, and year attributes in the __init__ method.
# Add a method summary() that prints a summary of the movie with the title, director, and year.

class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year
    def summary(self):
        print(f"Title: {self.title}, Director: {self.director}, Year: {self.year}")
the_movie = Movie("Lord of the Rings", "don't remember", "2002")
the_movie.summary()


# Student Class with Name and ID:
# Create a class called Student.
# Give it name and student_id attributes in the __init__ method.
# Add a method display_info() that prints the student's name and ID.

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
    def display_info(self):
        print(f"Name: {self.name}, Student ID: {self.student_id}")

studento = Student("Sergiusz", 420)
studento.display_info()


# Enhanced Student Class with Course Information:

# Create a class called Student.
# Give it name, student_id, and major attributes in the __init__ method.
# Add a method enroll(course_name) that takes a course_name as input and adds it to a list called courses
# (which should be initialized as an empty list in the __init__ method).
# Add a method display_info() that prints the student('s name, ID, major, and a list of the courses they are enrolled in. '
#                                                     'If the student is not enrolled in any courses, print "Not enrolled in any courses." '
#                                                     'instead of the list.)

class Student:
    def __init__(self, name, student_id, major, courses = None):
        self.courses = []
        self.name = name
        self.student_id = student_id
        self.major = major
    def enroll(self, course_name):
        self.courses.append(course_name)
    def display_info(self):
        print(f"Name: {self.name}, ID: {self.student_id}, major: {self.major}")
        if self.courses:
            print(f"Courses: {self.courses}")
        else:
            print("Not enrolled in any courses.")

studencik = Student("Sergiusz", "420", "Computer Science")
studencik.display_info()
studencik.enroll("English")
studencik.enroll("Maths")
studencik.display_info()



# Rectangle Class with Modified Attributes:
# Create a Rectangle class.
# Give it width and height attributes in the __init__ method.
# Add a method change_dimensions(new_width, new_height) that takes new width and height values
# and updates the object's width and height attributes.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def change_dimensions(self, new_width, new_height):
        self.width = new_width
        self.height = new_height
    def calculate(self):
        return self.width * self.height

rect = Rectangle(20, 30)
print(f"Area before changing dimension: {rect.calculate()}")
rect.change_dimensions(10, 20)
print(f"Area after changing dimension: {rect.calculate()}")

# Create a Person class with attributes like name and age. Instantiate an object and print its attributes.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

Sergiusz = Person("Sergiusz", 30)

print(f"name: {Sergiusz.name}, age: {Sergiusz.age}")

# Create a Person class with attributes name, age, and email. Add a method called greet() that prints a greeting message
# including the person('s name. '
# 'Instantiate an object with sample data, call the greet() method, and print out all the attributes separately.)



class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    def greet(self):
        print(f"Hello {self.name}!")

person1 = Person("Sergiusz", 30, "skuderski@gmail.com")
person1.greet()
print(person1.name)
print(person1.age)
print(person1.email)

# Create a Person class with attributes name, age, and email. Add a method called introduce()
# that prints a message including the person('s name and age. Implement a class method called from_birth_year() '
# 'that creates a Person object by calculating the age from the birth year provided. Instantiate two Person objects using both the regular constructor '
# 'and the class method, then call introduce() on both and print out all their attributes.)

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    def introduce(self):
        print(f"{self.name} is {self.age} years old.")

    @classmethod
    def from_birth_year(cls, name, email, birth_year):
        current_year = 2025
        age = current_year - birth_year
        return cls(name, age, email)

person1 = Person("Sergiusz", 30, "skuderski@gmail.com")
person2 = Person.from_birth_year("Martyna", "jakistam@gmail.com", 2000)

person1.introduce()
person2.introduce()

print(person1.__dict__)
print(person2.__dict__)



# Add a method to the Person class that prints a greeting message, e.g., "Hello, my name is [name]."

class Person:
    def __init__(self, name):
        self.name = name
        print(f"Hello, my name is {name}.")

persona = Person("Waclaw")


# Task:
# Extend the Person class to include a new method called greet(), which prints a personalized greeting like "Hello, my name is [name]."
#
# Then:
#
# Create two Person objects—one using the regular constructor and one using the from_birth_year() class method.
# Call the greet() method on both objects.
# Print all attributes of each person.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    @classmethod
    def from_birth_year(cls, name, birth_year, current_year = 2025):
        age = current_year - birth_year
        return cls(name, age)

personna1 = Person("Sergiusz", 30)
personna2 = Person.from_birth_year("Inga", 1986)

personna1.greet()
personna2.greet()


# Create a Car class with attributes like make, model, and year. Instantiate a few cars and print their details.


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def current_fkn_year(self, current_year = 2025):
        age = current_year - self.year
        return age

first_car = Car("Toyota", "Corolla", 2000)
second_car = Car("Subaru", "Impreza", 1992)

print(first_car.model)
print(f"{first_car.make}, year: {first_car.year}")
print(f"My car is {first_car.current_fkn_year()} years old.")
print(f"His car is {second_car.current_fkn_year()} years old.")


# Add a method to the Car class that returns the age of the car based on the current year.


# Create a Rectangle class with width and height attributes. Add methods to calculate area and perimeter.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
    def calculate_perimeter(self):
        return (2 * self.width) + (2 * self.height)

recta = Rectangle(10, 20)
print(recta.calculate_perimeter())
print(recta.calculate_area())

# Task:
# Create a Rectangle class with attributes width and height.
#
# Add methods to calculate area() and perimeter().
# Include a method called is_square() that returns True if the rectangle is a square, otherwise False.
# Implement a method called resize(new_width, new_height) that updates the rectangle's dimensions.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
    def calculate_perimeter(self):
        return (2 * self.width) + (2 * self.height)
    def is_square(self):
        return self.width == self.height
    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height
        return new_width, new_height

rectii = Rectangle(12, 6)
print(rectii.calculate_perimeter())
print(rectii.calculate_area())
print(rectii.is_square())
rectii.resize(3, 5)
print(rectii.calculate_area())

# Create a Student class with attributes like name and grade. Add a method to check if the student is passing (grade >= passing mark).


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def check(self, passing_mark):
        return self.grade >= passing_mark

me = Student("Sergiusz", 50)
print(me.check(40))

# Task:
# Create a Student class with attributes name and grades (a list of grades).
#
# Add a method called average_grade() that calculates and returns the student's average grade.
# Add another method called is_passing() that takes a passing_mark and returns True
# if the student's average grade is at least the passing mark, otherwise False.
# Create multiple student objects with different sets of grades, and test the methods to check if they're passing based on their average grades.



class Student:
    def __init__(self, name, grades: list):
        self.name = name
        self.grades = grades
    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
    def is_passing(self, passing_mark):
        return self.average_grade() >= passing_mark

student_uno = Student("Sergiusz", [1, 2, 5, 8])
print(student_uno.average_grade())
print(student_uno.is_passing(10))


# Implement a simple BankAccount class with attributes for account-holder's name and balance. Add methods to deposit and withdraw money.

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, money):
        self.balance += money
        return self.balance
my_account = BankAccount("Sergiusz", 2000)
my_account.deposit(2000)

print(my_account.balance)

# Create a BankAccount class with attributes for account-holder's name, balance, and account number.
#
# Implement methods to deposit, withdraw, and transfer money between accounts.
# Add a method to check the current balance.
# Ensure that withdrawals and transfers cannot exceed the available balance (prevent overdraft).
# Include basic error handling for invalid inputs.

class BankAccount:
    def __init__(self, name, balance, account_number):
        self.name = name
        self.balance = balance
        self.account_number = account_number
    def deposit(self, money):
        if money > 0:
            self.balance += money
        return self.balance
    def withdraw(self, money):
        if money <= self.balance:
            self.balance -= money
        else:
            print("Insufficient funds available")
        return self.balance
    def transfer(self, target_account, amount):
        if amount > 0 and amount <= self.balance:
            self.withdraw(amount)
            target_account.deposit(amount)
            print(f"Transferred {amount} to {target_account.name}")
        else:
            print("Transfer failed: insufficient funds or invalid amount.")

acc1 = BankAccount("Sergiusz", 300, 23323)
acc2 = BankAccount("Michal", 500, 1111)

acc1.transfer(acc2, 100)
print(acc1.balance)
print(acc2.balance)

# Create a class called Book with title, author, and pages attributes. Add a method that returns a formatted string describing the book.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def summary(self):
        print(f"The title: {self.title}, the author: {self.author}, amount of pages: {self.pages}")

book_one = Book("Lord of the Rings", "Tolkien", 500)
book_one.summary()


# Build a simple Animal class with a method make_sound, and create subclasses like Dog and Cat that override this method.

class Animal:
    def __init__(self):
        return
    def make_sound(self):
        print("eek")

class Dog(Animal):
    def make_sound(self):
        print("WOOF")

class Cat(Animal):
    def make_sound(self):
        print("meoow")

los_animal = Animal()
dog = Dog()
cat = Cat()
los_animal.make_sound()
dog.make_sound()
cat.make_sound()

# Create a Point class with x and y coordinates, and add a method to calculate the distance to another point.


import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def calculate(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx**2 +dy**2)

one_point = Point(2, 3)
two_point = Point(3, 4)
print(one_point.calculate(two_point))

# Create a Circle class with attributes radius and color. Add methods to calculate the circle's area and circumference.
import math
class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    def calculate_circumference(self):
        return 2 * math.pi * self.radius

circle = Circle(5,"blue")
print(circle.calculate_area())
print(circle.calculate_circumference())

#
# Design a Student class that tracks name, subject, and list of scores. Add methods to calculate average score
# and determine if the student is passing (e.g., average ≥ 60).

class Student:
    def __init__(self, name, subject, scores):
        self.name = name
        self.subject = subject
        self.scores = scores
    def average_score(self):
        return sum(self.scores) / len(self.scores)
    def is_passing(self, passing):
        return self.average_score() >= passing

studenciczek = Student("Sergiusz", "English", [2, 3, 4, 6, 2])
print(studenciczek.average_score())
print(studenciczek.is_passing(60))


# Build a WeatherForecast class with attributes city and temperature readings (list of temperatures for the week).
# Add methods to get the highest, lowest, and average temperature.


class WeatherForecast:
    def __init__(self, city, temperatures):
        self.city = city
        self.temperatures = temperatures
    def highest(self):
        return max(self.temperatures)
    def lowest(self):
        return min(self.temperatures)
    def average(self):
        return sum(self.temperatures) / len(self.temperatures)

Weather = WeatherForecast("Dubai", [1, 10, 15, 22, 30, 4, 7])
print(Weather.highest())
print(Weather.lowest())
print(Weather.average())






# Create a BankAccount class with methods to process deposits, withdrawals, and display the current balance.
# Add a method to apply a monthly interest rate.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposito(self, cash):
        if cash > 0:
            self.balance += cash
        return self.balance
    def withdrawalz(self, cash):
        if cash <= self.balance:
            self.balance -= cash
        return self.balance
    def current_balance(self):
        return self.balance


    def monthly_interest(self, percentage):
        self.balance += self.balance * (percentage / 100)
        return self.balance

my_bank_account = BankAccount(2000)
print(my_bank_account.deposito(200))
print(my_bank_account.withdrawalz(450))
print(my_bank_account.current_balance())
print(my_bank_account.monthly_interest(5))


# Implement an InventoryItem class with attributes name, price, and quantity. Add methods to increase/decrease stock,
# and calculate total inventory value.

class InventoryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def increase_stock(self, amount):
        self.quantity += amount
        return self.quantity
    def decrease_stock(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
        return self.quantity
    def calculate_price(self):
        inventory_value = self.price * self.quantity
        return inventory_value

the_stock = InventoryItem("Wedel", 5, 100)
print(the_stock.increase_stock(2))
print(the_stock.decrease_stock(5))
print(the_stock.calculate_price())



# Design a BookSeries class that stores multiple Book objects. Add methods to add books, remove books,
# and list all book titles.
class Book:
    def __init__(self, name, title):
        self.name = name
        self.title = title
class BookSeries:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def remove_book(self, title):
        self.books = [b for b in self.books if b.title != title]
    def list_titles(self):
        for book in self.books:
            print(book.title)

series = BookSeries()
book1 = Book("JK Rowling", "Harry Potter")
book2 = Book("David Goggins", "Never Finished")
series.add_book(book1)
series.add_book(book2)

series.list_titles()
series.remove_book("Harry Potter")
series.list_titles()



# Create a VideoGame class with attributes title, genre, and rating. Add methods to update ratings and display game details.


class VideoGame:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating
    def update_rating(self, new_rating):
        self.rating = new_rating
    def display(self):
        print(f"Title: {self.title}, Genre: {self.genre}, Rating: {self.rating}")

first_game = VideoGame("BattleBit Remasterd", "FPS", "8/10")
first_game.update_rating("9/10")
first_game.display()


# Task:
# Create a VideoGame class with title, genre, ratings (a list of ratings from users), and an average_rating() method
# that calculates the average rating.
#
# Add a method add_rating(new_rating) to include new user ratings.
# Add a method display_info() that shows the title, genre, and average rating (formatted to 2 decimal places).
# Ensure the class handles cases when there are no ratings yet.

class VideoGame:
    def __init__(self, title, genre, ratings):
        self.title = title
        self.genre = genre
        self.ratings = ratings
    def average_rating(self):
        if len(self.ratings) == 0:
            return 0
        return sum(self.ratings) / len(self.ratings)
    def add_rating(self, new_rating):
        self.ratings.append(new_rating)
    def display_info(self):
        avg = self.average_rating()
        print(f"The title: {self.title}, Genre: {self.genre}, Ratings: {avg:.2f}")

game = VideoGame("Dead Cells", "roguelike", [1, 2, 3, 10, 20, 6])
print(game.average_rating())
game.add_rating(10)
game.display_info()


# Task:
# Create a Library class that manages a collection of Book objects. Each Book should have attributes like title, author, and year.
# The Library class should have methods to:
#
# Add a new book
# Remove a book by title
# List all books (show title and author)
# Find books by a specific author
# Bonus:
# Add a method to count how many books the library has.
# class Book:
#     def __init__(self, name, author, year):
#         self.name = name
#         self.author = author
#         self.year = year
# class Library:
#     def __init__(self):
#         self.books = []
#     def add(self, book):
#         self.books.append(book)
#     def remove(self, name):
#         self.books = [book for book in self.books if book.name != name]
#     def listing(self):
#         for book in self.books:
#             print(f"{book.name}, {book.author}")
#
#     def find_by_author(self, author_name):
#         results = []
#         for book in self.books:
#             if book.author == author_name:
#                 results.append(book)
#         return results
#
#
#
#
#
#
#
# # Build a Playlist class containing songs (as strings). Add methods to add, remove, and list songs. Also, include a method to shuffle songs.
# #
# # Develop a CarRental class with attributes car model, rental days, and price per day.
# # Add methods to calculate total rental cost, apply discounts, and display rental info.
# #
# # Create a Time class with hours, minutes, and seconds. Add methods to add or subtract time, and display it in HH:MM:SS format.
#
# # Create a class called Student that has:
# #
# # An attribute name.
# # An attribute score.
# # When you create a Student object, it should just store the name and score.
# #
# # Now, create a list of students with different names and scores.
# #
# # Finally, write a small loop that goes through the list and prints each student's name and score.
#
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
# student1 = Student("Sergiusz", 22)
# student2 = Student("Michal", 33)
# student3 = Student("Wiesiek", 40)
# student4 = Student("Miroslawa", 50)
#
# the_list = [student1, student2, student3, student4]
#
# for s in the_list:
#     print(s.name, s.score)
#
#
#
# # Practice Task:
# # Create a Student class with:
# #
# # Attributes: name, score, and pass_threshold (the minimum score to pass).
# # A method is_passing() that returns True if the student is passing, otherwise False.
# # Then:
# #
# # Create a list of several Student objects with different scores.
# # Loop through the list and for each student, print their name, score, and whether they are passing or not.
#
# class Student:
#     def __init__(self, name, score, pass_threshold = 50):
#         self.name = name
#         self.score = score
#         self.pass_threshold = pass_threshold
#     def is_passing(self):
#         return self.score >= self.pass_threshold
#
# first = Student("Sergiusz", 40)
# second = Student("Michal", 60)
#
# list_of_students = [first, second]
#
# for s in list_of_students:
#     print(s.name, s.score, s.is_passing())
#
# # Create a class called Car. Each Car has:
# #
# # An attribute called brand.
# # An attribute called owner (which should be a Person object).
# # A method called car_info() that prints "This car is a [brand], owned by [owner's name]".
# # Create a class called Person with:
# #
# # An attribute called name.
# # Then:
# #
# # Instantiate some Person objects.
# # Instantiate some Car objects, assigning each a person as its owner.
# # Call the car_info() method for each car.
#
# class Car:
#     def __init__(self, brand, owner):
#         self.brand = brand
#         self.owner = owner
#     def car_info(self):
#         print(f"This car is a {self.brand}, owned by {self.owner.name}")
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
# first_person = Person("Sergiusz")
# second_person = Person("Michal")
# third_person = Person("Waclaw")
#
# firstc = Car("bmw", first_person)
# secondc = Car("subaru", second_person)
# thirdc = Car("toyota", third_person)
#
# firstc.car_info()
# secondc.car_info()
# thirdc.car_info()

# Create a class Employee with:
#
# Attributes: name, salary, and department.
# Methods:
# give_raise(amount) to increase salary.
# change_department(new_department) to update the department.
# display_info() to print the employee's details.
# Create a class Company with:
#
# An attribute: employees (a list of Employee objects).
# Methods:
# add_employee(employee) to add new employees.
# remove_employee(employee_name) to remove an employee by name.
# list_employees() to display all employees with their details.
# give_raise_all(amount) to give all employees a raise.
# find_by_department(department) to list employees in a specific department.

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def give_raise(self, amount):
        self.salary += amount
        return self.salary

    def change_department(self, new_department):
        self.department = new_department

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")

class Company:
    def __init__(self):
        self.employees = []
    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_name):
        for employee in self.employees:
            if employee.name == employee_name:
                self.employees.remove(employee)
                break
    def list_employees(self):
        for employee in self.employees:
            print(f"Name: {employee.name}, Salary: {employee.salary}, Department: {employee.department}")
    def give_raise_all(self, amount):
        for employee in self.employees:
            employee.salary += amount
    def find_by_department(self, department):
        for employee in self.employees:
            if employee.department == department:
                print(f"{employee.name}, Salary: {employee.salary}, Department: {employee.department}")
employee1 = Employee("Sergiusz", 2000, "Custumer Service")
employee2 = Employee("Irena", 30000, "Dentistry")
employee3 = Employee("Wiesiek", 500000, "Engineering")

print(employee3.give_raise(2000))
employee2.change_department("Firefighting")
print(employee2.department)
employee1.display_info()

company1 = Company()
new_employee = Employee("Piotrek", 20000, "Legal Executive")
new_employee2 = Employee("Witold", 200, "Chauffer")
company1.add_employee(new_employee2)
company1.add_employee(new_employee)
company1.add_employee(employee2)
company1.add_employee(employee1)
company1.add_employee(employee3)
company1.list_employees()
company1.give_raise_all(3000)
company1.list_employees()
company1.find_by_department("Custumer Service")


# Practice Task:
# Create a class Library with the following features:
#
# An attribute books that is a list of Book objects.
# A method add_book(book) to add a Book object.
# A method remove_book(title) to remove a book from the library by its title.
# A method list_books() to print details (title and author) of all books.
# A method find_books_by_author(author) to list all books written by a certain author.
# Create a class Book with:
#
# Attributes: title and author.

class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break
    def list_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}")
    def find_books_by_author(self, author):
        the_list = []
        for book in self.books:
            if book.author == author:
                print(f"{book.author}")
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("11", "22")
book2 = Book("22", "33")
book3 = Book("33", "44")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book1)
library.remove_book("11")
library.list_books()
library.find_books_by_author("22")

# Task: Person and Pet
# Create a Person class:
#
# Attributes: name, age
# Method: greet() — prints a greeting with the person's name.
# Create a Pet class:
#
# Attributes: name, type (like cat, dog)
# Attribute: owner (which should be a Person object)
# Method: describe() — prints the pet's name, type, and owner's name.
# Steps to do:
#
# Instantiate a Person.
# Instantiate a Pet, assign the person as the owner.
# Call the pet's describe() method to see the details.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, {self.name}")

class Pet:
    def __init__(self, name, pet_type, owner):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
    def describe(self):
        print(f"Name: {self.name}, type: {self.pet_type}, owner: {self.owner.name}")

person = Person("Sergiusz", 30)
pet = Pet("Piesiek", "chihuahua", person)

pet.describe()

# Create a Library and Book classes where:
#
# You can add/remove books.
# List books by genre or author.
# Find books published after a certain year.

class Book:
    def __init__(self, title, genre, author, year):
        self.title = title
        self.genre = genre
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = []
    def __add__(self, other):
        self.books.append(other)
        return self
    def remove(self, book):
            if book in self.books:
                self.books.remove(book)
            return self
    def listing(self, genre):
        for book in self.books:
            if genre is None or book.genre == genre:
                print(f"{book.title}")
    def other_listing(self, author):
        for book in self.books:
            if book.author == author:
                print(f"{book.title}")

book1 = Book("I don't know", "criminal", "Oscar Wilde", 1950)
book2 = Book("The same","fantasy", "Johnny Wick", 1960)
library = Library()
library + book1 + book2
library.listing("fantasy")
library.other_listing("Oscar Wilde")
library.remove(book1)

# Build a Movie and Actor classes:
#
# Actors can act in multiple movies.
# Movies can have multiple actors.
# Include methods to list movies an actor starred in and actors in a movie.
# Design a Course and Student classes:
#
# Students can enroll in multiple courses.
# Courses can have many students.
# Methods to enroll/drop students and list students in a course.
# Implement a SalesPerson and Sale classes:
#
# SalesPersons can make multiple sales.
# Record sale amounts and dates.
# Methods to calculate total sales per salesperson.
# Create an Order and Product classes:
#
# An order contains multiple products with quantities.
# Calculate total order cost.
# Apply discounts to products or entire orders.
# Design a Team and Player classes:
#
# Players can belong to multiple teams (e.g., for different seasons).
# Teams can list their players.
# Track player stats and display top performers.
# Create a Wallet and Transaction classes:
#
# Wallet holds multiple transactions.
# Transactions can be deposits or withdrawals.
# Methods to get the current balance and recent transactions.
# Implement a Company and Department classes:
#
# Departments contain employees.
# Add/remove employees, list department members.
# Transfer employees between departments.
# Design a Recipe and Ingredient classes:
#
# Recipes use multiple ingredients.
# Ingredients store quantity and units.
# Methods to calculate total cost, adjust quantities.
# Create an Event and Attendee classes:
#
# Attendees can register for multiple events.
# Events track their attendees.
# Methods to list attendees per event and events per attendee.

# Simple Vehicle Class
# Create a Vehicle class with attributes like make, model, and year. Add a method display_info() that prints out these details.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

car = Vehicle("Toyota", "Corolla", 1994)

car.display_info()

# Create a Vehicle class with the following features:

# Attributes: make, model, year, mileage.
# Methods:
# display_info() to print all vehicle details.
# drive(distance) to increase mileage based on a distance traveled.
# years_old(current_year) to calculate how old the vehicle is.
# is_classic() that returns True if the vehicle is older than 25 years.


class Vehicle:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Mileage: {self.mileage}")
    def distance(self, distance):
        self.mileage += distance
        return self.mileage
    def years_old(self, current_year = 2025):
        return current_year - self.year

    def is_classic(self):
        return 2025 - self.year > 25


# Rectangle Area Calculator
# Create a Rectangle class with width and height attributes. Add a method calculate_area() that returns the area.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height


# Student Score Tracker
# Create a Student class with attributes name and scores (a list). Add methods to add new scores and to compute the average score.

class Student:
    def __init__(self, name, scores: list):
        self.name = name
        self.scores = scores
    def add_scores(self, score):
        self.scores.append(score)
        return self.scores
    def average_score(self):
        if not self.scores:
            return 0
        average = sum(self.scores) / len(self.scores)
        return average
    # Task 1: Inventory Management System
    # Create an Item class with attributes: name, price, stock.
    # Add methods to:
    # - restock (increase stock)
    # - sell (decrease stock, but not below zero)
    # - display item details

class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def restock(self, increase):
        self.stock += increase
        return self.stock
    def sell(self, decrease):
        if decrease <= self.stock:
            self.stock -= decrease
            return self.stock
    def display(self):
        print(f"Name: {self.name}, Price: {self.price}, Stock: {self.stock}")

the_item = Item("kinder bueno", 20, 1000)

the_item.restock(10)
the_item.sell(100)
the_item.display()


    # Task 2: Bank System
    # Create an Account class with attributes: account_holder, balance.
    # Add methods to:
    # - deposit money
    # - withdraw money (with a check for insufficient funds)
    # - display balance info



class Account:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, money):
        self.balance += money
        return self.balance
    def withdraw(self, money):
        if self.balance >= money:
            self.balance -= money
        else:
            print(f"Insufficient funds")
        return self.balance
    def display(self):
        print(f"Account holder: {self.account_holder}, Balance: {self.balance}")

the_account = Account("Sergiusz", 1)
the_account.deposit(2)
the_account.withdraw(1)
the_account.display()



    # Task 3: Event Organizer
    # Create classes Event and Participant.
    # - Event has attributes: name, date, list of participants.
    # - Methods to add/remove participants, list all participants,
    #   and check if a participant is registered.
class Participant:
    def __init__(self, name, email=None):
        self.name = name
        self.email = email
class Event:
    def __init__(self, name, date, participants: list):
        self.name = name
        self.date = date
        self.participants = participants
    def add(self, participant):
        self.participants.append(participant)
    def remove(self, participant):
        self.participants.remove(participant)
    def listink(self):
        print(f"The name of the participant is {self.name}. The date of the event is {self.date}.")
        for participant in self.participants:
            print(f" {participant.name} (Email): {participant.email}")
    def regi(self, participant_name):
        for participant in self.participants:
            if participant.name == participant_name:
                return True
        return False


# Bank System: Create a BankAccount class with deposit, withdraw, transfer, and display balance methods. Add a feature to accrue interest.

class BankAccount:
    def __init__(self, name, account_balance, account_number):
        self.name = name
        self.account_balance = account_balance
        self.account_number = account_number
    def deposit(self, money):
        self.account_balance += money
        return self.account_balance
    def withdraw(self, money):
        if self.account_balance >= money:
            self.account_balance -= money
        return self.account_balance

    def transfer(self, other_account, money):
        if self.account_balance >= money:
            self.withdraw(money)
            other_account.deposit(money)
        else:
            print("Not enough funds")
        return self.account_balance
    def display(self):
        print(f"The name of the account holder: {self.name}, the balance: {self.account_balance}, the account number: {self.account_number}")

bank_account = BankAccount("Sergiusz", 2000, 1952432)
bank_account2 = BankAccount("Wiesiek", 3000, 15912)
bank_account.deposit(1000)
bank_account.withdraw(500)
bank_account.display()
bank_account.transfer(bank_account2, 5000)
bank_account2.display()


# Shopping Cart: Design Product and Cart classes. The cart can add/remove products, update quantities, and calculate total cost.

class Product:
    def __init__(self, name, quantity, cost):
        self.name = name
        self.quantity = quantity
        self.cost = cost

class Cart:
    def __init__(self):
        self.products = []
    def add(self, product):
        self.products.append(product)

    def remove(self, product):
        self.products = [p for p in self.products if p.name != product]
        return self.products

    def update_quantity(self, product, new_quantity):
        for p in self.products:
            if p.name == product:
                p.quantity = new_quantity
                break

    def total_cost(self):
        total = 0
        for p in self.products:
            total += p.cost * p.quantity
        return total

    def __str__(self):
        lines = []
        for p in self.products:
            lines.append(f"{p.name}: {p.quantity} @ {p.cost}")
        lines.append(f"Total cost: {self.total_cost()}")
        return "\n".join(lines)

product1 = Product("cheese", 50, 2)
product2 = Product("meat", 20, 5)
product3 = Product("water", 5, 10)
product4 = Product("sausages", 15, 7)

cart = Cart()

cart.add(product1)
cart.add(product2)
cart.add(product3)
cart.add(product4)
cart.update_quantity("meat", 30)
print(cart.total_cost())
print(cart)

# Create a Dog class with attributes like name and breed, and a method bark() that prints a bark message.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Bark Bark")

doggy = Dog("Rodi", "le szampinjon")
doggy.bark()

# Create a Dog class that includes:
#
# Attributes: name breed energy_level (initially set to 100)
# Methods: bark() — prints a bark message, but also decreases energy_level by 10.  eat() — increases energy_level by 20, up to a max of 100.
# play() — decreases energy_level by 30 and prints a playful message.rest() — increases energy_level by 50, up to 100.
# status() — prints the current energy level with a message.

class Dog:
    def __init__(self, name, breed, energy_level = 100):
        self.name = name
        self.breed = breed
        self.energy_level = energy_level
    def bark(self):
        print("bark")
        self.energy_level = max(self.energy_level - 10, 0)
        return self.energy_level
    def eat(self):
        self.energy_level = min(self.energy_level + 20, 100)
        return self.energy_level

    def play(self):
        self.energy_level = max(self.energy_level - 30, 0)
        print("who's a good boy")
        return self.energy_level

    def rest(self):
        self.energy_level = min(self.energy_level + 50, 100)
        return self.energy_level

    def status(self):
        print(f"The current energy level of {self.name} is: {self.energy_level}")

the_doggo = Dog("Buddy", "labrador")
the_doggo.bark()
the_doggo.play()
the_doggo.play()
the_doggo.status()
the_doggo.eat()
the_doggo.bark()
the_doggo.bark()
the_doggo.status()
the_doggo.rest()
the_doggo.status()

# Create a Dog class with the following features:
#
# Attributes: name breed energy_level (initially 100) happiness (initially 50)
# Methods:

# bark(): prints "Woof!", decreases energy_level by 10 (min 0), increases happiness by 2 (max 100).  eat(): increases energy_level by 20 (max 100), increases happiness by 1 (max 100).
# play(): decreases energy_level by 30 (min 0), increases happiness by 10 (max 100). rest(): increases energy_level by 50 (max 100), no change to happiness.
# greet(): prints a greeting that includes the dog's name. status(): prints current energy_level and happiness.
# Implement a method is_happy() that returns True if happiness > 75, otherwise False.
# Optional:
# Add a method train() that increases happiness by 15 but decreases energy by 20.

class Dog:
    def __init__(self, name, breed, energy_level = 100, happiness = 50):
        self.name = name
        self.breed = breed
        self.energy_level = energy_level
        self.happiness = happiness

    def bark(self):
        print("Woof!")
        self.energy_level = max(self.energy_level - 10, 0)
        self.happiness = min(self.happiness + 2, 100)

    def eat(self):
        self.energy_level = max(self.energy_level + 20, 100)
        self.happiness = min(self.happiness + 2, 100)

    def play(self):
        self.energy_level = max(self.energy_level - 30, 0)
        self.happiness = min(self.happiness + 10, 100)

    def rest(self):
        self.energy_level = min(self.energy_level + 50, 100)

    def greet(self):
        print(f"Hello, {self.name}")

    def status(self):
        print(f"{self.name}'s energy level: {self.energy_level}")
        print(f"{self.name}'s happiness: {self.happiness}")

    def is_happy(self):
        return self.happiness > 75

    def train(self):
        self.energy_level = min(self.energy_level + 15, 100)
        self.happiness = max(self.happiness - 20, 0)



the_dog = Dog("Rodi", "kundel")

the_dog.bark()
the_dog.status()
print(the_dog.is_happy())
the_dog.train()
the_dog.status()

# Design a Circle class with an attribute radius and a method calculate_area() to compute its area.
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * self.radius ** 2

the_circlo = Circle(5)
print(the_circlo.calculate_area())

# Create a Circle class that:
#
# Has an attribute radius.
# Includes methods to:
# calculate_area(): compute the area.
# calculate_circumference(): compute the circumference of the circle.
# scale(factor): multiply the radius by a scaling factor (and update the radius).
# info(): print detailed info about the circle (radius, area, circumference).
# Bonus:
# Add validation to ensure the radius can never be negative.
# Add a class variable circle_count that tracks how many Circle instances have been created.

class Circle:
    circle_count = 0
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius
        Circle.circle_count += 1

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def scale(self, factor):
        self.radius *= factor
        return self.radius

    def info(self):
        print(f"The radius is: {self.radius}. The area is {self.calculate_area()} and the circumference is: {self.calculate_circumference()}")



circlo = Circle(5)
circlo2 = Circle(10)
circlo.info()
circlo2.calculate_area()
circlo2.info()
circlo2.scale(3)
circlo2.calculate_area()
circlo2.info()

print(Circle.circle_count)

# Build a Person class with attributes name and age, and a method say_hello() that prints a greeting.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello {self.name}")

me = Person("Sergiusz", 30)

me.say_hello()

# Create a Person class with:
# Attributes:
# name
# birth_year
# Methods:
# say_hello(): prints a greeting with the person's name.
# calculate_age(current_year): returns the person's age based on the current year.
# is_adult(current_year): returns True if the person is 18 or older.
# have_birthday(): increases the age by 1.

class Person:
    def __init__(self, birth_year, age, name="Anonymous"):
        self.name = name
        self.birth_year = birth_year
        self.age = age
    def say_hello(self):
        print(f"Hello, {self.name}")

    def calculate_age(self, current_year = 2025):
        if current_year > 2025:
            print("Year in the future")
        self.age = current_year - self.birth_year
        return self.age

    def is_adult(self, current_year = 2025):
        return (current_year - self.birth_year) >= 18

    def have_birthday(self):
        self.age += 1

Sergiusz = Person(1994, 30, "Sergiusz")
Sergiusz.say_hello()
print(Sergiusz.calculate_age())
print(Sergiusz.is_adult())
Sergiusz.have_birthday()
Sergiusz.have_birthday()
print(Sergiusz.age)

# Create an Employee Management System with two classes: Employee and Company.

# 1. Employee Class:
#    - Attributes:
#        - name (string): the employee's name
#        - birth_year (int): year of birth
#        - hire_year (int): year when the employee was hired
#        - salary (number): employee's salary
#    - Methods:
#        - calculate_age(current_year): returns age based on birth_year
#        - calculate_years_of_service(current_year): returns years worked at the company
#        - give_raise(amount): increases salary by the specified amount
#        - status(): prints employee info: name, age, years of service, salary
#    - Validation:
#        - birth_year and hire_year should not be in the future (use datetime to check)
#
# 2. Company Class:
#    - Attributes:
#        - name (string): name of the company
#        - employees (list): list of Employee objects
#    - Methods:
#        - add_employee(employee): adds an employee
#        - remove_employee(employee_name): removes employee by name
#        - total_salary(): sums salaries of all employees
#        - list_employees(): prints info of all employees
#        - raise_all(amount): increases all employees' salaries
#        - find_employee(employee_name): returns Employee object or None
#
# 3. Additional Tips:
#    - Use current system year (datetime module) for age and service calculations.
#    - Handle invalid input gracefully.
#    - Test with multiple employees and company operations.

class Employee:
    def __init__(self, name, birth_year, hire_year, salary):
        current_year = datetime.datetime.now().year
        if birth_year > current_year:
            raise ValueError ("Birth year cannot be in the future.")
        if hire_year > current_year:
            raise ValueError ("Hire year cannot be in the future.")
        self.name = name
        self.birth_year = birth_year
        self.hire_year = hire_year
        self.salary = salary


    def calculate_age(self, current_year = None):
        if current_year is None:
            current_year = datetime.datetime.now().year
        age = current_year - self.birth_year
        return age

    def calculate_years_of_service(self, current_year = None):
        if current_year is None:
            current_year = datetime.datetime.now().year
        years_of_service = current_year - self.hire_year
        return years_of_service

    def give_raise(self, amount):
        self.salary += amount
        return self.salary

    def status(self):
        print(f"Name: {self.name}, Age: {self.calculate_age()}, Years of service: {self.calculate_years_of_service()}, Salary: {self.salary}")

    def __str__(self):
        return f"Employee: {self.name}, Salary: {self.salary}, Birth Year: {self.birth_year}"


class Company:
    def __init__(self, name: str):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees = [e for e in self.employees if e.name != employee.name]

    def total_salary(self):
        total = 0
        for employee in self.employees:
            total += employee.salary
        return total

    def list_employees(self):
        for e in self.employees:
            print(f"Name: {e.name}, salary: {e.salary}, birth year: {e.birth_year}")

    def raise_all(self, amount):
        for e in self.employees:
            e.salary += amount

    def find_employee(self, employee_name):
        for e in self.employees:
            if e.name == employee_name:
                return e
        return None


Sergiusz_Kuderski = Employee("Sergiusz", 1994, 2022, 1000)
Tomasz_Konopka = Employee("Tomasz", 1988, 2020, 1500)
Piotr_Kuderski = Employee("Piotr", 1985, 2015, 2000)
print(Sergiusz_Kuderski.calculate_age())
print(Sergiusz_Kuderski.calculate_years_of_service())
Sergiusz_Kuderski.give_raise(200)
Sergiusz_Kuderski.status()

company = Company("Wodka Holdings")
company.add_employee(Sergiusz_Kuderski)
company.list_employees()
company.add_employee(Tomasz_Konopka)
company.add_employee(Piotr_Kuderski)
company.list_employees()
company.remove_employee(Tomasz_Konopka)
company.list_employees()
print(company.total_salary())
company.raise_all(200)
company.add_employee(Tomasz_Konopka)
company.list_employees()
print(company.total_salary())
print(company.find_employee("Sergiusz"))

# Create a Student class with attributes name and scores (list). Include methods to add a score and compute the average score.

class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def adding(self, score):
        self.scores.append(score)
        return self.scores

    def compute_average(self):
        if len(self.scores) == 0:
            return 0
        return sum(self.scores) / len(self.scores)

student1 = Student("Sergiusz")
student1.adding(20)
student1.adding(30)
student1.adding(40)
student1.adding(50)

print(student1.compute_average())


# Create a Student class with:
#
# Attributes:
#
# name
# scores (list of scores only, e.g., [85, 90, 78])
# Methods:
#
# add_score(score): adds a new score to the list.
# calculate_average(): returns the average score of all recorded scores.
# highest_score(): returns the highest score.

class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)
        return self.scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def highest_score(self):
        return max(self.scores)

student_sergiusz = Student("Sergiusz")
student_sergiusz.add_score(20)
student_sergiusz.add_score(50)
student_sergiusz.add_score(30)
print(student_sergiusz.calculate_average())
print(student_sergiusz.highest_score())

# Create a Student class with:
#
# Attributes:
#
# name
# scores (list of scores)
# name (student's name)
# Methods:
#
# add_score(score): add a score.
# calculate_average(): return the average, but only considering scores from the last 5 entries.
# highest_score(): return the highest score and its position in the score list (the index).

class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def calculate_average(self):
        if not self.scores:
            return 0
        recent_scores = self.scores[-5:]
        return sum(recent_scores) / len(recent_scores)

    def highest_score(self):
        max_index, max_score = max(enumerate(self.scores), key=lambda x: x[1])
        return max_score, max_index

student_1 = Student("Sergiusz")
student_1.add_score(2)
student_1.add_score(3)
student_1.add_score(4)
student_1.add_score(5)
student_1.add_score(6)
print(student_1.calculate_average())
print(student_1.highest_score())

# Implement a Rectangle class with attributes width and height, and methods to calculate area and perimeter.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

some_rectangle = Rectangle(2, 5)
print(some_rectangle.calculate_area())
print(some_rectangle.calculate_perimeter())

# Create a Rectangle class with:
#
# Attributes:
#
# width
# height
# Methods:
#
# calculate_area(): returns the area.
# calculate_perimeter(): returns the perimeter.
# resize(new_width, new_height): update the width and height.
# is_square(): returns True if the rectangle is a square, otherwise False.
# swap_dimensions(): swaps the width and height.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def resize(self, new_width, new_height):
        if new_width <= 0 or new_height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self.width = new_width
        self.height = new_height

    def is_square(self):
        return self.width == self.height

    def swap_dimensions(self):
        self.width, self.height = self.height, self.width

first_rectangle = Rectangle(2, 10)
print(first_rectangle.calculate_area())
print(first_rectangle.calculate_perimeter())
first_rectangle.resize(5,10)
print(first_rectangle.is_square())
first_rectangle.swap_dimensions()
print(first_rectangle.calculate_area())

# Create a Rectangle class with:
#
# Attributes:
#
# width
# height
# color (optional, defaults to 'black')
# border_width (optional, defaults to 1)
# Methods:
#
# calculate_area(): returns area.
# calculate_perimeter(): returns perimeter.
# resize(new_width, new_height): updates dimensions with validation for positive values.
# is_square(): returns True if width == height.
# swap_dimensions(): swaps width and height.
# set_color(new_color): updates the rectangle's color.
# set_border_width(new_width): updates border width with validation for non-negative values.
# display(): prints all properties of the rectangle.

class Rectangle:
    def __init__(self, width, height, color = "black", border_width = 1):
        self.width = width
        self.height = height
        self.color = color
        self.border_width = border_width

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def resize(self, new_width, new_height):
        if new_width <= 0 or new_height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self.width = new_width
        self.height = new_height

    def is_square(self):
        return self.width == self.height

    def swap_dimensions(self):
        self.width, self.height = self.height, self.width

    def set_color(self, color):
        self.color = color
        return self.color

    def set_border_width(self, new_width):
        if new_width <= 0:
            raise ValueError("Must be a positive number")
        self.border_width = new_width

    def display(self):
        print(f"The height: {self.height}, the width: {self.width}, the color: {self.color}, the border width: {self.border_width}")

    def __str__(self):
        return (f"Rectangle(width={self.width}, height={self.height}, "
                f"color={self.color}, border_width={self.border_width})")


cool_rectangle = Rectangle(10, 15, "blue", 5)
print(cool_rectangle.calculate_area())
print(cool_rectangle.calculate_perimeter())
cool_rectangle.resize(5, 7)
print(cool_rectangle.is_square())
cool_rectangle.swap_dimensions()
cool_rectangle.set_color("yellow")
cool_rectangle.set_border_width(25)
cool_rectangle.display()
print(cool_rectangle)

# Design a Book class with attributes title, author, and year, and a method display() that prints the book details.

class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        print(f"The title: {self.title}, the author: {self.author}, the year: {self.year}")

some_book = Book("Harry Potter", "J.K. Rowling", 2000)
some_book.display()

# Create a Book class with:
#
# Attributes:
#
# title
# author, year, genre (optional, default to 'Unknown'), pages (optional, default to 0)
# Methods:
#
# display(): Prints all book details in a neat format.
# is_classic(): Returns True if the book was published more than 50 years ago.
# update_pages(new_pages): Updates the number of pages (with validation: must be positive).
# update_genre(new_genre): Changes the genre.
# Bonus:
# Add a class attribute book_count to keep track of how many Book instances have been created.

class Book:
    book_count = 0

    def __init__(self, title, author, year, genre = "Unknown", pages = 0):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.pages = pages
        Book.book_count += 1

    def display(self):
        print(f"The title of the book is: {self.title}. The author of the book is: {self.author}. The year it was published: {self.year}."
              f"The genre of the book is: {self.genre}. The book consists of {self.pages} pages.")

    def is_classic(self, current_year = None):
        import datetime
        if current_year is None:
            current_year = datetime.datetime.now().year
        return (current_year - self.year) >= 50

    def update_pages(self, new_pages):
        if new_pages < 0:
            raise ValueError ("Must be a positive number")
        self.pages = new_pages

    def update_genre(self, new_genre):
        self.genre = new_genre

booka = Book("some_title", "me", 2000, "criminal", 420)

booka.display()
print(f"is {booka.title} a classic? {booka.is_classic()}")
booka.update_pages(200)
booka.update_genre("history")
booka.display()
print(Book.book_count)

# Create a `Book` class with the following features:

# Attributes:
# - `title` (string): the title of the book
# - `author` (string): the author of the book
# - `publication_year` (int): year the book was published
# - `genre` (string, optional, default "Unknown")
# - `pages` (int): number of pages
# - `ratings` (list of integers, optional, default empty list): ratings between 1 and 5
#
# Methods:
# - `display()`: prints all details of the book.
# - `add_rating(rating)`: adds a rating (must be between 1 and 5), with validation.
# - `calculate_average_rating()`: returns the average rating, or `None` if no ratings exist.
# - `is_classic(current_year=None)`: checks if the book is over 50 years old based on the current year.
# - `update_pages(new_pages)`: updates the pages, with validation that pages are positive.
# - `update_genre(new_genre)`: changes the genre.
# - `get_summary()`: returns a string summarizing the book with key details (title, author, year, average rating).
#
# Additional:
# - Implement a class attribute `book_count` that tracks how many `Book` instances are created.
# - Add a method `recommend()` that returns `True` if the average rating is 4 or higher.

class Book:
    book_count = 0

    def __init__(self, title, author, publication_year, pages, genre = "Unknown"):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.pages = pages
        self.ratings = []
        Book.book_count += 1

    def display(self):
        print(f"Title: {self.title}"
              f"Author: {self.author}"
              f"Publication year: {self.publication_year}"
              f"Genre: {self.genre}"
              f"Pages: {self.pages}"
              f"Ratings: {self.ratings}")

    def add_rating(self, rating):
        if not isinstance(rating, (float, int)):
            raise ValueError("Rating must be a number")
        if 1 <= rating <= 5:
            self.ratings.append(rating)
        else:
            raise ValueError("Rating must be between 1 and 5")

    def calculate_average_rating(self):
        if not self.ratings:
            return None
        return sum(self.ratings) / len(self.ratings)

    def is_classic(self, current_year = None):
        import datetime
        if current_year is None:
            current_year = datetime.datetime.now().year
        return (current_year - self.publication_year) >= 50

    def update_pages(self, new_pages):
        self.pages = new_pages
        return self.pages

    def update_genre(self, new_genre):
        self.genre = new_genre
        return self.genre

    def recommend(self):
        avg_rating = self.calculate_average_rating()
        return avg_rating is not None and avg_rating >= 4

    def __str__(self):
        return (f"The title: {self.title}, the author: {self.author}, publication year: {self.publication_year}, genre: {self.genre}, pages: {self.pages}, "
                f"ratings: {self.ratings}")

some_fun_book = Book("Lord of the Rings", "J. R. R. Tolkien", 1955, 500, "Fantasy")
print(some_fun_book)
some_fun_book.add_rating(5)
some_fun_book.add_rating(3)
some_fun_book.add_rating(4)
some_fun_book.add_rating(2)
print(some_fun_book.calculate_average_rating())
print(some_fun_book.is_classic())
some_fun_book.update_pages(450)
some_fun_book.update_genre("Fantasy improved")
print(some_fun_book.recommend())
print(some_fun_book)

# Create a Car class with attributes make, model, and year, and a method display_info().

class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"The make of the car is: {self.make}. "
              f"The model of the car is: {self.model}. "
              f"The year of the car is: {self.year}.")

my_carro = Car("Toyota", "Corolla", 1990)

my_carro.display_info()

# Create a `Car` class with the following:
#
# Attributes:
# - `make` (string): the manufacturer - `model` (string): the model name  `year` (int): manufacturing year, not in the future
# - `mileage` (float, default 0.0): total driven distance  `color` (string, default "Black"): car color `price` (float): original price

# Methods:
# - `display_info()`: print all car details neatly
# - `update_mileage(new_mileage)`: update mileage; ensure it does not decrease
# - `paint(new_color)`: change the car's color
# - `calculate_age(current_year=None)`: compute how many years old the car is
# - `get_price_after_depreciation(current_year=None)`: estimate current value, assuming a fixed depreciation rate per year
#
# Additional:
# - Validate that `year` is not in the future during initialization.
# - Add a class attribute `car_count` to track total number of `Car` instances.

class Car:

    car_count = 0

    def __init__(self, make, model, year, price, mileage: float = 0.0, color = "black"):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.color = color
        self.price = price
        Car.car_count += 1

    def display_info(self):
        print(f"The make: {self.make}. "
              f"The model: {self.model}. "
              f"The year: {self.year}. "
              f"The mileage: {self.mileage}. "
              f"The color: {self.color}. "
              f"The price: {self.price}. ")

    def update_mileage(self, new_mileage):
        if new_mileage >= self.mileage:
            self.mileage = new_mileage
        else:
            print(f"Mileage must be equal or greater than the current mileage")

    def paint(self, color):
        self.color = color
        return self.color

    def calculate_age(self, current_year = None):
        import datetime
        if current_year is None:
            current_year = datetime.datetime.now().year
        return current_year - self.year

    def get_price_after_depreciation(self, current_year = None):
        import datetime
        if current_year is None:
            current_year = datetime.datetime.now().year
        age = current_year - self.year
        depreciation_rate = 0.15
        depreciated_price = self.price
        for _ in range(age):
            depreciated_price -= depreciated_price * depreciation_rate
        return depreciated_price

car = Car("Toyota", "Camry", 2010, 20000)
print(car.get_price_after_depreciation())




# Design an Employee class with attributes name, department, and salary, and methods to give a raise and display info.

class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount
        return self.salary

    def display_info(self):
        print(f"Name: {self.name} "
              f"Department: {self.department} "
              f"Salary: {self.salary} ")

Sergiusz_employee = Employee("Sergiusz", "engineer", 5000)
Sergiusz_employee.display_info()
Sergiusz_employee.give_raise(500)
Sergiusz_employee.display_info()


# Create an Employee class with the following:
#
# Attributes:
# - name (string): employee's name
# - department (string): department name
# - salary (float): current salary
# - hire_date (datetime.date): date of hire; defaults to today if not provided
#
# Methods:
# - give_raise(amount): increases salary by given amount (raise cannot be negative)
# - display_info(): prints detailed info about the employee
# - change_department(new_department): updates the department
# - years_with_company(current_year=None): calculates years from hire_date to current year (defaults to today)
# - is_eligible_for_promotion(current_year=None): returns True if employee has been with the company more than 5 years
#
# Additional:
# - Validate that salary is not negative
# - Validate hire_date is a datetime.date object if provided
# - hire_date defaults to today's date
import datetime
class Employee:

    def __init__(self, name, department, salary, hire_date = None):
        if salary < 0:
            raise ValueError("Salary cannot be negative.")
        self.name = name
        self.department = department
        self.salary = salary
        if hire_date is None:
            self.hire_date = datetime.date.today()
        else:
            if isinstance(hire_date, datetime.date):
                self.hire_date = hire_date
            else:
                raise TypeError("hire_date must be a datetime.date object.")
    def give_raise(self, amount):
        if amount < 0:
            raise ValueError("The raise cannot be negative")
        self.salary += amount
        return self.salary

    def display_info(self):
        print(f"The name: {self.name}, the department: {self.department}, the salary: {self.salary}, hiring date: {self.hire_date}")

    def change_department(self, new_department):
        self.department = new_department
        return self.department

    def years_with_company(self, current_year = None):
        if current_year is None:
            current_year = datetime.datetime.now().year
        return current_year - self.hire_date.year

    def is_eligible_for_promotion(self, current_year = None):
        if current_year is None:
            current_year = datetime.datetime.now().year
        return (current_year - self.hire_date.year) > 5





# Build a Point class with x and y coordinates, and a method to compute distance to another point.
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_other(self, other_point):
        distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        return distance

p1 = Point(0, 0)
p2 = Point(3,4)
print(p1.distance_to_other(p2))


# Create a Weather class with an attribute temperature, and methods to convert between Celsius and Fahrenheit.

class Weather:
    def __init__(self, temperature):
        self.temperature = temperature

    def convert_c_to_f(self):
        return (self.temperature * 9/5) + 32

one_day = Weather(20)

print(one_day.convert_c_to_f())

# Temperature Class:
# Create a class with class method from_fahrenheit(cls, temp_f) to instantiate an object from Fahrenheit, converting it to Celsius.

class Temperature:

    def __init__(self, celcius):
        self.celcius = celcius
    @classmethod
    def from_fahrenheit(cls, temp_f):
        celcius = (temp_f - 32) / 1.8
        return cls(celcius)

temp = Temperature.from_fahrenheit(68)
print(temp.celcius)


# Math Utility Class:
# Create a class with static method is_even(number) that returns True if the number is even.
class Uti:

    @staticmethod
    def is_even(number):
        return number % 2 == 0

num = Uti.is_even(4)
print(num)

# Circle Class:
# Create a class with a method to calculate the area and a class method from_diameter(cls, diameter) to create a circle instance from its diameter.
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = math.pi * self.radius **2
        return area

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)
circlinho = Circle(5)
print(circlinho.calculate_area())
circle2 = Circle.from_diameter(10)
print(circle2.calculate_area())

# Person Class:
# Create a class with a class method from_birth_year(cls, name, birth_year)
# that calculates age based on the current year and creates a person object.
import datetime
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = datetime.datetime.now().year
        age = current_year - birth_year
        return cls(name, age)

me = Person.from_birth_year("Sergiusz", 1994)

print(me.name)
print(me.age)


# Product Class:
# Create a class with static method calculate_discounted_price(price, discount_percentage)
# that returns the discount amount; demonstrate usage.

class Product:

    @staticmethod
    def calculate_discounted_price(price, discount_percentage):
        discount = price * (discount_percentage / 100)
        return discount

the_product = Product.calculate_discounted_price(500, 10)
print(the_product)





# Employee Class:
# Create a class with a class method set_default_vacation_days(cls, days) to set a default number of vacation days for all employees.


class Employii:

    default_vacation_days = 10
    def __init__(self, days=None):
        if days is None:
            self.days = Employii.default_vacation_days
        else:
            self.days = days
    @classmethod
    def set_default_vacation_days(cls, days):
        cls.default_vacation_days = days
        return f"You have {days} days of vacation"
Employii.set_default_vacation_days(15)
employii = Employii()
print(employii.days)


# Date Utility Class:
# Create a class with static method days_between(date1, date2) that calculates days difference between two dates.
from datetime import datetime
class Date:
    @staticmethod
    def days_between(date1, date2):
        delta = date2 - date1
        return abs(delta.days)

date1 = datetime.now().date()
date2 = datetime(2020, 7, 20).date()
print(Date.days_between(date1, date2))
# Vehicle Class:
# Create a class with a class method from_model_year(cls, model, year) that creates an object with a calculated age.
from datetime import datetime
class Vehi:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.age = datetime.now().year - year
    @classmethod
    def from_model_year(cls, model, year):
        return cls(model, year)

car = Vehi.from_model_year("Toyota", 1994)
print(car.model)
print(car.age)
print(car.year)

# Temperature Class (Extended):
# Create a class with static method celsius_to_fahrenheit(celsius) that converts Celsius to Fahrenheit, usable without instantiation.

class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (9/5) * celsius + 32

print(Temperature.celsius_to_fahrenheit(20))




# Printer Utility Class:
# Create a class with static method print_bold(text) that prints the text in bold (using ANSI escape codes).

class Printer:
    @staticmethod
    def print_bold(text):
        return f"\033[1;97m{text}\033[0m"

print(Printer.print_bold("Sergiusz"))

# Library Book Management
# Create a Book class with attributes like title, author, and year.
# Add methods to display book details and a class method to keep track of the total number of books created.


class Book:
    total_books = 0
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        Book.total_books += 1

    def details(self):
        print(f"The title: {self.title}, the author: {self.author}, the year: {self.year}")

    @classmethod
    def tracking(cls):
        return cls.total_books

# Student Grade Book
# Create a Student class with attributes name and a list of grades. Include:

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add(self, grade):
        self.grades.append(grade)
        return self.grades
    def average(self):
        return sum(self.grades) / len(self.grades)

    @staticmethod
    def passing_grade(grade, passing = 60):
        return grade >= passing

# An instance method to add a grade.
# An instance method to calculate average grade.
# A static method to check if a grade is passing.
# Vehicle Registration System
# Create a Vehicle class with attributes make, model, and year. Add:
# A class method to create a vehicle from a string like "Toyota,Camry,2020".
# An instance method to display vehicle info.


class Vehic:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    @classmethod
    def string(cls, vehicle_str):
        parts = vehicle_str.split(",")
        make, model, year = parts
        return cls(make, model, int(year))

vehicle_str = "Toyota,Camry,2020"
car = Vehic.string(vehicle_str)
print(f"make: {car.make}")

# E-commerce Cart
# Create an Item class with name, price, and quantity.
# Create a ShoppingCart class with methods to:
# Add items.
# Remove items.
# Calculate total cost (use an instance method).

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)

    def subtract(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]

    def total(self):
        total = 0
        for item in self.items:
            total += (item.price * item.quantity)


# Employee Payroll
# Create an Employee class with attributes name, hours_worked, and hourly_rate.
# Include:
# An instance method to calculate weekly pay.
# A class method to set a standard hourly rate for all employees.
# A static method to check if hours exceed a certain threshold (e.g., overtime).

class Employ:

    standard_rate = 10

    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate if hourly_rate is not None else Employ.standard_rate
    def weekly_pay(self):
        return self.hours_worked * self.hourly_rate

    @classmethod
    def standard_hourly_rate(cls, rate):
        cls.standard_rate = rate

    @staticmethod
    def exceeds_overtime(hours, threshold = 40):
        return hours > threshold


# Create a Book class with the following:
#
# Attributes: title, author, year, and genre.
# A class attribute to keep track of the total number of books created.
# Methods to:
# Display detailed book information.
# Update the book's genre.
# A class method to:
# Create a Book instance from a string that contains the title, author, year, and genre, separated by commas
# (e.g., "1984,George Orwell,1949,Dystopian").
# Implement input validation so that:
# The year must be a valid integer.
# The genre must be one of a predefined set of genres (e.g., "Fiction", "Science Fiction", "Dystopian"). If not, set it to "Unknown".

class Boook:
    books_created = 0
    allowed_genres = ["Fiction", "Science Fiction", "Dystopian"]
    def __init__(self, title, author, year: int, genre):
        self.title = title
        self.author = author
        self.year = year
        if genre in Boook.allowed_genres:
            self.genre = genre
        else:
            self.genre = "Unknown"
        Boook.books_created += 1

    def display(self):
        print(f"The title: {self.title}. "
              f"The author: {self.author}. "
              f"The year: {self.year}. "
              f"The genre: {self.genre}.\n"
              f"Total books: {Boook.books_created}. ")

    def update_genre(self, new_genre):
        if new_genre in Boook.allowed_genres:
            self.genre = new_genre
        else:
            self.genre = "Unknown"
        return self.genre

    @classmethod
    def string(cls, book_str):

        part = book_str.split(",")
        title, author, year, genre = part
        return cls(title, author, int(year), genre)

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Year: {self.year}\n"
                f"Genre: {self.genre}\n"
                f"Total books: {Boook.books_created}")

the_first_book = Boook("1984", "George Orwell", 1949, "Dystopian")
the_second_book = Boook("Brave New World", "Aldous Huxley", 1932, "Science Fiction")

the_first_book.display()
the_second_book.display()
Boook.string("1984,George Orwell,1949,Dystopian")

# Create a Student class with the following features:
# Attributes:name, grades (a dictionary mapping course names to lists of grades)
# Methods:
# To add a grade to a specific course.
# To calculate the average grade for a given course.
# To calculate the overall GPA (average of all course averages).
# Static method:
# To check if a grade is passing based on a specified threshold (default 60), applicable to individual grades.
# Class method:
# To create a student from a formatted string like "John,Math:85,Science:78,History:92"
# where each course and grade are comma-separated in the form CourseName:Grade.
# Bonus:
# Add a method to list all courses the student is enrolled in.
# Add validation to ensure grades are within 0-100.

class Studento:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add(self, course, grade):
        if course in self.grades:
            self.grades[course].append(grade)
        else:
            self.grades[course] = [grade]

    def average(self, course):
        if course in self.grades and self.grades[course]:
            total = sum(self.grades[course])
            count = len(self.grades[course])
            return total / count
        else:
            return None

    def overall_gpa(self):
        total = 0
        count = 0
        for grades_list in self.grades.values():
            total += sum(grades_list)
            count += len(grades_list)
        if count == 0:
            return 0
        return total / count

    @staticmethod
    def check_if_passing(grade, passing_mark = 60):
        return grade >= passing_mark

    @classmethod
    def from_string(cls, student_str):
        parts = student_str.split(",")
        name = parts[0]
        grades_dict = {}
        for item in parts[1:]:
            course, grade_str = item.split(":")
            grade = int(grade_str)
            # Optional: validate grade boundaries
            if 0 <= grade <= 100:
                grades_dict.setdefault(course, []).append(grade)
            else:
                # Handle invalid grades as needed
                grades_dict.setdefault(course, []).append(grade)
        student = cls(name)
        student.grades = grades_dict
        return student


# Rectangle Class:
# Create a class representing a rectangle with width and height attributes. Include methods to calculate area and perimeter.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        area = self.width * self.height
        return area

    def calculate_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

first_rectangle_this_one = Rectangle(2, 5)
print(first_rectangle_this_one.calculate_area())
print(first_rectangle_this_one.calculate_perimeter())

# Advanced Rectangle Class:
# Create a Rectangle class that includes:
#
# Width and height attributes.
# Methods to calculate area and perimeter.
# A method to check if the rectangle is a square (width == height).
# A method to resize the rectangle by a given scale factor (multiplying width and height).
# Overload the __str__() method to display the rectangle’s dimensions, area, and perimeter in a formatted string.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        area = self.width * self.height
        return area

    def calculate_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def if_square(self):
        return self.height == self.width

    def resizing(self, factor):
        self.width = self.width * factor
        self.height = self.height * factor
        return self.width, self.height

    def __str__(self):
        return (f"The area: {self.calculate_area()} "
                f"the perimeter: {self.calculate_perimeter()} "
                f"Is this rectangle a square? {self.if_square()} ")
rectangle = Rectangle(5, 10)
print(rectangle)
print(rectangle.resizing(9))
print(rectangle.calculate_area())






# Circle Class:
# Create a class for a circle with a radius attribute. Add methods to calculate area and circumference.
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = math.pi * self.radius ** 2
        return area

    def calculate_circumference(self):
        circumference = 2 * self.radius * math.pi
        return circumference


# Create a Circle class that includes:
#
# Attributes: radius, and an optional color attribute (default "blue").
# Methods:
# To calculate area and circumference (as before).
# To calculate the diameter.
# To change the circle's radius and color via methods.
# To compare two circles for equality (they are equal if their radii are the same).
# Additional features:
# Implement __str__() to provide a summary of the circumference, area, radius, and color.
# Validate the radius (must be a positive number) in the constructor and setter methods.
import math
class CircleClass:

    def __init__(self, radius, color = "blue"):
        if radius > 0:
            self.radius = radius
        else:
            raise ValueError ("Must be a positive number")
        self.color = color

    def calculate_area(self):
        area = math.pi * self.radius ** 2
        return area

    def calculate_circumference(self):
        circumference = 2 * math.pi * self.radius
        return circumference

    def calculate_diameter(self):
        diameter = 2 * self.radius
        return diameter

    def change_radius_color(self, new_radius, new_color = "blue"):
        self.radius = new_radius
        self.color = new_color
        return self.radius, self.color

    def __eq__(self, other):
        if isinstance(other, CircleClass):
            return self.radius == other.radius
        return False

    def __str__(self):
        return (f"The area: {self.calculate_area()}\n"
                f"The circumference: {self.calculate_circumference()}\n"
                f"The radius: {self.radius}\n"
                f"The diameter: {self.calculate_diameter()}\n"
                f"The color: {self.color}")

the_circle = CircleClass(5, "green")
the_circle2 = CircleClass(6, "red")
print(the_circle)
print(the_circle == the_circle2)
the_circle.change_radius_color(3, "brown")
print(the_circle)
the_circle2.change_radius_color(6.999)
print(the_circle2)

# Bank Account:
# Create a class that represents a bank account with attributes for account number, owner, and balance.
# Include methods to deposit, withdraw, and check the balance.

class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def depositto(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > 0:
            if self.balance > amount:
                self.balance -= amount
        return self.balance

    def display(self):
        print(f"The balance: {self.balance}")

my_account1 = BankAccount(123, "Sergiusz", 5000)
my_account1.withdraw(2000)
my_account1.display()
my_account1.depositto(1000)
my_account1.display()


# Create a BankAccount class with:
#
# Attributes for account number, owner, balance, and an account type (like 'checking' or 'savings').
# Methods to:
# Deposit funds.
# Withdraw funds, with validation for insufficient balance.
# Check the current balance.
# Transfer funds from one account to another.
# Implement a way to track the total number of accounts created.
# Add a method to display an account statement showing all transactions (you'll need to store transaction history).

class BankAccount:
    accounts_created = 0
    def __init__(self, account_number, owner, balance, account_type):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.account_type = account_type
        self.transactions = []
        BankAccount.accounts_created += 1
    def depossitti(self, the_amount):
        if the_amount > 0:
            self.balance += the_amount
        self.transactions.append(f"Deposit: +${the_amount:.2f} | Balance: ${self.balance:.2f}")
        return self.balance

    def withdrawillo(self, the_amount):
        if self.balance > the_amount:
            self.balance -= the_amount
        else:
            print("Unsufficient funds")
        self.transactions.append(f"Withdrawal: -${the_amount:.2f} | Balance: ${self.balance:.2f}")
        return self.balance

    def display(self):
        print(f"The amount: {self.balance} "
              f"The owner: {self.owner} "
              f"The account number: {self.account_number} "
              f"The account type: {self.account_type} ")

    def transferring(self, other_account, amount):
        if amount > 0:
            if self.balance >= amount:
                self.withdrawillo(amount)
                other_account.depossitti(amount)
                print(f"Transferred {amount} from account {self.account_number} to {other_account.account_number}.")
                self.transactions.append(f"Transferring from {self.account_number} to {other_account.account_number}")
                other_account.transactions.append((f"Transfer from {self.account_number}: +${amount:.2f} | Balance: ${other_account.balance:.2f}"))

    def show_statement(self):
        print(f"Statement for account {self.account_number}:")
        for transaction in self.transactions:
            print(transaction)
some_bank_account = BankAccount(12345, "Sergiusz", 2000, "checking")
some_other_bank_account = BankAccount(67890, "Michal", 2000, "checking")
some_bank_account.depossitti(1000)
some_bank_account.withdrawillo(500)
some_bank_account.display()
some_other_bank_account.display()
some_bank_account.transferring(some_other_bank_account, 200)
some_bank_account.display()
some_other_bank_account.display()
some_bank_account.show_statement()
some_other_bank_account.show_statement()


# Student Record:
# Create a class for managing student info with name, age, and a list of grades. Add methods to add grades and calculate the average grade.
#
# Book Library:
# Create a Book class with title, author, and year. Add a method to display info about the book.
#
# Vehicle Class:
# Create a class with attributes like make, model, and year. Add a method to display vehicle info.
#
# Time Class:
# Create a class representing a time (hours, minutes, seconds). Add a method to display the time in "HH:MM:SS" format.
#
# Point in 2D:
# Create a class for a point with x and y coordinates. Add methods to calculate distance to another point.
#
# Contact List:
# Create a Contact class with name, phone number, and email. Add a class method to create a contact from a formatted string like "John,555-1234,john@example.com".
#
# Temperature Converter:
# Create a class with static methods to convert Celsius to Fahrenheit and vice versa.