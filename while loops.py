# """1. Count from 1 to 10
# Task: Use a while loop to print numbers from 1 to 10."""
# count = 1
# while count <= 10:
#     print(count)
#     count += 1
#
# """2. Count down from 5 to 0
# Task: Use a while loop to print numbers starting at 5 and decreasing to 0."""
#
# count = 5
# while count >= 0:
#     print(count)
#     count -= 1
#
# """3. Repeat asking for input
# Task: Keep asking the user to type "exit" to stop. If the user types anything else, say "Try again" and ask again."""
#
# while True:
#     user_input = input()
#     if user_input == "exit":
#         break

"""4. Sum numbers until the total exceeds 100
Task: Keep asking the user to enter numbers. Keep adding them up until the total is more than 100. Then print the total."""
# total = 0
# while total <= 100:
#     user_input = input("Enter a number: ")
#     number = float(user_input)
#     total += number
#     print(total)
#     if total > 100:
#         print("We've reached 100")
#         break

# """5. Guess a number game
# Task: Pick a secret number (like 7). Keep asking the user to guess the number. If they guess wrong, say "Try again".
# When they guess right, print "You got it!"""

# while True:
#     number = 7
#     user_input = input("Enter a number: ")
#     if int(user_input) == 7:
#         print("You got it!")
#         break
#     else:
#         print("Try again")

# """6. Print numbers from 1 to 100
# Use a while loop to print all numbers starting from 1 up to 100."""
# count = 1
# while count <= 100:
#     print(count)
#     count += 1

# """7. Guess the password
# Pick a secret password (like "banana"). Keep asking the user to guess it until they get it right, then print "Correct!"."""
#
# while True:
#     user_input = input("Guess the password:")
#
#     if user_input == "banana":
#         print("Correct")
#         break
#     else:
#         print("Try again")

# """8. Count the even numbers
# Ask the user to input 10 numbers one by one. Once you've got all 10, print how many of those numbers are even.
# """
# count = 0
# even = []
# while count < 10:
#     user_input = int(input("Enter a number: "))
#     count += 1
#     if user_input % 2 == 0:
#         even.append(user_input)
# print(even)
# amount = len(even)
# print(f"{amount} of numbers are even.")

# """9. Calculate the sum of positive numbers
# Keep asking the user to enter numbers. When they enter a negative number,
# stop and print the sum of all positive numbers entered."""
# total = 0
# while True:
#     user_input = int(input("Enter a number: "))
#     if user_input > 0:
#         total += user_input
#     elif user_input < 0:
#         break
# print(total)

# """10. Simplified countdown
# Ask the user to enter a number (say, 10).
# Use a while loop to count down from that number to 1, printing each number, then print "Blast off!"."""
#
# number = int(input("Enter a number: "))
# while number > 0:
#     print(number)
#     number -= 1
# print("Blast off!")
#
# while True:
#     try:
#         user_input = input("Enter a positive integer: ")
#         number = int(user_input)
#
#         if number <= 0:
#             print("Please enter a *positive* integer.")
#             continue
#
#         while number > 0:
#             print(number)
#             number -= 1
#
#         break
#
#     except ValueError:
#         print("Invalid input. Please enter an integer.")
#         continue

# Number Guessing Game:
#
# Generate a random number between 1 and 100.
# Use a while True loop to allow the user to guess the number.
# Inside the loop:
# Get the user's guess as input.
# Provide feedback: "Too high," "Too low," or "Correct!"
# If the guess is correct, break out of the loop.
# Include input validation to handle non-integer input (print an error and ask again).
# import random
# number = random.randint(1, 100)
# print(number)
# while True:
#     user_input = int(input("Guess the number: "))
#     if user_input > number:
#         print("Too high")
#     elif user_input < number:
#         print("Too low")
#     else:
#         print("Correct")
#     break
#
# # Menu-Driven Program:
# # #
# # # Create a simple menu with options like "1. Print a greeting," "2. Calculate square," "3. Exit."
# # # Use a while True loop to keep the menu running.
# # # Get the user's choice as input.
# # # Implement the corresponding action for each choice.
# # # If the user chooses "3. Exit," break out of the loop.
# # # Handle invalid menu choices (print an error message).
# def print_menu():
#     print("Menu:")
#     print("1. Print a greeting")
#     print("2. Calculate square")
#     print("3. Exit")
#
# while True:
#     print_menu()
#     choice = int(input("Enter your choice: "))
#
#     if choice < 1 or choice > 3:
#             print("Invalid choice. Please enter 1, 2, or 3.")
#             continue  # Go back to the beginning of the loop
#
#     if choice == 1:
#             # Implement the "Print a greeting" action
#         print("Hello, user!")
#     elif choice == 2:
#             # Implement the "Calculate square" action
#         try:
#                 num = float(input("Enter a number to square: "))
#                 square = num ** 2
#                 print("The square of", num, "is", square)
#         except ValueError:
#                 print("Invalid number.")
#     elif choice == 3:
#             print("Exiting program. Goodbye!")
#             break  # Exit the loop
#
# Keep Asking Until the Right Password:
#
# Write a while True loop that repeatedly prompts the user to enter a password.
# Define a correct password (e.g., "secret").
# If the user enters the correct password, print "Access granted!" and break out of the loop.
# If the user enters the wrong password, print "Incorrect password. Try again." and continue to the next iteration of the loop.
password = "secret"
while True:
    user_input = input("Enter your password: ")
    if user_input == "secret":
        print("Access granted")
        break
    else:
        print("Incorrect password. Try again")

# Summing Numbers Until a Negative Input:
#
# Initialize a variable total to 0.
# Write a while True loop that repeatedly prompts the user to enter a number.
# Use a try-except block to handle potential ValueError exceptions if the user enters something that's not a number.
# If the user enters a negative number, print the current total and break out of the loop.
# If the user enters a valid positive number, add it to the total.

number = 0

while True:
    user_input = int(input("Enter a fucking number"))
    if user_input > 0:
        number += user_input
    else:
        print(number)
        break