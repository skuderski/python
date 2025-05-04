"""1. Generate a random decimal between 0 and 1
Create a program that prints a random float using random.random()."""
# import random
# def randomized():
#     for _ in range(5):
#         print(random.random())
# randomized()

"""2. Roll a six-sided die
Use random.randint() to simulate rolling a die, which gives a number between 1 and 6."""

# import random
# def six_sided():
#     for _ in range(5):
#         print(random.randint(1, 6))
# six_sided()

"""3. Pick a random color
Make a list of some colors (e.g., 'red', 'blue', 'green') and use random.choice() to randomly select and print one color."""

# import random
# colors = ["red", "blue", "green", "yellow", "pink"]
# print(random.choice(colors))

"""4. Generate a random decimal between 0 and 10
Use random.random() and multiply the output by 10 to get a decimal somewhere between 0 and 10."""
# import random
# def los_decimales():
#     print(random.random() * 10)
# los_decimales()

"""5. Simulate flipping a coin
Use random.choice() between 'Heads' and 'Tails' and print the result."""

# import random
#
# def heads_tails(options):
#     print(random.choice(options))
#
# heads_tails(["heads", "tails"])
#

"""6. Get a random number between 50 and 100
Use random.randint() to generate and print a number in that range."""
# import random
# print (random.randint(50, 100) / 100)

"""7. Generate a list of 5 random floats between 0 and 1
Use a loop with random.random() to create a list of 5 random decimals."""

# import random
# the_list = []
# for _ in range(5):
#     n = random.random()
#     the_list.append(n)
# print(the_list)

"""8. Pick 3 random students from a list
Create a list of student names, then use random.choice() or random.sample() to pick 3 students without repeats."""
# import random
# names = ["Sergiusz", "Waclaw", "Rysiek", "Wacek", "Jacek", "Grzybson"]
# for _ in range(3):
#     print(random.choice(names))

"""9. Simulate a random temperature
Generate a random float between -10 and 40 to simulate a temperature reading using random.uniform()."""

# print(random.uniform(-10, 40))

"""(Note: this uses random.uniform(), which is similar to random.random() but for a custom range.)
"""
"""10. Randomly shuffle a deck of cards
Create a list of the 52 cards and use random.shuffle() to shuffle the deck."""
# import random
#
# cards = [
#     'Ace of Hearts', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts',
#     '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts',
#     'Jack of Hearts', 'Queen of Hearts', 'King of Hearts',
#     'Ace of Diamonds', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds',
#     '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds',
#     'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds',
#     'Ace of Clubs', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs',
#     '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs',
#     'Jack of Clubs', 'Queen of Clubs', 'King of Clubs',
#     'Ace of Spades', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades',
#     '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades',
#     'Jack of Spades', 'Queen of Spades', 'King of Spades']
# random.shuffle(cards)
# print(cards)
