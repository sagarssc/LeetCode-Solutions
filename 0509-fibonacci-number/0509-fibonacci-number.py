class Solution:
    def fib(self, n: int) -> int:
        fst = 0
        scond = 1
        if n == 0:
            return fst
        elif n == 1:
            return scond
        else:
            i = 1
            v = 0
            while i < n:
                v = fst + scond
                fst = scond                
                scond = v
                i += 1
            return v
