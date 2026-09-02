from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Employee, User
from schemas import (
    EmployeeCreate,
    EmployeeResponse,
    EmployeeUpdate,
)
from routers.auth import get_current_user


router = APIRouter(
     dependencies=[Depends(get_current_user)],
)


@router.post("/employees",
    tags=["Employees"],
    response_model=EmployeeResponse
)
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    new_employee = Employee(
        department_id=employee.department_id,
        first_name=employee.first_name,
        last_name=employee.last_name,
        email=employee.email,
        phone=employee.phone,
        job_title=employee.job_title,
        salary=employee.salary,
        hire_date=employee.hire_date,
        status=employee.status
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee


@router.get("/employees",
    tags=["Employees"],
    response_model=list[EmployeeResponse]
)
def get_employees(
    db: Session = Depends(get_db)
):
    employees = db.query(Employee).all()

    return employees


@router.get("/employees/{employee_id}",
    tags=["Employees"],
    response_model=EmployeeResponse
)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


@router.put("/employees/{employee_id}",
    tags=["Employees"],
    response_model=EmployeeResponse
)
def update_employee(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db)
):
    existing_employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not existing_employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    existing_employee.department_id = employee.department_id
    existing_employee.first_name = employee.first_name
    existing_employee.last_name = employee.last_name
    existing_employee.email = employee.email
    existing_employee.phone = employee.phone
    existing_employee.job_title = employee.job_title
    existing_employee.salary = employee.salary
    existing_employee.hire_date = employee.hire_date
    existing_employee.status = employee.status

    db.commit()
    db.refresh(existing_employee)

    return existing_employee


@router.delete("/employee/{employee_id}",
    tags=["Employees"],
)
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    existing_employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not existing_employee:
            raise HTTPException(
                status_code=404,
                detail="Employee not found"
            )

    db.delete(existing_employee)
    db.commit()

    return {"message": "Employee Deleted"}