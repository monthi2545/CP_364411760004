"""
Name : Monthira Jamikorn
ID :364411760004
Grop:Mit421
"""

# function with multiple parameter

def myfunc(*msg):  # *msg --> tuple (...)
    print(msg)
    print(type(msg))

def myfunc2(*value):
    total = 0
    for x in value:
        total += x
    #print(total)
    return total


myfunc(10)
myfunc(10,20,30)

x = myfunc(10)
x = myfunc(10,25,47,96,332,85)
print(x)