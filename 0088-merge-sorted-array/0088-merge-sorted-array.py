from collections import Counter
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m + n
        i = 0
        while len(nums2) > 0:
            if nums1[i] <= nums2[0] and i<m:
                i += 1
            else:
                # print(i,'  ',nums2[0])
                nums1.insert(i,nums2[0])
                m += 1
                i += 1
                nums2.pop(0)
            if len(nums1) > l:
                nums1.pop()
        # print(nums1)
        