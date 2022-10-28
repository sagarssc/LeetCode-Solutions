class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            i = nums.index(target)
            li = nums[::-1].index(target)
            li = len(nums) - 1 - li
            return [i,li]
        except:
            return [-1,-1]