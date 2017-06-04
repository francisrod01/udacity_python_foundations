#!/usr/bin/python3.4

''' A change to `local_bad_scope.py` avoiding any error by passing a parameter '''


def main():
    x = 3
    f(x)


def f(whatever):
    print(whatever)  # error: f doesn't know about the x defined in main


main()
