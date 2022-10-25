class Solution:
    def binerySearch(self, nums, n):
        if len(nums) == 1:
            if nums[0] == n:
                return 0
            else:
                return -1
        m = len(nums) // 2
        # print(nums)
        # print(m)
        if nums[m] == n:
            return m
        elif nums[m] < n:
            i = self.binerySearch(nums[m:],n)
            if i >= 0:
                m = m+i
            else:
                m = i
        else:
            m = self.binerySearch(nums[:m],n)
        print(m)
        return m
    
    def search(self, nums: List[int], target: int) -> int:
        k = 0
        while nums[0] > nums[-1]:
            x = nums.pop()
            nums.insert(0,x)
            k += 1
        m = self.binerySearch(nums,target)
        # print(m,'  ',k,'  ',len(nums))
        if m == -1:
            return m
        else:
            m = m - k
            if m < 0:
                m = len(nums) + m 
            return m