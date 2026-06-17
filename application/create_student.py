from domain.student import Student
from infrastructure.student_repository_impl import StudentRepositoryImpl

repository = StudentRepositoryImpl()

def create_student(name: str, age: int):
    student = Student(None, name, age)
    repository.save(student)

    return {
        "message": "Student created successfully"
    }
    