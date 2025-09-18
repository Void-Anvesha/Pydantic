# Pydantic

A comprehensive collection of Pydantic examples, utilities, and learning resources.

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pydantic](https://img.shields.io/badge/pydantic-2.0+-green.svg)](https://pydantic.dev/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 🚀 Overview

This repository contains practical examples, utilities, and learning materials for working with Pydantic - the most widely used data validation library for Python. Whether you're just starting with Pydantic or looking for advanced patterns, this repository has something for you.

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Examples](#examples)
- [Project Structure](#project-structure)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- 📚 **Comprehensive Examples**: From basic models to advanced validation patterns
- 🛠️ **Utility Functions**: Helper functions for common Pydantic use cases
- 🎯 **Real-world Scenarios**: Practical implementations for API validation, configuration management, and data processing
- 📖 **Learning Resources**: Step-by-step tutorials and best practices
- 🔧 **Custom Validators**: Collection of reusable custom validation functions
- 🌐 **Integration Examples**: Pydantic with FastAPI, Django, SQLAlchemy, and more

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- pip or conda package manager

### Install Dependencies

```bash
# Clone the repository
git clone https://github.com/Void-Anvesha/Pydantic.git
cd Pydantic

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Core Dependencies

```bash
pip install pydantic>=2.0.0
pip install pydantic[email]  # For email validation
pip install pydantic[dotenv]  # For .env file support
```

## 🚀 Quick Start

Here's a simple example to get you started:

```python
from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: Optional[int] = None
    created_at: datetime = datetime.now()
    
    @validator('age')
    def validate_age(cls, v):
        if v is not None and v < 0:
            raise ValueError('Age must be positive')
        return v

# Usage
user_data = {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
}

user = User(**user_data)
print(user.json())
```

## 📁 Project Structure

```
Pydantic/
├── examples/
│   ├── basic/
│   │   ├── simple_models.py
│   │   ├── validation_examples.py
│   │   └── type_annotations.py
│   ├── advanced/
│   │   ├── custom_validators.py
│   │   ├── nested_models.py
│   │   ├── configuration.py
│   │   └── serialization.py
│   └── integrations/
│       ├── fastapi_example.py
│       ├── sqlalchemy_example.py
│       └── dataclass_example.py
├── utils/
│   ├── validators.py
│   ├── serializers.py
│   └── helpers.py
├── tutorials/
│   ├── 01_getting_started.md
│   ├── 02_validation_basics.md
│   ├── 03_advanced_features.md
│   └── 04_best_practices.md
├── tests/
│   ├── test_examples.py
│   ├── test_utils.py
│   └── conftest.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

## 📚 Examples

### Basic Model Creation

```python
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
    in_stock: bool = True
    
product = Product(name="Laptop", price=999.99)
```

### Data Validation

```python
from pydantic import BaseModel, validator

class Person(BaseModel):
    name: str
    age: int
    
    @validator('age')
    def age_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Age must be positive')
        return v
```

### Nested Models

```python
from pydantic import BaseModel
from typing import List

class Address(BaseModel):
    street: str
    city: str
    country: str

class User(BaseModel):
    name: str
    addresses: List[Address]
```

## 🧪 Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=.

# Run specific test file
pytest tests/test_examples.py
```

## 📖 Documentation

### Key Concepts

- **Models**: Classes that inherit from `BaseModel`
- **Validators**: Functions that validate and transform data
- **Serializers**: Methods to export data in different formats
- **Configuration**: Settings to customize model behavior

### Useful Resources

- [Official Pydantic Documentation](https://docs.pydantic.dev/)
- [Pydantic GitHub Repository](https://github.com/pydantic/pydantic)
- [FastAPI + Pydantic Guide](https://fastapi.tiangolo.com/)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Guidelines

- Follow PEP 8 style guidelines
- Add tests for new functionality
- Update documentation as needed
- Ensure all tests pass

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♀️ Author

**Anvesha** - [@Void-Anvesha](https://github.com/Void-Anvesha)

## 🌟 Acknowledgments

- Thanks to the Pydantic team for creating such an amazing library
- Inspired by the Python community's dedication to type safety and data validation
- Special thanks to all contributors and users of this repository

## 📞 Support

If you have any questions or need help, please:

- Open an issue on GitHub
- Check the [discussions](https://github.com/Void-Anvesha/Pydantic/discussions) page
- Refer to the official Pydantic documentation

---

⭐ **Star this repository if you find it helpful!** ⭐
