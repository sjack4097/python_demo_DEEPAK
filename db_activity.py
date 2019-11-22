#establishng db connection
import mysql.connector as mc
conn=mc.connect(host="localhost",user="root",password="",database="librarydb")
cursor=conn.cursor()
# for displaying all databases
def displaydatabases():
    cursor.execute("SHOW DATABASES")
    record = cursor.fetchall()
    for row in record:
        print(row)

# for all displaying all student records
def displaystudent_details():
    cursor.execute("SELECT * FROM STUDENT")
    record = cursor.fetchall()
    for row in record:
        print(row)

#for displaying available book
def diplayavailablebook():
    cursor.execute("select * from book where accessionnumber not in(select accessionnumber from issue)")
    record=cursor.fetchall()
    for row in record:
        print(row)

#searching a book by title
def searchbookbytitle():
    sub = input("enter a book title")
    cursor.execute("SELECT * FROM book NATURAL JOIN title WHERE title LIKE '%{}%'".format(sub))
    record=cursor.fetchall()
    for row in record:
        print(row)


def finedetails():
    cursor.execute("SELECT fname ,lname,(datediff(CURRENT_DATE,issuedate)-7)*50 from issue NATURAL JOIN student WHERE datediff(CURRENT_DATE,issuedate)>7")
    record=cursor.fetchall()
    for row in record:
        print(row)




#calling functions
#displaydatabases()
#displaystudent_details()
#diplayavailablebook()
searchbookbytitle()
finedetails()