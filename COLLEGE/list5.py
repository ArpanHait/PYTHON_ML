#11 reverse 
t=(4,5,6,8,9,7)
t=t[ ::-1]
print(t)

#12 access the value 20 form tupple
t=("orange",[10,20,30],(5,20,30))
print(t[1][1])

#13 swap two tupple
t1=(1,5,3,6)
t2=(5,8,9,5)
temp=t1
t1=t2
t2=temp

print(t1,t2)

#14 unpack a tupple

#15 modift the tupple
t1=(94,[7,22],8,6)
t1[1][1]=222
print(t1)

#16 no of occurence
t1=(1,2,3,4,5,6,7,8,9,1,2,3,6,5,4)
print(t1.count(4))

#17 wap to get the fourth element form the tupple:

t1=('a','b','c','d','e','f')
print(t1[4])
