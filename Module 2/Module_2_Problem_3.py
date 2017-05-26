"""
@author: Maneesh D
@date: May 15, 2017
@interpreter: Python 3.6.1
Fahrenheit to Celcius Converter
"""
fahren = float(input("Enter the temperature in Fahrenheit: "))
celcius = ((fahren - 32) * 5) / 9
print("%.2f in Degree Celcius is %.2f" % (fahren, celcius))
