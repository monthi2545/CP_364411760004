"""
Name : Monthira Jamikorn
ID :364411760004
Grop:Mit421

# list = []

mylist = [] # emppty list
print(mylist)
print(len(mylist)) # return value --> 0

mylist = [10,20,30,40,50]
print(mylist)
print(len(mylist))
print(type(mylist))


# access to member in list
# index
print(mylist[0]), type(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
print(mylist[4])
#print(mylist[5]) # out of range
# negative index
print(mylist[-1])
print(mylist[-2])
print(mylist[-3])
print(mylist[-4])
print(mylist[-5])
# range index [start :stop]
mylist = [10,20,30,40,50]
# [20,30,40]
print(mylist[1:4])
# [10,20]
print(mylist[0:2])
# [20,30,40,50]
print(mylist[1:6])
print(mylist[1:])
# [40,50]

# rnge negative index [start:stop]
# [20,30,40]
print(mylist[-4:-1])
# [10,20]
print(mylist[-5:-3])
# [20,30,40,50]
print(mylist[-4:])
# [40,50]
print(mylist[-2:])

# looe
# for

for x in mylist:
    print(x, x*10)

for x in range(len(mylist)):
    print(mylist[x])

# while
c = 0 # first index in list
while c < len(mylist):
    print(mylist[c],end=" ")
    c +=1

