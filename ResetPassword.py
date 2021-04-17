#!/usr/bin/python3
#!C:\Users\Work\AppData\Local\Programs\Python\Python39\python.exe
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
print(empID, email, color, borncity, "<br>")
# Error Handling
try:
    # Connecting to MySQL database
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="Project2")

    # Creating cursor
    mycursor = mydb.cursor(buffered=True)

    # Check if the information provided matches EXACTLY to a row 
    #Column names: emp_id, emp_email, emp_color, emp_borncity
    # Example command: SELECT COUNT(*) FROM `employees`
    # WHERE emp_id="20" AND emp_email="1@1.ca" AND emp_color="aaa" AND emp_borncity="aaa" 

    query_check = "SELECT * FROM employees WHERE emp_id=%s AND emp_email=%s AND emp_color=%s AND emp_borncity= %s"
    val = (empID, email, color, borncity)

    # Executing the SQL query
    test = mycursor.execute(query_check, val)
    num = mycursor.rowcount

    print(num,test)
    
    # Closing cursor
    mycursor.close()
    mydb.close()
except mysql.connector.DataError as err:
    print("Encountered DataError <br>")
    print("Error Code: ", err.errno)
    print("<br> SQL State: ", err.sqlstate)
    print("<br> Error Message: ", err.msg)
except mysql.connector.InternalError as err:
    print("Encountered InternalError <br>")
    print("Error Code: ", err.errno)
    print("<br> SQL State: ", err.sqlstate)
    print("<br> Error Message: ", err.msg)
except mysql.connector.IntegrityError as err:
    print("Encountered IntegrityError <br>")
    print("Error Code: ", err.errno)
    print("<br> SQL State: ", err.sqlstate)
    print("<br> Error Message: ", err.msg)
except mysql.connector.OperationalError as err:
    print("Encountered OperationalError <br>")
    print("Error Code: ", err.errno)
    print("<br> SQL State: ", err.sqlstate)
    print("<br> Error Message: ", err.msg)
except mysql.connector.NotSupportedError as err:
    print("Encountered NotSupportedError <br>")
    print("Error Code: ", err.errno)
    print("<br> SQL State: ", err.sqlstate)
    print("<br> Error Message: ", err.msg)
except mysql.connector.ProgrammingError as err:
    print("Encountered ProgrammingError <br>")
    print("Error Code: ", err.errno)
    print("<br> SQL State: ", err.sqlstate)
    print("<br> Error Message: ", err.msg)