
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        


if __name__ == "__main__":
    ll = LinkedList()

    first = Node(10)
    second = Node(20)
    third = Node(30)

    ll.head = first
    first.next = second
    second.next = third

    ll.display()
