class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linklist:
    def __init__(self):
        self.head=None

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
    
link=linklist()
first=node(10)
second=node(20)
third=node(30)

link.head=first
first.next=second
second.next=third

link.display()
    