# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        nodes = []
        current_node = [root]
        while current_node:
            l = []
            op = []
            for node in current_node:
                l.append(node.val)
                if node.left is not None:
                    op.append(node.left)
                if node.right is not None:
                    op.append(node.right)
            nodes.append(l)
            current_node = op
        return nodes