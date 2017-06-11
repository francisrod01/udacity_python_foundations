#!/usr/bin/python3

print('# Python String translate() method')

intab = "aeiou"
outtab = "12345"

str = "This is string example....wow!!!"
trantab = str.maketrans(intab, outtab)
print(str.translate(trantab))

print('Good bye!')
