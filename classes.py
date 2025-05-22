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
