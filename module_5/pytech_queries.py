import pymongo
from pymongo import MongoClient


client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.idipi.mongodb.net/pytech?retryWrites=true&w=majority")
db = client.pytech
collection = db.students

user1 = {"student_id": 1007, "first_name": "travis", "last_name": "nickerson", "enrollment": [{
    "term": "spring 2021", "gpa": 3.75, "start_date": "01/01/2021", "end_date": "06/15/2022", 
    "course_id": 101100}], "course": [{"course_id": 101100, "description": "CSD 310", "instructor":
    "chris soriano", "grade": "A"}]}

user2 = {"student_id": 1008, "first_name": "ryan", "last_name": "jones", "enrollment": [{
    "term": "spring 2021", "gpa": 3.95, "start_date": "01/01/2021", "end_date": "06/15/2022", 
    "course_id": 101100}], "course": [{"course_id": 101100, "description": "CSD 310", "instructor":
    "chris soriano", "grade": "A"}]}

user3 = {"student_id": 1009, "first_name": "mary", "last_name": "lamb", "enrollment": [{
    "term": "spring 2021", "gpa": 3.85, "start_date": "01/01/2021", "end_date": "06/15/2022", 
    "course_id": 101100}], "course": [{"course_id": 101100, "description": "CSD 310", "instructor":
    "chris soriano", "grade": "B"}]}


docs = collection.find({})
print()
for doc in docs:
    print(f'{doc}\n')
   
print('-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --\n')

for id in user1:
    print(f'{id}: {user1[id]}')
print()

for id in user2:
    print(f'{id}: {user2[id]}')
print()

for id in user3:
    print(f'{id}: {user3[id]}')
print()


id_one = collection.find_one({"student_id": 1007})
print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --\n")
for id in id_one:
    print(f'{id}: {id_one[id]}')
print()
