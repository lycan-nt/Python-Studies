from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "Felipe D. Santos",
        "age": 27,
        "class": "Code"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/students")
def get_all_students():
    return {"Students": students}

@app.get("/students/{id}")
def get_student(id: int = Path(description="The ID of the student you want to view", gt=0, lt=10)):
    return students[id]

@app.get("/get-by-name/{id}")
def get_student(*,id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}

@app.post("/create-students/{student_id}")
def create(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    students[student_id] = student
    return students[student_id]