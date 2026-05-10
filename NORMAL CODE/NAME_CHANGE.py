class person:
    name="arpan hait"
    no=456223588

    def namchange(self,new_name):
        person.name=new_name
    
    @classmethod
    def nochange(cls,new_no):
        cls.no=new_no

s1=person()
print(s1.name)
s1.namchange(" arpan2006")
print(s1.name)

print(s1.no)
s1.nochange(101010101)
print(s1.no)