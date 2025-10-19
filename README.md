# Library Management System - OOP & SOLID Assignment

## Overview
This is a **Python-based Library Management System** demonstrating **Object-Oriented Programming (OOP)** and **SOLID principles**.  
It also includes **unit testing** and a **CI/CD workflow** using **GitHub Actions**.

---

## Features

### 1. OOP Implementation
- **Book** is the base class.  
- **EBook** and **PrintedBook** inherit from `Book`.  
- **Polymorphism:** Both override `calculate_late_fee()`.  
- **Encapsulation:** Book details are private (`title`, `author`, `price`).  

### 2. SOLID Principles
- **Single Responsibility Principle:** Each class has one responsibility.  
- **Open/Closed Principle:** Subclasses extend `Book` without modifying it.  
- **Liskov Substitution Principle:** `EBook` and `PrintedBook` can replace `Book`.  
- **Interface Segregation:** Payment interface for different methods.  
- **Dependency Inversion:** `PaymentProcessor` depends on the `Payment` interface, not concrete classes.  

### 3. Payment System
Supports multiple payment methods:  
- PayPal  
- Credit Card  

### 4. Version Control & CI/CD
- Fully tracked using **Git**.  
- GitHub Actions workflow runs unit tests automatically on each push.  

---

## Installation & Running

### Prerequisites
- Python 3.10 or higher
- Git

### Clone the Repository
```bash
git clone https://github.com/rameshdhakal580-a11y/LibraryManagementSystem_OOP_SOLID.git
cd LibraryManagementSystem_OOP_SOLID
Run the Project
python main.py        # Windows
python3 main.py       # macOS/Linux
Run Unit Tests
python -m unittest discover -s . -p "test_*.py"    # Windows
python3 -m unittest discover -s . -p "test_*.py"   # macOS/Linux

Repository Structure
LibraryManagementSystem_OOP_SOLID/
├─ book.py
├─ ebook.py
├─ printed_book.py
├─ payment.py
├─ main.py
├─ test_library.py
├─ README.md
├─ .gitignore
└─ .github/workflows/python-app.yml

Author
Ramesh Dhakal
GitHub: rameshdhakal580-a11y
