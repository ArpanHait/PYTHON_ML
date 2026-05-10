class circle:
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return (22/7) * self.radius**2
    
    def parameter(self):
        return 2*(22/7)*self.radius**2

r=int(input("give radius here:"))
c=circle(r)
print("area is:",c.area(),"\n","parameter is:",c.parameter())
