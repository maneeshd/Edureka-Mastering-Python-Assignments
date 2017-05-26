"""
@author: Maneesh D
@date: 5/26/2017
@intepreter: Python 3.6

Interactive Quiz Application
"""
from random import randint, randrange, Random, choice, SystemRandom, random, sample
from sys import exit


def main():
    level = input("Choose level (easy:E, intermediate:I, and hard:H): ")
    if level.lower() not in ("easy", "intermediate", "hard", "e", "i", "h"):
        print("!!! Please enter a valid choice !!!")
        exit(1)
    else:
        level = level.lower()

    questions = int(input("Please give us the number of question you want to attempt(max=10): "))
    if questions < 0 or questions > 10:
        print("!!! Enter a number betwee 1 and 10 !!!")
        exit(1)
    elif questions == 0:
        print("Wow genius!!! You entered zero!!!")
        exit(1)

    type_of_q = input("Specify the question type "
                      "(multiplication:M, addition:A, subtraction:S, division:D): ")
    if type_of_q.lower() not in ("m", "a", "s", "d"):
        print("!!! Please enter a valid choice !!!")
        exit(1)
    else:
        type_of_q = type_of_q.lower()

    while True:
        questions -= 1
        if questions < 0:
            break

if __name__ == '__main__':
    main()
