"""
@author: Maneesh D
@date: 29-May-17
@intepreter: Python 3.6

Regular Expression that will match an email address.
"""
from re import compile


pattern = compile("[\w._\-]+@\w+\.[a-zA-Z.]{3}")
email_list = ["dmaneesh7@gmail.com",
              "Manesh.D@gmail.com",
              "dmaneesh7@gmail.co.in",
              "Manesh.D@gmail.net",
              "man.com",
              "255.255@255.0",
              "255.255@255.com"
              ]

for email in email_list:
    if pattern.match(email):
        print("%s is a valid email id." % email)
    else:
        print("%s is an invalid email id." % email)
