class student:
    def __init__(self,marks):
        self.marks=marks
    
    @property
    def percentage(self):
        return str((self.marks[0]+self.marks[1]+self.marks[2])/3) + "%"
    
    def size(self):
        return len(self.marks)

s=student([80,77,78])
store=s.size()
print("marks are:1")
for i in range(store):
    print(s.marks[i])
print("marks are:2")
for i in s.marks:
    print(i)

print(s.percentage)
s.marks[0]=7
print(s.percentage)
