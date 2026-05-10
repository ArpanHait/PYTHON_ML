class barbar:
    def __init__(self,money):
        self.money=money
    
    def getvalue(self):
        print("value is:",self.money)

s=barbar(45000)
s.getvalue()
del s.money
s.getvalue()