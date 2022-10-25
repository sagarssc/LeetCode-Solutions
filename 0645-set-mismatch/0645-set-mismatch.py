class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l = len(nums)
        d = Counter(nums)
        m = list(set(range(1,l+1)) - set(nums))[0]
        re = [item for item in d if d[item]>1][0]
        return [re,m]