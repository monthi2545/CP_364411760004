"""
Name : Monthira Jamikorn
ID :364411760004
Grop:Mit421
"""

# list comprehension

num = []
for x in range(1,100): #1-100
    num.append(x)


print(num)

newlist = [x for x in num if x%3==0]
print(newlist)
