# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a1 = ''
        a2 = ''
        while l1:
            a1 = str(l1.val) + a1
            l1 = l1.next
        while l2:
            a2 = str(l2.val) + a2
            l2 = l2.next
        
        x = str(int(a1) + int(a2))
        
        next = None
        a = None
        for i in range(len(x)):
            a = ListNode(val=x[i],next=next)
            next = a
        return a