#!/usr/bin/python3

import os


# Write into a file.
def write_into_a_file():
    try:
        fh = open('./files_test/testfile', 'w')
        fh.write('This is my test file for exception handling!!')
    except IOError:
        print('Error: can\'t find file or read data.')
    else:
        print('Written content in the file successfully!')
        fh.close()


# Read a file.
def read_a_file():
    try:
        fh = open('./files_test/testfile', 'r')
        fh.write('This is my test file for exception handling!!')
    except IOError:
        print('Error: can\'t find file or read data')
    else:
        print('Written content in the file successfully!')
        fh.close()


# Rename a file.
def rename_a_file():
    # Try to rename a file to a name that already exists in a folder.
    try:
        os.rename('./files_test/__testfile', './files_test/5bogota.jpg')
    except FileNotFoundError:
        print('Error: can\'t find the file!')
    # If *NIX and user has permission to change file, the old file will be
    # overwritten by the new file. Otherwise, an error is thrown.
    except FileExistsError:
        print('Error: can\'t possible to rename file that already exists in a folder!')
    else:
        print('File renamed successfully!')


# Try-finally clause.
def try_finally_clause():
    try:
        fh = open('./files_test/testfile', 'r')
        try:
            fh.write('This is my test file for exception handling!!')
        finally:
            print('Going to close the file.')
            fh.close()
    except IOError:
        print('Error: can\'t find file or read data.')


# Argument of an Exception.
def temp_convert(_var):
    try:
        return int(_var)
    except ValueError as Argument:
        print('Error: The argument does not contain numbers.')
        print(Argument)


# Raising an Exceptions.
def raising_an_exception(level):
    if level < 1:
        try:
            raise Exception('Invalid level!')
            # The code below to this would not be executed
            # if we raise the exception.
        except Exception as e:
            print(e)


class NetworkError(RuntimeError):
    def __init__(self, arg):
        # self.args = arg
        pass


# User-defined exceptions
def user_defined_exceptions():
    try:
        raise NetworkError('Bad Hostname!')
    except NetworkError as e:
        # print(e.args)
        print(e)


print('\n#1 - Writing into a file...')
write_into_a_file()

print('\n#2 - Reading a file...')
read_a_file()

print('\n#3 - Renaming a file...')
rename_a_file()

print('\n#4 - Try-finally clause...')
try_finally_clause()

print('\n#5 - Argument of an Exception...')
temp_convert('xyz')

print('\n#6 - Raising an Exception...')
raising_an_exception(-1)

print('\n#7 - User-Defined Exceptions...')
user_defined_exceptions()
