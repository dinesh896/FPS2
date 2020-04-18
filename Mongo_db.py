"""
Code Challenge 2

Write a python code to insert records to a MongoDB (Atlas Cloud) database 
named db_University with collection named univ_coll for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.
"""
# !pip install pymongo
# mongodb+srv://dineshsk:db898989@clusterdinesh-yjugo.mongodb.net/test?retryWrites=true&w=majority
# db_University
# coll_University

import pymongo

client = pymongo.MongoClient("mongodb+srv://dineshsk:db898989@clusterdinesh-yjugo.mongodb.net/test?retryWrites=true&w=majority")
mydb = client.db_University

def add_student(Student_Name, Student_Age, Student_Roll_No, Student_Branch):
    unique_student = mydb.coll_University.find_one({"Student_Name":Student_Name})
    if unique_student:
        return "Student already exists"
    else:
        mydb.coll_University.insert_one(
                {
                "Student_Name" : Student_Name,
                "Student_Age" : Student_Age,
                "Student_Roll_No" : Student_Roll_No,
                "Student_Branch" : Student_Branch
                })
        return "Student added successfully"

def fetch_all_student():
    user = mydb.coll_University.find()
    for i in user:
        print (i)

#Insert data in collection
add_student('Amit',20,21,'EC')
add_student('Gaurav',21,22,'ME')
add_student('Ram',21,23,'IT')
add_student('Karan',20,24,'CS')
add_student('Navin',20,25,'EC')
add_student('Mohan',22,26,'ME')
add_student('Raman',22,27,'IT')
add_student('Sita',20,28,'CS')
add_student('Amar',20,29,'IT')
add_student('Jai',21,30,'CS')

fetch_all_student()

# Drop a collection in Mongo, deletes the database as well
# mydb.coll_University.drop()
