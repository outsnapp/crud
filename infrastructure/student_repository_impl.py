from domain.student_repository import StudentRepository
from domain.student import Student

from infrastructure.connection import SessionLocal
from infrastructure.models import Student as StudentModel


class StudentRepositoryImpl(StudentRepository):

    def save(self, student: Student):

        session = SessionLocal()

        db_student = StudentModel(
            name=student.name,
            age=student.age
        )

        session.add(db_student)
        session.commit()

        session.close()

    def get_all(self):

        session = SessionLocal()

        rows = session.query(StudentModel).all()

        students = []

        for row in rows:
            students.append({
                "id": row.id,
                "name": row.name,
                "age": row.age
            })

        session.close()

        return students

    def get_by_id(self, student_id: int):

        session = SessionLocal()

        row = (
            session.query(StudentModel)
            .filter(StudentModel.id == student_id)
            .first()
        )

        session.close()

        if row is None:
            return None

        return {
            "id": row.id,
            "name": row.name,
            "age": row.age
        }

    def update(self, student: Student):

        session = SessionLocal()

        db_student = (
            session.query(StudentModel)
            .filter(StudentModel.id == student.id)
            .first()
        )

        if db_student:

            db_student.name = student.name
            db_student.age = student.age

            session.commit()

        session.close()

    def delete(self, student_id: int):

        session = SessionLocal()

        db_student = (
            session.query(StudentModel)
            .filter(StudentModel.id == student_id)
            .first()
        )

        if db_student:

            session.delete(db_student)
            session.commit()

        session.close()