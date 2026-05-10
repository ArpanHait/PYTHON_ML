class student:
    def __init__(self,name,subject,marks):
        self.name=name
        self.subjects=subject
        self.marks=marks
    def method(self):
        print("The average is:",(sum(self.marks)/3))
    def size(self):
        return len(self.subjects)
    # @staticmethod
     
    # def store():
    #     print("vrfvrfvvrfsvsvfsvsfbvfbfsb")

object=student("Arpan Hait",["Maths","English","Biolodgy"],[88,58,76])
store=object.size()
print(object.name)
for i in range (store):
    print(object.subjects[i],"=",object.marks[i])
    
object.method()
# object.store()

