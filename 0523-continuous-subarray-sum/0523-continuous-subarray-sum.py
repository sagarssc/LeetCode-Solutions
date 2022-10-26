class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod = 0
        d = {0:-1}
        for i in range(len(nums)):
            mod = (mod + nums[i]) % k
            # # print(mod)
            # if mod == 0:
            #     return True
            if mod not in d:
                d[mod] = i
            else:
                if i - d[mod] >= 2:
                    return True
        return False