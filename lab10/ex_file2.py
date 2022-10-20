"""
Name : Monthira Jamikorn
ID :364411760004
Grop:Mit421
"""

# create file
import  os
# create empty file
try:
    f = open("test2.txt","x")
except:
    print("File already exits.")

# create test3.txt on desktop of your computer
#C:\Users\LabCom_MT-4
#try:
#    f = open("C:\\users\LabCom_MT-4\Desktop\\test3.txt","x")
#except Exception as e:
#    print(e)


# write file
#mode "a" , "w"
try:
    f = open("test2.txt","w")
    f = write ("Monthira jamikorn\n")
except:
    print("Cloud not found a fine name 'test2.txt'")
finally:
    f.close()

# delete file

if os.path.exists("test3.txt"):
    os.remove("test2.txt")
else:
    print("File not foud.")
