class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x = list(set(nums[:]))
        x.sort()
        if len(x) >= 3:
            return x[-3]
        else:
            return x[-1]