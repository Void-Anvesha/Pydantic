# Pydantic

Advanced Pydantic patterns, validators, and real-world implementations.

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pydantic](https://img.shields.io/badge/pydantic-2.0+-green.svg)](https://pydantic.dev/)

## About Pydantic

Pydantic is Python's most popular data validation library that enforces type hints at runtime and provides user-friendly errors when data is invalid. It combines Python's type system with automatic validation, serialization, and documentation generation.

**Core Benefits:**
- **Runtime Type Validation**: Automatic data validation using Python type hints
- **Fast Performance**: Built on Rust foundations (Pydantic v2) for high-speed processing
- **Rich Type Support**: Native support for complex types, custom validators, and nested models  
- **JSON Schema Generation**: Automatic OpenAPI/JSON schema creation for APIs
- **Framework Integration**: First-class support in FastAPI, SQLModel, and other modern frameworks

## Overview

Collection of production-ready Pydantic implementations covering validation patterns, custom validators, serialization strategies, and framework integrations.

## Structure

```
├── core/
│   ├── models/           # Base model definitions
│   ├── validators/       # Custom validation logic
│   └── serializers/      # Data transformation utilities
├── patterns/
│   ├── nested_models.py  # Complex model hierarchies
│   ├── conditional.py    # Conditional validation
│   ├── generic_types.py  # Generic and parameterized models
│   └── inheritance.py    # Model inheritance patterns
├── integrations/
│   ├── fastapi/         # FastAPI integration examples
│   ├── sqlalchemy/      # ORM model mapping
│   ├── dataclass/       # Dataclass compatibility
│   └── settings/        # Configuration management
├── advanced/
│   ├── performance.py   # Optimization techniques
│   ├── security.py      # Input sanitization
│   ├── migrations.py    # Schema versioning
│   └── plugins.py       # Custom field types
└── examples/
    ├── api_models.py    # REST API schemas
    ├── config.py        # Application settings
    └── data_pipeline.py # ETL transformations
```

## Key Features

- **Custom Validators**: Reusable validation logic for complex business rules
- **Performance Optimization**: Efficient serialization and validation strategies  
- **Framework Integration**: Ready-to-use patterns for FastAPI, SQLAlchemy, Django
- **Security Patterns**: Input sanitization and data validation for security
- **Type Safety**: Advanced typing patterns with generic models

## Quick Start

```python
from pydantic import BaseModel, validator, Field
from typing import List, Optional
from datetime import datetime

class UserProfile(BaseModel):
    user_id: int = Field(..., gt=0)
    username: str = Field(..., min_length=3, max_length=20)
    email: str = Field(..., regex=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    created_at: datetime = Field(default_factory=datetime.utcnow)
    tags: Optional[List[str]] = Field(default_factory=list)
    
    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'Username must be alphanumeric'
        return v

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat()}
        schema_extra = {
            "example": {
                "user_id": 1,
                "username": "john_doe",
                "email": "john@example.com"
            }
        }
```

## Installation

```bash
pip install pydantic[email,dotenv] # Core dependencies
pip install fastapi uvicorn        # For API integration
pip install sqlalchemy            # For ORM patterns
```

## Usage Patterns

**Nested Models**: Complex data structures with validation cascading  
**Custom Validators**: Business logic validation with clear error messages  
**Serialization**: Flexible JSON/dict output with custom encoders  
**Configuration**: Type-safe application settings management  
**API Integration**: Request/response models for web frameworks

## Testing

```bash
pytest tests/ -v --cov=core --cov=patterns
```

---

**Author**: [@Void-Anvesha](https://github.com/Void-Anvesha) | **License**: MIT
