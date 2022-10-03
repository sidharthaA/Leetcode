# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        dup = head
        while head:
            count += 1
            head = head.next
        # print(count//2)
        count = count // 2
        
        while count > 0:
            count -= 1
            dup = dup.next
        return(dup)
        