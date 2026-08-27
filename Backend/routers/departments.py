from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Department
from schemas import ( 
    DepartmentCreate, 
    DepartmentResponse, 
    DepartmentUpdate, 
    PartialDepartmentUpdate
)


router = APIRouter()


@router.post("/departments",
              tags=["Departments"], 
              response_model=DepartmentResponse
)
def create_department(
    department: DepartmentCreate,
    db: Session = Depends(get_db),
):
    new_department = Department(
        name=department.name,
        description=department.description,
    )

    db.add(new_department)
    db.commit()
    db.refresh(new_department)

    return new_department


@router.get("/departments",
            tags=["Departments"],
            response_model=list[DepartmentResponse]
)
def get_departments(
    db: Session = Depends(get_db)
):
    departments = db.query(Department).all()

    return departments


@router.get("/departemnts/{department_id}",
            tags=["Departments"],
            response_model=DepartmentResponse
)
def get_department(
    department_id: int,
    db: Session = Depends(get_db)
):
    department = db.query(Department).filter(Department.id == department_id).first()

    return department


@router.put("/departments/{department_id}",
            tags=["Departments"],
            response_model=DepartmentResponse
)
def update_department(
    department_id: int,
    department: DepartmentUpdate,
    db: Session = Depends(get_db)
):
    existing_department = db.query(Department).filter(Department.id == department_id).first()

    if not existing_department:
        raise HTTPException(
            status_code=404, 
            detail="Department not found"
        )

    if department.name is not None:    
        existing_department.name = department.name

    if department.description is not None:
        existing_department.description = department.description

    db.commit()
    db.refresh(existing_department)

    return existing_department


@router.patch("/departments/{department_id}",
              tags=["Departments"],
              response_model=DepartmentResponse
)
def partial_update_department(
    department_id: int,
    department: PartialDepartmentUpdate,
    db: Session = Depends(get_db)
):
    existing_department = db.query(Department).filter(Department.id == department_id).first()

    if not existing_department:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    if department.name is not None:
        existing_department.name = department.name

    db.commit()
    db.refresh(existing_department)

    return existing_department


@router.delete("/departments/{department_id}",
               tags=["Departments"]
)
def delete_department(
    department_id: int,
    db: Session = Depends(get_db)
):
    existing_department = db.query(Department).filter(Department.id ==department_id).first()

    if not existing_department:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    db.delete(existing_department)
    db.commit()

    return {"message": "Department deleted successfully"}