# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build scalable REST APIs using the FastAPI framework. Create a complete API with multiple endpoints, request validation, and proper HTTP methods. You'll practice working with routing, path parameters, query parameters, and request bodies while building a production-ready API structure.

## 📝 Tasks

### 🛠️ Create a Todo List API

#### Description
Build a RESTful API for a todo list application with full CRUD (Create, Read, Update, Delete) operations. The API should handle multiple endpoints to manage todo items and demonstrate proper REST API design patterns.

#### Requirements
Completed API should:

- Define multiple routes using FastAPI decorators (@app.get, @app.post, @app.put, @app.delete)
- Accept and validate request data using Pydantic models
- Implement path parameters to identify specific resources (e.g., /todos/{todo_id})
- Support query parameters for filtering or pagination
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Include error handling for invalid requests

### 🛠️ Add Request Validation and Documentation

#### Description
Enhance your API with robust input validation using Pydantic models and leverage FastAPI's automatic API documentation features.

#### Requirements
Completed implementation should:

- Create Pydantic model classes for request and response data
- Use type hints for automatic validation and documentation
- Include field validation with constraints (e.g., required fields, string length limits)
- Test the auto-generated Swagger UI documentation at /docs
- Demonstrate proper HTTP method semantics (GET for retrieval, POST for creation, etc.)
