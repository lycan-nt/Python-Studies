from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1: {
        "name": "Felipe D. Santos",
        "age": 27,
        "class": "Code"
    }
}

@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/students")
def get_all_students():
    return {"Students": len(students)}

@app.get("/students/{id}")
def get_student(id: int = Path(description="The ID of the student you want to view", gt=0, lt=10)):
    return students[id]