# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def add_to_tree(self, root):
        # print(root.val)
        if root.val == 0 and root.left is None and root.right is None:
            root = None
        else:
            left = root.left
            right = root.right
            if root.left:
                left = self.add_to_tree(root.left)
                if left == 0:
                    root.left = None
                else:
                    root.left = left     
            if root.right:
                right = self.add_to_tree(root.right)
                if left == 0:
                    root.right = None
                else:
                    root.right = right
            if root.val == 0 and root.right is None and root.left is None:
                root = None
        return root
        
        
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tree = self.add_to_tree(root)
        return tree