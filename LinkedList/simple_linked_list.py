class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def printList(self, root = None):
        curr = self.head
        if root:
            curr = root
        while(curr):
            print(curr.data, end = ' ')
            curr = curr.next
        print()
        
    def isEmpty(self):
        if self.head:
            return False
        return True
    
    def insert(self,data):
        if not self.head:
            self.head = Node(data)
            return
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = Node(data)
    
    def removeTop(self):
        if not self.isEmpty():
            removed = self.head
            self.head = self.head.next
            return removed.data
        else:
            return -1
        
    def pop(self):
        if not self.head:
            return -1
        if self.head and self.head.next is None:
            popped = self.head.data
            self.head = None
            return popped
        
        curr = self.head
        prev = None
        while curr.next:
            prev = curr
            curr = curr.next
        
        popped = curr.data
        prev.next = None
        return popped

    def length(self):
        if self.isEmpty():
            return 0
        l = 0
        curr = self.head
        while curr:
            l += 1
            curr = curr.next
        return l
    
    def deleteMiddle(self):
        if self.length() > 1:
            slow = self.head
            fast = self.head 
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = slow.next
    
    def getMiddle(self):
        if self.length() > 1:
            slow = self.head
            fast = self.head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow.data        
        
llist = LinkedList()
llist.insert(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)

llist.printList()
print(llist.getMiddle())
llist.deleteMiddle()
llist.printList()
print(llist.getMiddle())





    
            
        
                
                
                
    
        
        
    
        