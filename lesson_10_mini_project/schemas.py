"""
PYDANTIC SCHEMAS
=================
Request and response schemas for the Todo API.
"""

from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime


class TodoCreate(BaseModel):
    """Schema for creating a new todo."""
    title: str
    description: Optional[str] = None
    priority: int = 1  # 1=Low, 2=Medium, 3=High


class TodoUpdate(BaseModel):
    """Schema for updating a todo."""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    priority: Optional[int] = None


class TodoResponse(BaseModel):
    """Schema for todo response."""
    id: int
    title: str
    description: Optional[str] = None
    completed: bool
    priority: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ============================================
# AI Endpoint Schemas
# ============================================

class AIRequest(BaseModel):
    """Schema for the AI endpoint request."""
    query: str  # e.g. "Create 3 todos for grocery shopping"


class CreateOperation(BaseModel):
    """AI wants to create a new todo."""
    action: Literal["create"]
    title: str
    description: Optional[str] = None
    priority: int = Field(default=1, ge=1, le=3)


class UpdateOperation(BaseModel):
    """AI wants to update an existing todo."""
    action: Literal["update"]
    todo_id: int
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    priority: Optional[int] = Field(default=None, ge=1, le=3)


class DeleteOperation(BaseModel):
    """AI wants to delete an existing todo."""
    action: Literal["delete"]
    todo_id: int


class AIOperations(BaseModel):
    """Structured response from the AI - a list of operations to execute."""
    operations: list[CreateOperation | UpdateOperation | DeleteOperation]


class OperationResult(BaseModel):
    """Result of a single AI operation."""
    action: str
    success: bool
    todo_id: Optional[int] = None
    detail: str


class AIResponse(BaseModel):
    """Response from the AI endpoint."""
    query: str
    operations_requested: int
    operations_succeeded: int
    results: list[OperationResult]
