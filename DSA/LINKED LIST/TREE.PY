class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data, end=" -> ")
        self.inorder(root.right)

if __name__ == "__main__":

    tree = BinaryTree()
    tree.root = Node(4)
    tree.root.left = Node(5)
    tree.root.right = Node(6)

    tree.inorder(tree.root)
    print("None")
