class employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showdetail(self):
        print("role is:",self.role)
        print("dept is:",self.dept)
        print("salary is:",self.salary)


em=employee("Ai Engineer","AI/ML",800000)
em.showdetail()