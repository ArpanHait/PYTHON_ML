class car:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def display(self):
        print(self.brand)
        print(self.model)
c=car("bmw","m5")
print(c.brand)
c.display()