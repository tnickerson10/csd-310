import pymongo
from pymongo import MongoClient


client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.idipi.mongodb.net/pytech?retryWrites=true&w=majority")
db = client.pytech
collection = db.students

user1 = {"student_id": 1007, "first_name": "travis", "last_name": "nickerson", "enrollment": [{
    "term": "spring 2021", "gpa": 3.75, "start_date": "01/01/2021", "end_date": "06/15/2022", 
    "course_id": 101100}], "course": [{"course_id": 101100, "description": "CSD 310", "instructor":
     "chris soriano", "grade": "A"}]}

user1_id = collection.insert_one(user1).inserted_id

user2 = {"student_id": 1008, "first_name": "ryan", "last_name": "jones", "enrollment": [{
    "term": "spring 2021", "gpa": 3.95, "start_date": "01/01/2021", "end_date": "06/15/2022", 
    "course_id": 101100}], "course": [{"course_id": 101100, "description": "CSD 310", "instructor":
     "chris soriano", "grade": "A"}]}

user2_id = collection.insert_one(user2).inserted_id

user3 = {"student_id": 1009, "first_name": "mary", "last_name": "lamb", "enrollment": [{
    "term": "spring 2021", "gpa": 3.85, "start_date": "01/01/2021", "end_date": "06/15/2022", 
    "course_id": 101100}], "course": [{"course_id": 101100, "description": "CSD 310", "instructor":
     "chris soriano", "grade": "B"}]}

user3_id = collection.insert_one(user3).inserted_id


print(f'\nInserted student record Travis Nickerson into the students collection with document_id {user1_id}')
print(f'Inserted student record Ryan Jones into the students collection with document_id {user2_id}')
print(f'Inserted student record Mary Lamb into the students collection with document_id {user3_id}\n')