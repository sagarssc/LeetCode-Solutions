class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = ''.join([str(i) for i in digits])
        digit = int(digit) + 1
        digits = [ i for i in str(digit) ]
        return digits