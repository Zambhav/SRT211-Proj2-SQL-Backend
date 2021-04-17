#!/usr/bin/python3
# Import mysql module (DB API)
import mysql.connector
import cgi
from http import cookies
import cgitb
cgitb.enable()

# Get access to the FORM data
fromData = cgi.FieldStorage()
empid = fromData["empid"].value
passwd = fromData["passwd"].value

cookie = cookies.SimpleCookie()

cookie[empid] = passwd
cookie[empid]["domain"] = "172.20.23.172"

page = """Content-Type: text/html
{cookie}

hoe
"""
print(page.format(cookie=cookie))