from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DateTime,
    Text,
    ForeignKey,
    Boolean
)

from app.database import Base


class Department(Base):
    __tablename__ = "department"

    department_id = Column(Integer, primary_key=True)
    department_code = Column(String(10), nullable=False, unique=True)
    department_name = Column(String(100), nullable=False, unique=True)
    hod_faculty_id = Column(Integer, nullable=True)
    contact_email = Column(String(100), nullable=True)
    contact_mobile = Column(String(15), nullable=True)


class Program(Base):
    __tablename__ = "program"

    program_id = Column(Integer, primary_key=True)
    program_code = Column(String(20), nullable=False, unique=True)
    program_name = Column(String(100), nullable=False)
    department_id = Column(
        Integer,
        ForeignKey("department.department_id"),
        nullable=False
    )


class Faculty(Base):
    __tablename__ = "faculty"

    faculty_id = Column(Integer, primary_key=True)
    faculty_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    mobile = Column(String(15), nullable=True)
    department_id = Column(
        Integer,
        ForeignKey("department.department_id"),
        nullable=False
    )


class Student(Base):
    __tablename__ = "student"

    student_id = Column(Integer, primary_key=True)
    student_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    mobile = Column(String(15), nullable=True)
    department_id = Column(
        Integer,
        ForeignKey("department.department_id"),
        nullable=False
    )
    program_id = Column(
        Integer,
        ForeignKey("program.program_id"),
        nullable=False
    )
class Subject(Base):
    __tablename__ = "subject"

    subject_id = Column(Integer, primary_key=True)
    subject_code = Column(String(20), nullable=False, unique=True)
    subject_name = Column(String(100), nullable=False)
    credits = Column(Integer, nullable=False)
    department_id = Column(
        Integer,
        ForeignKey("department.department_id"),
        nullable=False
    )
class Registration(Base):
    __tablename__ = "registration"

    registration_id = Column(Integer, primary_key=True)

    student_id = Column(
        Integer,
        ForeignKey("student.student_id"),
        nullable=False
    )

    subject_id = Column(
        Integer,
        ForeignKey("subject.subject_id"),
        nullable=False
    )

    registration_date = Column(Date, nullable=False)
    status = Column(String(20), nullable=False)
class ExaminationResult(Base):
    __tablename__ = "examination_result"

    result_id = Column(Integer, primary_key=True)

    student_id = Column(
        Integer,
        ForeignKey("student.student_id"),
        nullable=False
    )

    subject_id = Column(
        Integer,
        ForeignKey("subject.subject_id"),
        nullable=False
    )

    marks = Column(Integer, nullable=False)
    grade = Column(String(5), nullable=True)
class StudentActivity(Base):
    __tablename__ = "student_activity"

    activity_id = Column(Integer, primary_key=True)

    student_id = Column(
        Integer,
        ForeignKey("student.student_id"),
        nullable=False
    )

    activity_name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    activity_date = Column(Date, nullable=True)


class Attendance(Base):
    __tablename__ = "attendance"

    attendance_id = Column(Integer, primary_key=True)

    student_id = Column(
        Integer,
        ForeignKey("student.student_id"),
        nullable=False
    )

    subject_id = Column(
        Integer,
        ForeignKey("subject.subject_id"),
        nullable=False
    )

    attendance_date = Column(Date, nullable=False)
    status = Column(String(20), nullable=False)


class FacultyAssignment(Base):
    __tablename__ = "faculty_assignment"

    assignment_id = Column(Integer, primary_key=True)

    faculty_id = Column(
        Integer,
        ForeignKey("faculty.faculty_id"),
        nullable=False
    )

    subject_id = Column(
        Integer,
        ForeignKey("subject.subject_id"),
        nullable=False
    )

    semester = Column(String(20), nullable=False)
    academic_year = Column(String(20), nullable=False)


class CourseOffering(Base):
    __tablename__ = "course_offering"

    offering_id = Column(Integer, primary_key=True)

    subject_id = Column(
        Integer,
        ForeignKey("subject.subject_id"),
        nullable=False
    )

    faculty_id = Column(
        Integer,
        ForeignKey("faculty.faculty_id"),
        nullable=False
    )

    semester = Column(String(20), nullable=False)
    academic_year = Column(String(20), nullable=False)


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(30), nullable=False)
    is_active = Column(Boolean, default=True)