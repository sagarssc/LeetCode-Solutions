# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()
        cycle = False
        node = head
        while node is not None:
            if node in nodes:
                cycle = True
                break
            else:
                nodes.add(node)
                node = node.next
        return cycle