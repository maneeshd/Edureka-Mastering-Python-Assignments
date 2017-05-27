"""
@author: Maneesh D
@date: 5/26/2017
@intepreter: Python 3.6

Interactive Quiz Application
"""
from random import randint, choices
from sys import exit


def addition(difficulty, questions):
    if difficulty == "e":
        while questions:
            try:
                a = randint(0, 30)
                b = randint(0, 10)
                answer = int(input("What's %d + %d?\nAnswer: " % (a, b)))
                if answer == (a + b):
                    print("Correct :-)\n")
                else:
                    print("Wrong :-(\n")
                questions -= 1
            except TypeError:
                print("Trying to be too smart???\n")
                questions -= 1
                continue
            except KeyboardInterrupt:
                print("\n!!! USER CANCELLATION !!!")
                exit(1)
    elif difficulty == "i":
        while questions:
            try:
                a = randint(30, 100)
                b = randint(10, 50)
                answer = int(input("What's %d + %d?\nAnswer: " % (a, b)))
                if answer == (a + b):
                    print("Correct :-)\n")
                else:
                    print("Wrong :-(\n")
                questions -= 1
            except TypeError:
                print("Trying to be too smart???\n")
                questions -= 1
                continue
            except KeyboardInterrupt:
                print("\n!!! USER CANCELLATION !!!")
                exit(1)
    else:
        while questions:
            try:
                primes = [x for x in range(100, 1000) if all(x % y != 0 for y in range(2, int(x**0.5)+1))]
                nums = choices(primes, k=2)
                a = nums[0]
                b = nums[1]
                answer = int(input("What's %d + %d?\nAnswer: " % (a, b)))
                if answer == (a + b):
                    print("Correct :-)\n")
                else:
                    print("Wrong :-(\n")
                questions -= 1
            except TypeError:
                print("Trying to be too smart???\n")
                questions -= 1
                continue
            except KeyboardInterrupt:
                print("\n!!! USER CANCELLATION !!!")
                exit(1)
    return 0


def substration(difficulty, questions):
    if difficulty == "e":
        while questions:
            try:
                a = randint(0, 30)
                b = randint(0, 10)
                answer = int(input("What's %d - %d?\nAnswer: " % (a, b)))
                if answer == (a - b):
                    print("Correct :-)\n")
                else:
                    print("Wrong :-(\n")
                questions -= 1
            except TypeError:
                print("Trying to be too smart???\n")
                questions -= 1
                continue
            except KeyboardInterrupt:
                print("\n!!! USER CANCELLATION !!!")
                exit(1)
    elif difficulty == "i":
        while questions:
            try:
                a = randint(30, 100)
                b = randint(10, 50)
                answer = int(input("What's %d - %d?\nAnswer: " % (a, b)))
                if answer == (a - b):
                    print("Correct :-)\n")
                else:
                    print("Wrong :-(\n")
                questions -= 1
            except TypeError:
                print("Trying to be too smart???\n")
                questions -= 1
                continue
            except KeyboardInterrupt:
                print("\n!!! USER CANCELLATION !!!")
                exit(1)
    else:
        while questions:
            try:
                primes = [x for x in range(100, 1000) if all(x % y != 0 for y in range(2, int(x**0.5)+1))]
                nums = choices(primes, k=2)
                a = nums[0]
                b = nums[1]
                answer = int(input("What's %d - %d?\nAnswer: " % (a, b)))
                if answer == (a - b):
                    print("Correct :-)\n")
                else:
                    print("Wrong :-(\n")
                questions -= 1
            except TypeError:
                print("Trying to be too smart???\n")
                questions -= 1
                continue
            except KeyboardInterrupt:
                print("\n!!! USER CANCELLATION !!!")
                exit(1)
    return 0


def multiplication(difficulty, questions):
    if difficulty == "e":
        while questions:
            try:
                a = randint(0, 30)
                b = randint(0, 20)
                answer = int(input("What's %d * %d?\nAnswer: " % (a, b)))
                if answer == (a * b):
                    print("Correct :-)\n")
                else:
                    print("Wrong :-(\n")
                questions -= 1
            except TypeError:
                print("Trying to be too smart???\n")
                questions -= 1
                continue
            except KeyboardInterrupt:
                print("\n!!! USER CANCELLATION !!!")
                exit(1)
    elif difficulty == "i":
        while questions:
            try:
                a = randint(30, 100)
                b = randint(10, 50)
                answer = int(input("What's %d * %d?\nAnswer: " % (a, b)))
                if answer == (a * b):
                    print("Correct :-)\n")
                else:
                    print("Wrong :-(\n")
                questions -= 1
            except TypeError:
                print("Trying to be too smart???\n")
                questions -= 1
                continue
            except KeyboardInterrupt:
                print("\n!!! USER CANCELLATION !!!")
                exit(1)
    else:
        while questions:
            try:
                primes = [x for x in range(100, 1000) if all(x % y != 0 for y in range(2, int(x**0.5)+1))]
                nums = choices(primes, k=2)
                a = nums[0]
                b = nums[1]
                answer = int(input("What's %d * %d?\nAnswer: " % (a, b)))
                if answer == (a * b):
                    print("Correct :-)\n")
                else:
                    print("Wrong :-(\n")
                questions -= 1
            except TypeError:
                print("Trying to be too smart???\n")
                questions -= 1
                continue
            except KeyboardInterrupt:
                print("\n!!! USER CANCELLATION !!!")
                exit(1)
    return 0


def division(difficulty, questions):
    if difficulty == "e":
        while questions:
            try:
                a = randint(0, 30)
                b = randint(0, 10)
                answer = int(input("What's %d/%d?\nAnswer: " % (a, b)))
                if answer == (a / b):
                    print("Correct :-)\n")
                else:
                    print("Wrong :-(\n")
                questions -= 1
            except TypeError:
                print("Trying to be too smart???\n")
                questions -= 1
                continue
            except KeyboardInterrupt:
                print("\n!!! USER CANCELLATION !!!")
                exit(1)
    elif difficulty == "i":
        while questions:
            try:
                a = randint(30, 100)
                b = randint(10, 50)
                answer = int(input("What's %d/%d?\nAnswer: " % (a, b)))
                if answer == (a / b):
                    print("Correct :-)\n")
                else:
                    print("Wrong :-(\n")
                questions -= 1
            except TypeError:
                print("Trying to be too smart???\n")
                questions -= 1
                continue
            except KeyboardInterrupt:
                print("\n!!! USER CANCELLATION !!!")
                exit(1)
    else:
        while questions:
            try:
                primes = [x for x in range(100, 1000) if all(x % y != 0 for y in range(2, int(x**0.5)+1))]
                nums = choices(primes, k=2)
                a = nums[0]
                b = nums[1]
                answer = int(input("What's %d/%d?\nAnswer: " % (a, b)))
                if answer == (a / b):
                    print("Correct :-)\n")
                else:
                    print("Wrong :-(\n")
                questions -= 1
            except TypeError:
                print("Trying to be too smart???\n")
                questions -= 1
                continue
            except KeyboardInterrupt:
                print("\n!!! USER CANCELLATION !!!")
                exit(1)
    return 0


def main():
    try:
        difficulty = input("Choose level (easy:E, intermediate:I, and hard:H): ").lower()
        if difficulty not in ("easy", "intermediate", "hard", "e", "i", "h"):
            print("!!! Please enter a valid choice !!!")
            exit(1)

        questions = int(input("Please give us the number of question you want to attempt(max=10): "))
        if questions < 0 or questions > 10:
            print("!!! Enter a number between 1 and 10 !!!")
            exit(1)
        elif questions == 0:
            print("Wow genius!!! You entered zero!!!")
            exit(1)

        qtype = input("Specify the question type "
                      "(multiplication:M, addition:A, subtraction:S, division:D): ").lower()
        if qtype not in ("m", "a", "s", "d"):
            print("!!! Please enter a valid choice !!!")
            exit(1)

        while True:

            if questions:
                if qtype == "a":
                    questions = addition(difficulty, questions)
                elif qtype == "s":
                    questions = substration(difficulty, questions)
                elif qtype == "m":
                    questions = multiplication(difficulty, questions)
                else:
                    questions = division(difficulty, questions)
            else:
                cont = input("Continue or exit (Continue:C, Exit: E): ").lower()
                if cont not in ("c", "e"):
                    print("!!! Invalid Choice !!!")
                    continue
                if cont == "c":
                    questions = 1
                else:
                    print("\n<------------ THANK YOU ------------>")
                    exit(0)
    except KeyboardInterrupt:
        print("\n!!! USER CANCELLATION !!!")
        exit(1)
    except Exception as e:
        print("Encountered Exception: %s" % e)

if __name__ == '__main__':
    main()
