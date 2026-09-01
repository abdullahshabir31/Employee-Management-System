from fastapi import FastAPI
from sqlalchemy import text
from database import engine
from routers.departments import router as departments_router
from routers.employees import router as employees_router
from routers.projects import router as projects_router
from routers.employee_projects import router as employee_project_router
from routers.auth import router as auth_router


app = FastAPI()
app.include_router(auth_router)
app.include_router(departments_router)
app.include_router(employees_router)
app.include_router(projects_router)
app.include_router(employee_project_router)


@app.get("/")
def root():
    return {"message": "Employee Management System API is running"}

@app.get("/test-db")
def test_db():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

    return {
        "message": "Database connection successful",
        "result": result.scalar()
    }