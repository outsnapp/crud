from domain.student import Student
from infrastructure.student_repository_impl import StudentRepositoryImpl

repository = StudentRepositoryImpl()


def update_student(student_id: int, name: str, age: int):
    student = Student(student_id, name, age)

    repository.update(student)

    return {
        "message": "Student updated successfully"
    }