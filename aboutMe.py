#!/usr/bin/python3
#C:\Users\Work\AppData\Local\Programs\Python\Python39\python.exe

# Import mysql module (DB API)
import mysql.connector
import cgitb, os
cgitb.enable()
print("Content-Type: text/html \n\n")

# Error Handling
try:
    if "HTTP_COOKIE" in os.environ :
        cookie_info = os.environ["HTTP_COOKIE"]
        cookie_info = cookie_info.split('; ')
        for cookie in cookie_info:
            print
            cookie = cookie.split('=')
            empID = cookie[0]
            passwd = cookie[1]

            # Connecting to MySQL database
            mydb = mysql.connector.connect(host="localhost", user="root", password="", database="project2")

            # Creating cursor
            mycursor = mydb.cursor(buffered=True)

            query_check = "SELECT `emp_id`,`emp_passhash` FROM `login` WHERE `emp_id`=%s AND `emp_passhash`=%s"
            val = (empID,passwd)

            mycursor.execute(query_check, val)
            num = mycursor.rowcount
            if num >= 1:
                mycursor1 = mydb.cursor(buffered=True)
                query = "SELECT `emp_id`,`emp_fname`,`emp_lname`,`emp_role`,`emp_addr`,`emp_email`,`emp_hiredate` FROM `employees` WHERE `emp_id`=%s"
                val1 = (empID,)

                mycursor1.execute(query,val1)
                myresult = mycursor1.fetchall()
                for x in myresult:
                    emp_id = x[0]
                    fname = x[1]
                    lname = x[2]
                    role = x[3]
                    address = x[4]
                    email = x[5]
                    hiredate = x[6]
                    forwardPage = open("aboutMe.html").read().format(emp_id=emp_id, emp_fname=fname, emp_lname=lname, email=email, role=role, address=address, hiredate=hiredate)
                    print(forwardPage)
                else:
                    print("Something went wrong<br><meta http-equiv = 'refresh' content = 'time; URL=404-notfound.html'/>")
                mycursor1.close()
            else:
                    print("Something went wrong<br><meta http-equiv = 'refresh' content = 'time; URL=404-notfound.html'/>")
            mycursor.close()
            mydb.close()
    else:
        print("Something went wrong<br><meta http-equiv = 'refresh' content = 'time; URL=404-notfound.html'/>")
    # Open reset passwords html with the employee id populated
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