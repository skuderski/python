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