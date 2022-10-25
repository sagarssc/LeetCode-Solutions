class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        i, j = 0 , x
        while i < j:
            m = (i + j)//2
            # print(m)
            if m*m <= x < (m+1)*(m+1):
                i = m
                break
            elif m*m < x:
                i = m + 1
            else:
                j = m
        return i
        
        