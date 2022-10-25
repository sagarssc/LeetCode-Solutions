class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        val = dividend//divisor
        rem = dividend%divisor
        if val < 0 and rem != 0 :
            val += 1
        
        return max(min(val,2**31-1),-2**31)
            