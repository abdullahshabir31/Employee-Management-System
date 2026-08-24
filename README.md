# 👨‍💼 Employee Management System

A full-stack Employee Management System built with **React, FastAPI, PostgreSQL, SQLAlchemy, and Alembic**.

The project is designed to manage employees, departments, projects, authentication, and employee-project relationships while providing practical experience with complete full-stack application development.

---

## 📖 About

The Employee Management System provides a centralized platform for managing company employees and organizational data.

The application consists of three main parts:

- **Frontend** — React + Vite
- **Backend** — Python + FastAPI
- **Database** — PostgreSQL

The React frontend communicates with the FastAPI backend through REST APIs, while the backend communicates with PostgreSQL using SQLAlchemy ORM.

Alembic is used to manage database migrations.

---

## 🛠️ Tech Stack

### Frontend

- React
- JavaScript
- JSX
- Vite
- React Router
- ESLint
- CSS

### Backend

- Python
- FastAPI
- Uvicorn
- Pydantic
- SQLAlchemy
- Alembic
- python-dotenv
- JWT Authentication
- Password Hashing

### Database

- PostgreSQL

### Development Tools

- Git
- GitHub
- VS Code
- Swagger UI
- ReDoc

---

## ✨ Features

### 🔐 Authentication

- User registration
- User login
- User logout
- JWT authentication
- Password hashing
- Protected routes
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
- View department employees

### 📁 Project Management

- Create projects
- View projects
- View project details
- Update projects
- Delete projects
- Assign employees to projects
- Remove employees from projects
- View employees working on projects

### 🔗 Database Relationships

The application uses relational database concepts including:

- Primary Keys
- Foreign Keys
- One-to-Many Relationships
- Many-to-Many Relationships

### 🔍 Search & Filtering

Employees can be searched and filtered using:

- Employee name
- Email
- Department
- Status

---

## 🏗️ Application Architecture

```text
                    USER
                      │
                      ▼
               React Frontend
                      │
                      │ HTTP / REST API
                      ▼
               FastAPI Backend
                      │
                      ▼
                SQLAlchemy ORM
                      │
                      ▼
                PostgreSQL
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
Authentication
      ↓
SQLAlchemy ORM
      ↓
PostgreSQL Database
      ↓
Database Result
      ↓
FastAPI Response
      ↓
React Frontend
      ↓
Updated UI
```

---

## 🗄️ Database Structure

The application will contain the following main tables:

- Users
- Employees
- Departments
- Projects
- Employee Projects

### Department → Employees

One department can have multiple employees.

```text
Department
    │
    │ 1
    │
    │ many
    ▼
Employees
```

### Employees ↔ Projects

An employee can work on multiple projects, and a project can have multiple employees.

```text
Employees
    │
    ▼
Employee Projects
    ▲
    │
Projects
```

The `employee_projects` table manages the many-to-many relationship between employees and projects.

---

## 🔐 Authentication Flow

The application uses JWT-based authentication.

```text
User
  ↓
Register / Login
  ↓
FastAPI
  ↓
Validate Credentials
  ↓
Hash / Verify Password
  ↓
Generate JWT Token
  ↓
React Frontend
  ↓
Protected API Requests
```

Passwords are securely hashed before being stored in the database.

Sensitive configuration such as database credentials and secret keys is stored using environment variables.

---

## 📂 Project Structure

```text
Employee Management System/
│
├── backend/
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── employees.py
│   │   ├── departments.py
│   │   └── projects.py
│   │
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── requirements.txt
│   ├── .env
│   ├── .gitignore
│   └── README.md
│
├── frontend/
│   │
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── layouts/
│   │   ├── services/
│   │   ├── context/
│   │   ├── hooks/
│   │   ├── utils/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   │
│   ├── eslint.config.js
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   └── README.md
│
├── .gitignore
└── README.md
```

---

## 📁 Backend

The backend is responsible for:

- REST API development
- Authentication
- Authorization
- Business logic
- Data validation
- CRUD operations
- Database operations
- Database relationships
- JWT authentication
- Error handling

Backend technologies:

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic

Detailed backend documentation is available inside:

`backend/README.md`

---

## ⚛️ Frontend

The frontend is responsible for:

- User interface
- Navigation
- Authentication pages
- Dashboard
- Employee management
- Department management
- Project management
- Forms
- Tables
- Search
- Filtering
- API communication
- Responsive design

Frontend technologies:

- React
- JavaScript
- Vite
- React Router
- ESLint
- CSS

Detailed frontend documentation is available inside:

`frontend/README.md`

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

## ⚙️ Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Create a Python virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file inside the backend directory:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/employee_management
SECRET_KEY=your-secret-key
```

Run database migrations:

```bash
alembic upgrade head
```

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

Backend server:

`http://127.0.0.1:8000`

---

## ⚛️ Frontend Setup

Navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Frontend server:

`http://localhost:5173`

---

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

`http://127.0.0.1:8000/docs`

### ReDoc

`http://127.0.0.1:8000/redoc`

Swagger UI can be used to test backend API endpoints during development.

---

## 🔄 Database Migrations

Alembic is used to manage PostgreSQL database schema changes.

Migration workflow:

```text
SQLAlchemy Models
      ↓
Alembic Migration
      ↓
PostgreSQL Database
```

Create a migration:

```bash
alembic revision --autogenerate -m "create initial tables"
```

Apply migrations:

```bash
alembic upgrade head
```

Rollback the latest migration:

```bash
alembic downgrade -1
```

---

## 🔒 Security

Sensitive information must never be committed to GitHub.

The following information should remain inside environment variables:

- Database password
- Database credentials
- JWT secret key
- Private API keys
- Other sensitive configuration

The `.env` file must be included in `.gitignore`.

Passwords are hashed before being stored in the database.

Protected API routes require valid JWT authentication.

The frontend never connects directly to PostgreSQL.

Correct architecture:

```text
React
  ↓
FastAPI
  ↓
SQLAlchemy
  ↓
PostgreSQL
```

---

## 🧪 Testing

The project will include testing for:

- User registration
- User login
- JWT authentication
- Employee CRUD
- Department CRUD
- Project CRUD
- Database relationships
- Protected routes
- API validation
- Error handling
- Frontend API integration

---

## 🏗️ Development Roadmap

### Phase 1 — Project Setup

- Create project structure
- Initialize Git repository
- Create GitHub repository
- Create backend
- Create frontend
- Configure Python virtual environment
- Configure React + Vite
- Configure ESLint

### Phase 2 — PostgreSQL Setup

- Create PostgreSQL database
- Configure database URL
- Connect FastAPI with PostgreSQL

### Phase 3 — SQLAlchemy

- Create database engine
- Create database session
- Create SQLAlchemy Base
- Configure database dependency
- Create ORM models

### Phase 4 — Alembic

- Initialize Alembic
- Configure Alembic
- Connect Alembic with SQLAlchemy
- Create migrations
- Apply migrations

### Phase 5 — Database Models

- User model
- Employee model
- Department model
- Project model
- EmployeeProject model
- Primary keys
- Foreign keys
- Relationships

### Phase 6 — Pydantic Schemas

- Request schemas
- Response schemas
- Data validation
- Employee schemas
- Department schemas
- Project schemas
- User schemas

### Phase 7 — Authentication

- User registration
- Password hashing
- User login
- JWT generation
- JWT verification
- Protected routes
- Current user

### Phase 8 — Employee Management

- Create employee
- Get employees
- Get employee by ID
- Update employee
- Delete employee
- Search employees
- Filter employees

### Phase 9 — Department Management

- Create department
- Get departments
- Get department by ID
- Update department
- Delete department
- Get department employees

### Phase 10 — Project Management

- Create project
- Get projects
- Get project by ID
- Update project
- Delete project
- Assign employees
- Remove employees

### Phase 11 — Frontend

- Login page
- Register page
- Dashboard
- Employees page
- Departments page
- Projects page
- Employee details
- Forms
- Tables
- Protected routes

### Phase 12 — Integration

- Connect React with FastAPI
- Authentication integration
- Employee API integration
- Department API integration
- Project API integration
- Loading states
- Error handling
- Form validation

### Phase 13 — Testing

- Test authentication
- Test CRUD APIs
- Test database relationships
- Test protected routes
- Test frontend
- Fix bugs

### Phase 14 — Deployment

- Prepare production configuration
- Deploy frontend
- Deploy backend
- Configure PostgreSQL
- Configure environment variables
- Configure CORS
- Connect frontend with backend

---

## 🎯 Learning Objectives

This project is designed to provide practical experience with:

- React
- JavaScript
- FastAPI
- Python
- PostgreSQL
- SQLAlchemy
- Alembic
- REST APIs
- JWT Authentication
- Password Hashing
- CRUD Operations
- Primary Keys
- Foreign Keys
- One-to-Many Relationships
- Many-to-Many Relationships
- Pydantic Validation
- API Error Handling
- React API Integration
- Git
- GitHub
- Full-Stack Architecture

---

## 🔗 Full-Stack Integration

The final application will follow this architecture:

```text
React Frontend
      ↓
REST API
      ↓
FastAPI Backend
      ↓
Pydantic Validation
      ↓
SQLAlchemy ORM
      ↓
PostgreSQL Database
```

The frontend and backend are maintained separately inside the same project repository.

---

## 🚀 Deployment Architecture

```text
React Frontend
      ↓
Frontend Hosting
      ↓
FastAPI Backend
      ↓
Backend Hosting
      ↓
PostgreSQL Database
```

---

## 📌 Project Status

🚧 **Currently under development**

The project is being developed step-by-step, starting with the backend and database and then integrating the React frontend.

Current development order:

```text
Project Setup
     ↓
PostgreSQL Setup
     ↓
SQLAlchemy
     ↓
Alembic
     ↓
Database Models
     ↓
FastAPI APIs
     ↓
Authentication
     ↓
React Frontend
     ↓
Frontend + Backend Integration
     ↓
Testing
     ↓
Deployment
```

---

## 👨‍💻 Author

### Abdullah Shabir

Full-Stack Developer and Computer Science Student.

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

**Employee Management System — Full-Stack Employee & Project Management Platform**
