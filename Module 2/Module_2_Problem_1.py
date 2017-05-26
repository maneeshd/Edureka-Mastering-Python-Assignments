"""
@author: Maneesh D
@date: May 15, 2017
@interpreter: Python 3.6.1
"""
total = int(input('What is the total amount for your online shopping?\n'))
country = input('Shipping within the US or Canada?\n')
if country.lower() == "us":
    if total <= 50:
        print("Shipping Costs $6.00")
    elif total <= 100:
        print("Shipping Costs $9.00")
    elif total <= 150:
        print("Shipping Costs $12.00")
    else:
        print("FREE Shipping!!!")
elif country.lower() == "canada":
    if total <= 50:
        print("Shipping Costs $8.00")
    elif total <= 100:
        print("Shipping Costs $12.00")
    elif total <= 150:
        print("Shipping Costs $15.00")
    else:
        print("FREE Shipping!!!")
else:
    print("!Invalid Country Entered. Valid Country Entries are US and Canada!")
