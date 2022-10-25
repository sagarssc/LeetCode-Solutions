# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # print(root.val)
        if root.val == val:
            return root
        elif root.val > val:
            if root.left is not None:
                return self.searchBST(root.left, val)
            else:
                return None
        elif root.val < val:
            if root.right is not None:
                return self.searchBST(root.right, val)
            else:
                return None
        else:
            return None