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