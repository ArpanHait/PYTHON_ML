class student:
    # name=''
    # roll=''
    def __init__(self, name,roll):
        self.name=name
        self.roll=roll

    def store(self):
        print("your student name is:", self.name)

    def marks(self):
        return s1.roll
      
    

# s1=student()
# s1.name="arpan0"
# s1.roll="105"

# print(s1.name,s1.roll)
s1=student("arpan hait",105)
print(s1.name,s1.roll)

s1.store()
print(s1.marks())