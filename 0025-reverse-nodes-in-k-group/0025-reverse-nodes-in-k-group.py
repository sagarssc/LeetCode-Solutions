# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def to_list(self,head):
        op = []
        while head is not None:
            op.append(head.val)
            head = head.next
        return op
    def add_to_list(self,head,node):
        curr = head
        while curr.next is not None:
            curr = curr.next
        curr.next = node
        return head
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head.val == None:
            return head
        l = self.to_list(head)
        ls = []
        curr = ListNode(None)
        while len(l) >= k:
            t = l[:k][::-1]
            l = l[k:]
            for i in t:
                node = ListNode(i)
                curr = self.add_to_list(curr,node)
        for i in l:
            node = ListNode(i)
            curr = self.add_to_list(curr,node)
        return curr.next
            
                