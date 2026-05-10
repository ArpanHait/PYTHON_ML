class car():
    @staticmethod
    def start():
        print("car started:")

    @staticmethod
    def end():
        print("car stopped:")

class inheritance(car):

    def __init__(self,name):
        self.name=name
        

car1=inheritance("toyota")
car2=inheritance("supraa")

print(car1.start(),car1.name)