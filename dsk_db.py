"""
https://www.db4free.net
https://www.db4free.net/phpMyAdmin/
MySQL Host Name : db4free.net
Port : 
MySQL database name:  dsk_db
MySQL username: dineshsk
MySQL user password: db898989
Email address:  dineshsk@gmail.com
MYSQL URL : mysql://dineshsk:db898989@db4free.net/dsk_db

"""

"""
Code Challenge 1
Write a python code to insert records to a sqlite/MySQL database 
named dsk_db for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.
"""

# !pip install mysql-connector-python

import mysql.connector 
from pandas import DataFrame

# connect to  MySQL server along with Database name

conn = mysql.connector.connect(user='dineshsk', password='db898989',
                              host='db4free.net', database = 'dsk_db')

#conn.autocommit = True

# creating cursor
c = conn.cursor()

# STEP 0
#c.execute("DROP DATABASE dsk_db;")

# STEP 1
#c.execute("CREATE DATABASE dsk_db;")

# STEP 2
#c.execute("DROP Table Students;")

# STEP 3
c.execute ("""CREATE TABLE Students(
          Student_Name TEXT,
          Student_Age INTEGER,
          Student_Roll_No INTEGER,
          Student_Branch TEXT
          )""")


# STEP 4
c.execute("INSERT INTO Students VALUES ('Amit',20,21,'EC')")
c.execute("INSERT INTO Students VALUES ('Gaurav',21,22,'ME')")
c.execute("INSERT INTO Students VALUES ('Ram',21,23,'IT')")
c.execute("INSERT INTO Students VALUES ('Karan',20,24,'CS')")
c.execute("INSERT INTO Students VALUES ('Navin',20,25,'EC')")
c.execute("INSERT INTO Students VALUES ('Mohan',22,26,'ME')")
c.execute("INSERT INTO Students VALUES ('Raman',22,27,'IT')")
c.execute("INSERT INTO Students VALUES ('Sita',20,28,'CS')")
c.execute("INSERT INTO Students VALUES ('Amar',20,29,'IT')")
c.execute("INSERT INTO Students VALUES ('Jai',21,30,'CS')")


#You need to commit your transaction for the database to make your insert permanent
conn.commit() #not required if autocommit enabled

# c.execute("INSERT INTO Students VALUES ({},'{}', '{}', {})".format(Student_Name, Student_Age,Student_Roll_No,Student_Branch))

c.execute("SELECT * FROM Students")

# STEP 5
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of tuples

print ( c.fetchall() )

conn.close()
# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database

c.execute("SELECT * FROM Students")

# STEP 6
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["Student_Name","Student_Age","Student_Roll_No","Student_Branch"]
print(df)
conn.close()


