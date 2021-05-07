class LinkedList:

    def __init__(self,val):
        self.data = val
        self.next = None


    def traverse(self):
        curr = self
        while(curr is not None):
            print(curr.data)
            curr = curr.next

    def insertAtBegining(self,val):
        # if(self is not None):
        #     self = LinkedList(val)
        # else:
        newEl = LinkedList(val)
        newEl.next = self
        self =newEl
        return self


    def insertAtLast(self,val):
        newEl = LinkedList(val)
        tmp = self
        while(tmp.next is not None):
            tmp = tmp.next
        tmp.next = newEl

    def insertAtPos(self,val,pos):
        tmp = self
        count = 1
        while(tmp is not None):
            count+=1
            if(count ==pos):
                print('here at position:',pos,val)
                temporary = tmp.next
                tmp.next = LinkedList(val)
                tmp.next.next = temporary

            print(tmp.data)
            tmp = tmp.next

    def reverse(self):
        prev = None
        curr = self

        while(curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


root = LinkedList(1)
root.next = LinkedList(2)
root.next.next = LinkedList(3)
root.next.next.next = LinkedList(4)
root.next.next.next.next = LinkedList(5)

# root.traverse()
root = root.insertAtBegining(10)
root = root.insertAtBegining(20)

root.insertAtLast(9)
root.insertAtLast(9)
root.insertAtPos(23,5)

print('===================================')
root = root.reverse()
root.traverse()
