"""
@author: Maneesh D
@date: 29-May-17
@intepreter: Python 3.6

Regular Expression that will match an IPv4 address.
"""
from re import compile


pattern = compile("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
# ^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$
ip_list = ["192.168.0.1", "1023.123.44.1", "999.999.999.999", "10.8.0.40", "0.0.0.0", "255.255.255.0"]

for ip in ip_list:
    if pattern.match(ip):
        print("%s is a valid IPv4 IP." % ip)
    else:
        print("%s is an invalid IPv4 IP." % ip)
