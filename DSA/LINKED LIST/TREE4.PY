class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self):
        x = int(input("Value: "))
        new_node = node(x)
        if self.root is None:
            self.root = new_node
            return
        else:
            current = self.root
            while True:
                if x < current.data:
                    if current.left is None:
                        current.left = new_node
                        return
                    current = current.left
                elif x > current.data:
                    if current.right is None:
                        current.right = new_node
                        return
                    current = current.right
                else:  # Value already exists
                    print(f"Value {x} already exists. Not inserting.")
                    return

    # DELETION - Three cases to handle
    def delete(self):
        x = int(input("Value to delete: "))
        self.root = self._delete_recursive(self.root, x)

    def _delete_recursive(self, root, data):
        if root is None:
            print(f"Value {data} not found!")
            return root

        # Navigate to the node to delete
        if data < root.data:
            root.left = self._delete_recursive(root.left, data)
        elif data > root.data:
            root.right = self._delete_recursive(root.right, data)
        else:  # Node found
            print(f"Deleting node with value {data}")

            # Case 1: Node is a leaf (no children)
            if root.left is None and root.right is None:
                return None

            # Case 2: Node has only right child
            if root.left is None:
                return root.right

            # Case 3: Node has only left child
            if root.right is None:
                return root.left

            # Case 4: Node has both children
            # Find the in-order successor (smallest value in right subtree)
            successor = self._find_min(root.right)
            root.data = successor.data
            root.right = self._delete_recursive(root.right, successor.data)

        return root

    def _find_min(self, root):
        """Find node with minimum value"""
        current = root
        while current.left is not None:
            current = current.left
        return current

    
    def display(self):
        print("In-order traversal:", end=" ")
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node is None:
            return
        self._inorder(node.left)
        print(node.data, end=" -> ")
        self._inorder(node.right)

if __name__ == "__main__":
    tree = BinaryTree()
    c=1
    while c:
        print("1) Insert\n2) Delete\n3) Display\n4) Exit")
        a=int(input("____Choice:"))
        if(a==1):
           tree.insert()
        elif(a==2):
            tree.delete()
        elif(a==3):
            tree.display()
        elif(a==4):
            c=0
        else:
            print("invalid input!!")
            exit(0)