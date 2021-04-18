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
        cookie = cookies.SimpleCookie()
        cookie[empid] = passwd
        expires = datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
        cookie[empid]['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
        #note that the headers are printed here as well
        #also note that the blank line after the cookies is mandatory
        #the indentation matters
        page = """Content-Type: text/html
{cookie}

<meta http-equiv="refresh" content="0; url=aboutMe.py" />
"""
        print(page.format(cookie=cookie))
    else:
        print("Content-Type: text/html \n\n")
        print("Contact administrator as user not found or password provided was wrong. Try resetting your password.")
except mysql.connector.Error as err:
    print("Something went wrong<br><meta http-equiv = 'refresh' content = 'time; URL=404-notfound.html'/>")