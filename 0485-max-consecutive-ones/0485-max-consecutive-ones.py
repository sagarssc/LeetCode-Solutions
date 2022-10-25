class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        j = 0
        for i in nums:
            if i == 0:
                counter = max(counter,j)
                j = 0
            else:
                j += 1
        return max(counter,j)