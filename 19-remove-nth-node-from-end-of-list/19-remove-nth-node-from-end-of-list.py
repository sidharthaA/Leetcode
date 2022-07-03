# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp1 = head
        temp2 = head
        i = 0
        while temp1 != None:
            i = i + 1
            temp1 = temp1.next
        print(i)
        x = i - n
        print(x)
        p = 0
        
        while temp2 != None:
            if x == 0:
                return(head.next)
                break
            if p == x - 1:
                temp2.next = temp2.next.next
                break
            else:
                temp2 = temp2.next
            p = p + 1
        return(head)