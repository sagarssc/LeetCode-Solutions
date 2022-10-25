class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        y = heights[:]
        y.sort()
        i = 0
        for j in range(len(heights)):
            if heights[j] != y[j]:
                i += 1
        return i