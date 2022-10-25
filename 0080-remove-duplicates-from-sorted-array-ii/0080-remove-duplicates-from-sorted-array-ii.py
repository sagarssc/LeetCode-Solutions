class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d ={}
        t = 0
        i = 0
        while i < len(nums):
            if nums[i] in d:
                if d[nums[i]] == 2:
                    t += 1
                    del nums[i]
                    continue
                else:
                    d[nums[i]] += 1
            else:
                d[nums[i]] = 1
            i += 1
        print(nums[:-t])
        print(t)
        # return nums