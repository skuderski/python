class Pizza:
   def __init__(self, sauce: str, toppings: str, cheese: str):
       self.sauce = sauce
       self.toppings = toppings
       self.cheese = cheese


margherita_pizza = Pizza("tomato sauce", "tomatoes", "mozzarella")
buffalo_pizza = Pizza("buffalo sauce", "mushrooms", "provolone")

class User:
   def __init__(self, name: str, surname: str):
       self.name = name
       self.surname = surname

first_user = User("Joseph", "Green")

print(first_user.name)
print(first_user.surname)