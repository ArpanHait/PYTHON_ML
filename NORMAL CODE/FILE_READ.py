# store=open("mine.txt","w")

# store.write("FILE_TYPE=INDEX\nVERSION=1.0INDEX_FIELD=OBJECTID\nRECORD_COUNT=5000\nGENERATED_DATE=2026-03-03")
# store.close()

# data=open("mine.txt","r")
# print(data.read())
# data.close()

# hello=open("mine.txt","r+")
# hello.write("") #appends at first
# hello.close()

# with open("mine.txt","r+") as file:
#     file.write("my name not arpan")

# import os
# os.remove("mine.txt")

# file=open("mine.txt","w")
# file.write("my name is arpan:\n")
# file.write("your name is what !!")

with open("arpan.txt", "r") as file:
    data = file.read()

store = data.split(",")
print(store)
count=0
for i in store:
    if(int(i)%2==0):
        count=count+1

print(count)