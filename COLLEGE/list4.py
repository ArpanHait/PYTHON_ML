#slicing
demo=[1,5,8,7,9,6]
print(demo[1:])

#9
l1=[1,2,3,4,5]
l2=[2,3,5,6,8]

l3=l1+l2
print(l3)
l4=[44,55,77]+l3
print(l4)
print("no of elements in the list")
print(len(demo))
num=len(demo)
l4[num-3:num]=[100,300,500]
print(l4)

#10  deletion
del l4
print("list is deleted")


