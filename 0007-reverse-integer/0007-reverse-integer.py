class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
            x = str(x)[1:]
        else:
            x = str(x)
        x = x[::-1]
        if neg:
            x = '-'+x
        x = int(x)
        return x if -1*2**31<=x<=2**31-1 else 0