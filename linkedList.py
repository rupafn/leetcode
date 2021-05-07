class LinkedList:

    def __init__(self,val):
        self.data = val
        self.next = None

    def reverse(self):
        prev = None
        curr = self

        while(curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

        
    def traverse(self):
        root = self
        while(root):
            print(root.data)
            root = root.next



root = LinkedList(1)
root.next = LinkedList(2)
root.next.next = LinkedList(3)
root.next.next.next = LinkedList(4)
root.next.next.next.next = LinkedList(5)

root = root.reverse()

root.traverse()
