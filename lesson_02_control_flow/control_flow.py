"""
LESSON 2: Control Flow in Python
=================================
Level: Beginner

Learning Objectives:
- Use if, elif, else statements for decisions
- Use comparison and logical operators
- Create loops with for and while
- Control loops with break and continue
"""

# ============================================
# PART 1: Comparison Operators
# ============================================
print("=== Part 1: Comparison Operators ===")

a = 10
b = 5

print(f"a = {a}, b = {b}")
print(f"a == b (equal): {a == b}")          # False
print(f"a != b (not equal): {a != b}")      # True
print(f"a > b (greater than): {a > b}")     # True
print(f"a < b (less than): {a < b}")        # False
print(f"a >= b (greater or equal): {a >= b}")  # True
print(f"a <= b (less or equal): {a <= b}")     # False


# ============================================
# PART 2: If Statements
# ============================================
print("\n=== Part 2: If Statements ===")

age = 18

# Simple if statement
if age >= 18:
    print("You are an adult.")

# If-else statement
score = 75
if score >= 60:
    print("You passed!")
else:
    print("You failed.")

# If-elif-else (multiple conditions)
grade = 85

if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
elif grade >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# ============================================
# PART 3: Logical Operators
# ============================================
print("\n=== Part 3: Logical Operators ===")

# and - both conditions must be True
# or  - at least one condition must be True
# not - reverses the boolean value

age = 25
has_license = True

# Using 'and'
if age >= 18 and has_license:
    print("You can drive!")

# Using 'or'
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("No work today!")

# Using 'not'
is_raining = False

if not is_raining:
    print("Let's go outside!")


# ============================================
# PART 4: For Loops
# ============================================
print("\n=== Part 4: For Loops ===")

# Loop through a range of numbers
print("Counting 1 to 5:")
for i in range(1, 6):  # range(start, stop) - stop is not included
    print(i)

# Loop through a list
fruits = ["apple", "banana", "cherry"]
print("\nFruits in the list:")
for fruit in fruits:
    print(f"- {fruit}")

# Loop with index using enumerate()
print("\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Loop through a string
print("\nLetters in 'Python':")
for letter in "Python":
    print(letter, end=" ")
print()  # New line


# ============================================
# PART 5: While Loops
# ============================================
print("\n=== Part 5: While Loops ===")

# Basic while loop - runs while condition is True
count = 1
print("Counting with while loop:")
while count <= 5:
    print(count)
    count += 1  # Important: update the variable to avoid infinite loop!

# Countdown example
print("\nCountdown:")
countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Go!")


# ============================================
# PART 6: Break and Continue
# ============================================
print("\n=== Part 6: Break and Continue ===")

# break - exits the loop completely
print("Finding first even number:")
for num in [1, 3, 5, 4, 7, 8]:
    if num % 2 == 0:
        print(f"Found: {num}")
        break  # Stop the loop

# continue - skips current iteration, continues to next
print("\nPrinting odd numbers only:")
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num, end=" ")
print()


# ============================================
# PART 7: Nested Loops
# ============================================
print("\n=== Part 7: Nested Loops ===")

# Multiplication table (3x3)
print("Multiplication Table:")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{i} x {j} = {result}")
    print("---")


# ============================================
# EXERCISES - Try these yourself!
# ============================================
"""
Exercise 1: Write an if-elif-else statement that:
    - Checks a temperature variable
    - Prints "Cold" if below 15
    - Prints "Warm" if between 15 and 25
    - Prints "Hot" if above 25

Exercise 2: Use a for loop to print all numbers from 1 to 20
    that are divisible by 3

Exercise 3: Write a while loop that:
    - Starts with a number = 100
    - Keeps dividing by 2 until it's less than 1
    - Prints each step

Exercise 4: Create a simple number guessing game:
    - Set a secret number
    - Use a while loop
    - Print "Too high" or "Too low" based on guess
    - Break when correct
"""

# Write your exercise solutions below:
# --------------------------------------
