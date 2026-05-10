class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        

    def show(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):
        newreal=self.real + num2.real
        newimg=self.img + num2.img
        return complex(newreal,newimg)
    
    def __sub__(self,num2):
        newreal=self.real - num2.real
        newimg=self.img - num2.img
        return complex(newreal,newimg)
    

num1=complex(4,5)
num1.show()

num2=complex(8,9)
num2.show()


addition=num1+num2
addition.show()
addition=num1-num2
addition.show()