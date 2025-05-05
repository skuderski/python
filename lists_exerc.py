
# # Create a list of your favorite fruits and print the list.
# def fruits(l: list):
#     return l
# print(fruits(["banana", "apple", "kiwi", "orange"]))
#
# # Add a new item to the end of a list using append().
# def create_fruits(fruits: list):
#     fruits.append("strawberry")
#     return fruits
# print(create_fruits(["banana", "apple", "kiwi", "orange"]))
#
#
# # Remove an item from a list by value using remove().
#
# def remove_fruits(fruits: list):
#     fruits.remove("banana")
#     return fruits
#
# print(remove_fruits(["banana", "apple", "kiwi", "orange"]))
#
#
# # Insert an item at a specific position using insert().
#
# def insert_fruits(fruits: list):
#     fruits.insert(2, "strawberry")
#     return fruits
#
# print(insert_fruits(["banana", "apple", "kiwi", "orange"]))
#
# # Find the length of a list using len().
#
#
# def len_of_list(fruits: list):
#     return len(fruits)
#
# print(len_of_list(["banana", "apple", "kiwi", "orange"]))
#
# # Sort a list of integers in ascending order.
#
# def ascending_order(integers: list):
#     integers.sort()
#     return integers
#
# print(ascending_order([3, 8, 15, 22, 7, 14, 9, 30]))
# # Reverse a list without using the reverse() method, using slicing.
#
# def reverse_list(fruits: list):
#     return fruits[::-1]
#
# print(reverse_list(["banana", "apple", "kiwi", "orange"]))
# # Combine two lists into one using the + operator.
#
# def combining_lists(first: list, second: list):
#     return first + second
#
# print(combining_lists(["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown"], ["car", "bike", "train", "plane", "boat", "bus", "subway", "helicopter"]))
#
# # Create a new list containing only even numbers from an existing list.
# def even_numbers(numbers: list):
#     even_numbers_list = []
#     for n in numbers:
#         if n % 2 == 0:
#             even_numbers_list.append(n)
#     return even_numbers_list
#
# print(even_numbers([42, 87, 16, 55, 23, 9, 78, 61, 33, 4]))
#
# # Check if a specific value exists in a list using the in operator.
#
# def checking_value(numbers: list):
#     return 9 in numbers
#
# print(checking_value([12, 7, 25, 3, 18, 9, 30, 15, 22]))
#
# # Find the second largest unique number in a list:
# # Given a list of numbers that may contain duplicates, find the second highest number (excluding duplicates).
#
# def find_second_largest(numbers: list):
#     no_duplicates_list = set(numbers)
#     the_list = list(no_duplicates_list)
#
#     if len(the_list) < 2:
#         return None
#
#     the_largest_n = max(the_list)
#     the_list.remove(the_largest_n)
#     second_largest = max(the_list)
#     return second_largest
#
# print(find_second_largest([5, 2, 9, 1, 5, 9, 6]))
#
#
#
# # Remove duplicates from a list while preserving order:
# # Given a list with repeated elements, create a new list with only unique elements,
# # maintaining the original order of first appearances.
#
# def remove_duplicates(items: list):
#     unique_items = []
#     for item in items:
#         if item not in unique_items:
#             unique_items.append(item)
#     return unique_items
#
# print(remove_duplicates(["apple", "banana", "cherry", "apple", "date", "banana", "fig", "apple"]))
#
#
# # Partition a list based on a condition:
# # Given a list of numbers, split it into two lists: one containing all numbers greater than 10,
# # and the other containing the rest.
#
# def partition_list(numbers: list):
#     bigger_than_10 = []
#     the_rest = []
#     for n in numbers:
#         if n > 10:
#             bigger_than_10.append(n)
#         else:
#             the_rest.append(n)
#     return bigger_than_10, the_rest
#
# print(partition_list([10, 5, 8, 20, 5, 15, 10, 3]))
#
# # Rotate a list by n positions:
# # Given a list and a number n, rotate the list so that elements are shifted n positions to the right (or left if negative).
#
# def rotation(numbers: list, n: int):
#     n = n % len(numbers)
#     sliced = numbers[:-n]
#     second_sliced = numbers[-n:]
#     rotate = second_sliced + sliced
#     return rotate
# print(rotation([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],(2)))

# Find all pairs of numbers that sum up to a target value:
# Given a list of numbers and a target sum, find all unique pairs of elements that add up to that sum.

def find_pairs(numbers: list, total: int):
    unique = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == total:
                the_sum = tuple(sorted((numbers[i], numbers[j])))
                unique.add(the_sum)
    return list(unique)

print(find_pairs([3, 7, 1, 0, 3, 4, 9, 1, 5, 7, 2, 1, 3, 2, 0], 5))