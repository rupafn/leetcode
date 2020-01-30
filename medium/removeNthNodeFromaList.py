class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        next = head
        arrs = []
        i = 0
        while(next.next):
            arrs.append(next.val)
            next = next.next
        arrs.append(next.val)
        arr = []
        ind = len(arrs)-n
        for j in range(0,len(arrs)):
            if(j == ind):
                continue
            arr.append(arrs[j])
        if(len(arr)>0):
            newHead = ListNode(arr[0])
            arr.pop(0)
            i=len(arr)-1

            while(i>=0):
                x =arr[i]
                newList = ListNode(x)
                tmp =newHead.next
                newHead.next = newList
                newHead.next.next = tmp
                i=i-1
            return newHead
        else:
            newHead = ListNode('')
            return newHead


obj = Solution()

head = ListNode(1)
i = 1
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

obj.removeNthFromEnd(head,1)
