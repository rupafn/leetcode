# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        ptr = head
        tmp = ListNode('')
        while(ptr.next):
            if(ptr.val == 2):
                ptr = ptr.next
                # if(ptr.next == None):
                #     print(ptr.val)
                continue
            else:
                # print(ptr.val)
                
                tmp.val = ptr.val
                tmp.next = ptr.next
                ptr = ptr.next
                if(ptr.next == None):
                    # print(ptr.val)
                    tmp.val = ptr.val
                    tmp.next = ptr.next
        while(tmp.next):
            print(tmp.val)
            tmp=tmp.next
            if(tmp.next == None):
                print(tmp.val)




obj = Solution()

head = ListNode(1)
i = 4
while(i>1):
    newList =ListNode(i)
    tmp = head.next
    head.next = newList
    head.next.next = tmp
    i-=1
# next = head
# while(next.next):
#     print(next.val)
#     next = next.next
obj.reorderList(head)
