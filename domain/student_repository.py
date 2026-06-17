# domain/student_repository.py

from abc import ABC, abstractmethod
from domain.student import Student


class StudentRepository(ABC):

    @abstractmethod
    def save(self, student: Student):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, student_id: int):
        pass

    @abstractmethod
    def update(self, student: Student):
        pass

    @abstractmethod
    def delete(self, student_id: int):
        pass