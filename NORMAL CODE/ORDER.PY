class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self1,self2):
        return self1.price>self2.price
    
    def __add__(self1,self2):
        return self1.price+self2.price


order1=order("chips",50)
order2=order("basmati rice",150)
print(order1<order2)
print(order1+order2)