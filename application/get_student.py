from infrastructure.student_repository_impl import StudentRepositoryImpl

repository = StudentRepositoryImpl()


def get_students():
    return repository.get_all()