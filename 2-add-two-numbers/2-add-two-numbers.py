# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        mul = 1
        num2 = 0
        num1 = 0
        
        while l1 != None:
            num1 = num1 + (l1.val * mul)
            mul = mul * 10
            l1 = l1.next
        
        mul = 1
        while l2 != None:
            num2 = num2 + (l2.val * mul)
            mul = mul * 10
            l2 = l2.next
        str_sum = str(num1 + num2)[::-1]
        
        l_temp = ListNode()
        l3 = l_temp
        i = 1
        for s in str_sum:
            l3.val = int(s)
            if i < len(str_sum):
                l3.next = ListNode()
                l3 = l3.next
            else:
                l3.next = None
            i = i + 1
        return l_temp