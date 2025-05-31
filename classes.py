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
class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
class Library:
    def __init__(self):
        self.books = []
    def add(self, book):
        self.books.append(book)
    def remove(self, name):
        self.books = [book for book in self.books if book.name != name]
    def listing(self):
        for book in self.books:
            print(f"{book.name}, {book.author}")

    def find_by_author(self, author_name):
        results = []
        for book in self.books:
            if book.author == author_name:
                results.append(book)
        return results







# Build a Playlist class containing songs (as strings). Add methods to add, remove, and list songs. Also, include a method to shuffle songs.
#
# Develop a CarRental class with attributes car model, rental days, and price per day.
# Add methods to calculate total rental cost, apply discounts, and display rental info.
#
# Create a Time class with hours, minutes, and seconds. Add methods to add or subtract time, and display it in HH:MM:SS format.

# Create a class called Student that has:
#
# An attribute name.
# An attribute score.
# When you create a Student object, it should just store the name and score.
#
# Now, create a list of students with different names and scores.
#
# Finally, write a small loop that goes through the list and prints each student's name and score.

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

student1 = Student("Sergiusz", 22)
student2 = Student("Michal", 33)
student3 = Student("Wiesiek", 40)
student4 = Student("Miroslawa", 50)

the_list = [student1, student2, student3, student4]

for s in the_list:
    print(s.name, s.score)



# Practice Task:
# Create a Student class with:
#
# Attributes: name, score, and pass_threshold (the minimum score to pass).
# A method is_passing() that returns True if the student is passing, otherwise False.
# Then:
#
# Create a list of several Student objects with different scores.
# Loop through the list and for each student, print their name, score, and whether they are passing or not.

class Student:
    def __init__(self, name, score, pass_threshold = 50):
        self.name = name
        self.score = score
        self.pass_threshold = pass_threshold
    def is_passing(self):
        return self.score >= self.pass_threshold

first = Student("Sergiusz", 40)
second = Student("Michal", 60)

list_of_students = [first, second]

for s in list_of_students:
    print(s.name, s.score, s.is_passing())

# Create a class called Car. Each Car has:
#
# An attribute called brand.
# An attribute called owner (which should be a Person object).
# A method called car_info() that prints "This car is a [brand], owned by [owner's name]".
# Create a class called Person with:
#
# An attribute called name.
# Then:
#
# Instantiate some Person objects.
# Instantiate some Car objects, assigning each a person as its owner.
# Call the car_info() method for each car.

class Car:
    def __init__(self, brand, owner):
        self.brand = brand
        self.owner = owner
    def car_info(self):
        print(f"This car is a {self.brand}, owned by {self.owner.name}")

class Person:
    def __init__(self, name):
        self.name = name

first_person = Person("Sergiusz")
second_person = Person("Michal")
third_person = Person("Waclaw")

firstc = Car("bmw", first_person)
secondc = Car("subaru", second_person)
thirdc = Car("toyota", third_person)

firstc.car_info()
secondc.car_info()
thirdc.car_info()