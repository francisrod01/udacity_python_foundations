#!/usr/bin/python3.4

''' A function returning a string and using a local variable '''


def last_first(first_name, last_name):
    separator = ', '
    result = last_name + separator + first_name
    return result


print(last_first('Benjamin', 'Franklin'))
print(last_first('Andrew', 'Harrington'))
