#!/usr/bin/python3
#C:\Users\Work\AppData\Local\Programs\Python\Python39\python.exe

import cgitb, os
cgitb.enable()

# Print the headers
print("Content-Type: text/html")
print()

#get the cookie info
if "HTTP_COOKIE" in os.environ :
   cookie_info = os.environ["HTTP_COOKIE"]
   cookie_info = cookie_info.split('; ')
   handler = {}
   
   for cookie in cookie_info:
      print
      cookie = cookie.split('=')
      handler[cookie[0]] = cookie[1]
      print(cookie[0])
      print(cookie[1])
      print(handler)
else:
   print("ok")
# else :
#    cookie_info = "cookie not defined"

# print(cookie_info)
# #create an HTML page
# page = """
# <!DOCTYPE html>
# <html>
#   <head>
#      <title>Title for the tab</title>
#   </head>
#   <body>
#     <h1>Section Title</h1>
#     <p> Cookie Info: {cookie_info}</p>
#   </body>
# </html>"""

# print(page.format(cookie_info=cookie_info))