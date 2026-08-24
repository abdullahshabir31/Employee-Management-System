# 👨‍💼 Employee Management System — Frontend

The **Employee Management System** is a modern full-stack web application designed to manage employees, departments, projects, authentication, and employee-project relationships.

This repository contains the **frontend application**, built with **React, JavaScript, Vite, React Router, and ESLint**.

The frontend communicates with the **FastAPI backend** through REST APIs and provides a responsive user interface for managing the application.

---

## 🌐 Project

**Project Name:** Employee Management System

**Frontend:** React

**Backend:** FastAPI

**Database:** PostgreSQL

**ORM:** SQLAlchemy

**Migrations:** Alembic

**Authentication:** JWT

---

## 📖 About

The Employee Management System frontend provides a user-friendly interface for interacting with the FastAPI backend.

Authenticated users will be able to:

- Register an account
- Login securely
- Logout
- View dashboard
- Manage employees
- View employee details
- Add employees
- Update employees
- Delete employees
- Search employees
- Filter employees
- Manage departments
- Manage projects
- Assign employees to projects
- View employee-project relationships
- Access protected pages

The frontend is designed to work together with the FastAPI backend and PostgreSQL database.

---

## 🛠️ Tech Stack

### Frontend

- React
- JavaScript
- JSX
- Vite
- React Router
- ESLint

### Styling

- CSS
- Responsive Design

### Backend Integration

- FastAPI
- REST APIs
- HTTP Requests

### Database

- PostgreSQL

---

## ✨ Features

### 🔐 Authentication

- User registration
- User login
- JWT authentication
- Protected routes
- Authentication state management
- Logout functionality
- Current user information

### 📊 Dashboard

The dashboard will provide an overview of the employee management system.

Planned information includes:

- Total employees
- Total departments
- Total projects
- Active employees
- Project statistics
- Department statistics

### 👨‍💼 Employee Management

Users will be able to:

- View all employees
- Add new employees
- View employee details
- Update employee information
- Delete employees
- Search employees
- Filter employees
- View employee department
- View employee projects
- Manage employee status

### 🏢 Department Management

Users will be able to:

- View departments
- Add departments
- View department details
- Update departments
- Delete departments
- View department employees

### 📁 Project Management

Users will be able to:

- View projects
- Add projects
- View project details
- Update projects
- Delete projects
- Assign employees to projects
- Remove employees from projects
- View project employees

### 📱 Responsive Design

The frontend will be designed to work across:

- Desktop
- Laptop
- Tablet
- Mobile devices

---

## 🔗 Backend Integration

The React frontend communicates with the FastAPI backend using REST APIs.

Application architecture:

React Frontend
↓
HTTP Requests
↓
FastAPI Backend
↓
SQLAlchemy ORM
↓
PostgreSQL Database

The frontend will send requests to the backend for:

- Authentication
- Employees
- Departments
- Projects
- User information
- Search
- Filtering
- CRUD operations

---

## 📂 Project Structure

frontend/
│
├── public/
│
├── src/
│ ├── components/
│ │
│ ├── pages/
│ │ ├── Login.jsx
│ │ ├── Register.jsx
│ │ ├── Dashboard.jsx
│ │ ├── Employees.jsx
│ │ ├── EmployeeDetails.jsx
│ │ ├── Departments.jsx
│ │ └── Projects.jsx
│ │
│ ├── layouts/
│ │
│ ├── services/
│ │ └── api.js
│ │
│ ├── context/
│ │ └── AuthContext.jsx
│ │
│ ├── hooks/
│ │
│ ├── utils/
│ │
│ ├── App.jsx
│ ├── main.jsx
│ └── index.css
│
├── .gitignore
├── eslint.config.js
├── index.html
├── package.json
├── package-lock.json
├── vite.config.js
└── README.md

---

## 📄 Frontend Files

### App.jsx

Main React application component.

Responsibilities:

- Application routing
- Main application structure
- Connecting pages
- Connecting layouts
- Rendering application routes

### main.jsx

Entry point of the React application.

Responsibilities:

- Start React application
- Render App component
- Configure React providers

### index.css

Contains global CSS styles for the application.

Responsibilities:

- Global styles
- Base styles
- Typography
- Layout styles
- Responsive styles

### components/

Contains reusable React components.

Examples:

- Navbar
- Sidebar
- Button
- Input
- Modal
- Table
- Card
- Form
- Loading Spinner
- Error Message

Reusable components will help keep the application clean and maintainable.

### pages/

Contains the main pages of the application.

Planned pages:

- Login
- Register
- Dashboard
- Employees
- Employee Details
- Departments
- Projects

### layouts/

Contains reusable application layouts.

Planned layouts:

- Authentication Layout
- Dashboard Layout

### services/

Contains API-related functionality.

The main API service file will be:

`services/api.js`

It will handle communication between React and FastAPI.

### context/

Contains React Context providers.

The main context will be:

`AuthContext.jsx`

It will manage:

- Current user
- Login state
- Logout
- Authentication token
- User session

### hooks/

Contains reusable custom React hooks.

### utils/

Contains reusable helper functions and utility functions.

---

## 🔐 Authentication Flow

The frontend will communicate with the FastAPI authentication API.

Authentication flow:

User
↓
Register / Login
↓
React Frontend
↓
FastAPI Backend
↓
Validate Credentials
↓
Generate JWT Token
↓
React Frontend
↓
Store Authentication State
↓
Access Protected Pages

Protected pages will only be accessible to authenticated users.

---

## 🔌 API Integration

The frontend will consume REST APIs provided by the FastAPI backend.

### Authentication

POST /auth/register

POST /auth/login

GET /auth/me

### Employees

GET /employees

GET /employees/{id}

POST /employees

PUT /employees/{id}

DELETE /employees/{id}

### Departments

GET /departments

GET /departments/{id}

POST /departments

PUT /departments/{id}

DELETE /departments/{id}

### Projects

GET /projects

GET /projects/{id}

POST /projects

PUT /projects/{id}

DELETE /projects/{id}

---

## 🔄 Request Flow

When a user performs an action in the React application:

User
↓
React Component
↓
API Service
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
React
↓
Updated UI

---

## ⚙️ Local Development

### 1. Clone Repository

git clone YOUR_GITHUB_REPOSITORY_URL

cd employee-management-system

cd frontend

### 2. Install Dependencies

npm install

### 3. Start Development Server

npm run dev

The frontend will run at:

http://localhost:5173

---

## 🏗️ Production Build

To create a production build:

npm run build

To preview the production build locally:

npm run preview

---

## 🧹 Code Quality

ESLint is used to maintain code quality and identify potential problems in the React application.

Run ESLint:

npm run lint

---

## 🔄 Development Roadmap

### Phase 1 — Frontend Setup

- Create React application
- Configure Vite
- Configure ESLint
- Create folder structure
- Configure Git

### Phase 2 — Routing

- Install React Router
- Configure routes
- Create public routes
- Create protected routes
- Configure layouts

### Phase 3 — Authentication

- Create Login page
- Create Register page
- Connect authentication API
- Handle JWT token
- Create AuthContext
- Protect private routes
- Implement logout

### Phase 4 — Dashboard

- Create dashboard layout
- Create sidebar
- Create navbar
- Create statistics cards
- Display employee statistics
- Display department statistics
- Display project statistics

### Phase 5 — Employee Management

- Employee list
- Employee table
- Add employee form
- Employee details
- Edit employee
- Delete employee
- Search employees
- Filter employees
- Employee status

### Phase 6 — Department Management

- Department list
- Department form
- Add department
- Edit department
- Delete department
- Department employees

### Phase 7 — Project Management

- Project list
- Project form
- Add project
- Edit project
- Delete project
- Assign employees
- Remove employees
- Project employees

### Phase 8 — API Integration

- Connect React with FastAPI
- Configure API service
- Handle GET requests
- Handle POST requests
- Handle PUT requests
- Handle DELETE requests
- Handle API errors
- Handle loading states

### Phase 9 — UI Improvements

- Responsive design
- Reusable components
- Form validation
- Loading states
- Error messages
- Empty states
- Confirmation dialogs
- Better user experience

### Phase 10 — Testing & Deployment

- Test application
- Test authentication
- Test CRUD operations
- Fix frontend issues
- Create production build
- Deploy frontend
- Connect frontend with deployed backend

---

## 🎯 Project Goals

The main goal of this frontend is to build a professional React application while understanding how a modern frontend communicates with a backend API.

The project will provide practical experience with:

- React
- JavaScript
- JSX
- Vite
- React Router
- Component Architecture
- State Management
- Context API
- Custom Hooks
- API Integration
- REST APIs
- Authentication
- JWT
- Protected Routes
- Forms
- CRUD Interfaces
- Responsive Design
- ESLint
- Git & GitHub
- Full-Stack Architecture

---

## 🏗️ Application Architecture

React Application
│
├── Pages
│
├── Components
│
├── Layouts
│
├── Context
│
├── Hooks
│
├── Services
│
└── API Integration
│
▼
FastAPI Backend
│
▼
SQLAlchemy ORM
│
▼
PostgreSQL Database

---

## 🗄️ Backend & Database

The frontend does not directly communicate with PostgreSQL.

The communication flow is:

React
↓
FastAPI
↓
SQLAlchemy
↓
PostgreSQL

This keeps the database credentials and database logic on the backend.

The React frontend only communicates with the FastAPI REST API.

---

## 🔒 Security

The frontend will follow secure development practices.

Sensitive information should not be hardcoded into React components.

Authentication tokens will be handled carefully.

The frontend will never directly connect to the PostgreSQL database.

Database credentials will remain on the backend.

Protected API requests will include the required authentication token.

---

## 🚀 Future Deployment

The frontend will be deployed separately from the backend.

Planned architecture:

React Frontend
↓
Frontend Hosting
↓
FastAPI Backend
↓
Backend Hosting
↓
PostgreSQL Database

The frontend will use the deployed FastAPI API URL when running in production.

---

## 👨‍💻 Author

### Abdullah Shabir

Full-Stack Developer and Computer Science Student.

---

## ⭐ Project Status

🚧 Currently under development

The frontend is being developed step-by-step alongside the FastAPI backend.

---

## 📌 Important

This project is being developed for learning and practical full-stack development experience.

The development process focuses on understanding:

- How React works
- How FastAPI works
- How REST APIs work
- How PostgreSQL works
- How SQLAlchemy connects applications with databases
- How authentication works
- How frontend and backend communicate
- How a complete full-stack application is structured

---

**Employee Management System — Full-Stack Employee & Project Management Platform**
