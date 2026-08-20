from pydantic import BaseModel, ConfigDict, Field
from datetime import date


PositiveId = Field(gt=0)


# =========================
# DEPARTMENT
# =========================

class DepartmentBase(BaseModel):
    department_code: str
    department_name: str
    hod_faculty_id: int | None = Field(default=None, gt=0)
    contact_email: str | None = None
    contact_mobile: str | None = None


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentResponse(DepartmentBase):
    department_id: int = PositiveId

    model_config = ConfigDict(from_attributes=True)


# =========================
# PROGRAM
# =========================

class ProgramBase(BaseModel):
    program_code: str
    program_name: str
    department_id: int = PositiveId


class ProgramCreate(ProgramBase):
    pass


class ProgramResponse(ProgramBase):
    program_id: int

    model_config = ConfigDict(from_attributes=True)


# =========================
# FACULTY
# =========================

class FacultyBase(BaseModel):
    employee_id: str
    faculty_name: str
    email: str
    mobile: str | None = None
    department_id: int = PositiveId


class FacultyCreate(FacultyBase):
    pass


class FacultyResponse(FacultyBase):
    faculty_id: int

    model_config = ConfigDict(from_attributes=True)


# =========================
# STUDENT
# =========================

class StudentBase(BaseModel):
    roll_number: str
    student_name: str
    email: str
    mobile: str | None = None
    admission_year: int
    department_id: int = PositiveId
    program_id: int = PositiveId


class StudentCreate(StudentBase):
    pass


class StudentResponse(StudentBase):
    student_id: int

    model_config = ConfigDict(from_attributes=True)


# =========================
# SUBJECT
# =========================

class SubjectBase(BaseModel):
    subject_code: str
    subject_name: str
    credits: int
    department_id: int = PositiveId
    semester: int | None = None
    subject_type: str | None = None


class SubjectCreate(SubjectBase):
    pass


class SubjectResponse(SubjectBase):
    subject_id: int

    model_config = ConfigDict(from_attributes=True)


# =========================
# REGISTRATION
# =========================

class RegistrationBase(BaseModel):
    student_id: int = PositiveId
    offering_id: int = PositiveId
    registration_date: date
    status: str


class RegistrationCreate(RegistrationBase):
    pass


class RegistrationResponse(RegistrationBase):
    registration_id: int

    model_config = ConfigDict(from_attributes=True)


# =========================
# EXAMINATION RESULT
# =========================

class ExaminationResultBase(BaseModel):
    student_id: int = PositiveId
    offering_id: int = PositiveId
    internal_marks: float | None = None
    external_marks: float | None = None
    total_marks: float | None = None
    grade: str | None = None
    result_status: str | None = None


class ExaminationResultCreate(ExaminationResultBase):
    pass


class ExaminationResultResponse(ExaminationResultBase):
    result_id: int

    model_config = ConfigDict(from_attributes=True)


# =========================
# STUDENT ACTIVITY
# =========================

class StudentActivityBase(BaseModel):
    student_id: int = PositiveId
    activity_name: str
    description: str | None = None
    activity_date: date | None = None


class StudentActivityCreate(StudentActivityBase):
    pass


class StudentActivityResponse(StudentActivityBase):
    activity_id: int

    model_config = ConfigDict(from_attributes=True)


# =========================
# ATTENDANCE
# =========================

class AttendanceBase(BaseModel):
    student_id: int = PositiveId
    offering_id: int = PositiveId
    attendance_date: date
    period_session: int | None = None
    faculty_id: int = PositiveId
    status: str


class AttendanceCreate(AttendanceBase):
    pass


class AttendanceResponse(AttendanceBase):
    attendance_id: int

    model_config = ConfigDict(from_attributes=True)


# =========================
# FACULTY ASSIGNMENT
# =========================

class FacultyAssignmentBase(BaseModel):
    faculty_id: int = PositiveId
    offering_id: int = PositiveId
    role: str | None = None


class FacultyAssignmentCreate(FacultyAssignmentBase):
    pass


class FacultyAssignmentResponse(FacultyAssignmentBase):
    assignment_id: int

    model_config = ConfigDict(from_attributes=True)


# =========================
# COURSE OFFERING
# =========================

class CourseOfferingBase(BaseModel):
    subject_id: int = PositiveId
    semester: int
    academic_year: int
    section: str | None = None
    status: str | None = None


class CourseOfferingCreate(CourseOfferingBase):
    pass


class CourseOfferingResponse(CourseOfferingBase):
    offering_id: int

    model_config = ConfigDict(from_attributes=True)


# =========================
# USER
# =========================

class UserBase(BaseModel):
    username: str
    role: str
    is_active: bool = True


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    user_id: int

    model_config = ConfigDict(from_attributes=True)