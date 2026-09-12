# Student Eligibility Evaluation System

A clean, lightweight Python implementation demonstrating **Object-Oriented Programming (OOP)** principles, abstract base classes, and code extensibility.

## Features
- **Abstract Base Class Design:** Centralized evaluation rules ensuring all student variants share predictable behavior.
- **Configurable Thresholds:** Easily adjust or override GPA, attendance, and subject grade benchmarks for different tiers of students (e.g., Regular vs. Scholarship).
- **Comprehensive Grade Checks:** Evaluates multiple subjects dynamically using Python's built-in `all()` iteration.
- **Type Hinting:** Fully type-hinted methods for better IDE autocompletion and static analysis safety.

## How to Run

Run the main execution script:
```bash
python student_eligibility.py
```

Run the automated test suite:
```bash
python -m unittest test_student.py
```
