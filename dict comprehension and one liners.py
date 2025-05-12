numbers = [4, 2, 7, 10]

squares = {}

for num in numbers:
    if num % 2 == 0:
        squares[num] = num ** 2

print(squares)

squares2 = {num: num **2 for num in numbers if num % 2 == 0}
print(squares2)

set_of_squares = {num **2 for num in numbers if num % 2 == 0}
print(set_of_squares)

word = "hello"

symbols = {}

for char in word:
    if char not in symbols:
        symbols[char] = 1
    else:
        symbols[char] += 1
print(symbols)

"""ONE LINERS"""

def sum_if_three():
    return sum([i for i in range(100) if "3" in str(i)])

print(sum_if_three())

def make_uppercase(words: str):
    return " ".join([word.upper() for word in words.split(" ") if len(word) > 5])

print(make_uppercase("Sergiusz to fajny gosc"))
"""IMPORTANT EXAMPLE TO GO OVER"""
attendance = [
    ["Monday", "Wednesday", "Friday"],
    ["Tuesday", "Thursday"],
    ["Monday", "Tuesday", "Wednesday"],
    ["Wednesday", "Friday"]
]

def get_count_attendance(attendance: list):
    return {day: sum(attendance, []).count(day) for day in set(sum(attendance, []))}

print(get_count_attendance(attendance))


