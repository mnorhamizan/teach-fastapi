"""
LESSON 7: FastAPI Basics
=========================
Level: Beginner

Learning Objectives:
- Install FastAPI and Uvicorn
- Create your first FastAPI application
- Understand routes and endpoints
- Use the automatic documentation (Swagger UI)

To run this file:
    uvicorn main:app --reload

Then open: http://127.0.0.1:8000
API Docs:  http://127.0.0.1:8000/docs
"""

# ============================================
# STEP 1: Installation (run in terminal)
# ============================================
"""
First, install FastAPI and Uvicorn:

    pip install fastapi uvicorn

- fastapi: The web framework
- uvicorn: The ASGI server that runs your app
"""

# ============================================
# STEP 2: Import FastAPI
# ============================================
from fastapi import FastAPI

# ============================================
# STEP 3: Create the App Instance
# ============================================
# This creates your FastAPI application
app = FastAPI(
    title="My First API",
    description="Learning FastAPI basics",
    version="1.0.0"
)


# ============================================
# STEP 4: Create Your First Route
# ============================================
# A route is a URL path that returns something
# @app.get("/") means: when someone visits "/", run this function

@app.get("/")
def home():
    """This is the home page of our API."""
    return {"message": "Welcome to FastAPI!"}


# ============================================
# STEP 5: More GET Routes
# ============================================

@app.get("/hello")
def say_hello():
    """A simple hello endpoint."""
    return {"greeting": "Hello, World!"}


@app.get("/about")
def about():
    """Information about this API."""
    return {
        "app_name": "My First API",
        "version": "1.0.0",
        "author": "Your Name"
    }


# ============================================
# STEP 6: Returning Different Data
# ============================================

@app.get("/numbers")
def get_numbers():
    """Return a list of numbers."""
    return {"numbers": [1, 2, 3, 4, 5]}


@app.get("/user")
def get_user():
    """Return user information."""
    return {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com",
        "is_active": True
    }


@app.get("/products")
def get_products():
    """Return a list of products."""
    return {
        "products": [
            {"id": 1, "name": "Laptop", "price": 2500},
            {"id": 2, "name": "Mouse", "price": 50},
            {"id": 3, "name": "Keyboard", "price": 150}
        ]
    }


# ============================================
# STEP 7: Running the Application
# ============================================
"""
To run your FastAPI app, use this command in terminal:

    uvicorn main:app --reload

Breaking it down:
- main      = the Python file name (main.py)
- app       = the FastAPI instance variable
- --reload  = auto-restart when code changes (dev mode)

You should see:
    INFO:     Uvicorn running on http://127.0.0.1:8000
    INFO:     Started reloader process

Now visit these URLs in your browser:
    http://127.0.0.1:8000           - Home page
    http://127.0.0.1:8000/hello     - Hello endpoint
    http://127.0.0.1:8000/about     - About endpoint
    http://127.0.0.1:8000/products  - Products list
"""


# ============================================
# STEP 8: Automatic API Documentation
# ============================================
"""
FastAPI automatically generates interactive documentation!

Visit these URLs:

1. Swagger UI (Interactive):
   http://127.0.0.1:8000/docs
   - Try out your API directly in the browser
   - See all your endpoints
   - Test requests and see responses

2. ReDoc (Alternative docs):
   http://127.0.0.1:8000/redoc
   - Clean, readable documentation
   - Good for sharing with others
"""


# ============================================
# EXERCISES - Try these yourself!
# ============================================
"""
Exercise 1: Create a new endpoint
    - Path: /greet
    - Return: {"message": "Good morning!"}

Exercise 2: Create an endpoint that returns your info
    - Path: /me
    - Return: your name, age, and favorite programming language

Exercise 3: Create an endpoint that returns a shopping list
    - Path: /shopping
    - Return: a list of 5 items to buy

Exercise 4: Explore the documentation
    - Open http://127.0.0.1:8000/docs
    - Click on each endpoint
    - Click "Try it out" and "Execute"
    - See the response
"""

# Write your exercise solutions below:
# --------------------------------------

