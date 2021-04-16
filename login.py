#!/usr/bin/python3
# Import mysql module (DB API)
import mysql.connector
import cgi
print("Content-Type: text/html \n\n")

# Get access to the FORM data
fromData = cgi.FieldStorage()
email = fromData.getvalue('email')
passwd = fromData.getvalue('password')

print(email)
print(passwd)