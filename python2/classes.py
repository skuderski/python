# class User:
#     pass
#
# user1 = User()
#
# user1.name = "John"
# user1.age = 25
#
# user2 = User()
#
# user2.name = "Emily"
# user2.age = 20

class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

user1 = User("John", 25)
user2 = User("Emily", 20)

print(user1.name)
print(user2.age)

user3 = User(name="Sergiusz", age = 31)
print(user3.name)

# 1. Create a Person Class
# Define a class Person with attributes name and age. Instantiate a person and print their details.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         return f"Hello {self.name}"
# person = Person("Sergiusz", 31)
# print(person.name)
# print(person.age)
#
# print(person.greet())


# 2. Add a Method to Greet
# Extend the Person class to include a method greet() that prints a greeting message including their name.




# 3. Add a Method to Change Attributes
# Add a method have_birthday() that increases the person's age by 1 and prints a birthday message.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello {self.name}. You are {self.age} years old."

    def have_birthday(self):
        self.age += 1
        print(f"Happy birthday, dear {self.name}. You are {self.age}.")

person = Person("Sergiusz", 31)
person.have_birthday()


# 4. Create a Rectangle Class
# Define a class Rectangle with attributes width and height. Add a method area() that returns the area.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height

rectangle = Rectangle(10, 5)

print(rectangle.area())
print(rectangle.perimeter())

# 5. Add Method for Perimeter
# Add a method perimeter() to the Rectangle class that returns its perimeter.


# 6. Implement a BankAccount Class
# Create a class with attributes owner and balance. Add methods deposit(amount) and withdraw(amount) with appropriate checks.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print(f"Unsufficient funds.")
account = BankAccount("Sergiusz", 2000)
account.deposit(200)
print(account.balance)
account.withdraw(100)
print(account.balance)
account.withdraw(3000)
print(account.balance)


# 7. Create a Car Class
# Define a class Car with attributes make, model, and year. Include a method display() that prints all details.



# 8. Add a Method for Age Calculation
# For the Car class, add a method age(current_year) that returns how old the car is based on the current year.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(f"The make: {self.make}, the model: {self.model}, the year: {self.year}")

    def age(self, current_year):
        car_age = current_year - self.year
        return car_age

my_car = Car("Toyota", "Corolla", 1990)

my_car.display()
print(my_car.age(2025))


# 9. Create a Student Class
# Define a class with attributes name, grades (list of grades). Add a method average_grade() that computes and returns the average.

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        avg = sum(self.grades) / len(self.grades)
        return avg

me = Student("Sergiusz", [10, 20, 30, 50])
print(me.average_grade())


# 10. Implement a ShoppingCart Class
# Create a class that manages items in a cart:
# Attributes: list of items
# Methods: add_item(item), remove_item(item), and total_items() returning the number of items.

class ShoppingCart:
    def __init__(self, items):
        self.items = []
    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def total_items(self):
        return len(self.items)

cart = ShoppingCart([])
cart.add_item("zubrowka")
cart.add_item("vodka")
cart.add_item("tequila")
print(cart.total_items())
cart.remove_item("vodka")
print(cart.total_items())

# Task: Create a Node Class and Pair Nodes
# Objective:
#
# Create a class Node with attributes:
#
# id: a unique identifier (string or int),
# connected_node: initially None.
# Write a function connect_nodes(node_ids: list) that:
#
# Takes a list of two node IDs,
# Creates two Node instances with those IDs,
# Sets their connected_node attributes to each other (they become connected),
# Returns both nodes.

class Node:
    def __init__(self, id):
        self.id = id
        self.connected_node = None

def connect_nodes(node_ids: list):
    node1 = Node(node_ids[0])
    node2 = Node(node_ids[1])
    node1.connected_node = node2
    node2.connected_node = node1
    return node1, node2

node1, node2 = connect_nodes(['Node1', 'Node2'])

print(node1.id)
print(node2.id)
print(node1.connected_node.id)
print(node2.connected_node.id)

# Task: Create a Person Class and Link Friends
# Objective:
#
# Create a class Person with attributes:
#
# name (string),
# friend (initially None).
# Write a function make_friends(names: list) that:
#
# Takes a list of two names,
# Creates two Person instances with those names,
# Sets their friend attributes to each other (they become friends),
# Returns both Person objects.

class Person:
    def __init__(self, name: str):
        self.name = name
        self.friend = None

def make_friends(names: list):
    p1 = Person(names[0])
    p2 = Person(names[1])
    p1.friend = p2
    p2.friend = p1
    return p1, p2

person1, person2 = make_friends(['Alice', 'Bob'])
print(person1.name)  # "Alice"
print(person2.name)  # "Bob"
print(person1.friend.name)  # "Bob"
print(person2.friend.name)  # "Alice"

# Objective:
#
# Create a class Device with attributes:
#
# id (string),
# linked_device (initially None).
# Write a function pair_devices(ids: list) that:
#
# Accepts a list of three device IDs,
# Creates three Device objects with those IDs,
# Links each device to the next device in a circular fashion (i.e., device1 linked to device2, device2 linked to device3, device3 linked back to device1),
# Returns all three device objects.

class Device:
    def __init__(self, id: str):
        self.id = id
        self.linked_device = None

def pair_devices(ids: list):
    i1 = Device(ids[0])
    i2 = Device(ids[1])
    i3 = Device(ids[2])
    i1.linked_device = i2
    i2.linked_device = i3
    i3.linked_device = i1
    return i1, i2, i3

device1, device2, device3 = pair_devices(['D1', 'D2', 'D3'])
print(device1.id, device1.linked_device.id)  # D1 D2
print(device2.id, device2.linked_device.id)  # D2 D3
print(device3.id, device3.linked_device.id)  # D3 D1

# Task: Create a Node Class with Multiple Links
# Objective:
#
# Create a class Node with attributes:
#
# name (string),
# connected_nodes (a list of other Node objects).
# Write a function connect_nodes(names: list) that:
#
# Takes a list of at least three node names,
# Creates all Node objects,
# Connects each node to every other node (full mesh connectivity),
# Sets each node’s connected_nodes to include all other nodes,

class Node1:
    def __init__(self, name: str):
        self.name = name
        self.connected_nodes = []

def connect_nodes(names: list):
    node1 = Node1(names[0])
    node2 = Node1(names[1])
    node3 = Node1(names[2])
    node1.connected_nodes = node2, node3
    node2.connected_nodes = node1, node3
    node3.connected_nodes = node1, node2
    return [node1, node2, node3]

nodes = connect_nodes(['A', 'B', 'C'])
for node in nodes:
    print(f"{node.name} is connected to {[n.name for n in node.connected_nodes]}")


# Task: Create a City Class with Mutual Roads
# Objective:
#
# Create a class City with:
#
# name (string),
# connected_cities (list of other City objects).
# Write a function connect_cities(city_names: list) that:
#
# Accepts a list of city names (at least 3),
# Creates a City object for each name,
# Connects every city to every other city (full mesh),
# Ensures each city's connected_cities includes all other cities,
# Returns the list of all City objects.

class City:
    def __init__(self, name: str):
        self.name = name
        self.connected_cities = []

def connect_cities(city_names: list):
    city_one = City(city_names[0])
    city_two = City(city_names[1])
    city_three = City(city_names[2])
    city_one.connected_cities = [city_two, city_three]
    city_two.connected_cities = [city_one, city_three]
    city_three.connected_cities = [city_one, city_two]
    return [city_one, city_two, city_three]

cities = connect_cities(['NYC', 'LA', 'Chicago'])
for city in cities:
    print(f"{city.name} has roads to: {[c.name for c in city.connected_cities]}")

# Objective:
#
# Define a class Device with:
#
# name (string),
# connected_devices (list of other Device instances, initialize as empty list).
# Write a function connect_devices(device_names: list) that:
#
# Accepts a list of device names (at least 3),
# Creates a Device object for each name,
# Connects all devices to each other (full mesh connections),
# Sets each device’s connected_devices to include all other devices,
# Returns the list of all Device objects.

class Device:
    def __init__(self, name: str):
        self.name = name
        self.connected_devices = []

def connect_devices(device_names: list):
    dev1 = Device(device_names[0])
    dev2 = Device(device_names[1])
    dev3 = Device(device_names[2])
    dev1.connected_devices = [dev2, dev3]
    dev2.connected_devices = [dev1, dev3]
    dev3.connected_devices = [dev1, dev2]
    return [dev1, dev2, dev3]

devices = connect_devices(['Router', 'Switch', 'Firewall'])
for device in devices:
    print(f"{device.name} connected to {[d.name for d in device.connected_devices]}")


# Objective:
#
# Create a class Sensor with:
#
# id (string),
# connected_sensors (list of other Sensor objects, initially empty).
# Create a class SensorNetwork with:
#
# sensors (a list of Sensor objects).
# Write methods in SensorNetwork:
#
# add_sensor(sensor_id) to add a new sensor.
# connect_sensors(sensor_id1, sensor_id2) to connect two sensors bidirectionally.
# connect_all() to connect every sensor with every other sensor (full mesh).
# Demonstrate usage:
#
# Add multiple sensors.
# Connect some sensors manually.
# Call connect_all() and print the connections for each sensor.


class Sensor:
    def __init__(self, id):
        self.id = id
        self.connected_sensors = []

class SensorNetwork:
    def __init__(self, sensors=None):
        if sensors is None:
            self.sensors = []
        else:
            self.sensors = sensors
    def add_sensor(self, sensor_id):
        new_sensor = Sensor(sensor_id)
        self.sensors.append(new_sensor)

    def find_sensor(self, sensor_id):
        for sensor in self.sensors:
            if sensor.id == sensor_id:
                return sensor
        return None

    def connect_sensor(self, sensor_id1, sensor_id2):
        sensor1 = self.find_sensor(sensor_id1)
        sensor2 = self.find_sensor(sensor_id2)
        if sensor1 and sensor2:
            sensor1.connected_sensors.append(sensor2)
            sensor2.connected_sensors.append(sensor1)
        else:
            print("One or both sensors not found.")

network = SensorNetwork()
network.add_sensor("S1")
network.add_sensor("S2")
network.add_sensor("S3")
network.connect_sensor("S1", "S2")
network.connect_sensor("S2", "S3")

for sensor in network.sensors:
    print(f"{sensor.id} is connected to {[s.id for s in sensor.connected_sensors]}")

# Define a class Person with:
#
# Attributes: name (string), age (integer), and hobbies (list of strings).
# Implement the following methods:
#
# __init__(self, name, age, hobbies=None): Initialize the person, setting hobbies to an empty list if not provided.
# add_hobby(self, hobby): Add a new hobby to the hobbies list.
# remove_hobby(self, hobby): Remove a hobby if it exists.
# greet(self): Return a greeting string that includes the person's name and age.
# show_hobbies(self): Print all hobbies the person has.
# Instantiate a person with a name, age, and list of hobbies, then:
#
# Add a new hobby.
# Remove an existing hobby.
# Print the greeting.
# Show the current list of hobbies.


class Persona:
    def __init__(self, name, age, hobbies = None):
        self.name = name
        self.age = age
        if hobbies is None:
            self.hobbies = []
        else:
            self.hobbies = hobbies

    def add_hobby(self, hobby):
        self.hobbies.append(hobby)

    def remove_hobby(self, hobby):
        self.hobbies.remove(hobby)

    def greet(self):
        return f"Hello, {self.name}. Are you {self.age} years old?"

    def show_hobbies(self):
        print(f"My hobbies: {self.hobbies}")

persona = Persona("Sergiusz", 31, ["picie wodki"])
persona.add_hobby("picie wina")
persona.add_hobby("picie whiskey")
persona.remove_hobby("picie whiskey")
print(persona.greet())
persona.show_hobbies()

# Define a class Rectangle with:
#
# Attributes: width, height
# Optional attributes: color (string, default "blue") and border_width (default 1)
# Implement the following methods:
#
# area(): returns the rectangle’s area.
# perimeter(): returns the perimeter.
# resize(factor): scales both width and height by factor.
# change_color(new_color): updates the color attribute.
# display(): prints a descriptive string with all properties (dimensions, color, border).
# Create an instance, display its properties, resize it, change its color, and then display again.

class Rectangle:
    def __init__(self, width, height, color="blue", border_width = 1):
        self.width = width
        self.height = height
        self.color = color
        self.border_width = border_width

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height

    def resize(self, factor):
        self.width = factor * self.width
        self.height = factor * self.height

    def change_color(self, new_color):
        self.color = new_color

    def display(self):
        print(f"Rectangle(width={self.width}, height={self.height}, color={self.color}, border_width={self.border_width})")

rect = Rectangle(10, 5)
rect.display()
rect.resize(2)
rect.change_color("green")
rect.display()

# class User2:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_info(self):
#         print(f"{user1.name}, age = {user1.age}")
#
#
# user1 = User2("Sergiusz", 31)
# user1.print_info()
#
# # Objective:
# #
# # Define a class Book with attributes:
# #
# # title (string),
# # author (string),
# # year_published (int).
# # Write a function clone_book(book: Book, new_year: int) -> Book that:
# #
# # Creates a new Book object with the same title and author,
# # Sets the year_published to new_year (or modify as needed),
# # Returns the new Book.
#
# class Book:
#     def __init__(self, title, author, year_published):
#         self.title = title
#         self.author = author
#         self.year_published = year_published
#
# def clone_book(book: Book, new_year: int):
#     return Book(book.title, book.author, new_year)
#
# # Objective:
# #
# # Define a class Movie with attributes:
# #
# # title (string),
# # director (string),
# # release_year (int),
# # rating (float, optional, default to None).
# # Write a function clone_movie(movie: Movie, new_rating: float = None) -> Movie that:
# #
# # Creates a new Movie object with the same title, director, and release year.
# # Sets the rating to new_rating if provided; otherwise keeps the original rating.
# # Returns the new Movie.
#
# class Movie:
#     def __init__(self, title, director, release_year, rating = None):
#         self.title = title
#         self.director = director
#         self.release_year = release_year
#         self.rating = rating
#
# def clone_movie(movie: Movie, new_rating: float = None):
#     return Movie(movie.title, movie.director, movie.release_year, new_rating)
#
# original_movie = Movie("Inception", "Christopher Nolan", 2010, rating=8.8)
# new_reviewed_movie = clone_movie(original_movie, new_rating=9.0)
#
# print(f"Original: {original_movie.title}, Rating: {original_movie.rating}")
# print(f"Cloned: {new_reviewed_movie.title}, Rating: {new_reviewed_movie.rating}")

# Define a class Song with attributes:
#
# title (string),
# artist (string),
# album (string),
# year (int),
# rating (float, optional, default None).
# Write a function clone_song(song: Song, new_rating: float = None, new_year: int = None) -> Song that:
#
# Creates a new Song object with the same title, artist, and album.
# Optionally updates the rating if new_rating is provided.
# Optionally updates the year if new_year is provided.
# Returns the new Song object.

class Song:
    def __init__(self, title, artist, album, year, rating = None):
        self.title = title
        self.artist = artist
        self.album = album
        self.year = year
        self.rating = rating

def clone_song(song: Song, new_rating: float = None, new_year: int = None):
    return Song(song.title, song.artist, song.album,
                year=new_year if new_year is not None else song.year,
                rating = new_rating if new_rating is not None else song.rating)

original = Song("Yesterday", "The Beatles", "Help!", 1965, 9.2)
clone = clone_song(original, new_rating=9.8, new_year=1966)
print(clone.title, clone.year, clone.rating)

# Objective:
#
# Define a class Book with:
#
# Attributes: title (string), author (string), year_published (int), rating (float, optional, default None).
# Write a function clone_book(book: Book, new_year=None, new_rating=None) that:
#
# Creates a new Book object with the same title and author.
# If new_year is provided, set year_published to that; otherwise, keep original.
# If new_rating is provided, set rating to that; otherwise, keep original.
# Demonstrate by cloning an existing book with a new year and rating.

class Book:
    def __init__(self, title, author, year_published, rating = None):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.rating = rating

def clone_book(book: Book, new_year = None, new_rating = None):
    return Book(title=book.title,
                author=book.author,
                year_published=new_year if new_year is not None else book.year_published,
                rating=new_rating if new_rating is not None else book.rating)

original = Book("1984", "George Orwell", 1949, rating = 9.0)
cloned = clone_book(original, new_year=2002, new_rating=8.8)
print(cloned.title, cloned.year_published, cloned.rating)

# Objectives:
#
# Define a Movie class with attributes:
#
# title (str)
# director (str)
# release_year (int)
# rating (float, optional, default None)
# Write a function clone_movie(movie: Movie, new_year=None, new_rating=None) that:
#
# Creates a new Movie object with the same title and director
# Sets release_year to new_year if provided, otherwise keeps the original
# Sets rating to new_rating if provided, otherwise keeps the original
# Demonstrate by cloning an existing movie with different year and rating.

class Movie:
    def __init__(self, title, director, release_year, rating = None):
        self.title = title
        self.director = director
        self.release_year = release_year
        self.rating = rating

def clone_movie(movie: Movie, new_year=None, new_rating=None):
    return Movie(title=movie.title,
                 director=movie.director,
                 release_year=new_year if new_year is not None else movie.release_year,
                 rating= new_rating if new_rating is not None else movie.rating)

originall = Movie("Gladiator", "Stephen Spielberg", 2000, 9.2)
clonedd = clone_movie(originall, new_year=2002)
print(clonedd.title, clonedd.director, clonedd.release_year, clonedd.rating)

# Objective:
#
# Define a class Counter.
# It should have:
# An attribute value (initially 0).
# Implement the following methods:
# increment(): increases value by 1.
# decrement(): decreases value by 1.
# reset(): resets value to 0.
# display(): prints the current value.

class Counter:
    def __init__(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def reset(self):
        self.value = 0

    def display(self):
        print(f"{self.value}")

counter = Counter()
counter.increment()
counter.increment()
counter.decrement()
counter.increment()
counter.display()

# Define a class BankAccount with:
# 
# Attributes:
# owner (string)
# balance (float, initially 0.0)
# Methods:
# deposit(amount): adds amount to balance, only if amount is positive.
# withdraw(amount): subtracts amount if sufficient funds exist, and amount is positive.
# get_balance(): returns current balance.
# display(): prints the owner's name and current balance.
# Add validation:
# 
# If deposit() or withdraw() are called with invalid amounts (zero or negative), print an error message.
# Demonstrate usage:
# 
# Create an account, make some deposits and withdrawals, and display the account status after each operation.

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Negative amount cannot be added.")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Error: Insufficient funds.")
        else:
            self.balance -= amount
    
    def get_balance(self):
        return self.balance

    def display(self):
        print(f"The name: {self.owner}, current balance: {self.balance}")

acc = BankAccount("Alice")
acc.display()  # Owner: Alice, Balance: $0.00
acc.deposit(200)
acc.display()  # Owner: Alice, Balance: $200.00
acc.withdraw(50)
acc.display()  # Owner: Alice, Balance: $150.00
acc.withdraw(200)  # Insufficient funds
acc.deposit(-10)

# Define a class Car with attributes:
#
# doors (int)
# wheels (int)
# engines (int)
# Write a function total_car_parts(cars: list) -> dict that:
#
# Takes a list of Car objects
# Computes the total number of doors, wheels, and engines across all cars
# Returns a dictionary similar to: {"doors": total, "wheels": total, "engines": total}

class Car:
    def __init__(self, doors, wheels, engines):
        self.doors = doors
        self.wheels = wheels
        self.engines = engines

def total_car_parts(cars: list) -> dict:
    total = {"doors": 0, "wheels": 0, "engines": 0}
    for car in cars:
        total["doors"] += car.doors
        total["wheels"] += car.wheels
        total["engines"] += car.engines

    return total

cars = [Car(4, 4, 1), Car(2, 4, 1), Car(4, 4, 2)]
totals = total_car_parts(cars)
print(totals)

# Define a class Computer with attributes:
#
# cpu_cores (int)
# ram_gb (int)
# storage_gb (int)
# Write a function total_computer_specs(computers: list) -> dict that:
#
# Takes a list of Computer objects
# Computes the total number of CPU cores, RAM (GB), and storage (GB) across all systems
# Returns a dictionary like: {"total_cores": total, "total_ram_gb": total, "total_storage_gb": total}

class Computer:
    def __init__(self, cpu_cores, ram_gb, storage_gb):
        self.cpu_cores = cpu_cores
        self.ram_gb = ram_gb
        self.storage_gb = storage_gb

def total_computer_specs(computers: list) -> dict:
    total = {"cpu_cores": 0, "ram_gb": 0, "storage_gb": 0}
    for computer in computers:
        total["cpu_cores"] += computer.cpu_cores
        total["ram_gb"] += computer.ram_gb
        total["storage_gb"] += computer.storage_gb

    return total

computers = [
    Computer(8, 32, 1024),
    Computer(4, 16, 512),
    Computer(16, 64, 2048)
]
totals = total_computer_specs(computers)
print(totals)

# Define a class Smartphone with attributes:
#
# brand (str)
# model (str)
# storage_gb (int)
# camera_megapixels (int)
# Write a function total_smartphone_specs(smartphones: list) -> dict that:
#
# Takes a list of Smartphone objects
# Calculates the total storage (GB) and total camera megapixels
# Returns a dictionary like: {"total_storage_gb": total, "total_camera_megapixels": total}

class Smartphone:
    def __init__(self, brand, model, storage_gb, camera_megapixels):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.camera_megapixels = camera_megapixels

def total_smartphone_specs(smartphones: list) -> dict:
    total = {"total_storage_gb": 0, "total_camera_megapixels": 0}
    for smartphone in smartphones:
        total["total_storage_gb"] += smartphone.storage_gb
        total["total_camera_megapixels"] += smartphone.camera_megapixels

    return total

smartphones = [
    Smartphone("Apple", "iPhone 13", 128, 12),
    Smartphone("Samsung", "Galaxy S21", 256, 64),
    Smartphone("Google", "Pixel 6", 128, 50)
]
totals = total_smartphone_specs(smartphones)
print(totals)

# Define a class Laptop with attributes:
#
# brand (str)
# model (str)
# cpu_cores (int)
# ram_gb (int)
# storage_gb (int)
# Write a function aggregate_laptop_specs(laptops: list) -> dict that:
#
# Accepts a list of Laptop objects
# Calculates:
# Total CPU cores
# Total RAM (GB)
# Total storage (GB)

class Laptop:
    def __init__(self, brand, model, cpu_cores, ram_gb, storage_gb):
        self.brand = brand
        self.model = model
        self.cpu_cores = cpu_cores
        self.ram_gb = ram_gb
        self.storage_gb = storage_gb

def aggregate_laptop_specs(laptops: list) -> dict:
    total = {"total_cpu_cores": 0, "total_ram_gb": 0, "total_storage_gb": 0}
    for laptop in laptops:
        total["total_cpu_cores"] += laptop.cpu_cores
        total["total_ram_gb"] += laptop.ram_gb
        total["total_storage_gb"] += laptop.storage_gb

    return total


laptops = [
    Laptop("Dell", "XPS 13", 4, 16, 512),
    Laptop("MacBook", "Air", 4, 8, 256),
    Laptop("Lenovo", "ThinkPad", 4, 32, 1024)
]
totals = aggregate_laptop_specs(laptops)
print(totals)

# Define a class Server with:
#
# name (str)
# cpu_cores (int)
# ram_gb (int)
# network_bandwidth_gbps (float, network bandwidth in gigabits per second)
# Write a function total_network_capacity(servers: list) -> dict that:
#
# Takes a list of Server objects
# Calculates the:
# Total CPU cores
# Total RAM (GB)
# Total network bandwidth (sum of all servers’ network_bandwidth_gbps)

class Server:
    def __init__(self, name, cpu_cores, ram_gb, network_bandwidth_gbps):
        self.name = name
        self.cpu_cores = cpu_cores
        self.ram_gb = ram_gb
        self.network_bandwidth_gbps = network_bandwidth_gbps

def total_network_capacity(servers: list) -> dict:
    total = {"total_cpu_cores": 0, "total_ram_gb": 0, "total_network_bandwidth_gbps": 0}
    for server in servers:
        total["total_cpu_cores"] += server.cpu_cores
        total["total_ram_gb"] += server.ram_gb
        total["total_network_bandwidth_gbps"] += server.network_bandwidth_gbps

    return total

servers = [
    Server("Server1", 16, 64, 10.0),
    Server("Server2", 32, 128, 40.0),
    Server("Server3", 8, 32, 5.0)
]
totals = total_network_capacity(servers)
print(totals)

# Create a Student class with: name (str) student_id (int) courses (list of course names)
# Create a Department class with: name (str)students (list of Student objects)
# Methods: # add_student(student: Student)##
# average_students_per_course(): calculates the average number of students per course (assume each student can have multiple courses)
# Create a University class with:
# name (str)
# departments (list of Department objects)
# Methods:
# add_department(department: Department)
# total_students(): total number of students in all departments
# average_students_per_department()
# Create some students, departments, and add them to the university.
# Calculate and print:
# Total students in the university.
# Average students per department.
# Average students per course across all departments.

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def add_course(self, course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)
        else:
            print(f"{course_name} is already in {self.name}'s course list.")

class Department:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []

    def add_student(self, student: Student):
        self.students.append(student)
        for course in student.courses:
            if course not in self.courses:
                self.courses.append(course)

    def average_students_per_course(self):
        total_courses = len(self.courses)
        if total_courses == 0:
            return 0
        total_students = len(self.students)
        return total_students / total_courses

    def print_department_info(self):
        print(f"Department: {self.name}")
        print(f"Number of students: {len(self.students)}")
        print("Students and their courses:")
        for student in self.students:
            print(f" - {student.name}: {student.courses}")
        print(f"Courses offered: {self.courses}")
        print(f"Average students per course: {self.average_students_per_course():.2f}")
        print("-" * 40)


class University:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department: Department):
        self.departments.append(department)

    def total_students(self):
        total = 0
        for department in self.departments:
            total += len(department.students)
        return total

    def average_student_per_department(self):
        total = 0
        for department in self.departments:
            total += len(department.students)

        average = total / len(self.departments)
        return average
student1 = Student("Sergiusz", 123)
student2 = Student("Michal", 321)
student3 = Student("Martyna", 333)
student4 = Student("Inga", 232)
student5 = Student("Irena", 120)
student1.add_course("Psychology")
student2.add_course("Psychology")
student3.add_course("Psychology")
student4.add_course("Psychology")
student5.add_course("Psychology")
department1 = Department("CS")
department2 = Department("Medicine")
department1.add_student(student1)
department1.add_student(student2)
department1.add_student(student3)
department2.add_student(student4)
department2.add_student(student5)
uni = University("Stefana Wyszynskiego")
uni.add_department(department1)
uni.add_department(department2)
print(uni.total_students())
print(uni.average_student_per_department())
print(department1.average_students_per_course())
print(department2.average_students_per_course())
department1.print_department_info()
department2.print_department_info()

# Objective:
#
# Define a class BankAccount with attributes:
#
# owner (string)
# balance (float, default 0.0)
# Implement the following methods:
#
# deposit(amount) — adds money to the balance. If the amount is negative, print an error.
# withdraw(amount) — subtracts money if enough balance exists. If insufficient, print a message.
# get_balance() — returns the current balance.
# display() — prints the owner and current balance.
# Create an account instance, perform some deposits and withdrawals, and print out the account details.

class BankAccount:
    def __init__(self, owner, balance = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print(f"Negative amount")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance

    def display(self):
        print(f"The owner: {self.owner}, the balance: {self.balance}")

my_bank_account = BankAccount("Sergiusz", 100000)
my_bank_account.deposit(2000)
my_bank_account.withdraw(1000)
print(my_bank_account.get_balance())
my_bank_account.display()

# Objective:
# Define a class Book with attributes:
# title (string)
# author (string)
# total_copies (int)
# copies_available (int)
# Implement methods:
# borrow() — decreases copies_available by 1 if available. If none available, print a message.
# return_book() — increases copies_available by 1.
# add_copies(number) — increases total_copies and copies_available by the given number.
# display() — shows the book details, including how many copies are available.
# Create a Book object, simulate borrowing and returning books, and display the status.

class Book:
    def __init__(self, title, author, total_copies, copies_available):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.copies_available = copies_available

    def borrow(self):
        if self.copies_available <= 0:
            print(f"no copies available")
        else:
            self.copies_available -= 1

    def return_book(self):
        if self.copies_available < self.total_copies:
            self.copies_available += 1
        else:
            print("All copies already in the library.")

    def add_copies(self, number):
        self.total_copies += number
        self.copies_available += number

    def display(self):
        print(f"Title: {self.title}, author: {self.author}, total copies: {self.total_copies}, copies available: {self.copies_available}")


book = Book("1984", "George Orwell", 5, 3)

book.borrow()
book.borrow()
book.display()
book.return_book()
book.display()
book.add_copies(2)
book.display()


class Matrix:
    def __init__(self, matrix: list) -> None:
        self.matrix = matrix

    def get_diagonal(self) -> list:
        return [self.matrix[i][i] for i in range(len(self.matrix))]

    def get_counter_diagonal(self) -> list:
        return [self.matrix[i][-i - 1] for i in range(len(self.matrix))]

    def rotate_rows(self, number: int) -> None:
        if not self.matrix:
            return
        num = number % len(self.matrix)
        self.matrix = self.matrix[num:] + self.matrix[:num]

    def rotate_columns(self, number: int) -> None:
        if not self.matrix:
            return
        num = number % len(self.matrix)
        for i in range(len(self.matrix)):
            self.matrix[i] = self.matrix[i][num:] + self.matrix[i][:num]

matrix = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(matrix.get_diagonal())
print(matrix.get_counter_diagonal())
matrix.rotate_columns(1)
print(matrix.matrix)

# 1. Create a Vehicle Class
# Define a class Vehicle with attributes like make, model, and year.
# Add methods to display info and determine if the vehicle is vintage (older than 25 years).
import datetime
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        current_year = datetime.datetime.now().year
        age = current_year - self.year
        if age > 25:
            print(f"{self.make} {self.model} is vintage and is from {self.year}.")
        else:
            print(f"{self.make} {self.model} is not vintage and is from {self.year}")

vehic = Vehicle("Toyota", "Corolla", 1990)
vehic.display()


# 2. Employee Management
# Create an Employee class with attributes like name, employee_id, and department.
# Add methods to change department, display employee info, and give a raise (increase salary).

class Employee:
    def __init__(self, name, employee_id, department, salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def change_dep(self, new_dep):
        self.department = new_dep

    def display(self):
        print(f"Name of the employee: {self.name}, employee id: {self.employee_id}, the department: {self.department}, salary: {self.salary}")

    def give_raise(self, give_raise):
        if give_raise > 0:
            self.salary += give_raise
me = Employee("Sergiusz", "12345", "Customer Service", 20000)
me.change_dep("HR")
me.give_raise(2000)
me.display()

# 3. Book Library System
# Create a Book class with attributes title, author, copies_available.
# Add methods to borrow a book (reduce copies), return a book, and add new copies.

class Book:
    def __init__(self, title, author, copies_available):
        self.title = title
        self.author = author
        self.copies_available = copies_available

    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -= 1
        else:
            print("No copies available to borrow.")

    def return_book(self):
        self.copies_available += 1

    def add_new_copies(self, num):
        self.copies_available += num

    def display(self):
        print(f"Name: {self.title}, author: {self.author}, copies available: {self.copies_available}")

one = Book("The Bible", "God", 20)
one.borrow_book()
one.borrow_book()
one.return_book()
one.add_new_copies(5)
one.display()


# 4. Bank Account with Transfer
# Create a BankAccount class with methods to deposit, withdraw, and transfer money between accounts.

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("The amount cannot be negative")

    def withdraw(self, amount):
        if self.balance <= 0:
            print("Cannot withdraw, no money")
        elif amount > self.balance:
            print("Cannot withdraw. Insufficient funds.")
        else:
            self.balance -= amount
    def transfer(self, target_account, amount):
        if amount <= 0:
            print("Transfer amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds for transfer.")
        else:
            self.withdraw(amount)
            target_account.deposit(amount)

    def display(self):
        print(f"name: {self.name}, balance: {self.balance}")

my_account = BankAccount("Sergiusz", 20000)
other_account = BankAccount("Waclaw", 30000)
my_account.deposit(300)
my_account.withdraw(100)
my_account.transfer(other_account, 350)
my_account.display()
other_account.display()




# 5. School Class Management
# Create a School class that contains students as objects with attributes before name and grade.
# Add methods to add students, remove students, and find students by grade.

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


class School:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def remove_student(self, student_name):
        self.students = [s for s in self.students if s.name != student_name]

    def find_student_by_grade(self, grade):
        return [s for s in self.students if s.grade == grade]

    def display(self):
        print(f"The students:")
        for s in self.students:
            print(f"Name: {s.name}, Grade: {s.grade}")

Serg = Student("Sergiusz", "B")
Tom = Student("Tommy", "A")
Pete = Student("Piotrek", "C")
the_sql = School()
the_sql.add_student(Serg)
the_sql.add_student(Tom)
the_sql.add_student(Pete)
the_sql.remove_student("Sergiusz")
the_sql.find_student_by_grade("A")
the_sql.add_student(Serg)
the_sql.display()



# 6. Simple Shopping Cart
# Build a Product class with attributes like name and price.
# Then create a ShoppingCart class that can add products, calculate total, and list all items.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_products(self, product):
        self.items.append(product)

    def calc_total(self):
        return sum(product.price for product in self.items)

    def list_products(self):
        for product in self.items:
            print(f"{product.name}: ${product.price:.2f}")

p1 = Product("pen", 2.99)
p2 = Product("banana", 3.99)
p3 = Product("apple", 2)
cart = ShoppingCart()
cart.add_products(p1)
cart.add_products(p2)
cart.add_products(p3)
print(cart.calc_total())
cart.list_products()

# 7. Online User Profile
# Create a UserProfile class with username, email, and list of friends.
# Add methods to add friends, remove friends, and display the friends list.

class UserProfile:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
        else:
            print(f"{friend.username} is already a friend")

    def remove_friends(self, friend):
        if friend in self.friends:
            self.friends.remove(friend)

    def display(self):
        print(f"{self.username}'s friends:")
        for friend in self.friends:
            print(f" - {friend.username}")

user11 = UserProfile("skuderski", "skuderski@gmail.com")
user22 = UserProfile("qwwerty", "qwerty@gmail.com")
user33 = UserProfile("xyz", "xyz@gmail.com")
user11.add_friend(user22)
user11.add_friend(user33)
user11.display()
user11.remove_friends(user33)
user11.display()

user22.add_friend(user11)
user22.add_friend(user33)
user22.display()

# 8. Airline Booking System
# Create a Flight class with attributes such as flight_number, origin, destination,
# and passenger_list. Add methods to book a passenger, cancel booking, and print passenger list.

class Flight:
    def __init__(self, flight_number, origin, destination):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.passenger_list = []

    def book_passenger(self, name):
        if name not in self.passenger_list:
            self.passenger_list.append(name)
        else:
            print(f"{name} already on the list")

    def cancel_booking(self, name):
        if name in self.passenger_list:
            self.passenger_list.remove(name)
        else:
            print(f"{name} is not booked.")

    def print_list(self):
        print(f"The list of passengers:")
        for passenger in self.passenger_list:
            print(f" - {passenger}")

flight1 = Flight("1234567", "New York", "LA")
flight1.book_passenger("Sergiusz Kuderski")
flight1.book_passenger("Martyna Mojecka")
flight1.print_list()


# 9. Movie Collection
# Create a Movie class with attributes like title, director, and rating.
# Add methods to rate the movie, display info, and check if the movie is top-rated (above a certain rating).

class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director
        self.ratings = []

    def rate_movie(self, new_rating):
        if 0 <= new_rating <= 10:
            self.ratings.append(new_rating)
        else:
            print("Rating must be between 0 and 10")
    def top_rated(self):
        if not self.ratings:
            print(f"{self.title} has no ratings yet.")
            return
        if any(r > 9 for r in self.ratings):
            print(f"{self.title} is top-rated.")
        else:
            print(f"{self.title} is not top-rated.")
    def display(self):
        print(f"The movie: {self.title}, by {self.director},")
        for r in self.ratings:
            print(f" rating - {r}")
movie1 = Movie("Gladiator", "Ridley Scott")
movie2 = Movie("The Departed", "Martin Scorsese")
movie1.rate_movie(9.2)
movie1.rate_movie(8)
movie2.rate_movie(8)
movie2.rate_movie(7)
movie1.top_rated()
movie2.top_rated()
movie1.display()
movie2.display()



# 10. Weather Station
# Create a WeatherStation class with attributes location, temperature, humidity.
# Add methods to update readings, display current weather, and convert temperature to Celsius or Fahrenheit.

class WeatherStation:
    def __init__(self, location, temperature_celsius, humidity):
        self.location = location
        self.temperature_celsius = temperature_celsius
        self.humidity = humidity

    def update_reading(self, new_temperature, new_humidity):
        self.temperature_celsius = new_temperature
        self.humidity = new_humidity

    def current_weather(self):
        print(f"The current weather in {self.location} is {self.temperature_celsius} C with {self.humidity}% humidity")

    def convertion(self):
        return self.temperature_celsius * 9 / 5 + 32


ws = WeatherStation("Vilnius", 30, 25)
ws.update_reading(29, 24)
ws.current_weather()
print(ws.convertion())

# 1. Create a Person Class
# Define a class with attributes name and age, with methods to display info, celebrate birthday (increment age), and introduce themselves.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def celebrate_birthday(self):
        self.age += 1

    def introduce_yourself(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

Sergiusz = Person("Sergiusz", 31)
Sergiusz.display()
Sergiusz.celebrate_birthday()
Sergiusz.introduce_yourself()

# 2. Create a Rectangle Class
# Define a rectangle with width and height; add methods to compute area, perimeter, and resize the rectangle.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def compute_area(self):
        area = self.width * self.height
        return area

    def perimeter(self):
        peri = self.width * 2 + self.height * 2
        return peri

    def resizing(self, scale_factor):
        self.width *= scale_factor
        self.height *= scale_factor

    def display(self):
        print(f"perimeter: {rect.perimeter()}, area: {rect.compute_area()}")

rect = Rectangle(10, 20)
rect.compute_area()
rect.perimeter()
rect.display()
rect.resizing(3)
rect.display()


# 3. Create a BankAccount Class
# Implement deposit, withdraw, transfer, and display methods, including validation for sufficient balance.

class BankAccount:
    def __init__(self, balance, bank_number):
        self.balance = balance
        self.bank_number = bank_number

    def deposit(self, amount):
        if amount < 0:
            print("Amount has to be positive")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough funds in the bank account")
        else:
            self.balance -= amount
    def transfer(self, amount, target_account):
        if amount <= 0:
            print("Transfer amount must be positive")
        elif amount > self.balance:
            print("Not enough funds to transfer")
        self.balance -= amount
        target_account.deposit(amount)
    def display(self):
        print(f"The account has {self.balance}$ and the account number is {self.bank_number}")


my_bank_acc = BankAccount(10000, 1234)
other_bank_acc = BankAccount(20000, 4567)
my_bank_acc.deposit(1000)
my_bank_acc.withdraw(500)
my_bank_acc.display()
my_bank_acc.transfer(100, other_bank_acc)
other_bank_acc.display()
my_bank_acc.display()


# 4. Create a Student Class
# Include attributes like name, student_id, and courses (list). Add methods to add courses, remove courses, and display student info.

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f"{course} is already enrolled.")
    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)

    def display_info(self):
        print(f"Student's name: {self.name}, student id: {self.student_id}, enrolled in {self.courses}")

Sergiuszek = Student("Sergiusz", 69420)
Sergiuszek.add_course("Computer Science")
Sergiuszek.display_info()


# 5. Create a Car Class
# With attributes make, model, year, and miles_driven. Add methods to drive (increment miles) and display info.

class Car:
    def __init__(self, make, model, year, miles_driven):
        self.make = make
        self.model = model
        self.year = year
        self.miles_driven = miles_driven

    def drive(self, increment):
        self.miles_driven += increment

    def display_info(self):
        print(f"Make: {self.make}, model: {self.model}, year: {self.year}, miles driven: {self.miles_driven}")


toyota = Car("Toyota", "Corollakis", 1994, 20000)
toyota.drive(2000)
toyota.display_info()


# 6. Create a Book Class
# Attributes: title, author, total_copies, copies_available. Methods for borrowing (decrementing available copies), returning, and restocking.

class Book:
    def __init__(self, title, author, total_copies, copies_available):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.copies_available = copies_available

    def borrow(self, copies):
        if copies <= 0:
            print("Number of copies must be positive")
        elif copies > self.copies_available:
            print(f"Not enough copies to borrow. Available: {self.copies_available}")
        else:
            self.copies_available -= copies
            print(f"Borrowed {copies} copies of '{self.title}'")

    def returning(self, copies):
        if copies <= 0:
            print("Number of copies must be positive")
        self.copies_available += copies

    def restocking(self, copies):
        self.total_copies += copies
        self.copies_available += copies

    def displaying(self):
        print(f"title: {self.title}, author: {self.author}, total copies: {self.total_copies}, copies available: {self.copies_available}")

the_book = Book("Lord of the Rings", "J. R. R. Tolkien", 20000, 20)
the_book.borrow(3)
the_book.restocking(5)
the_book.displaying()


# 7. Create an Inventory Class
# Manage items with name and quantity. Add methods to add items, remove items, and check total stock.

class Inventory:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def add_items(self, amount):
        if amount <= 0:
            print("Add amount must be positive.")
        else:
            self.quantity += amount

    def remove_items(self, amount):
        if amount <= 0:
            print("Remove amount must be positive.")
        elif amount > self.quantity:
            print(f"Cannot remove {amount} {self.name}(s). Only {self.quantity} in stock.")
        else:
            self.quantity -= amount
            print(f"Removed {amount} {self.name}(s). New stock: {self.quantity}")

    def check_stock(self):
        return self.quantity



# 8. Create a Movie Class
# Attributes: title, director, release_year, rating. Methods to update rating, and display movie info,
# and check if it's a classic (e.g., older than 30 years).

class Movie:
    def __init__(self, title, director, release_year, rating):
        self.title = title
        self.director = director
        self.release_year = release_year
        self.rating = rating

    def update_rating(self, new_rating):
        self.rating = new_rating

    def classic_check(self, current_year = 2025):
        return (current_year - self.release_year) > 30


    def display(self):
        print(f"The title: {self.title}, the director: {self.director}, the release year: {self.release_year}, the rating: {self.rating}")

the_movie = Movie("Gladiator", "Ridley Scott", 2002, 8.0)
print(the_movie.classic_check())
the_movie.display()


# 9. Create a ShoppingCart Class
# Items (name, price, quantity). Methods to add items, remove items, and calculate total cost.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_items(self, item):
        self.items.append(item)

    def remove_items(self, product_name):
        for product in self.items:
            if product.name == product_name:
                self.items.remove(product)
                print(f"Removed {product_name}.")
                return
        print(f"{product_name} not found in cart.")

    def calc_cost(self):
        total = 0
        for product in self.items:
            total += product.price * product.quantity
        return total


banana = Product("banana", 2.99, 100)
apple = Product("apple", 2.00, 50)
kiwi = Product("kiwi", 4.40, 25)
cart  = ShoppingCart()
cart.add_items(banana)
cart.add_items(apple)
cart.add_items(kiwi)
print(cart.calc_cost())

# 10. Create a Light Class
# Attributes: color, status (on/off). Methods to turn on/off, change color, and display status.

class Light:
    def __init__(self, color, status: bool):
        self.color = color
        self.status = status

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

    def change_color(self, new_color):
        self.color = new_color

    def display_status(self):
        print(f"Current color is {self.color}.")
        if self.status is True:
            print(f"The status is on.")
        else:
            print(f"The status is off.")

the_light = Light("blue", True)
the_light.display_status()
the_light.change_color("yellow")
the_light.turn_off()
the_light.display_status()



# 1. Create a Calculator Class
# Attributes: None needed initially.
# Methods:
# add(a, b)
# subtract(a, b)
# multiply(a, b)
# divide(a, b) (handle division by zero)
# Use the class without storing any state; just call methods and print results.

class Calculator:
    def __init__(self):
        return

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            print(f"Cannot divide by 0")
            return None
        return a / b
calculator = Calculator()
print(calculator.add(2, 5))
print(calculator.subtract(2, 5))
print(calculator.multiply(2, 5))
print(calculator.divide(5, 5))



# 2. Create a Timer Class
# Attributes:
# start_time (set to None initially)
# Methods:
# start(): start the timer (record current time)
# stop(): stop the timer (calculate elapsed time)
# reset(): reset the timer
# get_elapsed_time(): return the elapsed time
# Use the class to time a sleep operation (time.sleep()), then display the elapsed time.
# import time
# class Timer:
#     def __init__(self):
#         self.start_time = None
#     def start(self):
#         self.start_time = time.time()
#
#     def stop(self):
#         if self.start_time is None:
#             print("Timer was not started.")
#             return
#         elapsed_time = time.time() - self.start_time
#         print(f"Timer stopped. Total elapsed: {elapsed_time:.2f} seconds.")
#         self.start_time = None  # Reset or keep as needed
#         return elapsed_time
#
#     def elapsed(self):
#         if self.start_time is None:
#             print("Timer has not been started.")
#             return
#         current_time = time.time()
#         current_elapsed = current_time - self.start_time
#         print(f"Current elapsed time: {current_elapsed:.2f} seconds")
#         return current_elapsed
#
#     def reset(self):
#         self.start_time = None
#         print("Timer reset")
#
# timer = Timer()
# timer.start()
# time.sleep(2)
# timer.elapsed()
# timer.stop()
# timer.reset()
# time.sleep(3)
# timer.start()
# time.sleep(0.5)
# timer.elapsed()





# 3. Create a Rectangle Class
# Attributes:
# length, width
# Methods:
# area()
# perimeter()
# resize(factor) (scale both length and width)
# display() (print dimensions and area)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * self.width + 2 * self.length

    def resize(self, factor):
        self.width *= factor
        self.length *= factor

    def display(self):
        print(f"length: {self.length}, width: {self.width}, area: {self.area()}, perimeter: {self.perimeter()}")

recti = Rectangle(5, 9)
print(recti.area())
print(recti.perimeter())
recti.resize(1.5)
recti.display()





# 4. Create a Fan Class
# Attributes:
# speed (1, 2, 3)
# status (on or off)
# Methods:
# turn_on()
# turn_off()
# set_speed(speed)
# display() (show current state)

class Fan:
    def __init__(self, speed = 1, status = False):
        self.speed = speed
        self.status = status

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

    def set_speed(self, speed):
        if speed in (1, 2, 3):
            self.speed = speed
        else:
            print("Invalid speed, must be 1, 2 or 3")

    def display(self):
        state = "On" if self.status else "Off"
        print(f"Fan is {state}. Speed: {self.speed}")

my_fan = Fan()
my_fan.turn_off()
my_fan.set_speed(2)
my_fan.display()


# 5. Create a Point Class
# Attributes:
# x, y coordinates
# Methods:
# move(dx, dy) (move the point by delta values)
# distance_to(other_point) (calculate Euclidean distance)
# display() (print coordinates)
# set_coordinates(x, y)
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

    def display(self):
        print(f"Point at: {self.x}, {self.y}")

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

first_point = Point(5, 6)
second_point = Point(3, 3)
first_point.move(2, -2)
print(first_point.distance_to(second_point))
first_point.display()
first_point.set_coordinates(2, 2)
first_point.display()
second_point.display()


# Task: Create a CoffeeShop Class
# Objective:
#
# Create a Coffee class with attributes:
#
# name (e.g., "Espresso")
# price (per cup)
# sold (number of cups sold, starting at 0)
# Create a CoffeeShop class with:
#
# A list of Coffee objects
# Methods for CoffeeShop:
#
# sell_coffee(coffee_name, cups):
# Finds the coffee by name.
# Checks if enough cups are available (imagine a stock limit).
# Sells the cups, increasing sold for that coffee.
# Calculates total earnings from those cups.
# add_stock(coffee_name, cups):
# Adds cups to the coffee's stock.
# print_sales():
# Prints total cups sold and total earnings for each coffee.


class Coffee:
    def __init__(self, name, price, stock, sold = 0):
        self.name = name
        self.price = price
        self.stock = stock
        self.sold = sold

class CoffeeShop:
    def __init__(self):
        self.coffee = []

    def adding(self, coffee):
        self.coffee.append(coffee)

    def sell_coffee(self, coffee_name, cups):
        coffee = None
        for c in self.coffee:
            if c.name == coffee_name:
                coffee = c
                break
        if coffee is None:
            print(f"Coffee {coffee_name} not found")
            return 0
        if cups > coffee.stock:
            print(f"Not enough stock for {coffee.name}. Available: {coffee.stock}")
            return 0
        coffee.stock -= cups
        coffee.sold += cups

        earnings = cups * coffee.price
        return earnings

# add_stock(coffee_name, cups):
# Adds cups to the coffee's stock.

    def add_stock(self, coffee_name, cups):
        for c in self.coffee:
            if c.name == coffee_name:
                c.stock += cups
                print(f"Added {cups} to {c.name}. Total stock: {c.stock}")
                return
        print(f"Coffee ' {coffee_name} not found")

# print_sales():
# Prints total cups sold and total earnings for each coffee.

    def print_sales(self):
        for c in self.coffee:
            total_earnings = c.sold * c.price
            print(f"{c.name}:")
            print(f"sold {c.sold} cups")
            print(f"remaining stock: {c.stock}")
            print(f"total earnings: ${total_earnings:.2f}")

coffee1 = Coffee("Lavazza", 5, 100, 20)
coffee2 = Coffee("Tschibo", 4, 200, 33)
shop = CoffeeShop()
shop.adding(coffee1)
shop.adding(coffee2)
shop.add_stock("Lavazza", 20)
shop.sell_coffee("Tschibo", 12)
shop.print_sales()

# Create a GroceryItem class with attributes:
#
# name (str)
# price (float)
# quantity_in_stock (int)
# quantity_sold (int, default 0)
# Create a Store class with:
#
# An attribute: items (list of GroceryItem)
# Methods:
# add_item(item: GroceryItem): Add a new item to the store.
# sell_item(item_name, quantity): Sell a certain quantity of the item, update stock and sold quantity.
# restock_item(item_name, quantity): Add stock to an item.
# print_sales(): Display total quantity sold and total earnings for each item.

class GroceryItem:
    def __init__(self, name, price, quantity_in_stock, quantity_sold = 0):
        self.name = name
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        self.quantity_sold = quantity_sold

class Store:
    def __init__(self):
        self.items = []

    def add_item(self, item: GroceryItem):
        self.items.append(item)

    def sell_item(self, item_name, quantity):
        item = None
        for i in self.items:
            if i.name == item_name:
                item = i
                break
        if item is None:
            print(f"{item_name} not found in store")
            return

        if item.quantity_in_stock < quantity:
            print("Not enough in stock.")
        else:
            item.quantity_in_stock -= quantity
            item.quantity_sold += quantity
            print(f"Sold {quantity} {item_name}")

# restock_item(item_name, quantity): Add stock to an item.
# print_sales(): Display total quantity sold and total earnings for each item.

    def restock_items(self, item_name, quantity):
        if quantity <= 0:
            print(f"Cannot restock non-positive amount of {item_name}")
        for i in self.items:
            if i.name == item_name:
                i.quantity_in_stock += quantity
                print(f"Restocked {quantity} {item_name}(s).")
                return
        print(f"{item_name} not found in store")

    def print_sales(self):
        for i in self.items:
            total_earnings = i.quantity_sold * i.price
            print(f"item {i.name}")
            print(f"quantity sold: {i.quantity_sold} for price of {i.price}")
            print(f"total earnings: {total_earnings}")
one1 = GroceryItem("banana", 2, 1000, 200)
one2 = GroceryItem("potato", 3.00, 250, 100)
store = Store()
store.add_item(one1)
store.add_item(one2)
store.print_sales()
store.restock_items("banana", 200)
store.restock_items("potato", 300)
store.sell_item("banana", 400)
store.sell_item("potato", 250)
store.print_sales()


# Create a Book class with attributes: title (str)  author (str) total_copies (int) copies_borrowed (int, default 0)
# Create a Library class with attributes:
# name (str)
# books (list of Book objects)
# Implement methods for Library:
# add_book(book: Book): add a new book to the library.
# borrow_book(title: str, copies=1): borrow a number of copies of a book (if available).
# return_book(title: str, copies=1): return copies of a book.
# print_inventory(): display all books with their available copies and total copies.
# calculate_overdue_fees(days_overdue): estimate overall late fee based on overdue days, e.g., $0.50 per day per copy borrowed.
# Use case:
#
# Add multiple books.
# Borrow some copies.
# Return some copies.
# Calculate total late fees for overdue books.

class Book:
    def __init__(self, title, author, total_copies, copies_borrowed = 0):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.copies_borrowed = copies_borrowed

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def borrow_book(self, title, copies = 1):
        for book in self.books:
            if book.title == title:
                available_copies = book.total_copies - book.copies_borrowed

            if copies <= 0:
                print("Number of copies must be positive")
                return
            elif copies > available_copies:
                print("Not enough copies to borrow")
                return

            book.copies_borrowed += copies
            print(f"Borrowed {copies} copies of {title}.")
            return
        print(f"Book {title} not found in the library.")
# return_book(title: str, copies=1): return copies of a book.
# print_inventory(): display all books with their available copies and total copies.
# calculate_overdue_fees(days_overdue): estimate overall late fee based on overdue days, e.g., $0.50 per day per copy borrowed.

    def return_book(self, title, copies = 1):
        for b in self.books:
            if b.title == title:
                if copies <= 0:
                    print("Number of copies to return must be positive.")
                    return
                if copies > b.copies_borrowed:
                    print(f"Cannot return more books than borrowed. Borrowed: {b.copies_borrowed}")
                    return
                b.copies_borrowed -= copies
                print(f"Returned {copies} books of {b.title}")
                return
        print(f"{title} not found in the library.")

    def print_inventory(self):
        for b in self.books:
            print(f"Title of the book: {b.title}, total copies: {b.total_copies}, available copies: {b.total_copies - b.copies_borrowed}")

    def calculate_overdue_fees(self, days_overdue):
        total_fee = 0
        fee_per_day = 0.50
        for book in self.books:
            total_fee += book.copies_borrowed * days_overdue * fee_per_day
        return round(total_fee, 2)


book1 = Book("Harry Potter", "J. K. Rowling", 2000, 30)
book2 = Book("Romeo and Juliet", "Shakespeare", 2000, 200)
libr = Library("The Big Library")
libr.add_book(book1)
libr.add_book(book2)
print(libr.calculate_overdue_fees(10))
libr.print_inventory()
libr.borrow_book("Harry Potter", 1970)
libr.return_book("Romeo and Juliet", 100)
libr.return_book("Harry Potter", 500)
libr.print_inventory()

# 1. SmartLight Class
# Attributes:
#
# color (str): e.g., "white", "red", "blue"
# status (bool): on or off (default off)
# Methods:
#
# turn_on(): sets status to True
# turn_off(): sets status to False
# change_color(new_color): updates the color
# display(): prints current color and status
# 2. SmartLightController Class
# Attributes:
#
# lights (list of SmartLight objects)
# Methods:
#
# add_light(light: SmartLight): to add a light to the system
# turn_all_on(): turn all lights on
# turn_all_off(): turn all lights off
# change_all_colors(new_color): change color of all lights
# show_status(): display status of all lights in the system


class SmartLight:
    def __init__(self, color: str, status=False):
        self.color = color
        self.status = status

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

    def change_color(self, new_color):
        self.color = new_color
        print(f"Changed color to: {self.color}")

    def display(self):
        status_str = "on" if self.status else "off"
        print(f"The current color is {self.color} and status is {status_str}")


# 2. SmartLightController Class
# Attributes:
#
# lights (list of SmartLight objects)
# Methods:
#
# add_light(light: SmartLight): to add a light to the system
# turn_all_on(): turn all lights on
# turn_all_off(): turn all lights off
# change_all_colors(new_color): change color of all lights
# show_status(): display status of all lights in the system


class SmartLightController:
    def __init__(self):
        self.lights = []

    def add_light(self, light: SmartLight):
        self.lights.append(light)

    def turn_all_on(self):
        for l in self.lights:
            l.turn_on()
        print("All lights have been turned on.")

    def turn_all_off(self):
        for l in self.lights:
            l.turn_off()
        print("All lights have been turned off.")

    def change_all_colors(self, new_color):
        for l in self.lights:
            l.change_color(new_color)
        print(f"All lights have been changed to {new_color}")

    def show_status(self):
        for l in self.lights:
            print(f"Color: {l.color}, Status: {'on' if l.status else 'off'}")
light1 = SmartLight("red", True)
light2 = SmartLight("yellow", False)
light3 = SmartLight("blue", True)
controller = SmartLightController()
controller.add_light(light1)
controller.add_light(light2)
controller.add_light(light3)
controller.turn_all_on()
controller.show_status()
controller.change_all_colors("brown")
controller.show_status()
light1.change_color("red")
controller.show_status()
light2.turn_off()
controller.show_status()
light3.display()
light1.display()
#
# Task: Create an OnlineGame System
# 1. Player Class
# Attributes:
# username (str)
# level (int)
# experience (int)
# 2. GameServer Class
# Attributes:
# server_name (str)
# max_players (int)
# players (list of Player objects)
# average_score (float)
# player_count (int)

class Player:
    def __init__(self, username, level, experience):
        self.username = username
        self.level = level
        self.experience = experience

class GameServer:
    def __init__(self, server_name, max_players, average_score, player_count):
        self.server_name = server_name
        self.max_players = max_players
        self.average_score = average_score
        self.player_count = player_count
        self.players = []

    def add_player(self, player: Player):
        self.players.append(player)

    def remove_player(self, username):
        for p in self.players:
            if p.username == username:
                self.players.remove(p)
                print(f"Player {username} removed.")
                return
        print("Couldn't find the player")



    def play_game(self, player: Player, experience_gained):
        player.experience += experience_gained

        while player.experience >= 100:
            player.level += 1
            player.experience -= 100
            print(f"{player.username} leveled up! Now level {player.level}.")

    def calculate_average_score(self):
        if not self.players:
            return 0
        total_experience = sum(p.experience for p in self.players)
        return total_experience / len(self.players)

    def player_stats(self):
        for p in self.players:
            print(f"Username: {p.username}, Level: {p.level}, Experience: {p.experience}")
player1 = Player("Jonas", 3, 80)
player2 = Player("Nathan", 4, 50)
player3 = Player("Dzuba", 2, 30)
server = GameServer("Marino", 10, 3, 3)
server.add_player(player1)
server.add_player(player2)
server.add_player(player3)
server.play_game(player2, 60)
server.player_stats()
print(server.calculate_average_score())
server.remove_player("Jonas")
server.player_stats()