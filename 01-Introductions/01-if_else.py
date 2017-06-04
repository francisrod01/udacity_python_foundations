#!/usr/bin/python3.4

print("Example utilizing if/else...")

var1 = 100
if var1:
    print("1 - Got a true expression value: ", var1)
else:
    print("1 - Got a false expression value: ", var1)

var2 = 0
if var2:
    print("2 - Got a true expression value: ", var2)
else:
    print("2 - Got a false expression value: ", var2)


print("\nExample utilizing if/elif/else...")

var = 100
if var == 200:
    print("1 - Got a true expression value: ", var)
elif var == 150:
    print("2 - Got a true expression value: ", var)
elif var == 100:
    print("3 - Got a true expression value: ", var)
else:
    print("4 - Got a false expression value: ", var)

print("\nGood bye!")
