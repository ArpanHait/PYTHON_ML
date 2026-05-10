
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self):
        temp=self.head
        x=int(input("Enter value:"))
        new=node(x)
        if self.head is None:
            self.head = new
        else:
            while temp.next:
                temp=temp.next
            temp.next=new
        
    def delete(self,pos):
        if self.head is None:
            print("List is empty")
            return
        
        temp=self.head

        if(pos==1):
            self.head=temp.next
        else:
            for i in range(pos-2):
                temp=temp.next
            store=temp.next
            temp.next=store.next
            

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None\n")


if __name__ == "__main__":
    link = LinkedList()
    c=1
    while c:
        print("1) Insert\n2) Delete\n3) Display\n4) Exit")
        a=int(input("____Choice:"))
        if(a==1):
           link.insert()
        elif(a==2):
            pos=int(input("Enter position:"))
            link.delete(pos)
        elif(a==3):
            link.display()
        elif(a==4):
            c=0
        else:
            print("invalid input!!")
            exit(0)
            