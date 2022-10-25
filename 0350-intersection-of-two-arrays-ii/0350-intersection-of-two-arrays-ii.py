class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt = Counter(nums1)
        op = []
        for i in nums2:
            if cnt.get(i) and cnt[i] > 0:
                op.append(i)
                cnt[i] -= 1
        return op