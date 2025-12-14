"""
LESSON 5: Modules and Imports in Python
=========================================
Level: Beginner

Learning Objectives:
- Understand what modules are
- Import built-in Python modules
- Use different import styles
- Install and import external packages (like FastAPI!)
"""

# ============================================
# PART 1: What is a Module?
# ============================================
print("=== Part 1: What is a Module? ===")

# A module is a file containing Python code (functions, classes, variables)
# Modules help organize code and allow code reuse
# Python has many built-in modules ready to use!

print("Modules are like toolboxes - import what you need!")


# ============================================
# PART 2: Importing Entire Modules
# ============================================
print("\n=== Part 2: Importing Entire Modules ===")

# Import the entire module
import math

# Use module functions with module_name.function_name
print(f"Pi: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"2 to the power of 3: {math.pow(2, 3)}")

import random

# Random number between 1 and 10
print(f"Random number: {random.randint(1, 10)}")

# Random choice from a list
colors = ["red", "blue", "green"]
print(f"Random color: {random.choice(colors)}")


# ============================================
# PART 3: Import Specific Items
# ============================================
print("\n=== Part 3: Import Specific Items ===")

# Import specific functions/classes from a module
# This is the MOST COMMON style in FastAPI!
from datetime import datetime, date

# Now use directly without module prefix
current_time = datetime.now()
today = date.today()

print(f"Current time: {current_time}")
print(f"Today's date: {today}")

# Another example
from math import sqrt, pi

print(f"Pi value: {pi}")
print(f"Square root of 25: {sqrt(25)}")


# ============================================
# PART 4: Import with Alias
# ============================================
print("\n=== Part 4: Import with Alias ===")

# Give a module a shorter name using 'as'
import datetime as dt

now = dt.datetime.now()
print(f"Current datetime: {now}")

# Common aliases you'll see:
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt


# ============================================
# PART 5: Common Built-in Modules
# ============================================
print("\n=== Part 5: Common Built-in Modules ===")

# os - Operating system interactions
import os

print(f"Current directory: {os.getcwd()}")
# print(f"Files in directory: {os.listdir('.')}")

# json - Work with JSON data (VERY important for APIs!)
import json

# Convert dictionary to JSON string
data = {"name": "Alice", "age": 25}
json_string = json.dumps(data)
print(f"Python dict: {data}")
print(f"JSON string: {json_string}")

# Convert JSON string back to dictionary
parsed_data = json.loads(json_string)
print(f"Parsed back: {parsed_data}")

# time - Time-related functions
import time

print("Waiting 1 second...")
time.sleep(1)  # Pause for 1 second
print("Done waiting!")


# ============================================
# PART 6: Installing External Packages
# ============================================
print("\n=== Part 6: Installing External Packages ===")

# Python has a package manager called 'pip'
# External packages are installed from PyPI (Python Package Index)

# To install a package, run in terminal:
# pip install package_name

# Examples:
# pip install fastapi        # Install FastAPI
# pip install uvicorn        # Install Uvicorn (ASGI server)
# pip install requests       # Install requests library

print("""
Common pip commands:
  pip install fastapi     - Install a package
  pip install -U fastapi  - Upgrade a package
  pip uninstall fastapi   - Remove a package
  pip list                - Show installed packages
  pip freeze              - Show packages with versions
""")


# ============================================
# PART 7: FastAPI Import Preview
# ============================================
print("\n=== Part 7: FastAPI Import Preview ===")

# This is what FastAPI imports look like!
# (Don't run this unless FastAPI is installed)

fastapi_example = '''
# Basic FastAPI imports
from fastapi import FastAPI

# Create app instance
app = FastAPI()

# Import for request/response handling
from fastapi import FastAPI, HTTPException, status

# Import for data validation (Pydantic)
from pydantic import BaseModel

# Import for path and query parameters
from fastapi import Path, Query

# Import for type hints
from typing import Optional, List
'''

print("FastAPI typically starts with these imports:")
print(fastapi_example)


# ============================================
# PART 8: Import Patterns Summary
# ============================================
print("\n=== Part 8: Import Patterns Summary ===")

summary = """
IMPORT PATTERNS:

1. Import entire module:
   import math
   math.sqrt(16)

2. Import specific items (MOST COMMON):
   from math import sqrt, pi
   sqrt(16)

3. Import with alias:
   import datetime as dt
   dt.datetime.now()

4. Import all (NOT RECOMMENDED):
   from math import *
   sqrt(16)

For FastAPI, you'll mostly use pattern #2:
   from fastapi import FastAPI
   from pydantic import BaseModel
"""
print(summary)


# ============================================
# EXERCISES - Try these yourself!
# ============================================
"""
Exercise 1: Import the 'random' module and:
    - Generate a random number between 1-100
    - Shuffle a list of numbers [1, 2, 3, 4, 5]
    - Pick a random item from a list

Exercise 2: Import 'datetime' and:
    - Print the current date and time
    - Print just today's date
    - Print the current year

Exercise 3: Import 'json' and:
    - Create a dictionary with name, age, city
    - Convert it to a JSON string
    - Parse it back to a dictionary

Exercise 4: Try installing and importing FastAPI:
    - Run: pip install fastapi
    - Import FastAPI: from fastapi import FastAPI
    - Create an app: app = FastAPI()
    - Print: print(app) to confirm it works
"""

# Write your exercise solutions below:
# --------------------------------------
