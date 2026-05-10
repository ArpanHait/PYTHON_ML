class account:

    def __init__(self,bal,acc):
        self.balance=bal
        self.acc_no=acc

    def debit(self,ammount):
        if(ammount>self.balance):
            print(" Insufficient amount !!")                                               
        else:
            self.balance=self.balance-ammount
            print("current ammount:",self.balance)

    def credit(self,ammount):
        self.balance=self.balance+ammount
        print("current ammount:",self.balance)


user1=account(10000,456892138)
store=input("creadit/debit_(c/d):")
if(store=='c'):
    ammount=int(input("Enter ammount for creadit:"))
    user1.credit(ammount)
else:
    ammount=int(input("Enter ammount for debit:"))
    user1.debit(ammount)








# store=open("user_data.txt","r+")
# cache=store.read()
# check=input("NAME:")
# data=list(cache).split("\n")
# if check in data:
#     s=input("debit/cradit_(d/c):")
#     if(s=="c"):
#         user1.
        


