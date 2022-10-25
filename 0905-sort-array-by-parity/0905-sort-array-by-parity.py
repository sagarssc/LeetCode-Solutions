class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        x = []
        y = []
        for n in nums:
            if n%2 == 0:
                x.append(n)
            else:
                y.append(n)
                
        return x+y