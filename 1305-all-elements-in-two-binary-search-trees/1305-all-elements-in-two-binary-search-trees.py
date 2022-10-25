# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_nodes(self,root, op):
        op.append(root.val)
        if root.left:
            op = self.get_nodes(root.left, op)
        if root.right:
            op = self.get_nodes(root.right, op)
        return op
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ops = []
        ops2 = []
        if root1:
            ops = self.get_nodes(root1,ops)
        if root2:
            ops2 = self.get_nodes(root2,ops2)
        op = ops + ops2
        op.sort()
        print(op)
        print(ops)
        print(ops2)
        return op