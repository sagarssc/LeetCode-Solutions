class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        op = False
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                op = True
                break
        return op