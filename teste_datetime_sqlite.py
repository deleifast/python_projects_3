import datetime
import sqlite3
 
# get the current datetime and store it in a variable
currentDateTime = datetime.datetime.now()
 
# make the database connection with detect_types
connection = sqlite3.connect('StudentAssignment.db',
                             detect_types=sqlite3.PARSE_DECLTYPES |
                             sqlite3.PARSE_COLNAMES)
cursor = connection.cursor()
 
# create table in database
createTable = '''CREATE TABLE ASSIGNMENT (
    StudentId INTEGER,
    StudentName VARCHAR(100),
    SubmissionDate TIMESTAMP);'''
cursor.execute(createTable)
 
# create query to insert the data
insertQuery = """INSERT INTO ASSIGNMENT
    VALUES (?, ?, ?);"""
 
# insert the data into table
cursor.execute(insertQuery, (1, "Virat Kohli",
                             currentDateTime))
cursor.execute(insertQuery, (2, "Rohit Pathak",
                             currentDateTime))

print("Data Inserted Successfully !")


# commit the changes,
# close the cursor and database connection
connection.commit()

for row in cursor.execute('SELECT * FROM ASSIGNMENT'):
    print(row)

cursor.close()
connection.close()