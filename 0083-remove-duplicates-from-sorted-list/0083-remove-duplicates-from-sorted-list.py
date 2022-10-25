# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        node = head
        prev = node.val
        while node.next != None:
            if node.next.val != prev:
                node = node.next
                prev = node.val
            else:
                node.next = node.next.next
        print(head)
        return head