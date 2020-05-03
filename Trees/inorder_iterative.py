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

stack = []
while True:
    if root:
        stack.append(root)
        root = root.left
    
    elif stack:
        popped = stack.pop()
        print(popped.data, end = ' ')
        root = popped.right
        
    else:
        break
        
