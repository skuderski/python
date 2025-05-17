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

# Counter with Reset: Create a closure that maintains a counter. Include functions to increment, decrement,
# and reset the counter back to its initial value.

def counter_with_reset():
    counter = 0
    initial_value = 0
    def increment():
        nonlocal counter
        counter += 2
        return counter
    def decrement():
        nonlocal counter
        counter -= 2
        return counter
    def reset():
        nonlocal counter
        counter = initial_value
        return counter
    return increment, decrement, reset

increment, decrement, reset = counter_with_reset()

print(f"Initial increment:{increment()}")
print(f"Second increment:{increment()}")
print(f"First decrement:{decrement()}")
print(f"Third increment:{increment()}")
print(f"Reset:{reset()}")

# Greeting Generator: Write a function that takes a greeting (e.g., "Hello", "Good morning") as input and returns a closure.
# The closure should take a name as input and return the full greeting string (e.g., "Hello, Alice").

def greeting(greet):
    def greeting_name(name):
        return f"{greet}, {name}!"
    return greeting_name

hello_greeter = greeting("Hello")

print(hello_greeter("Alice"))


# Average Calculator: Create a closure that calculates the average of a series of numbers. Each time you call the closure with a new number,
# updates the average.

def average_calculator():
    sum = 0
    count = 0
    def calculating_average(number):
        nonlocal sum
        nonlocal count
        count += 1
        sum += number
        average = sum / count
        return average
    return calculating_average

avg_calc = average_calculator()
print(avg_calc(10))
print(avg_calc(20))
print(avg_calc(5))


# Multiplier Generator: Create a function that takes a number (the multiplier) as input and returns a closure.
# The closure should take another number as input and return the product of the two numbers.

def multiplier(number):
    def closure(other_number):
        return number * other_number
    return closure

multi = multiplier(2)
print(multi(3))




# Limited-Use Function: Write a function that takes another function and a number n as input, and returns a closure.
# The closure can only call the original function a maximum of n times.
# After that, it should return a message indicating that the function's usage limit has been reached.

def some_function(func, n):
    counter = 0
    def closure(*args, **kwargs):
        nonlocal counter
        if counter < n:
            counter += 1
            result = func(*args, **kwargs)
            return result
        else:
            return "limit reached"

    return closure

def greet(name):
    return f"Hello, {name}"

limited_greet = some_function(greet, 3)

print(limited_greet("Alice"))
print(limited_greet("Sergiusz"))
print(limited_greet("Michael"))
print(limited_greet("Wiesiek"))




# Simple Counter: Create a closure that increments a counter each time it's called and returns the current count.

def function():
    counter = 0
    def closure():
        nonlocal counter
        counter += 1
        return counter
    return closure

the_counting = function()
print(the_counting())
print(the_counting())
print(the_counting())
print(the_counting())

# Customizable Counter
# Create a function called make_counter(start=0, increment=1). This function should take two optional arguments:


# start: The initial value of the counter (default is 0).
# increment: The amount by which the counter should increase each time it's called (default is 1).
# The function should return a closure that:
#
# Increments the counter by the specified increment each time it's called.
# Returns the current value of the counter.

def make_counter(start = 0, increment = 1):
    counter = start
    def inner():
        nonlocal counter
        counter += increment
        return counter
    return inner

incrementing = make_counter(10, 2)
print(incrementing())
print(incrementing())
print(incrementing())
print(incrementing())


# Add to Number: Write a function that takes a number x as input and returns a closure.
# The closure should take another number y as input and return the sum of x and y.

def add(x):
    def closure(y):
        return x + y
    return closure

adding = add(2)
print(adding(4))

# Write a function called make_adder(initial_value=0). This function takes an optional argument initial_value (defaulting to 0).
# The make_adder function should return a closure that:
#
# Takes a number as input.
# Adds that number to an accumulated sum.
# Returns the updated accumulated sum.

def make_adder(initial_value = 0):
    sum = initial_value
    def closure(x):
        nonlocal sum
        sum += x
        return sum
    return closure

addy = make_adder(5)
print(addy(3))

# Resettable Accumulating Adder
#
# Write a function called make_adder(initial_value=0). This function takes an optional argument initial_value (defaulting to 0).
# The make_adder function should return a closure that is a dictionary containing the following functions:
# add(number): Takes a number as input, adds it to an accumulated sum, and returns the updated accumulated sum.
# reset(): Resets the accumulated sum back to the initial_value and returns the initial_value.

def make_adder(initial_value = 0):
    accumulated_sum = initial_value
    def add(number):
        nonlocal accumulated_sum
        accumulated_sum += number
        return accumulated_sum
    def reset():
        nonlocal accumulated_sum
        accumulated_sum = initial_value
        return initial_value
    return {'add': add, 'reset': reset}

adder = make_adder(3)
print(adder['add'](5))
print(adder['reset']())


# String Concatenator: Create a function that takes an initial string as input and returns a closure.
# The closure should take another string as input and return the concatenation of the initial string and the new string.

def concatenator(string):
    def closure(other_string):
        return string + other_string
    return closure

adding = concatenator("Sergiusz")(" jest kochany")
print(adding)

# Task: Accumulating String Concatenator
#
# Write a function called make_concatenator(initial_string="").
# This function takes an optional argument initial_string (defaulting to an empty string).
# The make_concatenator function should return a closure that:
#
# Takes a string as input.
# Concatenates the input string to an accumulated string.
# Returns the updated accumulated string.

def make_concatenator(initial_string =""):
    accumulated_string = initial_string
    def closure(string):
        nonlocal accumulated_string
        accumulated_string += string
        return accumulated_string
    return closure

addz = make_concatenator("Serwiusz")
print(addz(" niebieski"))



# Power Function: Write a function that takes a number n as input and returns a closure.
# The closure should take a number x as input and return x raised to the power of n (xn).

def power(n):
    def closure(x):
        return x ** n
    return closure

power_function = power(5)
print(power_function(5))