from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app=FastAPI()

class Student(BaseModel):
    std_id:int
    name:str 
    roll_no:int
    grade:str
    
students=[]

def search(student_id):
    for index,student in enumerate(students):
        if student.std_id == student_id:
            return index
    raise HTTPException(status_code=404, detail="Student not found!")
        
@app.get("/")
def all_students():
    return students

@app.get("/students/{student_id}", response_model=Student)
def id_student(student_id:int)->Student:
        get_index=search(student_id)
        return students[get_index]
    
@app.post("/students")
def create_student(student:Student):
    students.append(student)
    return student

@app.put("/students/{student_id}")
def update_student(student_id:int,student:Student):
        update_index=search(student_id)
        students[update_index]=student
        return students[update_index]

@app.delete("/students/{student_id}")
def delete_student(student_id:int):
        del_index=search(student_id)
        del students[del_index]
        return students
    
    