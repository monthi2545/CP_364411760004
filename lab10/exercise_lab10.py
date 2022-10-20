"""
Name : Monthira Jamikorn
ID :364411760004
Grop:Mit421
"""

"""
ให้นักศึกษาเขียนตารางสูตรคูณลงในไฟล์   test3.txt
โดยการรับ Input
แม่สูตรคูณจากผู้ใช้มา 1 ตัวเลข
"""

num = int(input("Enter an integer: "))

try:
    f = open("C:\\users\LabCom_MT-4\Desktop\\test3.txt","x")
    for x in range(1,13):
        f.write(f'{num} x {x} = {num*x}\n')
    f.close()
except:
    print("Cloud not found a file.")
finally:

    print("Done.")












