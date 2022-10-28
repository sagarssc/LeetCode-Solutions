# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def LListToList(self,head):
        l = []
        node = head
        while node is not None:
            l.append(node.val)
            node = node.next
        return l
    
    def add_to_list(self,head,val):
        node = ListNode(val)
        curr = head
        while curr.next is not None:
            curr = curr.next
        curr.next = node
        return head
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head
        l = self.LListToList(head)
        l_len = len(l)
        if l_len == 0:
            return head
        if k >= l_len:
            k = k%l_len
        l = l[-k:] + l [:-k]
        head = ListNode(None)
        for i in l:
            head = self.add_to_list(head,i)
        return head.next