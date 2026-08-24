# 👨‍💼 Employee Management System — Backend

The **Employee Management System** is a full-stack web application designed to manage employees, departments, projects, authentication, and employee-project relationships.

This repository contains the backend API, built with **Python, FastAPI, PostgreSQL, SQLAlchemy, Alembic, and Pydantic**.

The backend provides RESTful APIs that will be consumed by the React frontend.

---

## 📖 About

The Employee Management System is designed to provide a centralized platform for managing company employees and organizational data.

The backend is responsible for:

- User authentication
- Employee management
- Department management
- Project management
- Employee-project assignments
- CRUD operations
- Database relationships
- Data validation
- Authentication and authorization
- REST API development
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

### Authentication

- JWT Authentication
- Password Hashing

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
- JWT-based authentication
- Protected API routes
- Password hashing
- Current authenticated user

### 👨‍💼 Employee Management

- Add employees
- View employees
- View employee details
- Update employee information
- Delete employees
- Search employees
- Filter employees
- Manage employee status
- Assign employees to departments

### 🏢 Department Management

- Create departments
- View departments
- View department details
- Update departments
- Delete departments
- Assign employees to departments

### 📁 Project Management

- Create projects
- View projects
- View project details
- Update projects
- Delete projects
- Assign employees to projects
- View employees working on projects

### 🔗 Database Relationships

The backend implements relational database concepts including:

- Primary Keys
- Foreign Keys
- One-to-Many Relationships
- Many-to-Many Relationships

### 🔍 Search & Filtering

Employees can be searched and filtered using API query parameters such as:

- Employee name
- Department
- Status
- Email

---

## 🗄️ Database

The application uses **PostgreSQL** as its relational database.

Planned database tables:

- Users
- Employees
- Departments
- Projects
- Employee Projects

### Department → Employees

One department can have multiple employees.

Department → Employees  
1 Department → Many Employees

### Employees ↔ Projects

An employee can work on multiple projects, and a project can have multiple employees.

Employees ↔ Employee Projects ↔ Projects

The `employee_projects` table manages the many-to-many relationship between employees and projects.

---

## 🔐 Authentication & Security

The backend uses **JWT-based authentication** to protect authenticated API routes.

Authentication flow:

User → Register/Login → FastAPI → Validate Credentials → Generate JWT Token → React Frontend → Protected API

Passwords will be securely hashed before being stored in the database.

Sensitive configuration such as database credentials and secret keys will be stored using environment variables.

---

## 🔌 API Endpoints

### Authentication

- `POST /auth/register`
- `POST /auth/login`
- `GET /auth/me`

### Employees

- `GET /employees`
- `GET /employees/{id}`
- `POST /employees`
- `PUT /employees/{id}`
- `DELETE /employees/{id}`

### Departments

- `GET /departments`
- `GET /departments/{id}`
- `POST /departments`
- `PUT /departments/{id}`
- `DELETE /departments/{id}`

### Projects

- `GET /projects`
- `GET /projects/{id}`
- `POST /projects`
- `PUT /projects/{id}`
- `DELETE /projects/{id}`

---

## 📂 Project Structure

backend/

├── routers/  
│ ├── **init**.py  
│ ├── auth.py  
│ ├── employees.py  
│ ├── departments.py  
│ └── projects.py  
│  
├── main.py  
├── database.py  
├── models.py  
├── schemas.py  
├── .env  
├── .gitignore  
├── requirements.txt  
└── README.md

---

## 📄 Backend Files

### main.py

Main entry point of the FastAPI application.

Responsibilities:

- Create FastAPI application
- Register routers
- Configure API
- Provide application entry point

### database.py

Responsible for connecting the FastAPI application with PostgreSQL through SQLAlchemy.

Responsibilities:

- Database engine
- Database session
- SQLAlchemy Base
- Database dependency

### models.py

Contains SQLAlchemy ORM models that represent database tables.

Planned models:

- User
- Employee
- Department
- Project
- EmployeeProject

### schemas.py

Contains Pydantic schemas used for request and response validation.

Responsibilities:

- Validate incoming data
- Define API request structures
- Define API response structures
- Validate employee data
- Validate department data
- Validate project data

### routers/auth.py

Contains authentication-related API endpoints.

Responsibilities:

- Registration
- Login
- JWT generation
- Current user
- Authentication validation

### routers/employees.py

Contains employee-related API endpoints.

Responsibilities:

- Employee CRUD
- Employee search
- Employee filtering
- Employee details

### routers/departments.py

Contains department-related API endpoints.

Responsibilities:

- Department CRUD
- Department employees
- Department management

### routers/projects.py

Contains project-related API endpoints.

Responsibilities:

- Project CRUD
- Employee-project assignments
- Project employee management

---

## 🔄 Backend Architecture

React Frontend  
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

---

## 🔄 Request Flow

React Frontend  
↓  
HTTP Request  
↓  
FastAPI Router  
↓  
Pydantic Validation  
↓  
Authentication  
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

---

## 🔄 Database Migration

**Alembic** will be used to manage database schema changes.

Migration workflow:

SQLAlchemy Models → Alembic Migration → PostgreSQL Database

Common commands:

- `alembic revision --autogenerate -m "create initial tables"`
- `alembic upgrade head`

---

## ⚙️ Local Development

### 1. Clone Repository

`git clone YOUR_GITHUB_REPOSITORY_URL`

`cd employee-management-system`

`cd backend`

### 2. Create Virtual Environment

`python -m venv venv`

### 3. Activate Virtual Environment

Windows PowerShell:

`.\venv\Scripts\Activate.ps1`

### 4. Install Dependencies

`pip install -r requirements.txt`

### 5. Configure Environment Variables

Create a `.env` file in the backend directory.

Required variables:

- `DATABASE_URL`
- `SECRET_KEY`

Example:

`DATABASE_URL=postgresql://username:password@localhost:5432/employee_management`

`SECRET_KEY=your-secret-key`

Never commit the `.env` file to GitHub.

### 6. Run Database Migrations

`alembic upgrade head`

### 7. Start Development Server

`uvicorn main:app --reload`

The backend will run at:

`http://127.0.0.1:8000`

---

## 📚 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

`http://127.0.0.1:8000/docs`

### ReDoc

`http://127.0.0.1:8000/redoc`

Swagger UI can be used to test API endpoints during development.

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

Passwords will be hashed before being stored in the database.

Protected routes will require valid JWT authentication.

---

## 🏗️ Development Roadmap

### Phase 1 — Project Setup

- Create project structure
- Initialize Git repository
- Create GitHub repository
- Configure virtual environment

### Phase 2 — PostgreSQL Setup

- Create PostgreSQL database
- Configure database URL
- Connect FastAPI with PostgreSQL

### Phase 3 — SQLAlchemy Configuration

- Create engine
- Create session
- Create Base
- Configure database dependency

### Phase 4 — Alembic Configuration

- Initialize Alembic
- Connect Alembic with SQLAlchemy
- Create migrations
- Apply migrations

### Phase 5 — Database Models

- Create User model
- Create Department model
- Create Employee model
- Create Project model
- Create EmployeeProject model
- Configure relationships

### Phase 6 — Pydantic Schemas

- Create request schemas
- Create response schemas
- Add validation
- Configure model serialization

### Phase 7 — Authentication & JWT

- User registration
- Password hashing
- User login
- JWT generation
- JWT verification
- Protected routes

### Phase 8 — Employee CRUD

- Create employee
- Get employees
- Get employee by ID
- Update employee
- Delete employee

### Phase 9 — Department CRUD

- Create department
- Get departments
- Get department by ID
- Update department
- Delete department

### Phase 10 — Project CRUD

- Create project
- Get projects
- Get project by ID
- Update project
- Delete project

### Phase 11 — Database Relationships

- Department and Employee relationship
- Employee and Project relationship
- EmployeeProject association table
- Relationship queries

### Phase 12 — Search & Filtering

- Search employees
- Filter by department
- Filter by status
- Filter by other fields

### Phase 13 — API Testing

- Test APIs with Swagger
- Test successful requests
- Test validation errors
- Test authentication
- Test database operations

### Phase 14 — Error Handling

- HTTP exceptions
- Validation errors
- Authentication errors
- Database errors
- Proper API responses

### Phase 15 — React Frontend Integration

- Connect React with FastAPI
- Authentication integration
- Employee API integration
- Department API integration
- Project API integration

### Phase 16 — Deployment

- Prepare production configuration
- Deploy backend
- Configure production database
- Connect frontend with deployed backend

---

## 🎯 Project Goals

The main goal of this project is to build a complete real-world full-stack application while understanding how the frontend, backend, API, and database work together.

The project will provide practical experience with:

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
- Database Relationships
- API Validation
- Error Handling
- React API Integration
- Git & GitHub
- Full-Stack Architecture

---

## 🔗 Frontend Integration

The backend will be connected with a React frontend.

React Frontend  
↓  
REST API  
↓  
FastAPI Backend  
↓  
SQLAlchemy  
↓  
PostgreSQL Database

The React application will communicate with the FastAPI backend through HTTP requests.

---

## 🚀 Future Deployment

The application is planned to use separate services for the frontend, backend, and database.

React Frontend  
↓  
Frontend Hosting  
↓  
FastAPI Backend  
↓  
Backend Hosting  
↓  
PostgreSQL Database

---

## 👨‍💻 Author

### Abdullah Shabir

Full-Stack Developer and Computer Science Student.

---

## ⭐ Project Status

🚧 **Currently under development**

The backend is being developed step-by-step while implementing and learning real-world full-stack development concepts.

---

**Employee Management System — Full-Stack Employee & Project Management Platform**
