# 👨‍💼 Employee Management System — Backend

The **Employee Management System** is a full-stack web application designed to manage employees, departments, projects, authentication, and employee-project relationships.

This repository contains the backend REST API built with **Python, FastAPI, PostgreSQL, SQLAlchemy, Alembic, Pydantic, and JWT authentication**.

The backend provides APIs that can be consumed by the React frontend.

---

## 📖 About

The Employee Management System provides a centralized backend for managing company employees and organizational data.

The backend is responsible for:

- User registration and login
- JWT authentication
- Protected API routes
- Employee management
- Department management
- Project management
- Employee-project assignments
- CRUD operations
- Database relationships
- Request and response validation
- PostgreSQL database management

---

## 🛠️ Tech Stack

### Backend

- Python
- FastAPI
- Uvicorn
- Pydantic
- python-dotenv

### Database

- PostgreSQL
- SQLAlchemy ORM
- Alembic
- psycopg2

### Authentication & Security

- JWT Authentication
- Password Hashing
- Passlib
- bcrypt
- python-jose

### API Documentation

- Swagger UI
- ReDoc

### Frontend Integration

- React
- REST APIs
- HTTP Requests

---

## ✨ Features

### 👤 Authentication

- User registration
- User login
- JWT access tokens
- Protected API routes
- Password hashing
- Current authenticated user
- JWT token verification

### 👨‍💼 Employee Management

- Create employees
- View all employees
- View employee by ID
- Update employees
- Delete employees
- Assign employees to departments

### 🏢 Department Management

- Create departments
- View all departments
- View department by ID
- Update departments
- Delete departments
- Department-employee relationship

### 📁 Project Management

- Create projects
- View all projects
- View project by ID
- Update projects
- Delete projects
- Assign employees to projects
- Manage employee-project relationships

### 🔗 Database Relationships

The backend implements relational database concepts including:

- Primary Keys
- Foreign Keys
- One-to-Many Relationships
- Many-to-Many Relationships
- Association tables

Department → Employees

One department can have multiple employees.

Employees ↔ Employee Projects ↔ Projects

The `employee_projects` table manages the many-to-many relationship between employees and projects.

---

## 🗄️ Database

The application uses **PostgreSQL** as its relational database.

### Database Tables

- Users
- Departments
- Employees
- Projects
- Employee Projects

### Department → Employees

A department can have multiple employees.

```text
Department
    │
    └── Employees
            ├── Employee 1
            ├── Employee 2
            └── Employee 3
```

### Employees ↔ Projects

An employee can work on multiple projects, and a project can have multiple employees.

```text
Employees
    │
    ├── Employee Projects
    │
    └── Projects
```

The `employee_projects` association table manages this many-to-many relationship.

---

## 🔐 Authentication & Security

The backend uses **JWT-based authentication** to protect authenticated API routes.

### Authentication Flow

```text
User
  ↓
Register / Login
  ↓
FastAPI
  ↓
Validate Credentials
  ↓
Generate JWT Access Token
  ↓
Client / React Frontend
  ↓
Protected API Request
  ↓
JWT Verification
  ↓
FastAPI Protected Route
```

Passwords are hashed before being stored in the database.

Sensitive configuration such as database credentials and the JWT secret key is stored using environment variables.

---

## 🔌 API Endpoints

### Authentication

| Method | Endpoint         | Description                    |
| ------ | ---------------- | ------------------------------ |
| POST   | `/auth/register` | Register a new user            |
| POST   | `/auth/login`    | Login and receive JWT token    |
| GET    | `/auth/me`       | Get current authenticated user |

### Employees

| Method | Endpoint                   | Description        |
| ------ | -------------------------- | ------------------ |
| POST   | `/employees`               | Create employee    |
| GET    | `/employees`               | Get all employees  |
| GET    | `/employees/{employee_id}` | Get employee by ID |
| PUT    | `/employees/{employee_id}` | Update employee    |
| DELETE | `/employees/{employee_id}` | Delete employee    |

### Departments

| Method | Endpoint                       | Description          |
| ------ | ------------------------------ | -------------------- |
| POST   | `/departments`                 | Create department    |
| GET    | `/departments`                 | Get all departments  |
| GET    | `/departments/{department_id}` | Get department by ID |
| PUT    | `/departments/{department_id}` | Update department    |
| DELETE | `/departments/{department_id}` | Delete department    |

### Projects

| Method | Endpoint                 | Description       |
| ------ | ------------------------ | ----------------- |
| POST   | `/projects`              | Create project    |
| GET    | `/projects`              | Get all projects  |
| GET    | `/projects/{project_id}` | Get project by ID |
| PUT    | `/projects/{project_id}` | Update project    |
| DELETE | `/projects/{project_id}` | Delete project    |

### Employee Projects

The employee-project endpoints manage assignments between employees and projects.

---

## 📂 Project Structure

```text
Backend/
│
├── alembic/
│   ├── versions/
│   │   └── 7428db9f164c_create_initial_database_tables.py
│   ├── env.py
│   └── script.py.mako
│
├── routers/
│   ├── __init__.py
│   ├── auth.py
│   ├── departments.py
│   ├── employees.py
│   ├── employee_projects.py
│   └── projects.py
│
├── .env
├── .gitignore
├── alembic.ini
├── database.py
├── main.py
├── models.py
├── README.md
├── requirements.txt
├── schemas.py
└── security.py
```

---

## 📄 Backend Files

### `main.py`

Main entry point of the FastAPI application.

Responsibilities:

- Create FastAPI application
- Register API routers
- Configure application
- Provide application entry point

### `database.py`

Responsible for connecting the FastAPI application with PostgreSQL through SQLAlchemy.

Responsibilities:

- Database engine
- Database session
- SQLAlchemy Base
- Database dependency

### `models.py`

Contains SQLAlchemy ORM models representing the database tables.

Models include:

- User
- Employee
- Department
- Project
- EmployeeProject

### `schemas.py`

Contains Pydantic schemas used for request and response validation.

Responsibilities:

- Validate incoming data
- Define API request structures
- Define API response structures
- Validate user data
- Validate employee data
- Validate department data
- Validate project data
- Configure model serialization

### `security.py`

Contains authentication and security-related functionality.

Responsibilities:

- Password hashing
- Password verification
- JWT creation
- JWT configuration
- Secret key management
- Token expiration

### `routers/auth.py`

Contains authentication-related API endpoints.

Responsibilities:

- User registration
- User login
- JWT generation
- JWT verification
- Current authenticated user

### `routers/employees.py`

Contains employee-related API endpoints.

Responsibilities:

- Employee CRUD operations
- Employee management
- Department assignment

### `routers/departments.py`

Contains department-related API endpoints.

Responsibilities:

- Department CRUD operations
- Department management
- Employee relationships

### `routers/projects.py`

Contains project-related API endpoints.

Responsibilities:

- Project CRUD operations
- Project management

### `routers/employee_projects.py`

Contains employee-project assignment endpoints.

Responsibilities:

- Assign employees to projects
- Manage employee-project relationships
- Remove employee-project assignments

---

## 🔄 Backend Architecture

```text
React Frontend
      ↓
   REST API
      ↓
FastAPI Backend
      ↓
Pydantic Validation
      ↓
Authentication
      ↓
SQLAlchemy ORM
      ↓
PostgreSQL Database
```

---

## 🔄 Request Flow

```text
React Frontend
      ↓
HTTP Request
      ↓
FastAPI Router
      ↓
Pydantic Validation
      ↓
JWT Authentication
      ↓
SQLAlchemy
      ↓
PostgreSQL
      ↓
Database Result
      ↓
FastAPI Response
      ↓
React Frontend
```

---

## 🔄 Database Migration

**Alembic** is used to manage database schema changes.

Migration workflow:

```text
SQLAlchemy Models
       ↓
Alembic Migration
       ↓
PostgreSQL Database
```

### Common Alembic Commands

Create a migration:

```bash
alembic revision --autogenerate -m "migration message"
```

Apply migrations:

```bash
alembic upgrade head
```

---

## ⚙️ Local Development

### 1. Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd employee-management-system
cd Backend
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the backend directory.

Required environment variables:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/employee_management
SECRET_KEY=your-secret-key
```

Never commit the `.env` file to GitHub.

### 6. Run Database Migrations

```bash
alembic upgrade head
```

### 7. Start Development Server

```bash
uvicorn main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

Swagger UI can be used to interact with and test the API endpoints during development.

---

## 🔒 Security

Sensitive credentials are stored using environment variables.

The following information should never be committed to GitHub:

- Database password
- Database credentials
- JWT secret key
- Private API keys
- Environment configuration

The `.env` file is excluded from version control through `.gitignore`.

Passwords are hashed before being stored in the database.

Protected API routes require a valid JWT access token.

---

## 🎯 Project Goals

The main goal of this project is to build a practical full-stack application while understanding how the frontend, backend, API, authentication, and database work together.

This backend provides practical experience with:

- FastAPI
- REST APIs
- PostgreSQL
- SQLAlchemy ORM
- Alembic
- Pydantic
- JWT Authentication
- Password Hashing
- CRUD Operations
- Primary Keys
- Foreign Keys
- One-to-Many Relationships
- Many-to-Many Relationships
- API Validation
- React API Integration
- Git & GitHub
- Full-Stack Architecture

---

## 🔗 Frontend Integration

The backend is designed to be consumed by a React frontend.

```text
React Frontend
      ↓
    REST API
      ↓
FastAPI Backend
      ↓
   SQLAlchemy
      ↓
PostgreSQL Database
```

The React application communicates with the FastAPI backend through HTTP requests.

---

## 🚀 Project Status

✅ **Backend Core Development Completed**

The backend currently includes:

- PostgreSQL database integration
- SQLAlchemy ORM
- Alembic migrations
- User registration and login
- JWT authentication
- Protected API routes
- Employee CRUD
- Department CRUD
- Project CRUD
- Employee-project assignments
- Pydantic validation
- Swagger UI and ReDoc documentation

---

## 👨‍💻 Author

## Abdullah Shabir

### Connect With Me

- **GitHub:** https://github.com/abdullahshabir31
- **LinkedIn:** https://www.linkedin.com/in/abdullahshabir31/
- **Portfolio:** https://abdullah-myportfolio.vercel.app/

---

**Employee Management System — Full-Stack Employee & Project Management Platform**
