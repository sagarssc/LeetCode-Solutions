class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        y = [i*i for i in nums]
        y.sort()
        return y
        
        