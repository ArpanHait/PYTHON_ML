class car():
    @staticmethod
    def start():
        print("car started:")

    @staticmethod
    def end():
        print("car stopped:")

    def namei(self):
        print("yourr car")
    

class toyota(car):
    def __init__(self,name):
        self.name=name


class fortuner(toyota):
    def __init__(self,milage):
        self.milage=milage


car1=fortuner(58256)
car2=toyota("hondai")
print(car1.start(),car2.namei())