#Travis Nickerson
#April 15th, 2021
#Assignment 6.3 Pytech_delete
#Goal: to add student_id: 1010 to current documents in the students collection of db pytech then delete student_id 1010
#GitHub: https://github.com/tnickerson10/csd-310
import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.idipi.mongodb.net/pytech?retryWrites=true&w=majority")
db = client.pytech
collection = db.students

docs = collection.find({})

print(" -- DISPLAYING STUDENTS DOCUMENT FROM find() QUERY -- ")
for doc in docs:
    print(f" Student ID: {doc['student_id']} \n First Name: {doc['first_name']} \n Last Name: {doc['last_name']}\n")

newStudent = {"student_id": 1010, "first_name": "walter", "last_name": "heisenberg"}
newStudentId = collection.insert_one(newStudent).inserted_id

print("\n -- INSERT STATEMENTS --\n")
print(f" Inserted student record into the students collection with document_id {newStudentId} ")

newStudentFind = collection.find_one({"student_id": 1010})

print("\n -- DISPLAYING NEW STUDENT TEST --\n")

print(f" Student ID: {newStudentFind['student_id']} \n First Name: {newStudentFind['first_name']} \n Last Name: {newStudentFind['last_name']}\n")

deletedNewStudent = collection.delete_one({"student_id": 1010})

updatedDocs = collection.find({})

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --\n")

for doc in updatedDocs:
    print(f" Student ID: {doc['student_id']} \n First Name: {doc['first_name']} \n Last Name: {doc['last_name']}\n")