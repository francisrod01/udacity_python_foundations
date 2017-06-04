#!/usr/bin/python3.4

def happy_birthday(person):
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear " + person + ".")
    print("Happy Birthday to you!")


def main():
    user_name = input("Enter the Birthday person's name: ")
    happy_birthday(user_name)


main()
