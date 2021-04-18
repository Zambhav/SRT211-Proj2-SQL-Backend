#!/usr/bin/python3
#C:\Users\Work\AppData\Local\Programs\Python\Python39\python.exe

# Import mysql module (DB API)
import mysql.connector
import cgitb, os
cgitb.enable()
print("Content-Type: text/html \n\n")

# Error Handling
try:
    # Reads cookie data by looking for "HTTP_COOKIE" in OS environment, if cookie not found it redirects to 404-notfound.html.
    if "HTTP_COOKIE" in os.environ :
        cookie_info = os.environ["HTTP_COOKIE"]
        cookie_info = cookie_info.split('; ')
        for cookie in cookie_info:
            cookie = cookie.split('=')
            # Saves each element of cookie as empID and passwd from list of cookie
            empID = cookie[0]
            passwd = cookie[1]

            # Connecting to MySQL database to check autheticate user, if doesnt authenticate it redirects user to 404-notfound.html
            mydb = mysql.connector.connect(host="localhost", user="root", password="", database="project2")

            # Creating cursor specifically handiling users's password hash and id.
            mycursor = mydb.cursor(buffered=True)

            query_check = "SELECT `emp_id`,`emp_passhash` FROM `login` WHERE `emp_id`=%s AND `emp_passhash`=%s"
            val = (empID,passwd)

            mycursor.execute(query_check, val)
            num = mycursor.rowcount
            # Now user has been validated it trys to get employee information which will be populated in "aboutMe.html"
            if num >= 1:
                mycursor1 = mydb.cursor(buffered=True)
                query = "SELECT `emp_id`,`emp_fname`,`emp_lname`,`emp_role`,`emp_addr`,`emp_email`,`emp_hiredate` FROM `employees` WHERE `emp_id`=%s"
                val1 = (empID, )
                
                # New cursor was opened because it is dealing with not senstive information.
                mycursor1.execute(query,val1)
                myresult = mycursor1.fetchall()
                for x in myresult:
                    eid = x[0]
                    fname = x[1]
                    lname = x[2]
                    role = x[3]
                    address = x[4]
                    email = x[5]
                    hiredate = x[6]
                forwardPage = open('aboutMe.html').read().format(emp_id=eid, fname=fname, lname=lname, email=email, role=role, address=address, hiredate=hiredate)
                print(forwardPage)
                mycursor1.close()
            else:
                    print("Something went wrong<br><meta http-equiv = 'refresh' content = 'time; URL=404-notfound.html'/>")
            mycursor.close()
            mydb.close()
    else:
        print("Something went wrong<br><meta http-equiv = 'refresh' content = 'time; URL=404-notfound.html'/>")
except mysql.connector.Error as err:
    print("Something went wrong<br><meta http-equiv = 'refresh' content = 'time; URL=404-notfound.html'/>")