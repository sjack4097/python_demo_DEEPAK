import mysql.connector as mc
conn=mc.connect(host="localhost",user="root",password="",database="librarydb")
if conn:
    print("database connected successfully")
else:
    print("failed")