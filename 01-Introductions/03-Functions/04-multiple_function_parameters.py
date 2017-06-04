#!/usr/bin/python3.4

'''
Display any number of sum problems with a function.
Handle keyboard input separately.
'''


def sum_problem(x, y):
    nsum = x + y
    sentence = 'The sum of {} and {} is {}.'.format(x, y, nsum)
    print(sentence)


def main():
    sum_problem(2, 3)
    sum_problem(1234567890123, 535790269358)
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    sum_problem(a, b)


main()
