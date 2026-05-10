class car():
    @staticmethod
    def start():
        print("car started:")

    @staticmethod
    def end():
        print("car stopped:")

    def __init__(self,type):
        self.matal=type

class fortuner(car):
    def __init__(self,milage,type):
        self.milage=milage
        super().__init__(type)


car1=fortuner(58256,"disel")
print(car1.matal)
