# Create a Set: Create a set containing the first five even positive integers.

def create_set():
    integers = set()
    number = 2
    while len(integers) < 5:
        integers.add(number)
        number += 2
    return integers

print(create_set())


# Add Elements: Start with an empty set. Add the following elements to the set: "apple", "banana", "cherry".

def add_elements():
    fruits = set()
    fruits.update(["apple", "banana", "cherry"])
    return fruits

print(add_elements())


# Remove Elements: Create a set with the elements: 1, 2, 3, 4, 5. Try to remove the element 3.
# Then, try to remove the element 6 (which is not in the set) and handle the potential error.

numbers = {1, 2, 3, 4, 5}
numbers.remove(3)
numbers.discard(6)
print(numbers)


# Check Membership: Create a set with some elements. Write a function that takes a value and a set as input
#
# and returns True if the value is in the set and False otherwise.

def check_membership(fruits: set, value: str):
    return value in fruits

print(check_membership({"strawberry", "blueberry", "raspberry", "blackberry", "cranberry"}, "strawberry"))

# Set Union: Create two sets: set1 with elements {1, 2, 3} and set2 with elements {3, 4, 5}.
#
# Create a new set that contains all elements from both set1 and set2 (union).

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# set3 = set1.union(set2)
# print(set3)
# Set Intersection: Create two sets: set1 with elements {1, 2, 3, 4} and set2 with elements {3, 4, 5, 6}.
# Create a new set that contains only the elements that are present in both set1 and set2 (intersection).

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = set1.intersection(set2)

print(set3)

# Set Difference: Create two sets: set1 with elements {1, 2, 3, 4, 5} and set2 with elements {3, 4}.
# Create a new set that contains the elements that are in set1 but not in set2 (difference).

set4 = {1, 2, 3, 4, 5}
set5 = {3, 4}
set6 = set4.difference(set5)
print(set6)

# Set Symmetric Difference: Create two sets: set1 with elements {1, 2, 3, 4, 5} and set2 with elements {3, 4, 6, 7}.
# Create a new set that contains the elements that are in either set1 or set2, but not in both (symmetric difference).

secik = {1, 2, 3, 4, 5}
secik2 = {3, 4, 6, 7}

seciczek = secik.symmetric_difference(secik2)
print(seciczek)

# Check Subset: Create two sets: set1 with elements {1, 2} and set2 with elements {1, 2, 3, 4, 5}.
# Write a function that checks if set1 is a subset of set2.

def check_subset(first: set, second: set):
    return first.issubset(second)

print(check_subset({1, 2}, {1, 2, 3, 4, 5}))

# Remove Duplicates from a List: Given a list of numbers with duplicate values,
# use a set to create a new list containing only the unique values from the original list.

def remove_duplicates(numbers: list):
    unique_val = set(numbers)
    return unique_val

print(remove_duplicates({1, 1, 2, 3, 4, 4, 2}))