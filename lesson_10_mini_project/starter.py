"""
LESSON 10: Mini Project - Todo List API with SQLAlchemy (STARTER)
==================================================================
Level: Beginner

Project: Build a complete Todo List API with database persistence

Your task is to complete this Todo API with the following features:
1. Create a new todo
2. Get all todos (with optional filters)
3. Get a single todo by ID
4. Update a todo
5. Delete a todo
6. Toggle todo completion status
7. Get statistics

Project Structure:
    lesson_10_mini_project/
    ├── database.py    # Database setup (provided)
    ├── models.py      # SQLAlchemy model (provided)
    ├── schemas.py     # Pydantic schemas (provided)
    ├── starter.py     # YOUR CODE HERE
    └── solution.py    # Reference solution

Installation:
    pip install fastapi uvicorn sqlalchemy

To run:
    uvicorn starter:app --reload

API Docs: http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List, Optional

# Import from our modules
from database import engine, get_db, Base
from models import Todo
from schemas import TodoCreate, TodoUpdate, TodoResponse


# ============================================
# Create App and Database Tables
# ============================================

app = FastAPI(
    title="Todo List API",
    description="Mini Project - Todo API with SQLAlchemy",
    version="1.0.0"
)

# Create tables
Base.metadata.create_all(bind=engine)


# ============================================
# Home Endpoint (Provided)
# ============================================

@app.get("/")
def home():
    return {
        "message": "Todo List API with SQLAlchemy",
        "docs": "/docs"
    }


# ============================================
# TODO: Implement CREATE endpoint
# ============================================
# POST /todos
# - Accept TodoCreate in body
# - Create new Todo in database
# - Return created todo with 201 status

@app.post("/todos", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    """Create a new todo."""
    # TODO: Implement this
    # Hint:
    # 1. Create Todo model instance: db_todo = Todo(title=todo.title, ...)
    # 2. Add to session: db.add(db_todo)
    # 3. Commit: db.commit()
    # 4. Refresh: db.refresh(db_todo)
    # 5. Return db_todo
    pass


# ============================================
# TODO: Implement READ ALL endpoint
# ============================================
# GET /todos
# - Optional query params: completed (bool), priority (int)
# - Return list of todos

@app.get("/todos", response_model=List[TodoResponse])
def get_all_todos(
    completed: Optional[bool] = None,
    priority: Optional[int] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Get all todos with optional filters."""
    # TODO: Implement this
    # Hint:
    # 1. Start query: query = db.query(Todo)
    # 2. Add filters if provided:
    #    if completed is not None:
    #        query = query.filter(Todo.completed == completed)
    # 3. Apply pagination: query.offset(skip).limit(limit).all()
    pass


# ============================================
# TODO: Implement READ ONE endpoint
# ============================================
# GET /todos/{todo_id}
# - Return todo if found
# - Raise 404 if not found

@app.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    """Get a single todo by ID."""
    # TODO: Implement this
    # Hint:
    # 1. Query: todo = db.query(Todo).filter(Todo.id == todo_id).first()
    # 2. If None, raise HTTPException(status_code=404, detail="...")
    # 3. Return todo
    pass


# ============================================
# TODO: Implement UPDATE endpoint
# ============================================
# PUT /todos/{todo_id}
# - Update only provided fields
# - Raise 404 if not found

@app.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(
    todo_id: int,
    todo_update: TodoUpdate,
    db: Session = Depends(get_db)
):
    """Update an existing todo."""
    # TODO: Implement this
    # Hint:
    # 1. Find todo (raise 404 if not found)
    # 2. Get update data: update_data = todo_update.model_dump(exclude_unset=True)
    # 3. Loop and update: for field, value in update_data.items(): setattr(db_todo, field, value)
    # 4. Commit and refresh
    pass


# ============================================
# TODO: Implement DELETE endpoint
# ============================================
# DELETE /todos/{todo_id}
# - Delete todo from database
# - Raise 404 if not found

@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """Delete a todo."""
    # TODO: Implement this
    # Hint:
    # 1. Find todo (raise 404 if not found)
    # 2. Delete: db.delete(db_todo)
    # 3. Commit: db.commit()
    # 4. Return None
    pass


# ============================================
# TODO: Implement TOGGLE endpoint
# ============================================
# POST /todos/{todo_id}/toggle
# - Toggle completed status (True -> False, False -> True)

@app.post("/todos/{todo_id}/toggle", response_model=TodoResponse)
def toggle_todo(todo_id: int, db: Session = Depends(get_db)):
    """Toggle the completed status of a todo."""
    # TODO: Implement this
    # Hint:
    # 1. Find todo
    # 2. Toggle: db_todo.completed = not db_todo.completed
    # 3. Commit and refresh
    pass


# ============================================
# TODO: Implement STATS endpoint
# ============================================
# GET /todos/stats
# - Return: total, completed, pending counts

@app.get("/todos/stats")
def get_stats(db: Session = Depends(get_db)):
    """Get todo statistics."""
    # TODO: Implement this
    # Hint:
    # 1. total = db.query(Todo).count()
    # 2. completed = db.query(Todo).filter(Todo.completed == True).count()
    # 3. Return dict with stats
    pass


# ============================================
# BONUS CHALLENGES
# ============================================
"""
If you finish early, try adding:

1. GET /todos/search?q=keyword
   - Search todos by title

2. DELETE /todos/completed
   - Delete all completed todos

3. GET /todos/priority/{priority}
   - Get todos by priority level (1, 2, or 3)

4. PUT /todos/{todo_id}/priority
   - Update only the priority field
"""
