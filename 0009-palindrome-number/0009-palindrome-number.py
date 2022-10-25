class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        n = len(x)//2
        i = 0
        op = True
        while i <= n:
            if x[i] == x[-i-1]:
                i += 1
                continue
            else:
                op = False
                break
        return op