"""
LESSON 3: Functions in Python
==============================
Level: Beginner

Learning Objectives:
- Understand what functions are and why we use them
- Create functions with def keyword
- Use parameters and return values
- Understand variable scope
"""

# ============================================
# PART 1: What is a Function?
# ============================================
print("=== Part 1: What is a Function? ===")

# A function is a reusable block of code that performs a specific task.
# Benefits:
# - Avoid repeating code (DRY - Don't Repeat Yourself)
# - Makes code organized and readable
# - Easier to test and debug


# ============================================
# PART 2: Creating a Simple Function
# ============================================
print("\n=== Part 2: Simple Functions ===")


# Define a function using 'def' keyword
def greet():
    print("Hello! Welcome to Python!")


# Call the function by its name with ()
greet()
greet()  # You can call it multiple times


# Function with a docstring (documentation)
def say_goodbye():
    """This function prints a goodbye message."""
    print("Goodbye! See you next time!")


say_goodbye()


# ============================================
# PART 3: Functions with Parameters
# ============================================
print("\n=== Part 3: Functions with Parameters ===")


# Parameters allow you to pass data into functions
def greet_person(name):
    print(f"Hello, {name}!")


greet_person("Alice")
greet_person("Bob")


# Multiple parameters
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")


introduce("Charlie", 25)
introduce("Diana", 30)


# ============================================
# PART 4: Return Values
# ============================================
print("\n=== Part 4: Return Values ===")


# Functions can return a value using 'return'
def add(a, b):
    return a + b


result = add(5, 3)
print(f"5 + 3 = {result}")

# Use return value directly
print(f"10 + 20 = {add(10, 20)}")


# Multiple calculations
def calculate(a, b):
    total = a + b
    difference = a - b
    product = a * b
    return total, difference, product  # Return multiple values


sum_val, diff_val, prod_val = calculate(10, 3)
print(f"Sum: {sum_val}, Difference: {diff_val}, Product: {prod_val}")


# ============================================
# PART 5: Default Parameters
# ============================================
print("\n=== Part 5: Default Parameters ===")


# Default values are used when no argument is provided
def greet_with_message(name, message="Hello"):
    print(f"{message}, {name}!")


greet_with_message("Alice")  # Uses default message
greet_with_message("Bob", "Good morning")  # Custom message


# Power function with default exponent
def power(base, exponent=2):
    return base ** exponent


print(f"3 squared: {power(3)}")      # 3^2 = 9
print(f"2 cubed: {power(2, 3)}")     # 2^3 = 8


# ============================================
# PART 6: Keyword Arguments
# ============================================
print("\n=== Part 6: Keyword Arguments ===")


def create_profile(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")


# Positional arguments (order matters)
create_profile("Alice", 25, "New York")

# Keyword arguments (order doesn't matter)
create_profile(city="London", name="Bob", age=30)


# ============================================
# PART 7: Variable Scope
# ============================================
print("\n=== Part 7: Variable Scope ===")

# Global variable - accessible everywhere
global_var = "I am global"


def scope_example():
    # Local variable - only accessible inside function
    local_var = "I am local"
    print(f"Inside function: {local_var}")
    print(f"Inside function: {global_var}")  # Can access global


scope_example()
print(f"Outside function: {global_var}")
# print(local_var)  # This would cause an error!


# ============================================
# PART 8: Practical Examples
# ============================================
print("\n=== Part 8: Practical Examples ===")


# Example 1: Calculate area of a circle
def circle_area(radius):
    pi = 3.14159
    return pi * radius ** 2


print(f"Area of circle (r=5): {circle_area(5):.2f}")


# Example 2: Check if number is even or odd
def is_even(number):
    return number % 2 == 0


print(f"Is 4 even? {is_even(4)}")
print(f"Is 7 even? {is_even(7)}")


# Example 3: Find maximum of three numbers
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


print(f"Maximum of 5, 12, 8: {find_max(5, 12, 8)}")


# Example 4: Count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


print(f"Vowels in 'Hello World': {count_vowels('Hello World')}")


# ============================================
# EXERCISES - Try these yourself!
# ============================================
"""
Exercise 1: Create a function called 'celsius_to_fahrenheit'
    - Takes temperature in Celsius as parameter
    - Returns temperature in Fahrenheit
    - Formula: F = (C * 9/5) + 32

Exercise 2: Create a function called 'is_palindrome'
    - Takes a string as parameter
    - Returns True if the string is same forwards and backwards
    - Example: "radar" -> True, "hello" -> False

Exercise 3: Create a function called 'factorial'
    - Takes a number n as parameter
    - Returns n! (n factorial)
    - Example: factorial(5) = 5 * 4 * 3 * 2 * 1 = 120

Exercise 4: Create a function called 'fizzbuzz'
    - Takes a number as parameter
    - Returns "Fizz" if divisible by 3
    - Returns "Buzz" if divisible by 5
    - Returns "FizzBuzz" if divisible by both
    - Returns the number itself otherwise
"""

# Write your exercise solutions below:
# --------------------------------------
