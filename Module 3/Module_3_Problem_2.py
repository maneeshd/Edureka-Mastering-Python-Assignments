"""
@author: Maneesh D
@date: 5/26/2017
@intepreter: Python 3.6

Recursive function to calulate x raised to the power of n.
"""


def power(x, n):
    if n:
        return x * power(x, n-1)
    return 1


def main():
    num = int(input("Enter the number: "))
    exp = int(input("Enter the exponent: "))
    print("%d^%d = %d" % (num, exp, power(num, exp)))

if __name__ == '__main__':
    main()
