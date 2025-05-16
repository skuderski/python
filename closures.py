# Simple Counter Closure
# Create a function that returns a nested function which increments and returns a counter each time it is called.
# Call it multiple times to see the count increase.

def first():
    count = 0
    def second():
        nonlocal count
        count += 2
        return count
    return second
counter = first()
print(counter())
print(counter())
print(counter())


# Multiplier Closure
# Write a function that takes one argument n and returns a function that multiplies its input by n. Test it with n=3 and n=5.

def multiplier(n):
    def other_multiplier(x):
        return n * x
    return other_multiplier
times_3 = multiplier(3)
print(times_3(10))

times_5 = multiplier(5)
print(times_5(10))




# Accumulator Closure
# Create a function that, when called,
# returns a nested function that accumulates the sum of all the arguments passed to it each time it's called.

def accumulator_closure():
    sum_total = 0
    def adding():
        nonlocal sum_total
        sum_total += 10
        return sum_total
    return adding

my_accumulator = accumulator_closure()

print(my_accumulator())
print(my_accumulator())
print(my_accumulator())

# String Repeater Closure
# Write a function that takes a string s and returns a function which, when called,
# appends s to an internal string and returns the full string each time.

def stringi(s: str):
    accumulated = ""
    def internal():
        nonlocal accumulated
        accumulated += s
        return accumulated

    return internal

f = stringi("Sergiusz")
print(f())

# Filter Closure
# Create a closure that takes a list of numbers and a threshold,
# and returns a function that filters numbers greater than the threshold using that list.

def first(numbers:list, threshold):
    def greater():
        return [num for num in numbers if num > threshold]
    return greater

my_list = [1, 2, 3, 4, 5, 6]
filter_func = first(my_list, 3)
print(filter_func())





# Delayed Computation Closure
# Write a function that takes a number
# and returns a nested function that computes and returns number + x each time it is called,
# where x is passed when creating the closure.

def one(number):
    def nested(x):
        return number + x
    return nested

something = one(2)
print(something(5))



# Closure with State Reset
# Create a closure that maintains a count, but also has a method to reset the counter to zero.

def outer():
    count = 0
    def inner():
        nonlocal count
        count += 2
        return count
    def reset():
        nonlocal count
        count = 0

    return inner, reset

inner, reset = outer()

print(inner())
print(inner())
print(inner())
reset()
print(inner())



# Nested Closure
# Create a function that returns a nested function which, in turn, returns another nested function.
# Both should modify some internal state.

def outer():
    counter = 10
    def inner_first():
        nonlocal counter
        counter -= 2
        def inner_second():
            nonlocal counter
            counter -= 1
            return counter
        return inner_second
    return inner_first

my_func = outer()
first_inner = my_func()
second_inner = first_inner()

print(second_inner)



# Multiple Closures with Shared State
# Create two closures that share a single counter variable. Show how calling either updates the same counter.

def counter():
    count = 0

    def inner_increase():
        nonlocal count
        count += 2
        return count


    def inner_decrease():
        nonlocal count
        count -= 1
        return count

    return inner_increase, inner_decrease

inner_increase, inner_decrease = counter()

print(f"Initial increment: {inner_increase()}")  # Output: Initial increment: 1
print(f"First decrement: {inner_decrease()}")   # Output: First decrement: 0
print(f"Second increment: {inner_increase()}") # Output: Second increment: 1
print(f"Second decrement: {inner_decrease()}")   # Output: Second decrement: 0

# Closure with Arguments
# Write a closure that takes an initial list.
# The nested function appends elements to this list and returns the current list each time.

def one(initial_list):
    def appender(element):
        initial_list.append(element)
        return initial_list
    return appender

my_appender = one([1, 2, 3])

print(my_appender(5))