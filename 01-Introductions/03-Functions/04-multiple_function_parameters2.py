#!/usr/bin/python3.4

'''
Display any number of sum problems with a function.
Handle keyboard input separately.
'''


def sum_problem(x, y):
    nsum = x + y
    return 'The sum of {} and {} is {}.'.format(x, y, nsum)


def main():
    print(sum_problem(2, 3))
    print(sum_problem(1234567890123, 535790269358))
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    print(sum_problem(a, b))


main()
