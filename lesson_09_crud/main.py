"""
LESSON 9: CRUD Operations with SQLAlchemy
==========================================
Level: Beginner

Learning Objectives:
- Connect FastAPI to a SQLite database using SQLAlchemy
- Create database tables from Python models
- Implement CRUD operations with real database persistence
- Use dependency injection for database sessions

Installation:
    pip install fastapi uvicorn sqlalchemy

To run:
    uvicorn main:app --reload

API Docs: http://127.0.0.1:8000/docs

Project Structure:
    lesson_09_crud/
    ├── main.py        # FastAPI app (this file)
    ├── database.py    # Database connection setup
    ├── models.py      # SQLAlchemy ORM models
    └── schemas.py     # Pydantic request/response schemas
"""

from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List

# Import our modules
from database import engine, get_db, Base
from models import Item
from schemas import ItemCreate, ItemUpdate, ItemResponse


# ============================================
# STEP 1: Create the FastAPI App
# ============================================

app = FastAPI(
    title="CRUD with SQLAlchemy",
    description="Learn database operations with FastAPI and SQLAlchemy",
    version="1.0.0"
)


# ============================================
# STEP 2: Create Database Tables
# ============================================
# This creates all tables defined in models.py
# Only creates tables that don't exist yet

Base.metadata.create_all(bind=engine)


# ============================================
# STEP 3: Home Endpoint
# ============================================

@app.get("/")
def home():
    """Welcome message with API information."""
    return {
        "message": "Welcome to CRUD API with SQLAlchemy",
        "database": "SQLite (items.db)",
        "endpoints": {
            "Create": "POST /items",
            "Read All": "GET /items",
            "Read One": "GET /items/{id}",
            "Update": "PUT /items/{id}",
            "Delete": "DELETE /items/{id}"
        },
        "docs": "/docs"
    }


# ============================================
# STEP 4: CREATE - POST /items
# ============================================

@app.post("/items", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    """
    Create a new item in the database.

    - **name**: Item name (required)
    - **description**: Item description (optional)
    - **price**: Item price (required)
    - **quantity**: Stock quantity (default: 0)
    - **is_available**: Availability status (default: True)
    """
    # Create SQLAlchemy model instance
    db_item = Item(
        name=item.name,
        description=item.description,
        price=item.price,
        quantity=item.quantity,
        is_available=item.is_available
    )

    # Add to database
    db.add(db_item)
    db.commit()
    db.refresh(db_item)  # Refresh to get the generated ID and timestamps

    return db_item


# ============================================
# STEP 5: READ ALL - GET /items
# ============================================

@app.get("/items", response_model=List[ItemResponse])
def get_all_items(
    skip: int = 0,
    limit: int = 100,
    available_only: bool = False,
    db: Session = Depends(get_db)
):
    """
    Get all items from the database.

    - **skip**: Number of items to skip (pagination)
    - **limit**: Maximum items to return
    - **available_only**: Only return available items
    """
    query = db.query(Item)

    if available_only:
        query = query.filter(Item.is_available == True)

    items = query.offset(skip).limit(limit).all()
    return items


# ============================================
# STEP 6: READ ONE - GET /items/{item_id}
# ============================================

@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    """
    Get a single item by ID.

    Raises 404 if item not found.
    """
    item = db.query(Item).filter(Item.id == item_id).first()

    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found"
        )

    return item


# ============================================
# STEP 7: UPDATE - PUT /items/{item_id}
# ============================================

@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(
    item_id: int,
    item_update: ItemUpdate,
    db: Session = Depends(get_db)
):
    """
    Update an existing item.

    Only updates fields that are provided.
    Raises 404 if item not found.
    """
    # Find the item
    db_item = db.query(Item).filter(Item.id == item_id).first()

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found"
        )

    # Update only provided fields
    update_data = item_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_item, field, value)

    # Save changes
    db.commit()
    db.refresh(db_item)

    return db_item


# ============================================
# STEP 8: DELETE - DELETE /items/{item_id}
# ============================================

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """
    Delete an item by ID.

    Raises 404 if item not found.
    """
    db_item = db.query(Item).filter(Item.id == item_id).first()

    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found"
        )

    db.delete(db_item)
    db.commit()

    return None


# ============================================
# BONUS: Search Items
# ============================================

@app.get("/items/search/", response_model=List[ItemResponse])
def search_items(
    q: str = None,
    min_price: float = None,
    max_price: float = None,
    db: Session = Depends(get_db)
):
    """
    Search items by name and/or price range.

    - **q**: Search query (searches in name)
    - **min_price**: Minimum price filter
    - **max_price**: Maximum price filter
    """
    query = db.query(Item)

    if q:
        query = query.filter(Item.name.ilike(f"%{q}%"))

    if min_price is not None:
        query = query.filter(Item.price >= min_price)

    if max_price is not None:
        query = query.filter(Item.price <= max_price)

    return query.all()


# ============================================
# BONUS: Get Items Count
# ============================================

@app.get("/items/stats/count")
def get_items_count(db: Session = Depends(get_db)):
    """Get total count of items in database."""
    total = db.query(Item).count()
    available = db.query(Item).filter(Item.is_available == True).count()

    return {
        "total_items": total,
        "available_items": available,
        "unavailable_items": total - available
    }


# ============================================
# SQLALCHEMY QUERY REFERENCE
# ============================================
"""
COMMON SQLALCHEMY QUERIES:

# Get all records
db.query(Item).all()

# Get first record
db.query(Item).first()

# Filter by condition
db.query(Item).filter(Item.price > 100).all()

# Multiple conditions (AND)
db.query(Item).filter(Item.price > 100, Item.is_available == True).all()

# Filter with OR
from sqlalchemy import or_
db.query(Item).filter(or_(Item.price < 50, Item.price > 500)).all()

# Search (case-insensitive)
db.query(Item).filter(Item.name.ilike("%laptop%")).all()

# Order by
db.query(Item).order_by(Item.price.desc()).all()

# Pagination
db.query(Item).offset(10).limit(5).all()

# Count
db.query(Item).count()

# Get by ID
db.query(Item).get(1)  # or filter(Item.id == 1).first()
"""


# ============================================
# EXERCISES
# ============================================
"""
Exercise 1: Add a new endpoint
    - GET /items/{item_id}/stock
    - Return: {"in_stock": true/false} based on quantity > 0

Exercise 2: Add update quantity endpoint
    - PATCH /items/{item_id}/quantity
    - Accept: {"quantity": 10}
    - Only update quantity field

Exercise 3: Add a Category model
    - Create a new Category table
    - Add category_id foreign key to Item
    - Create endpoints for categories

Exercise 4: Add sorting
    - Modify GET /items to accept sort_by parameter
    - Support sorting by: name, price, created_at
"""
