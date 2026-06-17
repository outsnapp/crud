# domain/student.py

class Student:
    def __init__(self, id: int, name: str, age: int):
        self.id = id
        self.name = name
        self.age = age

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age
        }