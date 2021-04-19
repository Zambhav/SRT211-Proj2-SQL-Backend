#!/usr/bin/python3
#C:\Users\Work\AppData\Local\Programs\Python\Python39\python.exe

# Import mysql module (DB API)
import mysql.connector
import cgi
print("Content-Type: text/html \n\n")

# Get access to the FORM data

fromData = cgi.FieldStorage()
empid = fromData.getvalue('empid')
passwd = fromData.getvalue('passwd')


# Error Handling
try:
    # Connecting to MySQL database
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="project2")

    # Creating cursor
    mycursor = mydb.cursor(buffered=True)

    #Calculate the hash value 
    
    updatePassword = "UPDATE login SET emp_passhash=%s WHERE emp_id=%s" 
    val = (passwd, empid)

    # Executing the SQL query
    query = mycursor.execute(updatePassword, val)
    mydb.commit()

    print("<meta http-equiv = 'refresh' content = 'time; URL=Login.html'/>")
    # Closing cursor
    mycursor.close()
    mydb.close()
except:
    print("Something went wrong<br><meta http-equiv = 'refresh' content = 'time; URL=404-notfound.html'/>")