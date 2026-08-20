from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.schemas import StudentActivityCreate, SubjectCreate
from app.services import student_activity_service, subject_service


def test_subject_crud():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()

    try:
        created = subject_service.create_subject(
            db,
            SubjectCreate(
                subject_code="CS101",
                subject_name="Computer Science",
                credits=4,
                department_id=1,
            ),
        )

        assert created.subject_id == 1
        assert len(subject_service.get_subjects(db)) == 1

        updated = subject_service.update_subject(
            db,
            created.subject_id,
            SubjectCreate(
                subject_code="CS102",
                subject_name="Algorithms",
                credits=5,
                department_id=1,
            ),
        )

        assert updated.subject_code == "CS102"
        assert updated.subject_name == "Algorithms"

        deleted = subject_service.delete_subject(db, created.subject_id)
        assert deleted is not None
        assert subject_service.get_subject(db, created.subject_id) is None
    finally:
        db.close()


def test_student_activity_crud():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()

    try:
        created = student_activity_service.create_student_activity(
            db,
            StudentActivityCreate(
                student_id=1,
                activity_name="Hackathon",
                description="Team participation",
                activity_date="2026-01-15",
            ),
        )

        assert created.activity_id == 1
        assert len(student_activity_service.get_student_activities(db)) == 1

        updated = student_activity_service.update_student_activity(
            db,
            created.activity_id,
            StudentActivityCreate(
                student_id=1,
                activity_name="Workshop",
                description="Updated description",
                activity_date="2026-02-15",
            ),
        )

        assert updated.activity_name == "Workshop"

        deleted = student_activity_service.delete_student_activity(db, created.activity_id)
        assert deleted is not None
        assert student_activity_service.get_student_activity(db, created.activity_id) is None
    finally:
        db.close()
