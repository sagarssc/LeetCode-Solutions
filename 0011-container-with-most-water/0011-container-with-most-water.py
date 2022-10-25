class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        area = 0
        while i < j:
            if height[i] <= height[j]:
                lowest = height[i]
                diff = j - i
                i += 1
            else:
                lowest = height[j]
                diff = j-i
                j -= 1
            temp = diff * lowest
            if temp > area:
                area = temp
        return area
            