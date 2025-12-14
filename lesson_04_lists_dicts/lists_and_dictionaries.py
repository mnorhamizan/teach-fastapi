"""
LESSON 4: Lists and Dictionaries in Python
============================================
Level: Beginner

Learning Objectives:
- Create and manipulate lists
- Create and manipulate dictionaries
- Understand when to use each data structure
- Work with nested structures (important for JSON/APIs!)
"""

# ============================================
# PART 1: Lists - Ordered Collections
# ============================================
print("=== Part 1: Creating Lists ===")

# A list is an ordered collection of items
# Use square brackets []
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, 3.14, True]  # Can mix types

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")

# Empty list
empty_list = []


# ============================================
# PART 2: Accessing List Items
# ============================================
print("\n=== Part 2: Accessing List Items ===")

colors = ["red", "green", "blue", "yellow", "purple"]

# Indexing starts at 0
print(f"First item (index 0): {colors[0]}")
print(f"Second item (index 1): {colors[1]}")
print(f"Last item (index -1): {colors[-1]}")
print(f"Second to last (index -2): {colors[-2]}")

# Slicing - get a portion of the list
print(f"First 3 items: {colors[0:3]}")
print(f"Items 2 to 4: {colors[1:4]}")
print(f"From index 2 onwards: {colors[2:]}")


# ============================================
# PART 3: Modifying Lists
# ============================================
print("\n=== Part 3: Modifying Lists ===")

animals = ["cat", "dog", "bird"]
print(f"Original: {animals}")

# Change an item
animals[0] = "lion"
print(f"After change: {animals}")

# Add items
animals.append("elephant")  # Add to end
print(f"After append: {animals}")

animals.insert(1, "tiger")  # Insert at index
print(f"After insert: {animals}")

# Remove items
animals.remove("bird")  # Remove by value
print(f"After remove: {animals}")

last_animal = animals.pop()  # Remove and return last item
print(f"Popped: {last_animal}, List: {animals}")

# List length
print(f"Number of animals: {len(animals)}")


# ============================================
# PART 4: List Operations
# ============================================
print("\n=== Part 4: List Operations ===")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Check if item exists
print(f"Is 5 in list? {5 in numbers}")
print(f"Is 7 in list? {7 in numbers}")

# Sort and reverse
numbers.sort()
print(f"Sorted: {numbers}")

numbers.reverse()
print(f"Reversed: {numbers}")

# Loop through a list
print("Looping through list:")
for num in numbers:
    print(num, end=" ")
print()


# ============================================
# PART 5: Dictionaries - Key-Value Pairs
# ============================================
print("\n=== Part 5: Creating Dictionaries ===")

# A dictionary stores data as key-value pairs
# Use curly braces {} with key: value format
# VERY IMPORTANT: This is similar to JSON format!

person = {
    "name": "Alice",
    "age": 25,
    "city": "Kuala Lumpur"
}
print(f"Person: {person}")

# Empty dictionary
empty_dict = {}


# ============================================
# PART 6: Accessing Dictionary Items
# ============================================
print("\n=== Part 6: Accessing Dictionary Items ===")

student = {
    "name": "Bob",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Science", "English"]
}

# Access by key
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Courses: {student['courses']}")

# Using get() - safer, returns None if key doesn't exist
print(f"Grade: {student.get('grade')}")
print(f"Email: {student.get('email')}")  # Returns None
print(f"Email: {student.get('email', 'Not provided')}")  # Default value


# ============================================
# PART 7: Modifying Dictionaries
# ============================================
print("\n=== Part 7: Modifying Dictionaries ===")

user = {
    "username": "john_doe",
    "email": "john@example.com"
}
print(f"Original: {user}")

# Add or update items
user["age"] = 30  # Add new key
user["email"] = "john.doe@gmail.com"  # Update existing
print(f"After changes: {user}")

# Remove items
del user["age"]
print(f"After delete: {user}")

# Pop - remove and return value
email = user.pop("email")
print(f"Popped email: {email}")


# ============================================
# PART 8: Dictionary Operations
# ============================================
print("\n=== Part 8: Dictionary Operations ===")

product = {
    "name": "Laptop",
    "price": 2500,
    "brand": "Dell"
}

# Get all keys
print(f"Keys: {list(product.keys())}")

# Get all values
print(f"Values: {list(product.values())}")

# Get all key-value pairs
print(f"Items: {list(product.items())}")

# Check if key exists
print(f"Has 'price' key? {'price' in product}")
print(f"Has 'color' key? {'color' in product}")

# Loop through dictionary
print("\nLooping through dictionary:")
for key, value in product.items():
    print(f"  {key}: {value}")


# ============================================
# PART 9: Nested Structures (Important for APIs!)
# ============================================
print("\n=== Part 9: Nested Structures ===")

# List of dictionaries - VERY COMMON in APIs!
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
]

print("All users:")
for user in users:
    print(f"  {user['id']}: {user['name']} ({user['email']})")

# Access specific user
print(f"\nFirst user's name: {users[0]['name']}")

# Dictionary with nested dictionary
company = {
    "name": "Tech Corp",
    "address": {
        "street": "123 Main St",
        "city": "KL",
        "country": "Malaysia"
    },
    "employees": ["Alice", "Bob", "Charlie"]
}

print(f"\nCompany: {company['name']}")
print(f"City: {company['address']['city']}")
print(f"First employee: {company['employees'][0]}")


# ============================================
# PART 10: Real-World API Example Preview
# ============================================
print("\n=== Part 10: API Response Preview ===")

# This is what API responses typically look like!
api_response = {
    "status": "success",
    "data": {
        "user": {
            "id": 123,
            "name": "John Doe",
            "email": "john@example.com"
        },
        "posts": [
            {"id": 1, "title": "Hello World"},
            {"id": 2, "title": "Learning Python"}
        ]
    },
    "message": "User retrieved successfully"
}

# Accessing nested API data
print(f"Status: {api_response['status']}")
print(f"User Name: {api_response['data']['user']['name']}")
print(f"First Post: {api_response['data']['posts'][0]['title']}")


# ============================================
# EXERCISES - Try these yourself!
# ============================================
"""
Exercise 1: Create a list of 5 favorite movies and:
    - Print the first and last movie
    - Add a new movie to the end
    - Remove the second movie
    - Print the final list

Exercise 2: Create a dictionary representing a book with:
    - title, author, year, pages, genres (list)
    - Print each piece of information

Exercise 3: Create a list of 3 dictionaries representing students:
    - Each student has: name, age, grade
    - Loop through and print each student's info
    - Calculate and print the average age

Exercise 4: Given this API response, extract the required data:
    response = {
        "results": [
            {"name": "Product A", "price": 100},
            {"name": "Product B", "price": 200}
        ],
        "total": 2
    }
    - Print all product names
    - Calculate total price of all products
"""

# Write your exercise solutions below:
# --------------------------------------
