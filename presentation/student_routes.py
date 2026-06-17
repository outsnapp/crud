# presentation/student_routes.py
print("student_routes loaded")

from fastapi import APIRouter

from application.create_student import create_student
from application.get_student import get_students
from application.update_student import update_student
from application.delete_student import delete_student

router = APIRouter()


@router.post("/students")
def add_student(name: str, age: int):
    return create_student(name, age)


@router.get("/students")
def read_students():
    return get_students()


@router.put("/students/{student_id}")
def edit_student(student_id: int, name: str, age: int):
    return update_student(student_id, name, age)


@router.delete("/students/{student_id}")
def remove_student(student_id: int):
    return delete_student(student_id)