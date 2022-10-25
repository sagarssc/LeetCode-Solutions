class Solution:
    def tribonacci(self, n: int) -> int:
        start = [0,1,1]
        if n < 3:
            return start[n]
        v = 0
        for i in range(3,n):
            v = sum(start)
            start.pop(0)
            start.append(v)
        return sum(start)