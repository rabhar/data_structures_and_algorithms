class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end = ' ')
        inorder(root.right)
        
inorder(root)