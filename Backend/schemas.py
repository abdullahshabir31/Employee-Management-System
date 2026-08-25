from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)



class DepartmentCreate(BaseModel):
    name: str
    description: str | None = None


class DepartmentUpdate(BaseModel):
    name: str | None = None
    description: str | None = None


class DepartmentResponse(BaseModel):
    id: int
    name: str
    description: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)



class EmployeeCreate(BaseModel):
    department_id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone: str | None = None
    job_title: str
    salary: float | None = None
    hire_date: date | None = None
    status: str = "active"


class EmployeeUpdate(BaseModel):
    department_id: int | None = None
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    job_title: str | None = None
    salary: float | None = None
    hire_date: date | None = None
    status: str | None = None


class EmployeeResponse(BaseModel):
    id: int
    department_id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone: str | None
    job_title: str
    salary: float | None
    hire_date: date | None
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)



class ProjectCreate(BaseModel):
    name: str
    description: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    status: str = "planned"


class ProjectUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    status: str | None = None


class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str | None
    start_date: date | None
    end_date: date | None
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)



class EmployeeProjectCreate(BaseModel):
    employee_id: int
    project_id: int
    role: str | None = None


class EmployeeProjectResponse(BaseModel):
    id: int
    employee_id: int
    project_id: int
    role: str | None
    assigned_at: datetime

    model_config = ConfigDict(from_attributes=True)