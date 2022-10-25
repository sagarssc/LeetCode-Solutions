# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        nodes = [{'node':root,'last_sum':0}]
        sums = []
        last_sum = 0
        while nodes:
            data = nodes.pop(0)
            node = data['node']
            last_sum = data['last_sum'] + node.val
            if node.right:
                nodes.insert(0,{'node':node.right,'last_sum':last_sum})
            if node.left:
                nodes.insert(0,{'node':node.left,'last_sum':last_sum})
            if not (node.left or node.right):
                sums.append(last_sum)
        if targetSum in sums:
            return True
        else:
            return False
        
        