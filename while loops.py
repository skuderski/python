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

"""5. Guess a number game
Task: Pick a secret number (like 7). Keep asking the user to guess the number. If they guess wrong, say "Try again". 
When they guess right, print "You got it!"""

while True:
    number = 7
    user_input = input("Enter a number: ")
    if int(user_input) == 7:
        print("You got it!")
        break
    else:
        print("Try again")