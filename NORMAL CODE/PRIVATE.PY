class bank:
    def __init__(self,money,acc,passw):
        self.balance=money
        self.acc_no=acc
        self.__password=passw
    def access(self):
        return self.__password
    
user1=bank(51000,84561225,"Arpan@2006")
print(user1.access())
print(user1.__password)

