"""
Name : Monthira Jamikorn
ID :364411760004
Grop:Mit421
"""

# Exception
print("Start")

x = "MIT421"

try:
    print(x)
except NameError:
    print("variable name not define.")
except:
    print("Something went wrong.")
else:
    print("No error.")
finally:
    print("Error has been excepted.")


print("End")