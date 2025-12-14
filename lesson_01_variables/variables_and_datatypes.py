"""
LESSON 1: Variables and Data Types in Python
=============================================
Level: Beginner

Learning Objectives:
- Understand what variables are
- Learn basic data types (int, float, str, bool)
- Practice creating and using variables
"""

# ============================================
# PART 1: What is a Variable?
# ============================================
# A variable is like a container that stores data.
# You can give it a name and put a value inside.

# Creating variables - use the = sign (assignment operator)
name = "Alice"
age = 25
height = 1.65

print("=== Part 1: Variables ===")
print(name)
print(age)
print(height)


# ============================================
# PART 2: Data Types
# ============================================
print("\n=== Part 2: Data Types ===")

# 1. STRING (str) - Text data, wrapped in quotes
greeting = "Hello, World!"
city = 'Kuala Lumpur'  # Single or double quotes work
print(f"String example: {greeting}")

# 2. INTEGER (int) - Whole numbers (no decimal)
students = 30
year = 2024
negative_number = -10
print(f"Integer example: {students}")

# 3. FLOAT - Decimal numbers
price = 19.99
temperature = 36.5
pi = 3.14159
print(f"Float example: {price}")

# 4. BOOLEAN (bool) - True or False only
is_student = True
is_raining = False
print(f"Boolean example: {is_student}")


# ============================================
# PART 3: Checking Data Types
# ============================================
print("\n=== Part 3: Checking Types ===")

# Use type() function to check the data type
print(type(greeting))    # <class 'str'>
print(type(students))    # <class 'int'>
print(type(price))       # <class 'float'>
print(type(is_student))  # <class 'bool'>


# ============================================
# PART 4: Basic Operations
# ============================================
print("\n=== Part 4: Basic Operations ===")

# Math with numbers
a = 10
b = 3
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Integer Division: {a} // {b} = {a // b}")
print(f"Modulus (remainder): {a} % {b} = {a % b}")

# String concatenation (joining strings)
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"String concatenation: {full_name}")


# ============================================
# PART 5: Input from User
# ============================================
print("\n=== Part 5: User Input ===")

# input() always returns a string
# Uncomment the lines below to try interactive input:

# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}!")

# Converting input to numbers:
# user_age = int(input("Enter your age: "))
# print(f"Next year you will be {user_age + 1}")


# ============================================
# EXERCISES - Try these yourself!
# ============================================
"""
Exercise 1: Create variables for:
    - Your favorite color (string)
    - Your birth year (integer)
    - Your height in meters (float)
    - Whether you like Python (boolean)

Exercise 2: Calculate and print:
    - Your age (current year - birth year)
    - The area of a rectangle with width=5 and height=3

Exercise 3: Create two string variables and combine them
    into one sentence using concatenation (+)
"""

# Write your exercise solutions below:
# --------------------------------------
