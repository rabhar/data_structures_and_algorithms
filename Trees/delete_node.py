class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end = ' ')
        inorder(root.right)
        
def minValue(root):
    curr = root
    while curr.left:
        curr = curr.left
    return curr

def deleteNode(root,key):
    if not root:
        return root

    if root.data > key:
        root.left = deleteNode(root.left, key)
    
    elif root.data < key:
        root.right = deleteNode(root.right, key)
    
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        if root.right is None:
            temp = root.left
            root = None
            return temp
        
        temp = minValue(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)
        
    return root


def deleteNode2(root, key):
    if not root:
        return root

    if root.data > key:
        root.left = deleteNode2(root.left, key)
        return root
    
    elif root.data < key:
        root.right = deleteNode2(root.right, key)
        return root
        
    else:
        if root.left is None:
            t = root.right
            root = None
            return t

        if root.right is None:
            t = root.left
            root = None
            return t

        parent = root
        minimum = root.right
        while minimum.left:
            parent = minimum
            minimum = minimum.left
        
        if parent == root:
            parent.right = minimum.right
        else:
            parent.left = minimum.right
        
        root.data = minimum.data
        del minimum
        return root

        
root = Node(8)
root.right = Node(10)
root.right.left = Node(9)
root.right.right = Node(11)

root.left = Node(4)
root.left.left = Node(2)
root.left.left.left = Node(1)
root.left.left.right = Node(3)

root.left.right = Node(6)
root.left.right.left = Node(5)
root.left.right.right = Node(7)

inorder(root)
print()
deleteNode2(root,4)

inorder(root)