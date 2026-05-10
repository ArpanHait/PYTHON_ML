#3 replace the specified phasse with another://///
str="nil"
print(str.replace("n" , "t"))

#4 tupple 
t=("hello","world")
print(t)

#5 convertion
tuple1=tuple('world')
print(tuple1)

#6 concatination
tupple1=(0,1,2,5,6)
tupple2=('python','spider')
tupple3=(tupple1, tupple2)
print(tupple3)

#7 operation
for i in range(5):
    demo=list(map(input(f"colour {i}:")))
# demo=["white","brown","yello","red"]
print(demo)
demo.insert(1,"orange")
print(demo)
demo.append("black")
print("demo")
demo.remove("yello")
print(demo)
demo.sort()
print(demo)
i=demo.index('red')
demo[i]="brick red"
print(demo)
print(demo.reverse())
