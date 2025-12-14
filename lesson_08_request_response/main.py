"""
LESSON 8: Request and Response in FastAPI
===========================================
Level: Beginner

Learning Objectives:
- Use path parameters to get dynamic values from URL
- Use query parameters for optional filters
- Accept JSON data in request body using Pydantic
- Define response models for consistent output

To run this file:
    uvicorn main:app --reload

API Docs: http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(
    title="Request & Response API",
    description="Learning to handle requests and responses",
    version="1.0.0"
)


# ============================================
# PART 1: Path Parameters
# ============================================
# Path parameters are part of the URL path
# Use curly braces {} in the path to define them

@app.get("/")
def home():
    return {"message": "Welcome! Visit /docs for API documentation"}


# Basic path parameter
@app.get("/users/{user_id}")
def get_user(user_id: int):
    """Get a user by their ID."""
    return {
        "user_id": user_id,
        "name": f"User {user_id}",
        "email": f"user{user_id}@example.com"
    }


# Try: http://127.0.0.1:8000/users/1
# Try: http://127.0.0.1:8000/users/42


# Multiple path parameters
@app.get("/users/{user_id}/posts/{post_id}")
def get_user_post(user_id: int, post_id: int):
    """Get a specific post from a specific user."""
    return {
        "user_id": user_id,
        "post_id": post_id,
        "title": f"Post {post_id} by User {user_id}"
    }


# Try: http://127.0.0.1:8000/users/1/posts/5


# String path parameter
@app.get("/greet/{name}")
def greet_user(name: str):
    """Greet a user by name."""
    return {"message": f"Hello, {name}!"}


# Try: http://127.0.0.1:8000/greet/Alice


# ============================================
# PART 2: Query Parameters
# ============================================
# Query parameters come after ? in the URL
# Example: /items?skip=0&limit=10

# Simple query parameters
@app.get("/items")
def get_items(skip: int = 0, limit: int = 10):
    """
    Get items with pagination.
    - skip: number of items to skip (default: 0)
    - limit: maximum items to return (default: 10)
    """
    # Simulated database of items
    all_items = [f"Item {i}" for i in range(1, 101)]

    return {
        "skip": skip,
        "limit": limit,
        "items": all_items[skip:skip + limit]
    }


# Try: http://127.0.0.1:8000/items
# Try: http://127.0.0.1:8000/items?skip=5
# Try: http://127.0.0.1:8000/items?limit=3
# Try: http://127.0.0.1:8000/items?skip=10&limit=5


# Optional query parameter
@app.get("/search")
def search_products(
    q: Optional[str] = None,
    category: Optional[str] = None,
    min_price: float = 0,
    max_price: float = 10000
):
    """
    Search products with optional filters.
    - q: search query (optional)
    - category: filter by category (optional)
    - min_price: minimum price (default: 0)
    - max_price: maximum price (default: 10000)
    """
    return {
        "query": q,
        "category": category,
        "price_range": {"min": min_price, "max": max_price},
        "results": ["Product A", "Product B", "Product C"]
    }


# Try: http://127.0.0.1:8000/search
# Try: http://127.0.0.1:8000/search?q=laptop
# Try: http://127.0.0.1:8000/search?category=electronics&min_price=100


# Combining path and query parameters
@app.get("/users/{user_id}/orders")
def get_user_orders(
    user_id: int,
    status: Optional[str] = None,
    limit: int = 10
):
    """Get orders for a user with optional status filter."""
    return {
        "user_id": user_id,
        "status_filter": status,
        "limit": limit,
        "orders": [
            {"id": 1, "total": 150.00, "status": "delivered"},
            {"id": 2, "total": 89.99, "status": "pending"}
        ]
    }


# Try: http://127.0.0.1:8000/users/1/orders
# Try: http://127.0.0.1:8000/users/1/orders?status=pending


# ============================================
# PART 3: Request Body with Pydantic
# ============================================
# For POST/PUT requests, use Pydantic models to define the body

# Define a Pydantic model for the request body
class UserCreate(BaseModel):
    name: str
    email: str
    age: Optional[int] = None
    is_active: bool = True


# POST endpoint with request body
@app.post("/users")
def create_user(user: UserCreate):
    """
    Create a new user.

    Send JSON body like:
    {
        "name": "Alice",
        "email": "alice@example.com",
        "age": 25
    }
    """
    return {
        "message": "User created successfully",
        "user": {
            "id": 123,  # In real app, this would be generated
            "name": user.name,
            "email": user.email,
            "age": user.age,
            "is_active": user.is_active
        }
    }


# More complex request body
class Product(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int = 0
    category: str


@app.post("/products")
def create_product(product: Product):
    """
    Create a new product.

    Send JSON body like:
    {
        "name": "Laptop",
        "description": "A powerful laptop",
        "price": 2500.00,
        "quantity": 10,
        "category": "electronics"
    }
    """
    return {
        "message": "Product created",
        "product": product
    }


# Request body with nested objects
class Address(BaseModel):
    street: str
    city: str
    country: str
    postal_code: str


class CustomerCreate(BaseModel):
    name: str
    email: str
    address: Address
    tags: List[str] = []


@app.post("/customers")
def create_customer(customer: CustomerCreate):
    """
    Create a customer with nested address.

    Send JSON body like:
    {
        "name": "Bob",
        "email": "bob@example.com",
        "address": {
            "street": "123 Main St",
            "city": "Kuala Lumpur",
            "country": "Malaysia",
            "postal_code": "50000"
        },
        "tags": ["premium", "verified"]
    }
    """
    return {
        "message": "Customer created",
        "customer": customer
    }


# ============================================
# PART 4: Response Models
# ============================================
# Define what the response should look like

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool


class UserListResponse(BaseModel):
    total: int
    users: List[UserResponse]


# Using response_model to define output structure
@app.get("/api/users/{user_id}", response_model=UserResponse)
def get_user_api(user_id: int):
    """Get a user with a defined response structure."""
    # In real app, fetch from database
    return UserResponse(
        id=user_id,
        name="Alice",
        email="alice@example.com",
        is_active=True
    )


@app.get("/api/users", response_model=UserListResponse)
def list_users_api():
    """Get all users with a defined response structure."""
    users = [
        UserResponse(id=1, name="Alice", email="alice@example.com", is_active=True),
        UserResponse(id=2, name="Bob", email="bob@example.com", is_active=True),
        UserResponse(id=3, name="Charlie", email="charlie@example.com", is_active=False),
    ]
    return UserListResponse(total=len(users), users=users)


# ============================================
# PART 5: Status Codes
# ============================================
from fastapi import status

@app.post("/api/items", status_code=status.HTTP_201_CREATED)
def create_item_api(product: Product):
    """Create an item and return 201 Created status."""
    return {
        "message": "Item created",
        "item": product
    }


@app.delete("/api/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item_api(item_id: int):
    """Delete an item and return 204 No Content."""
    # In real app, delete from database
    return None  # 204 returns no content


# ============================================
# SUMMARY
# ============================================
"""
KEY CONCEPTS:

1. PATH PARAMETERS:
   @app.get("/users/{user_id}")
   def get_user(user_id: int):

2. QUERY PARAMETERS:
   @app.get("/items")
   def get_items(skip: int = 0, limit: int = 10):

3. REQUEST BODY (Pydantic):
   class User(BaseModel):
       name: str
       email: str

   @app.post("/users")
   def create_user(user: User):

4. RESPONSE MODEL:
   @app.get("/users", response_model=UserResponse)

5. STATUS CODES:
   @app.post("/items", status_code=201)
"""


# ============================================
# EXERCISES - Try these yourself!
# ============================================
"""
Exercise 1: Create an endpoint GET /products/{product_id}
    - Accept product_id as path parameter
    - Return product details

Exercise 2: Create an endpoint GET /books
    - Accept query params: author (optional), year (optional), limit (default 10)
    - Return a list of books

Exercise 3: Create a POST /orders endpoint
    - Create an Order model with: customer_name, items (list of strings), total
    - Return the created order with an ID

Exercise 4: Create a complete endpoint:
    - GET /api/products/{product_id}
    - Define a ProductResponse model
    - Use response_model parameter
"""

# Write your exercise solutions below:
# --------------------------------------

