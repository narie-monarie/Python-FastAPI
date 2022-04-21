from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import studentEntity, listOfStudentEntity
from bson import ObjectId


student_router = APIRouter()

# getting all students
@student_router.get("/students")
async def findAllStudents():
    return listOfStudentEntity(connection.local.student.find())

#get student by Id
@student_router.get('/students/{studentId}')
async def findStudentbyID(studentId):
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))

# creating a student
@student_router.post("/students")
async def createStudent(student: Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudentEntity(connection.local.student.find())

#update a student
@student_router.put("/students/{studentId}")
async def updateStudent(studentId, student: Student):
    #find the student and then update it with new student data
    connection.local.student.find_one_and_update(
        {"_id": ObjectId(studentId)},
        {"$set": dict(student)})
    
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))

#delete a student
@student_router.delete("/students/{studentId}")
async def deleteStudent(studentId):
    #find the student id and delete him/her from the DB and return the same student object
    return studentEntity(connection.local.student.find_one_and_delete({"_id": ObjectId(studentId)}))