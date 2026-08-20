from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

from app.routers import students
from app.routers import faculty
from app.routers import departments
from app.routers import course_offerings
from app.routers import attendance
from app.routers import examination_results
from app.routers import faculty_assignments
from app.routers import programs
from app.routers import registrations
from app.routers import users
from app.routers import subjects
from app.routers import student_activities

app = FastAPI(
    title="Student Management System",
    description="Backend API for Student Management System",
    version="1.0.0"
)


@app.exception_handler(IntegrityError)
async def handle_integrity_error(request: Request, exc: IntegrityError):
    return JSONResponse(
        status_code=400,
        content={
            "detail": "The request conflicts with existing database data. "
            "Check referenced IDs and unique fields."
        },
    )

app.include_router(examination_results.router)
app.include_router(faculty_assignments.router)
app.include_router(programs.router)
app.include_router(registrations.router)
app.include_router(users.router)
app.include_router(subjects.router)
app.include_router(student_activities.router)
app.include_router(students.router)
app.include_router(faculty.router)
app.include_router(departments.router)
app.include_router(course_offerings.router)
app.include_router(attendance.router)


@app.get("/")
def home():
    return {
        "message": "Student Management System API is running"
    }