#2 insert,append,delete,sort,replace/////////
l=["anil","amol","aditya","arpan","sufal"]
print(l)
l.insert(2,"animesh")
print(l)

l.append("zulu")
print(l)

l.remove("arpan")
print(l)

i=l.index("sufal")
l[i]="ankush"
print(l)

l.sort()
print(l)

l.reverse()
print(l)