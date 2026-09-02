from datetime import date, datetime
from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    email: Mapped[str] = mapped_column(
        String(300),
        unique=True,
        nullable=False,
    )

    password_hash: Mapped[str] = mapped_column(
        String(300),
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )


class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    employees: Mapped[list["Employee"]] = relationship(
        back_populates="department",
    )


class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.id"),
        nullable=False,
    )

    first_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    last_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(300),
        unique=True,
        nullable=False,
    )

    phone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    job_title: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    salary: Mapped[float | None] = mapped_column(
        nullable=True,
    )

    hire_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="active",
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    department: Mapped["Department"] = relationship(
        back_populates="employees",
    )

    employee_projects: Mapped[list["EmployeeProject"]] = relationship(
    back_populates="employee",
    cascade="all, delete-orphan",
    )


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    start_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    end_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="planned",
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    employee_projects: Mapped[list["EmployeeProject"]] = relationship(
        back_populates="project",
        cascade="all, delete-orphan",
    )


class EmployeeProject(Base):
    __tablename__ = "employee_projects"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    employee_id: Mapped[int] = mapped_column(
        ForeignKey("employees.id"),
        nullable=False,
    )

    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id"),
        nullable=False,
    )

    role: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    assigned_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    employee: Mapped["Employee"] = relationship(
        back_populates="employee_projects",
    )

    project: Mapped["Project"] = relationship(
        back_populates="employee_projects",
    )