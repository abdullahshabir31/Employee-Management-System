from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Employee, EmployeeProject, Project
from schemas import (
    EmployeeProjectCreate,
    EmployeeProjectResponse,
)


router = APIRouter()


@router.post("/employee-project",
             tags=["Employee Projects"], 
             response_model=EmployeeProjectResponse
)
def assign_employee_to_project(
    assignment: EmployeeProjectCreate,
    db: Session = Depends(get_db),
):
    employee = db.query(Employee).filter(Employee.id == assignment.employee_id).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found",
        )

    project = db.query(Project).filter(Project.id == assignment.project_id).first()

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    existing_assignment = (
        db.query(EmployeeProject)
        .filter(
            EmployeeProject.employee_id == assignment.employee_id,
            EmployeeProject.project_id == assignment.project_id,
        )
        .first()
    )

    if existing_assignment:
        raise HTTPException(
            status_code=400,
            detail="Employee is already assigned to this project",
        )

    new_assignment = EmployeeProject(
        employee_id=assignment.employee_id,
        project_id=assignment.project_id,
        role=assignment.role,
    )

    db.add(new_assignment)
    db.commit()
    db.refresh(new_assignment)

    return new_assignment


@router.get("/employee-projects",
            tags=["Employee Projects"], 
            response_model=list[EmployeeProjectResponse]
)
def get_employee_projects(
    db: Session = Depends(get_db),
):
    assignments = db.query(EmployeeProject).all()

    return assignments


@router.get("/employee-project/{assignment_id}",
            tags=["Employee Projects"], 
            response_model=EmployeeProjectResponse
)
def get_employee_project(
    assignment_id: int,
    db: Session = Depends(get_db),
):
    assignment = (
        db.query(EmployeeProject)
        .filter(EmployeeProject.id == assignment_id)
        .first()
    )

    if not assignment:
        raise HTTPException(
            status_code=404,
            detail="Employee-project assignment not found",
        )

    return assignment


@router.delete("/employee-project/{assignment_id}",
               tags=["Employee Projects"],
)
def delete_employee_project(
    assignment_id: int,
    db: Session = Depends(get_db),
):
    assignment = (
        db.query(EmployeeProject)
        .filter(EmployeeProject.id == assignment_id)
        .first()
    )

    if not assignment:
        raise HTTPException(
            status_code=404,
            detail="Employee-project assignment not found",
        )

    db.delete(assignment)
    db.commit()

    return {
        "message": "Employee removed from project successfully"
    }


# Projects of an Employee


@router.get(
    "/employee/{employee_id}/projects",
    tags=["Employee Projects"],
    response_model=list[EmployeeProjectResponse],
)
def get_employee_projects_by_employee(
    employee_id: int,
    db: Session = Depends(get_db),
):
    employee = (
        db.query(Employee)
        .filter(Employee.id == employee_id)
        .first()
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found",
        )

    assignments = (
        db.query(EmployeeProject)
        .filter(EmployeeProject.employee_id == employee_id)
        .all()
    )

    return assignments


# Employees of a Project


@router.get(
    "/project/{project_id}/employees",
    tags=["Employee Projects"],
    response_model=list[EmployeeProjectResponse],
)
def get_project_employees(
    project_id: int,
    db: Session = Depends(get_db),
):
    project = (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    assignments = (
        db.query(EmployeeProject)
        .filter(EmployeeProject.project_id == project_id)
        .all()
    )

    return assignments