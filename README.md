# Student Course Management CLI

## Overview

This project is a **Command Line Interface (CLI)** application that simulates a simple **student course management system**. The system allows administrators to manage courses and students, while students can register for available courses.

The project is built using **Python** and follows **Object-Oriented Programming (OOP)** principles. Data persistence is implemented using **JSON files**, allowing information to be saved between program runs.

---

## Features

### Admin Capabilities

* Add new courses
* Add new students
* View all available courses
* View students registered for a specific course

### Student Capabilities

* Login to the system
* View available courses
* Register for courses
* Prevent duplicate course registration

---

## Technologies Used

* Python
* JSON (for data storage)
* CLI interface

---

## Project Structure

```
project/
│
├── main.py
│   Contains class definitions for the system models:
│   User, Admin, Student, Course, Registration
│
├── cli.py
│   Implements the CLI interface and system logic
│
├── users.json
│   Stores user data (admins and students)
│
├── courses.json
│   Stores available courses
│
├── registrations.json
│   Stores student course registrations
│
└── README.md
│   Project documentation
```

---

## Object Model

### User

Represents a system user.

Attributes:

* user_id
* username
* password
* role
* email

### Admin

Inherits from **User** and manages courses and students.

### Student

Inherits from **User** and can register for courses.

### Course

Represents a course offered in the system.

Attributes:

* course_id
* title
* description
* instructor_name
* created_at

### Registration

Represents a student's enrollment in a course.

Attributes:

* reg_id
* user_id
* course_id
* status
* registered_at

---

## Data Persistence

The system uses **JSON files** to store data:

* `users.json`
* `courses.json`
* `registrations.json`

These files allow the program to **save data between executions**.

---

## How to Run the Application

Run the CLI application with:

```
python3 CLI.py
```

---

## Example Workflow

1. Administrator logs into the system.
2. Administrator adds courses or students.
3. Students log into the system.
4. Students register for available courses.
5. Administrators can view registered students for each course.

---


## Contributors
muhudin and sharif
Group 9
