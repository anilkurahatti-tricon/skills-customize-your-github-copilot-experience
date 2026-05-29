"""
FastAPI Todo List API - Starter Code
This is a template to help you build a REST API with FastAPI.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI(title="Todo List API", version="1.0.0")

# Define Pydantic models for request/response validation
class TodoItem(BaseModel):
    """Model for a single todo item"""
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False


class TodoCreate(BaseModel):
    """Model for creating a new todo item"""
    title: str
    description: Optional[str] = None


# In-memory storage for todos (replace with a database in production)
todos_db: List[TodoItem] = [
    TodoItem(id=1, title="Learn FastAPI", description="Complete the FastAPI tutorial", completed=False),
    TodoItem(id=2, title="Build an API", description="Create a simple REST API", completed=False),
]


# TODO: Implement the following endpoints:

# GET /todos - Retrieve all todos
# GET /todos/{todo_id} - Retrieve a specific todo by ID
# POST /todos - Create a new todo
# PUT /todos/{todo_id} - Update an existing todo
# DELETE /todos/{todo_id} - Delete a todo


@app.get("/")
async def root():
    """Root endpoint - returns a welcome message"""
    return {"message": "Welcome to the Todo List API", "docs_url": "/docs"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
