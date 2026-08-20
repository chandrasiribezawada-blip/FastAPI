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
    status = Column(String(20), nullable=True)


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
    duration_years = Column(Integer, nullable=True)
    status = Column(String(20), nullable=True)


class Faculty(Base):
    __tablename__ = "faculty"

    faculty_id = Column(Integer, primary_key=True)
    employee_id = Column(String(20), nullable=False, unique=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=True)
    email = Column(String(100), nullable=False, unique=True)
    mobile = Column(String(15), nullable=True)
    department_id = Column(
        Integer,
        ForeignKey("department.department_id"),
        nullable=False
    )
    designation = Column(String(100), nullable=True)
    joining_date = Column(Date, nullable=True)
    status = Column(String(20), nullable=True)

    @property
    def faculty_name(self):
        return " ".join(filter(None, (self.first_name, self.last_name)))


class Student(Base):
    __tablename__ = "student"

    student_id = Column(Integer, primary_key=True)
    roll_number = Column(String(20), nullable=False, unique=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=True)
    email = Column(String(100), nullable=False, unique=True)
    mobile = Column(String(15), nullable=True)
    admission_year = Column(Integer, nullable=False)
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

    @property
    def student_name(self):
        return " ".join(filter(None, (self.first_name, self.last_name)))

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
    semester = Column(Integer, nullable=True)
    subject_type = Column(String(30), nullable=True)

class Registration(Base):
    __tablename__ = "course_registration"

    registration_id = Column(Integer, primary_key=True)

    student_id = Column(
        Integer,
        ForeignKey("student.student_id"),
        nullable=False
    )

    offering_id = Column(
        Integer,
        ForeignKey("course_offering.offering_id"),
        nullable=False
    )

    registration_date = Column(Date, nullable=False)
    registration_status = Column(String(20), nullable=False)

    @property
    def status(self):
        return self.registration_status
class ExaminationResult(Base):
    __tablename__ = "examination_result"

    result_id = Column(Integer, primary_key=True)

    student_id = Column(
        Integer,
        ForeignKey("student.student_id"),
        nullable=False
    )

    offering_id = Column(
        Integer,
        ForeignKey("course_offering.offering_id"),
        nullable=False
    )

    internal_marks = Column(Integer, nullable=True)
    external_marks = Column(Integer, nullable=True)
    total_marks = Column(Integer, nullable=True)
    grade = Column(String(5), nullable=True)
    result_status = Column(String(10), nullable=True)
class StudentActivity(Base):
    __tablename__ = "student_activity"

    activity_id = Column(Integer, primary_key=True)

    student_id = Column(
        Integer,
        ForeignKey("student.student_id"),
        nullable=False
    )

    activity_name = Column(String(100), nullable=False)
    club_name = Column(String(100), nullable=True)
    event_name = Column(String(100), nullable=True)
    participation_date = Column(Date, nullable=True)
    achievement = Column(String(255), nullable=True)

    @property
    def description(self):
        return self.achievement

    @property
    def activity_date(self):
        return self.participation_date


class Attendance(Base):
    __tablename__ = "attendance"

    attendance_id = Column(Integer, primary_key=True)

    student_id = Column(
        Integer,
        ForeignKey("student.student_id"),
        nullable=False
    )

    offering_id = Column(
        Integer,
        ForeignKey("course_offering.offering_id"),
        nullable=False
    )

    attendance_date = Column(Date, nullable=False)
    period_session = Column(String(20), nullable=True)
    attendance_status = Column(String(20), nullable=False)
    faculty_id = Column(Integer, ForeignKey("faculty.faculty_id"), nullable=False)

    @property
    def status(self):
        return self.attendance_status


class FacultyAssignment(Base):
    __tablename__ = "faculty_subject_assignment"

    assignment_id = Column(Integer, primary_key=True)

    faculty_id = Column(
        Integer,
        ForeignKey("faculty.faculty_id"),
        nullable=False
    )

    offering_id = Column(
        Integer,
        ForeignKey("course_offering.offering_id"),
        nullable=False
    )

    role = Column(String(30), nullable=True)


class CourseOffering(Base):
    __tablename__ = "course_offering"

    offering_id = Column(Integer, primary_key=True)

    subject_id = Column(
        Integer,
        ForeignKey("subject.subject_id"),
        nullable=False
    )

    semester = Column(Integer, nullable=False)
    academic_year = Column(Integer, nullable=False)
    section = Column(String(10), nullable=True)
    status = Column(String(20), nullable=True)


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(30), nullable=False)
    is_active = Column(Boolean, default=True)