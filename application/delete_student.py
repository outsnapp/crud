from infrastructure.student_repository_impl import StudentRepositoryImpl

repository = StudentRepositoryImpl()


def delete_student(student_id: int):
    repository.delete(student_id)

    return {
        "message": "Student deleted successfully"
    }