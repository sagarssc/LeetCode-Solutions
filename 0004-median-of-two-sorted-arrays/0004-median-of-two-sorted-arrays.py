class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = nums1 + nums2
        n.sort()
        
        if len(n)%2 == 0:
            i = len(n)//2
            j = i-1
            m = (n[i] + n[j])/2
            return m
        else:
            i = len(n)//2
            return n[i]