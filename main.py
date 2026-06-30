from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr
app=FastAPI()

class Student(BaseModel):
    std_id:int = Field(
        gt = 0
    )
    name:str = Field(
        min_length=2,
        max_length=50
    )
    roll_no:int = Field(
        gt=0
    )
    grade:str = Field(
        min_length=1,
        max_length=1
    )
    email: EmailStr
    
students=[]

def search(student_id):
    for index,student in enumerate(students):
        if student.std_id == student_id:
            return index
    return -1;
        
@app.get("/")
def all_students():
    return students

@app.get("/students/{student_id}", response_model=Student)
def id_student(student_id:int)->Student:
        get_index=search(student_id)
        if get_index == -1: 
            raise HTTPException(status_code=404, detail="Student not found!")
        return students[get_index]
    
@app.post("/students")
def create_student(student:Student):
    verify_stud=search(student.std_id)
    if verify_stud != -1: 
        raise HTTPException(status_code=409, detail="Student already added!") 
    students.append(student)
    raise HTTPException(status_code=201, detail="Student added successfully!")

@app.put("/students/{student_id}")
def update_student(student_id:int,student:Student):
        update_verify=search(student.std_id)
        if update_verify != -1: 
            raise HTTPException(status_code=409, detail="Student already added!") 
        update_index=search(student_id)
        if update_index == -1: 
            raise HTTPException(status_code=404, detail="Student not found!")
        students[update_index]=student
        raise HTTPException(status_code=200, detail="Student updated successfully!")

@app.delete("/students/{student_id}")
def delete_student(student_id:int):
        del_index=search(student_id)
        if del_index == -1: 
            raise HTTPException(status_code=404, detail="Student not found!")
        del students[del_index]
        raise HTTPException(status_code=200, detail="Student deleted successfully!")

    
    