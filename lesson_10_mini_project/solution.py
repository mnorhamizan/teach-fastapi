"""
LESSON 10: Mini Project - Todo List API with SQLAlchemy (SOLUTION)
===================================================================
Level: Beginner

Complete solution for the Todo List API with database persistence.

Project Structure:
    lesson_10_mini_project/
    ├── database.py    # Database setup
    ├── models.py      # SQLAlchemy model
    ├── schemas.py     # Pydantic schemas
    ├── starter.py     # Student template
    └── solution.py    # This file

Installation:
    pip install fastapi uvicorn sqlalchemy

To run:
    uvicorn solution:app --reload

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
    description="Complete Todo API with SQLAlchemy - Solution",
    version="1.0.0"
)

# Create tables in database
Base.metadata.create_all(bind=engine)


# ============================================
# Home Endpoint
# ============================================

@app.get("/")
def home():
    """Welcome endpoint with API information."""
    return {
        "message": "Todo List API with SQLAlchemy",
        "version": "1.0.0",
        "database": "SQLite (todos.db)",
        "endpoints": {
            "Create": "POST /todos",
            "Read All": "GET /todos",
            "Read One": "GET /todos/{id}",
            "Update": "PUT /todos/{id}",
            "Delete": "DELETE /todos/{id}",
            "Toggle": "POST /todos/{id}/toggle",
            "Stats": "GET /todos/stats",
            "Search": "GET /todos/search"
        },
        "docs": "/docs"
    }


# ============================================
# CREATE - POST /todos
# ============================================

@app.post("/todos", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    """
    Create a new todo item.

    - **title**: Todo title (required)
    - **description**: Optional description
    - **priority**: 1=Low, 2=Medium, 3=High (default: 1)
    """
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        priority=todo.priority
    )

    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)

    return db_todo


# ============================================
# READ ALL - GET /todos
# ============================================

@app.get("/todos", response_model=List[TodoResponse])
def get_all_todos(
    completed: Optional[bool] = None,
    priority: Optional[int] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Get all todos with optional filters.

    - **completed**: Filter by completion status
    - **priority**: Filter by priority (1, 2, or 3)
    - **skip**: Number of items to skip (pagination)
    - **limit**: Maximum items to return
    """
    query = db.query(Todo)

    # Apply filters
    if completed is not None:
        query = query.filter(Todo.completed == completed)

    if priority is not None:
        query = query.filter(Todo.priority == priority)

    # Apply pagination and return
    return query.offset(skip).limit(limit).all()


# ============================================
# STATS - GET /todos/stats
# ============================================

@app.get("/todos/stats")
def get_stats(db: Session = Depends(get_db)):
    """Get todo statistics."""
    total = db.query(Todo).count()
    completed = db.query(Todo).filter(Todo.completed == True).count()
    pending = total - completed

    # Priority breakdown
    high_priority = db.query(Todo).filter(Todo.priority == 3).count()
    medium_priority = db.query(Todo).filter(Todo.priority == 2).count()
    low_priority = db.query(Todo).filter(Todo.priority == 1).count()

    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "completion_rate": f"{(completed/total*100):.1f}%" if total > 0 else "0%",
        "by_priority": {
            "high": high_priority,
            "medium": medium_priority,
            "low": low_priority
        }
    }


# ============================================
# BONUS: Search
# ============================================

@app.get("/todos/search", response_model=List[TodoResponse])
def search_todos(q: str, db: Session = Depends(get_db)):
    """
    Search todos by title.

    - **q**: Search query (case-insensitive)
    """
    return db.query(Todo).filter(Todo.title.ilike(f"%{q}%")).all()


# ============================================
# BONUS: Delete All Completed
# ============================================

@app.delete("/todos/completed", status_code=status.HTTP_204_NO_CONTENT)
def delete_completed(db: Session = Depends(get_db)):
    """Delete all completed todos."""
    db.query(Todo).filter(Todo.completed == True).delete()
    db.commit()
    return None


# ============================================
# BONUS: Get by Priority
# ============================================

@app.get("/todos/priority/{priority}", response_model=List[TodoResponse])
def get_by_priority(priority: int, db: Session = Depends(get_db)):
    """
    Get todos by priority level.

    - **priority**: 1=Low, 2=Medium, 3=High
    """
    if priority not in [1, 2, 3]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Priority must be 1 (Low), 2 (Medium), or 3 (High)"
        )

    return db.query(Todo).filter(Todo.priority == priority).all()


# ============================================
# READ ONE - GET /todos/{todo_id}
# ============================================

@app.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    """
    Get a single todo by ID.

    Raises 404 if not found.
    """
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with ID {todo_id} not found"
        )

    return todo


# ============================================
# UPDATE - PUT /todos/{todo_id}
# ============================================

@app.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(
    todo_id: int,
    todo_update: TodoUpdate,
    db: Session = Depends(get_db)
):
    """
    Update an existing todo.

    Only updates fields that are provided.
    """
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if db_todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with ID {todo_id} not found"
        )

    # Update only provided fields
    update_data = todo_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_todo, field, value)

    db.commit()
    db.refresh(db_todo)

    return db_todo


# ============================================
# DELETE - DELETE /todos/{todo_id}
# ============================================

@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """
    Delete a todo by ID.

    Raises 404 if not found.
    """
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if db_todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with ID {todo_id} not found"
        )

    db.delete(db_todo)
    db.commit()

    return None


# ============================================
# TOGGLE - POST /todos/{todo_id}/toggle
# ============================================

@app.post("/todos/{todo_id}/toggle", response_model=TodoResponse)
def toggle_todo(todo_id: int, db: Session = Depends(get_db)):
    """
    Toggle the completed status of a todo.

    If completed is True, it becomes False, and vice versa.
    """
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if db_todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with ID {todo_id} not found"
        )

    db_todo.completed = not db_todo.completed
    db.commit()
    db.refresh(db_todo)

    return db_todo


# ============================================
# TESTING GUIDE
# ============================================
"""
TEST YOUR API:

1. Open http://127.0.0.1:8000/docs

2. Create some todos:
   POST /todos
   {"title": "Learn FastAPI", "description": "Complete tutorial", "priority": 3}
   {"title": "Build project", "priority": 2}
   {"title": "Review code", "priority": 1}

3. Get all todos:
   GET /todos

4. Filter todos:
   GET /todos?completed=false
   GET /todos?priority=3

5. Get one todo:
   GET /todos/1

6. Update a todo:
   PUT /todos/1
   {"completed": true}

7. Toggle completion:
   POST /todos/1/toggle

8. Get stats:
   GET /todos/stats

9. Search:
   GET /todos/search?q=learn

10. Delete a todo:
    DELETE /todos/1

11. Delete all completed:
    DELETE /todos/completed
"""


# ============================================
# WHAT YOU LEARNED
# ============================================
"""
CONGRATULATIONS! You've built a complete REST API with SQLAlchemy!

Skills practiced:
1. Setting up SQLAlchemy with FastAPI
2. Creating database models (ORM)
3. Defining Pydantic schemas for request/response
4. Using dependency injection (Depends)
5. Implementing full CRUD operations
6. Writing database queries with SQLAlchemy
7. Error handling with HTTPException
8. Using proper HTTP status codes

Key SQLAlchemy patterns:
- db.query(Model).all()           # Get all
- db.query(Model).first()         # Get first
- db.query(Model).filter(...)     # Filter
- db.add(item)                    # Add new
- db.commit()                     # Save changes
- db.refresh(item)                # Reload from DB
- db.delete(item)                 # Delete item

Next steps:
- Add user authentication (JWT)
- Use PostgreSQL for production
- Add database migrations (Alembic)
- Write unit tests with pytest
- Deploy to cloud (Railway, Render, AWS)
"""
