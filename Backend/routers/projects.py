from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Project, User
from schemas import (
    ProjectCreate,
    ProjectResponse,
    ProjectUpdate,
)
from routers.auth import get_current_user


router = APIRouter(
    dependencies=[Depends(get_current_user)]
)


@router.post("/projects",
    tags=["Projects"],
    response_model=ProjectResponse
)
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db)
):
    new_project = Project(
        name=project.name,
        description=project.description,
        start_date=project.start_date,
        end_date=project.end_date,
        status=project.status
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project


@router.get("/projects",
    tags=["Projects"],
    response_model=list[ProjectResponse]
)
def get_projects(
    db: Session = Depends(get_db)
):
    projects = db.query(Project).all()

    return projects


@router.get("/projects/{project_id}",
    tags=["Projects"],
    response_model=ProjectResponse
)
def get_project(
    project_id: int,
    db: Session = Depends(get_db)
):
    projects = db.query(Project).filter(Project.id == project_id).first()

    if not projects:
        raise HTTPException(status_code=404, detail="Project not found")

    return projects


@router.put("/projects/{project_id}",
    tags=["Projects"],
    response_model=ProjectResponse
)
def update_project(
    project_id: int,
    project: ProjectUpdate,
    db: Session = Depends(get_db)
):
    existing_project = db.query(Project).filter(Project.id == project_id).first()

    if not existing_project:
        raise HTTPException(status_code=404, detail="Project not found")

    existing_project.name = project.name,
    existing_project.description = project.description,
    existing_project.start_date = project.start_date,
    existing_project.end_date = project.end_date,
    existing_project.status = project.status,

    db.commit()
    db.refresh(existing_project)

    return existing_project


@router.delete("/projects/{project_id}",
    tags=["Projects"],
)
def delete_project(
    project_id: int,
    db: Session = Depends(get_db)
):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    db.delete(project)
    db.commit()

    return {"message": "Project Deleted"}