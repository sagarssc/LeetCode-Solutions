# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a = []
        if root is not None:
            a += self.inorderTraversal(root.left)
            a.append(root.val)
            a += self.inorderTraversal(root.right)
        return a