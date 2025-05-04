"""1. Print all numbers from 0 to 9
Use range() to print numbers starting at 0, ending at 9."""

# for i in range(10):
#     print(i)

"""2. Print even numbers from 2 to 20
Use range() with a step of 2 to print 2, 4, 6, ..., 20."""

# for i in range(2, 21, 2 ):
#     print(i)

"""3. Count backward from 10 to 1
Use range() with a negative step to count down from 10 to 1."""

# for i in range(10, 0, -1):
#     print(i)

"""4. Print all odd numbers between 1 and 20
Use range() starting at 1, ending at 20, with a step of 2."""

# for i in range(1, 21, 2):
#     print(i)

"""5. Sum of numbers from 1 to 100
Use range() to generate numbers 1 to 100 and compute their total sum."""

# summ = 0
# for i in range(1, 101):
#     summ += i
# print(summ)

"""6. Print multiples of 3 from 0 to 30
Use range() with a step of 3."""

# for i in range(0, 31, 3):
#     print(i)

"""7. Print the multiplication table for 5 (from 1 to 10)
Use range() to generate multipliers and multiply them by 5."""

# for i in range(1, 11):
#     multip = i * 5
#     print(multip)

"""8. Create a list of squares of numbers from 1 to 10
Use range() to generate numbers, and calculate the square of each."""

# for i in range(1, 11):
#     square = i * i
#     print(square)

"""9. Print a pattern of stars (*) forming a triangle of height 5
Use range() to control how many stars print on each line."""

# for i in range(1, 6):
#     print(i * "*")


"""10. Count the number of even numbers between 1 and 50
Use range() to generate even numbers and count."""

# even = 0
#
# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)
#         even += 1
# print(even)

"""11. Create a list of all multiples of 4 between 20 and 100
Use range() to generate all numbers divisible by 4 within that range, then store them in a list."""
# the_list = []
# for i in range(20, 101):
#     if i % 4 == 0:
#         the_list.append(i)
# print(the_list)


"""12. Print a pattern: numbers from 1 to 25, but with a twist
Print numbers 1 to 25, but for every 5 numbers, start a new line to form a grid."""
counter = 0
# for i in range(1, 26):
#     print(i, end = " ")
#     counter += 1
#     if counter == 5:
#         print()
#         counter = 0


"""13. Sum all odd numbers between 1 and 100
Use range() with a step, and compute the total of all odd numbers in that range.
"""
# the_list = []
# odd = 0
# for i in range(1, 101, 2):
#     odd += 1
#     the_list.append(i)
# print(odd, the_list)


"""14. Print a pyramid of stars of height 10
Using nested loops and range(), print a pyramid shape where each row has increasing stars.
"""

# for i in range(1, 11):
#     print(i * "*")
"""15. Generate a list of square numbers from 1 to 20
Use range() to generate numbers and create a list with their squares."""

the_list = []

for i in range(1, 21):
    square = i * i
    the_list.append(square)
print(the_list)