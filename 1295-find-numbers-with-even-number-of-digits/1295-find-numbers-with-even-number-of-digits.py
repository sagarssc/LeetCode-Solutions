class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        j =0 
        for i in nums:
            if len(str(i)) %2 == 0:
                j += 1
        return j