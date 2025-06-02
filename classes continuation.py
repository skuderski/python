class Dog:

    # class attribute
    animal = "dog"

    def __init__(self, breed: str, color: str):
        #instance attribute
        self.breed = breed
        self.color = color

hatiko = Dog("akita", "brown")
buzo = Dog("bulldog", "black")

print(hatiko.breed)
print(hatiko.color)
print(hatiko.animal)
print(Dog.animal)
print(hatiko.__class__)
print(hatiko.__dict__)
print(buzo.__dict__)
print(Dog.__dict__)

Dog.animal = "cat"

print(hatiko.animal)
print(buzo.animal)

Dog.animal = "dog"

hatiko.animal = "cat"

print(hatiko.animal)

print(buzo.animal)

print(hatiko.__dict__)

class Citizen:
    city = "Springfield"

    def __init__(self, full_name: str):
        self.full_name = full_name
    @classmethod
    def change_city_name(cls, new_name: str):
        cls.city = new_name
mayor = Citizen("Joe Quimby")
homer = Citizen("Homer Simpson")

print(mayor.full_name)
print(mayor.city)
print(homer.city)
mayor.change_city_name("Tokyo")
print(mayor.city)
print(homer.city)

print(mayor.__dict__)
print(homer.__dict__)

print(Citizen.__dict__)

class Car:
    def __init__(self, max_speed_km: int):
        self.max_speed_km = max_speed_km
    def print_max_speed_km(self):
        print(f"Car's maximum speed is {self.max_speed_km} km/h")

    def print_max_speed_miles(self):
        print(f"Car's maximum speed is {self.km_to_miles(self.max_speed_km)} miles/h")
    @staticmethod
    def km_to_miles(km: int):
        return round(km * 0.62137, 2)

tesla_roadster = Car(max_speed_km=400)

tesla_roadster.print_max_speed_km()

tesla_roadster.print_max_speed_miles()


class Grow:
    def __init__(self, stem_diff = 0.0, leaf_diff = 0.0):
        self.stem_diff = stem_diff
        self.leaf_diff = leaf_diff
    def __add__(self, other):
        if not isinstance(other, Grow):
            raise TypeError ("error")
        return Grow(
            stem_diff=self.stem_diff + other.stem_diff,
            leaf_diff=self.leaf_diff + other.leaf_diff
        )


day1 = Grow(stem_diff=2, leaf_diff=0.5)
day2 = Grow(stem_diff=2.5, leaf_diff=3)
day3 = Grow(stem_diff=1.2, leaf_diff=0.2)


print(str(day1 + day2 + day3))


print(dir(Grow))

# Create a Temperature class with a class method from_fahrenheit(cls, temp_f) that converts Fahrenheit to Celsius and creates a Temperature object.

class Temperature:
    def __init__(self, celcius):
        self.celcius = celcius

    @classmethod
    def from_fahrenheit(cls, temp_f):
        celcius = (temp_f - 32) * (5/9)
        return cls(celcius)
    @staticmethod
    def is_even(number):
        return number % 2 == 0

temp = Temperature.from_fahrenheit(50)
print(f"{temp.celcius}")
print(Temperature.is_even(2))

# Add a static method is_even(number) that returns True if a number is even, False otherwise.



# Create a Person class with a class method from_birth_year(cls, name, birth_year)
# that calculates age from the current year and creates a Person object.

class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
    @classmethod
    def from_birth_year(cls, name, birth_year, current_year = 2025):
        age = current_year - birth_year
        person = cls(name, birth_year)
        person.age = age
        return person
    @staticmethod
    def calculate_area_of_circle(radius):
        area = 3.14 * (radius ** 2)
        return area

p = Person.from_birth_year("Sergiusz", 1994)
print(p.name)
print(p.birth_year)
print(p.age)
print(Person.calculate_area_of_circle(5))


# Add a static method calculate_area_of_circle(radius) that returns the area of a circle (use 3.14 for π).
#
# Create a BankAccount class with a class method with_initial_deposit(cls, name, deposit) that creates an account with a starting balance.
import math
class BankAccount:
    def __init__(self, name, deposit):
        self.name = name
        self.deposit = deposit
    @classmethod
    def with_initial_deposit(cls, name, deposit):
        return cls(name, deposit)
    @staticmethod
    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True
account1 = BankAccount.with_initial_deposit("Sergiusz", 5000)
print(account1.name)
print(account1.deposit)
print(BankAccount.is_prime(2))


# Add a static method is_prime(number) that checks whether a number is prime.
#
# Create a Car class with a class method convert_mpg_to_lpkm(mpg) that converts miles per gallon to liters per 100 km.

class Car:
    def __init__(self, mpg):
        self.mpg = mpg

    @classmethod
    def convert_mpg_to_lpkm(cls, mpg):
        km_per_mile = 1.60934
        liters_per_gallon = 3.78541

        l_per_100_km = (liters_per_gallon / mpg) * (100 / km_per_mile)
        return l_per_100_km

print(Car.convert_mpg_to_lpkm(20))


# Create a MathHelper class with static methods like add(x, y) and multiply(x, y).
#
# Create a Book class with a class method from_string(book_str) where book_str is formatted like "Title,Author"; the method creates a Book object.
#
# Add a static method calculate_discount(price, percentage) that returns the discounted price.