class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(4)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(2)


def get_path(root, key, stack):
    if not root:
        return False
    
    stack.append(root.data)
    
    if root.data == key:
        return True

    if get_path(root.left, key, stack) or get_path(root.right, key, stack):
        return True
    
    stack.pop()
    return False


p1 = []
get_path(root,2,p1)
print(p1)

p2 = []
get_path(root,1,p2)
print(p2)

i = 0 
j = 0
while  i < len(p1) and j < len(p2):
    if p1[i] != p2[i]:
        break
    i += 1
    j +=1
    
print(p1[i-1])
