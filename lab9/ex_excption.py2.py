"""
Name : Monthira Jamikorn
ID :364411760004
Grop:Mit421
"""

# Exception
print("Starty")
while True:
    try:
        num = int(input("Enter an integer: "))
        print(f'Your number is {num}')
    except ValueError as e :
         print("Error log: ",e.args)
         print("Please, enter only integer.")


print("End")


