# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def check_left_right(self, left, right):
        if left and right and left.val == right.val:
            left_val = True
            right_val = True
            if left.left or right.right:
                left_val = self.check_left_right(left.left,right.right)
            if left.right or right.left:
                right_val = self.check_left_right(left.right,right.left)
            return left_val and right_val
        else:
            return False
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not (root.left or root.right):
            return True
        left = root.left
        right = root.right
        return self.check_left_right(left,right)