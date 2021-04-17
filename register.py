#!/usr/bin/python3
# C:\Users\Work\AppData\Local\Programs\Python\Python39\python.exe
# Import mysql module (DB API)
import mysql.connector
import cgi
print("Content-Type: text/html \n\n")

# Get access to the FORM data
fromData = cgi.FieldStorage()
fname = fromData.getvalue('fname')
lname = fromData.getvalue('lname')
role = fromData.getvalue('role')
hiredate = fromData.getvalue('hiredate')
addr = fromData.getvalue('addr')
color = fromData.getvalue('color')
borncity = fromData.getvalue('borncity')
email = fromData.getvalue('email')
passwd = fromData.getvalue('passwd')

# Error Handling
try:
    # Connecting to MySQL database
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="Project2")

    # Creating cursor
    mycursor = mydb.cursor(buffered=True)

    # Check if email exists
    query_check = "SELECT emp_email, COUNT(*) FROM employees WHERE  emp_email = %s GROUP by emp_lname"
    val1 = (email,)

    # Executing the SQL query
    mycursor.execute(query_check, val1)
    num = mycursor.rowcount
    if num >= 1:
        print("Email already exists, user cannot be registed.")
    else:
        # Cursor for Insert
        mycursor1 = mydb.cursor(buffered=True)
        # Passes query
        query = "INSERT INTO `employees`(`emp_fname`, `emp_lname`, `emp_role`, `emp_addr`, `emp_email`, `emp_hiredate`, `emp_color`, `emp_borncity`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        val2 = (fname, lname, role, addr, email, hiredate, color, borncity)

        # Executing the SQL query
        mycursor1.execute(query, val2)

        # Commiting changes
        mydb.commit()
        query_empid = "select emp_id from employees where emp_email = %s"
        val3 = (email,)

        # Cursor for employeeID
        mycursor2 = mydb.cursor(buffered=True)
        # Executing the SQL query
        mycursor2.execute(query_empid, val3)
        myresult = mycursor2.fetchall()
        for x in myresult:
            for empid in x:
                print("<h3>Your employee id is", empid,
                      "<br>Please don't lose your Employee ID number.</h3>")
                # Creating cursor for password
                mycursor3 = mydb.cursor(buffered=True)
                # Passes query
                query_password = "INSERT INTO `login`(`emp_id`, `emp_passhash`) VALUES (%s,%s)"
                val4 = (empid, passwd)
                mycursor3.execute(query_password, val4)
                mydb.commit()
                mycursor3.close()
        # Closing cursor
        mycursor1.close()
        mycursor2.close()
    # Closing cursor
    mycursor.close()
    mydb.close()
except mysql.connector.Error as err:
    print("Something went wrong<br><meta http-equiv = 'refresh' content = 'time; URL=404-notfound.html'/>")
# For Debugging
    # print(mycursor.rowcount)
    # print(mycursor.fetchall())
