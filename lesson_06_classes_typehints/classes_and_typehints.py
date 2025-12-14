"""
LESSON 6: Classes and Type Hints in Python
============================================
Level: Beginner

Learning Objectives:
- Understand basic class structure
- Create simple classes with attributes
- Use type hints for better code
- Preview Pydantic models (used in FastAPI!)
"""

# ============================================
# PART 1: What is a Class?
# ============================================
print("=== Part 1: What is a Class? ===")

# A class is a blueprint for creating objects
# Think of it like a template or cookie cutter

# Example: A "Car" class is the blueprint
# Individual cars (Toyota, Honda) are objects created from that blueprint

print("Class = Blueprint")
print("Object = Instance created from the blueprint")


# ============================================
# PART 2: Creating a Simple Class
# ============================================
print("\n=== Part 2: Creating a Simple Class ===")


# Define a class using 'class' keyword
class Dog:
    # __init__ is called when creating a new object
    def __init__(self, name, age):
        self.name = name  # 'self' refers to the object itself
        self.age = age

    # Method (function inside a class)
    def bark(self):
        print(f"{self.name} says: Woof!")

    def describe(self):
        print(f"{self.name} is {self.age} years old.")


# Create objects (instances) from the class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Use object attributes and methods
print(f"Dog 1: {dog1.name}")
print(f"Dog 2: {dog2.name}")

dog1.bark()
dog2.describe()


# ============================================
# PART 3: Class with More Features
# ============================================
print("\n=== Part 3: Class with More Features ===")


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.courses = []  # Empty list for courses

    def add_course(self, course):
        self.courses.append(course)
        print(f"{self.name} enrolled in {course}")

    def get_info(self):
        return {
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
            "courses": self.courses
        }


# Create a student
student = Student("Alice", 20, "A")
student.add_course("Python 101")
student.add_course("Web Development")

info = student.get_info()
print(f"Student info: {info}")


# ============================================
# PART 4: Introduction to Type Hints
# ============================================
print("\n=== Part 4: Introduction to Type Hints ===")

# Type hints tell Python what type of data to expect
# They make code easier to read and help catch errors


# WITHOUT type hints
def add(a, b):
    return a + b


# WITH type hints (recommended!)
def add_typed(a: int, b: int) -> int:
    return a + b


# The hints don't enforce types, but they document intent
result = add_typed(5, 3)
print(f"5 + 3 = {result}")


# More type hint examples
def greet(name: str) -> str:
    return f"Hello, {name}!"


def is_adult(age: int) -> bool:
    return age >= 18


print(greet("Alice"))
print(f"Is 20 adult? {is_adult(20)}")


# ============================================
# PART 5: Type Hints with Collections
# ============================================
print("\n=== Part 5: Type Hints with Collections ===")

from typing import List, Dict, Optional

# List of strings
def get_names() -> List[str]:
    return ["Alice", "Bob", "Charlie"]


# Dictionary with string keys and int values
def get_scores() -> Dict[str, int]:
    return {"Alice": 95, "Bob": 87, "Charlie": 92}


# Optional - can be the type OR None
def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)  # Returns None if not found


print(f"Names: {get_names()}")
print(f"Scores: {get_scores()}")
print(f"User 1: {find_user(1)}")
print(f"User 99: {find_user(99)}")


# ============================================
# PART 6: Classes with Type Hints
# ============================================
print("\n=== Part 6: Classes with Type Hints ===")


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name: str = name
        self.price: float = price
        self.quantity: int = quantity

    def total_value(self) -> float:
        return self.price * self.quantity

    def to_dict(self) -> Dict[str, any]:
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }


laptop = Product("Laptop", 2500.00, 5)
print(f"Product: {laptop.to_dict()}")
print(f"Total value: RM{laptop.total_value()}")


# ============================================
# PART 7: Preview - Pydantic Models (FastAPI)
# ============================================
print("\n=== Part 7: Pydantic Models Preview ===")

# In FastAPI, you'll use Pydantic for data validation
# Pydantic classes look similar but with a key difference

pydantic_example = '''
from pydantic import BaseModel
from typing import Optional, List

# Pydantic model - notice the simpler syntax!
class User(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int] = None  # Optional with default None
    tags: List[str] = []       # Default empty list

# Create a user - Pydantic validates the data!
user = User(id=1, name="Alice", email="alice@example.com")

# Convert to dictionary easily
print(user.dict())
# Output: {'id': 1, 'name': 'Alice', 'email': 'alice@example.com', 'age': None, 'tags': []}

# Pydantic will raise an error if data is invalid:
# User(id="not_a_number", name="Bob", email="bob@example.com")
# ValidationError: id must be an integer!
'''

print("In FastAPI, you'll use Pydantic models like this:")
print(pydantic_example)


# ============================================
# PART 8: FastAPI Request/Response Preview
# ============================================
print("\n=== Part 8: FastAPI Request/Response Preview ===")

fastapi_example = '''
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define request body structure
class Item(BaseModel):
    name: str
    price: float
    is_available: bool = True

# FastAPI uses type hints everywhere!
@app.post("/items/")
def create_item(item: Item):
    return {"message": f"Created item: {item.name}"}

@app.get("/items/{item_id}")
def get_item(item_id: int):  # Type hint validates the path parameter
    return {"item_id": item_id}
'''

print("This is how classes and type hints are used in FastAPI:")
print(fastapi_example)


# ============================================
# PART 9: Summary - Key Concepts for FastAPI
# ============================================
print("\n=== Part 9: Summary ===")

summary = """
KEY CONCEPTS FOR FASTAPI:

1. CLASSES:
   - Define with 'class ClassName:'
   - Use __init__ for initialization
   - 'self' refers to the instance

2. TYPE HINTS:
   - variable: type (e.g., name: str)
   - function(param: type) -> return_type
   - Makes code clear and enables validation

3. COMMON TYPES:
   - Basic: str, int, float, bool
   - Collections: List[str], Dict[str, int]
   - Optional: Optional[str] = None

4. PYDANTIC MODELS (for FastAPI):
   class MyModel(BaseModel):
       field1: str
       field2: int
       field3: Optional[str] = None

You're now ready for FastAPI!
"""
print(summary)


# ============================================
# EXERCISES - Try these yourself!
# ============================================
"""
Exercise 1: Create a 'Book' class with:
    - Attributes: title (str), author (str), pages (int)
    - Method: describe() that prints book info
    - Create 2 book objects and call describe()

Exercise 2: Write these functions with type hints:
    - multiply(a: int, b: int) -> int
    - get_full_name(first: str, last: str) -> str
    - calculate_average(numbers: List[float]) -> float

Exercise 3: Create a 'Person' class with type hints:
    - name: str
    - age: int
    - email: Optional[str] = None
    - Add a to_dict() method that returns a dictionary

Exercise 4: Preview exercise - Write a Pydantic-style class:
    class Product(BaseModel):
        name: str
        price: float
        category: str
        in_stock: bool = True

    (You can run this if you install pydantic: pip install pydantic)
"""

# Write your exercise solutions below:
# --------------------------------------
