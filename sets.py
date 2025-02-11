# task 1

"""Unique Elements: Write a function that takes a list and
returns a list of the unique elements by converting the list to a set and back to a list."""

def conversion(some_list:list) -> list:
    seen = set()
    result = []
    for item in some_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(conversion(["Wodka", 1, 24.4, 1, 5, "Wodka", 33]))

# task 2
"""Set Intersection: Create two sets and write a function to find their intersection using the intersection() method 
or the & operator."""

def intersekcjone(first: set, second: set):
    return first.intersection(second)

print(intersekcjone({1,2,3}, {3,4,5}))


# task 3
"""Set Union: Construct two sets and write a function to find their union using the union() method or the | operator."""

def unijone(first: set, second: set) -> set:
    return first.union(second)

print(unijone({1,2,3}, {3,4,5}))

"""Set Difference: Create two sets and write a function to find elements that are in the first set but not in the second using the difference() method or the - operator."""

def differencijone(first: set, second: set) -> set:
    return first.difference(second)

print (differencijone({1,2,3}, {3,4,5}))

"""Symmetric Difference: Write a function that takes two sets and 
returns their symmetric difference using the symmetric_difference() method or the ^ operator."""

def sym_differencijone(first: set, second: set) -> set:
    return first.symmetric_difference(second)

print(sym_differencijone({1,2,3}, {3,4,5}))

"""Subset Check: Implement a function that checks if one set is a subset of another using the issubset() method."""

def subasetto(first: set, second: set) -> bool:
    return first.issubset(second)

print(subasetto({1,2,3}, {1,2,3,4,5}))

"""Superset Check: Write a function to determine if one set is a superset of another using the issuperset() method."""

def supaset(first: set, second: set) -> bool:
    return first.issuperset(second)

print(supaset({1, 2, 3 , 4, 5}, {1, 2, 3, 4, 5}))

"""Duplicate Removal: Write a function that removes duplicate entries from a list of integers by converting it to a set
 and then back to a list."""

def duplicates(some_list: list) -> list:
    seen = set()
    result = []
    for i in some_list:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result

print(duplicates([1, 1, 2, 2, 3, 3, 5, 6, 6, 6]))

"""Disjoint Sets: Create a function to check if two sets are disjoint (have no common elements) using the isdisjoint() method."""

def disjointed(first: set, second: set) -> bool:
    return first.isdisjoint(second)

print(disjointed({1,2,3},{4,5,6}))

"""Count Unique Words: Write a function that counts the number of unique words in a sentence 
by splitting the sentence into words and using a set to store them."""

def count_unique(sentence: str):
    splitted = sentence.split()
    unique_words = set(splitted)
    return len(unique_words)
print(count_unique("Sergiusz to kochany czlowiek"))