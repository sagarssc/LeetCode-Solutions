class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if nums[i] in data.keys():
                return [i,data[nums[i]]]
            else:
                data[dif] = i
        return []