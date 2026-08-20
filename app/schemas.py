from pydantic import BaseModel, ConfigDict
from datetime import date


# =========================
# DEPARTMENT
# =========================

class DepartmentBase(BaseModel):
    department_code: str
    department_name: str
    hod_faculty_id: int | None = None
    contact_email: str | None = None
    contact_mobile: str | None = None


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentResponse(DepartmentBase):
    department_id: int

    model_config = ConfigDict(from_attributes=True)


# =========================
# PROGRAM
# =========================

class ProgramBase(BaseModel):
    program_code: str
    program_name: str
    department_id: int


class ProgramCreate(ProgramBase):
    pass


class ProgramResponse(ProgramBase):
    program_id: int

    model_config = ConfigDict(from_attributes=True)


# =========================
# FACULTY
# =========================

class FacultyBase(BaseModel):
    faculty_name: str
    email: str
    mobile: str | None = None
    department_id: int


class FacultyCreate(FacultyBase):
    pass


class FacultyResponse(FacultyBase):
    faculty_id: int

    model_config = ConfigDict(from_attributes=True)


# =========================
# STUDENT
# =========================

class StudentBase(BaseModel):
    student_name: str
    email: str
    mobile: str | None = None
    department_id: int
    program_id: int


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
    department_id: int


class SubjectCreate(SubjectBase):
    pass


class SubjectResponse(SubjectBase):
    subject_id: int

    model_config = ConfigDict(from_attributes=True)


# =========================
# REGISTRATION
# =========================

class RegistrationBase(BaseModel):
    student_id: int
    subject_id: int
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
    student_id: int
    subject_id: int
    marks: int
    grade: str | None = None


class ExaminationResultCreate(ExaminationResultBase):
    pass


class ExaminationResultResponse(ExaminationResultBase):
    result_id: int

    model_config = ConfigDict(from_attributes=True)


# =========================
# STUDENT ACTIVITY
# =========================

class StudentActivityBase(BaseModel):
    student_id: int
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
    student_id: int
    subject_id: int
    attendance_date: date
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
    faculty_id: int
    subject_id: int
    semester: str
    academic_year: str


class FacultyAssignmentCreate(FacultyAssignmentBase):
    pass


class FacultyAssignmentResponse(FacultyAssignmentBase):
    assignment_id: int

    model_config = ConfigDict(from_attributes=True)


# =========================
# COURSE OFFERING
# =========================

class CourseOfferingBase(BaseModel):
    subject_id: int
    faculty_id: int
    semester: str
    academic_year: str


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