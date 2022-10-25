class Solution:
    def count(self, x):
        w = ""
        p = x[0]
        c = 1
        for i in x[1:]:
            if p == i:
                c += 1
            else:
                w  = w+str(c)+p
                p = i
                c = 1
        w = w+str(c)+p
        return w
            
    def countAndSay(self, n: int) -> str:
        x = "1"
        i = 1
        while i < n:
            x = self.count(x)
            i += 1
        return x