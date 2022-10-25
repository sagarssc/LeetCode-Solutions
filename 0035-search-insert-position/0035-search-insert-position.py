class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        while start < end:
            mid = (start + end) // 2
            print(mid)
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        return start