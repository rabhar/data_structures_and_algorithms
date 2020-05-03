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
    
    def reverse(self):
        prev = None
        next = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        
    def reverse_recursive_(self, root):
        if not root.next:
            self.head = root
            return

        self.reverse_recursive_(root.next)
        root.next.next = root
        root.next = None
        
    def reverse_recursive(self):
        self.reverse_recursive_(self.head)
            
    def reverse_from_middle(self):
        slow = self.head
        fast = self.head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        p = None
        n = None
        curr = slow
        while curr:
            n = curr.next
            curr.next = p
            p = curr
            curr = n
        prev.next = p
        
        
    def rearrange(self):
        curr = self.head
        stack = []
        while curr:
            stack.append(curr)
            curr = curr.next
            
        curr = self.head
        while True:
            popped = stack.pop()
            if curr.data == popped.data:
                curr.next = None
                break
            
            if curr.next.data == popped.data:
                curr.next.next = None
                break
            
            temp = curr.next
            curr.next = popped
            curr.next.next = temp
            curr = temp
    
    def rearrangeRecursive_(self, root, head):
        if not root:
            return
        self.rearrangeRecursive_(root.next, head)
        
        if not head[0]:
            return
        
        if head[0].data != root.data and head[0].next.data != root.data:
            temp = head[0].next
            head[0].next = root
            root.next = temp
            head[0] = temp
        else:
            if head[0] == root:
                head[0].next = None
            else:
                head[0].next.next = None
            head[0] = None
        
        
    
        
        
            
llist = LinkedList()
llist.insert(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)
#llist.append(7)


llist.printList()
llist.rearrangeRecursive_(llist.head, [llist.head])
llist.printList()




    
            
        
                
                
                
    
        
        
    
        