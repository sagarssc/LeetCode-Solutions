class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        while 0 in nums:
            nums.remove(0)
            i += 1
        for j in range(i):
            nums.append(0)
        """
        Do not return anything, modify nums in-place instead.
        """
        