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