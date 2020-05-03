class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.data, end = ' ')
        inorderTraversal(root.right)
        
def morris_traversal(root):
    curr = root
    
    while curr:
        if curr.left is None:
            print(curr.data, end = ' ')
            curr = curr.right
        else:
            prev = curr.left
            while prev.right and prev.right != curr:
                prev = prev.right
                
            if prev.right is None:
                prev.right = curr
                curr = curr.left

            else:
                prev.right = None
                print(curr.data, end = ' ')
                curr = curr.right
    

def KthLargest_(root,k):
    if root:
        dat = KthLargest_(root.right,k)
        if dat:
            return dat
        k[0] = k[0] - 1
        if k[0] == 0:
            return root.data
        return KthLargest_(root.left, k)
        

def kthLargest(root, k):
    return KthLargest_(root,[k])


root = Node(4)
root.right = Node(5)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)

#morris_traversal(root)
#inorderTraversal(root)

print(kthLargest(root, 3))