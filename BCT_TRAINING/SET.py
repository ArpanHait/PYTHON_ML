s={1,7,88,"hallo",2,"goal"}
print(s)

list1=[7,55,99,44,55,"coal","boy","coal",55]
store=set(list1)
print(store)

s.update(["my name",477])
print(s)

s.discard(88) #removes specific elements:
s.remove(1) #removes specific elements:
print(s)
s.clear() #removes whole set of data:
#s.pop()

s1={1,5,4,8}
s2={5,9,7,6}
print(f"union:",s1|s2) #set union
print(s1.union(s2))

#set intersection:
print("intersection:",s1.intersection(s2))