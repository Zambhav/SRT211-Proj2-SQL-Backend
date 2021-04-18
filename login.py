#!/usr/bin/python3
#C:\Users\Work\AppData\Local\Programs\Python\Python39\python.exe

# Import mysql module (DB API)
import mysql.connector
import cgi
import cgitb
cgitb.enable()

# Get access to the FORM data
fromData = cgi.FieldStorage()
try:
    empid = fromData["empid"].value
except KeyError:
    empid = "Undefined"

try:
    passwd = fromData["passwd"].value
except KeyError:
    passwd = "Undefined"

try:
    # Connecting to MySQL database
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="project2")

    # Creating cursor
    mycursor = mydb.cursor(buffered=True)

    # Check if user exists
    query_check = "SELECT * FROM `login` WHERE emp_id=%s AND emp_passhash = %s"
    val = (empid,passwd)

    mycursor.execute(query_check, val)
    num = mycursor.rowcount
    if num >= 1:
        from http import cookies
        import datetime
        import uuid 
        # Cookie adds emp_id and maps it to emp_passhash as a dictionary element inside a list.
        cookie = cookies.SimpleCookie()
        cookie[empid] = passwd
        # Makes use of uuid and datetime to convert local timezone to "GMT" timezone for 10 minutes 
        expires = datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
        # Appends 'exipres' and the time being specified as another dictonary element with in cookie list.
        cookie[empid]['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
        #note that the headers are printed here as well
        #also note that the blank line after the cookies is mandatory
        #the indentation matters
        # Format on how the cookies needs to be added to the webpage and redirects to the "aboutMe.py"
        page = """Content-Type: text/html
{cookie}

<meta http-equiv="refresh" content="0; url=aboutMe.py" />
"""
        # Prints the cookie on the webpage which is ingested by the browser 
        print(page.format(cookie=cookie))
    else:
        print("Content-Type: text/html \n\n")
        print("Contact administrator as user not found or password provided was wrong. Try resetting your password.")
except mysql.connector.Error as err:
    print("Something went wrong<br><meta http-equiv = 'refresh' content = 'time; URL=404-notfound.html'/>")