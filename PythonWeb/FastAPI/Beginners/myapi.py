from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
from config import route_context
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

# Middleware para adicionar o contexto da rota
class AddRouteContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request.scope["path"] = request.scope["path"].replace(route_context, "", 1)
        response = await call_next(request)
        return response

# Adiciona a Middleware em todas as rotas
app.add_middleware(AddRouteContextMiddleware)

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

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

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

@app.put("/update/{id}")
def update(id: int, student: UpdateStudent):
    if id not in students:
        return {"Error": "Student does not exists"}
    
    if student.name != None:
        students[id].name = student.name
    
    if student.age != None:
        students[id].age = student.age

    if student.year != None:
        students[id].year = student.year

    return students[id]

@app.delete("/delete/{id}")
def delete(id: int):
    if id not in students:
        return {"Error": "Student does not exests"}
    del students[id]
    return {"Message": " Student deletes Successfully"}