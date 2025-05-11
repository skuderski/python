# count_people = 5
# price = 13.25
# is_empty = True
# message = "Hello, world!"
#
# marks = (2, 3, 4, 5)
# students = ["John", "Bob", "Alice", "Anna"]
# fruits = {"banana", "apple", "strawberry", "cherry"}
# user = {"name": "John", "age": 25}
# message = "Hello, world."
# message2 = message + "How are you?"
#
# print(type(user))
# students[0] = "Ivan"
# print(students)
# students.append("Sergiusz")
# students += ["Jacob"]
# print(id(students))
# print(students)
# print(message2)
#
# print(id(students))
# students.extend(["Wiesiek"])
# print(id(students))
#
# students_list = students
# print(students_list)
# print(id(students))
# print(id(students_list))
# students_list += ["Irena"]
# print(students)
#
# my_list = ["apple", "banana"]
# my_text = "I love apple"
#
#
# def add_word(lst: list, text: str, word: str):
#     lst.append(word)
#     text += word
#     return text
#
#
# print(add_word(my_list, my_text, "orange"))

# message = "Hello, world!"
# students = ["Anna", "John"]
#
# print("message id: ", id(message))
# print("students id: ", id(students))
#
# message += "How are you?"
# students += ["Sergiusz"]
#
# print("message id: ", id(message))
# print("students id: ", id(students))
#
# a = 10
# b = a
# print(id(a), id(b))
#
# a += 1
# print(id(a), id(b))
#
# arr1 = [5]
# arr2 = arr1
#
# print(id(arr1), id(arr2))
#
# arr1 += [1]
#
# print(id(arr1), id(arr2))
#
a = [1, 2, 3]
b = [1, 2, 3]

print(id(a), id(b))

print(a == b)

print (a is b)

a = 0
b = False

print(a == b)

print(id(a), id(b))

none1 = None
none2 = None

print(id(none1), id(none2))

zero = 22222222
zzero = 22222222
print(zero is zzero)
print(id(zero), id(zzero))

print(none1 == none2)

c = True
d = False

print(c is d)