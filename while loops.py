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

"""10. Simplified countdown
Ask the user to enter a number (say, 10). 
Use a while loop to count down from that number to 1, printing each number, then print "Blast off!"."""

number = int(input("Enter a number: "))
while number > 0:
    print(number)
    number -= 1
print("Blast off!")