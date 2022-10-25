# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        swap = True
        while node is not None and node.next != None:
            if swap:
                node.val, node.next.val = node.next.val, node.val
            swap = not swap
            node = node.next
            # print(node)
        print(head)
        return head