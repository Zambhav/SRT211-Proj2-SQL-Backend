#!/usr/bin/python3
#C:\Users\Work\AppData\Local\Programs\Python\Python39\python.exe

# Import mysql module (DB API)
import mysql.connector
import cgi
print("Content-Type: text/html \n\n")

# Get access to the FORM data

fromData = cgi.FieldStorage()
empID = fromData.getvalue('empid')
color = fromData.getvalue('color')
borncity = fromData.getvalue('borncity')
email = fromData.getvalue('email')

# Error Handling
try:
    # Connecting to MySQL database
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="project2")

    # Creating cursor
    mycursor = mydb.cursor(buffered=True) 

    query_check = "SELECT * FROM employees WHERE emp_id=%s AND emp_email=%s AND emp_color=%s AND emp_borncity= %s"
    val = (empID, email, color, borncity)

    # Executing the SQL query
    test = mycursor.execute(query_check, val)
    num = mycursor.rowcount

    # Open reset passwords html with the employee id populated
    forwardPage = open("ResetPassword-Reset.html").read().format(emp_id=empID)

    # checks if the info is correct, if yes open correct page. else give warning. 
    if num == 1:
        print(forwardPage)
    else: 
        print("<meta http-equiv = 'refresh' content = 'time; URL=ResetPassword-Wrong.html'/>")
    # Closing cursor
    mycursor.close()
    mydb.close()
except mysql.connector.Error as err:
    print("Something went wrong<br><meta http-equiv = 'refresh' content = 'time; URL=404-notfound.html'/>")