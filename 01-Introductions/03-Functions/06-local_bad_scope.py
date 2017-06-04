#!/usr/bin/python3.4

''' program causing an error with an undefined variable '''


def main():
    x = 3
    f()


def f():
    print(x)  # error: f doesn't know about the x defined in main


main()
