# 1. Check if any number in a list is greater than 100
# Given a list of numbers, determine if at least one number is greater than 100.

# some_list = [101, 25, 33, 100]
# print(any(number > 100 for number in some_list))

# 2. Verify all students passed
# Given a list of boolean values indicating if students passed (True) or failed (False), check if all students passed.

# passed = ["passed", "passed", "passed", "passed", "passed"]
# print(all(n =="passed" for n in passed))

# 3. Check if any string in a list contains a certain letter
# For example, check if any string contains the letter 'a'.

# names = ["Sergiusz", "Michal", "Witold"]
# print(any ("b" in name for name in names))

# 4. Verify if all strings in a list are lowercase
# Make a list of strings, check if all are lowercase.

# cities = ["New York", "Paris", "Tokyo", "Sydney", "Berlin"]
# are_all_lower = all(city == city.lower() for city in cities)
# print(are_all_lower)


# 5. Check if any date in a list is a weekend
# Assuming you have a list of booleans indicating if a date is a weekend (True) or not (False).

# days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#
# weekend = [day in ["Saturday", "Sunday"] for day in days_of_week]
# check = any(weekend)
# print(check)

#
# 6. Verify if all numbers are even
# Given a list of integers, check if every one is divisible by 2.

# integers = [2, 2, 4, 6, 8, 10, 22, 4]
# divisible = all( n % 2 == 0 for n in integers)
# print(divisible)

# 7. Check if any user is an admin
# Given a list of user objects/dictionaries with an 'is_admin' key, verify if any user is an admin.

# users = [
#     {"name": "Alice", "is_admin": True},
#     {"name": "Bob", "is_admin": False},
#     {"name": "Charlie", "is_admin": False},
#     {"name": "Diana", "is_admin": True},
#     {"name": "Ethan", "is_admin": False}
# ]
#
# check_if_admin = any(user["is_admin"] for user in users)
# print(check_if_admin)
# 8. Verify all passwords are strong
# Given a list of password strings, check if all meet certain criteria (length, uppercase, numbers, etc.).

passwords = ["P@ssw0rd123", "qwerty!", "letmein", "abc123", "Secure*Pass1"]
check_pass = all(len(password) > 5 and password == password.upper() for password in passwords)
print(check_pass)


# 9. Check if at least one input is valid
# Given a list of user inputs, check if at least one input is an integer or matches a specific pattern.

user_inputs = ["Hello", "123", "How are you?", "Python", "Goodbye"]

check_inputs = any(input_str.isdigit() for input_str in user_inputs)
print(check_inputs)

# 10. Verify if all responses are affirmative
# Given a list of responses like ["yes", "Y", "YES", "No"], check if all responses are affirmative ("yes", "Y", etc.).

list_of_responses = ["yes", "Y", "YES"]

responses = all("y" in response.lower() for response in list_of_responses)
print(responses)